#%%
from inspect import stack
import inspect
from os import get_terminal_size
from os.path import relpath
# from re import search as re_search
from re import match as re_match
from typing import Union, Literal
from varname import VarnameRetrievingError, argname, nameof
from pprint import pformat

# if __name__ == '__main__':
    # from Cope._config import config
    # from Cope._None import _None
# else:
#     from ._config import config
#     from ._None import _None
from pathlib import Path
from typing import Union, SupportsInt
from rich.console import Console
from rich.theme import Theme

class _ConfigSingleton:
    # Override the debug parameters and display the file/function for each debug call
    #   (useful for finding debug calls you left laying around and forgot about)
    display_file = True
    display_func = True
    display_path = False
    root_dir = None

    _debug_count = 0
    verbosity = 0

    hide_todo = False

    theme = Theme.read(Path(__file__).parent/'style.cfg')
    console = Console(theme=theme)


config = _ConfigSingleton()

#%%
# A unique dummy class for parameters
class _None: pass

print = config.console.out
_repr = repr
#%%
def printArgs(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

def get_metadata(calls=1):
    """ Gets the meta data of the line you're calling this function from.
        Calls is for how many function calls to look back from.
    """
    try:
        s = stack()[calls]
        return s
    except IndexError:
        return None

def get_iterable_str(
    iterable: Union[tuple, list, set, dict],
    method: Literal['pprint', 'custom']='custom',
    width: int=...,
    depth: int=...,
    indent: int=4,
    # useMultiline: bool=True,
    # limitToLine: bool=False,
    # minItems: int=2,
    # maxItems: int=50
    ) -> str:
    """ "Cast" a tuple, list, set or dict to a string, automatically shorten
        it if it's long, and display how long it is.

        Params:
            limitToLine: if True, limit the length of list to a single line
            minItems: show at least this many items in the list
            maxItems: show at most this many items in the list
            color: a simple int color

        Note:
            If limitToLine is True, it will overrule maxItems, but *not* minItems
    """
    if width is Ellipsis:
        width == get_terminal_size().columns

    if method == 'pprint':
        return pformat(iterable, width=width, depth=depth, indent=indent)
    elif method == 'custom':
        def getBrace(opening):
            if isinstance(iterable, list):
                return '[' if opening else ']'
            elif isinstance(iterable, (set, dict)):
                return '{' if opening else '}'
            else:
                return '(' if opening else ')'

        lengthAddOn = f'(len={len(iterable)})'
        defaultStr  = str(iterable)

        # Print in lines
        # if (not limitToLine and len(defaultStr) + len(lengthAddOn) > (get_terminal_size().columns / 2)) or useMultiline:
        if len(defaultStr) + len(lengthAddOn) > (get_terminal_size().columns / 2):
            rtnStr = f'{lengthAddOn} {getBrace(True)}'
            if isinstance(iterable, dict):
                for key, val in iterable.items():
                    rtnStr += f'\n\t<{type(key).__name__}> {key}: <{type(val).__name__}> {val}'
            else:
                for cnt, i in enumerate(iterable):
                    rtnStr += f'\n\t{cnt}: <{type(i).__name__}> {i}'
            if len(iterable):
                rtnStr += '\n'
            rtnStr += getBrace(False)
        else:
            rtnStr = defaultStr + lengthAddOn

        return rtnStr
    else:
        raise TypeError(f"Incorrect method `{method}` given. Options are 'pprint' and 'custom'.")

    """
    if type(v) in (tuple, list, set) and len(v) > minItems:
        if type(v) is set:
            v = tuple(v)

        ellipsis = f', ... '
        length = f'(len={len(v)})'

        if limitToLine:
            firstHalf  = str(v[0:round(minItems/2)])[:-1]
            secondHalf = str(v[-round(minItems/2)-1:-1])[1:]
            prevFirstHalf = firstHalf
            prevSecondHalf = secondHalf
            index = 0

            # The 54 is a fugde factor. I don't know why it needs to be there, but it works.
            while (6 + 54 + len(length) + len(firstHalf) + len(secondHalf)) < get_terminal_size().columns:
                index += 1
                firstHalf  = str(v[0:round((minItems+index)/2)])[:-1]
                secondHalf = str(v[-round((minItems+index)/2)-1:-1])[1:]
                prevFirstHalf = firstHalf
                prevSecondHalf = secondHalf
                if index > 6:
                    break

            firstHalf = prevFirstHalf
            secondHalf = prevSecondHalf

        else:
            firstHalf  = str(v[0:round(maxItems/2)])[:-1]
            secondHalf = str(v[-round(maxItems/2)-1:-1])[1:]

        return firstHalf + ellipsis + secondHalf + length

    else:
        return str(v) + f'(len={len(v)})'
    """

def get_typename(var, addBraces=True):
    """ Get the name of the type of var, formatted nicely.
        Also gets the types of the elements it holds, if `var` is a collection.
    """
    def getUniqueType(item):
        returnMe = type(item).__name__
        while isinstance(item, (tuple, list, set)):
            try:
                item = item[0]
            except (KeyError, IndexError, TypeError):
                returnMe += '('
                break
            returnMe += '(' + type(item).__name__

        cnt = 0
        for i in returnMe:
            if i == '(':
                cnt += 1
        return returnMe + (')'*cnt)

    if isinstance(var, dict):
        name = type(var).__name__
        if len(var) > 0:
            rtn = f'{name}({type(list(var.keys())[0]).__name__}:{type(list(var.values())[0]).__name__})'
        else:
            rtn = f'{name}()'
    elif isinstance(var, (tuple, list, set, dict)):
        types = []
        for i in var:
            types.append(getUniqueType(i))
        types = sorted(set(types), key=lambda x: types.index(x))
        fullName = type(var).__name__ + str(tuple(types)).replace("'", "")
        if len(types) == 1:
            fullName = fullName[:-2] + ')'
        rtn = fullName
    else:
        rtn = type(var).__name__
    return f'<{rtn}>' if addBraces else rtn

def print_debug_count(leftAdjust=2):
    config._debug_count += 1
    print(f'{str(config._debug_count)+":":<{leftAdjust+2}}', end='', style='count')

def get_varname(var, full=True, calls=1, metadata=None):
    def get_varname_manually(calls):
        # Not quite sure why it's plus 2?...
        context = get_metadata(calls=calls+2).code_context
        if context is None:
            return '?'
        else:
            line = context[0]
        # Made with ezregex
        # optional(stuff) + 'debug(' + group(stuff + multiOptional('(' + optional(stuff) + ')')) + ')' + optional(stuff)
        match = re_match(r"(?:.+)?debug\((.+(?:\((?:.+)?\))*)\)(?:.+)?", line)
        if match is None:
            return '?'
        else:
            return match.groups()[0]
        # ans.test('abc = lambda a: 6+ debug(parseColorParams((5, 5, 5)), name=8, clr=(a,b,c))\n')
        return '?'


    try:
        rtn = argname('var', frame=calls+1)
    # It's a *likely* string literal
    except Exception as e:
        if type(var) is str:
            rtn = None
        else:
            try:
                # print('var:', var)
                # print('var type:', type(var))
                rtn = nameof(var, frame=calls+1, vars_only=False)
            except Exception as e2:
                if config.verbosity >= 2 and not isinstance(var, Exception):
                    raise e2
                else:
                    rtn = get_varname_manually(calls+1)
    except VarnameRetrievingError as e:
        if config.verbosity:
            raise e
        else:
            rtn = get_varname_manually(calls+1)

    try:
        # It auto-adds ' around strings
        if rtn == str(var) or rtn == f"'{var}'":
            # If the value is the same as the name, it must be a literal
            return None
        else:
            return rtn
    except:
        return rtn

def get_adjusted_filename(filename):
    # Default behavior
    if config.root_dir is None:
        return relpath(filename)
    elif len(config.root_dir):
        return relpath(filename, config.root_dir)
    else:
        return filename

def get_context(metadata, showFunc=True, showFile=True, showPath=False) -> str:
    """ Returns the stuff in the [] (the "context") """
    if metadata is None:
        return ''

    # This logically must be true
    if showPath:
        showFile = True

    s = '['
    if showPath:
        s += f'"{metadata.filename}", line {metadata.lineno}, in '
    elif showFile:
        s += f'"{get_adjusted_filename(metadata.filename)}", line {metadata.lineno}, in '
    # We apparently don't want any context at all (for whatever reason)
    elif not showFunc:
        return ''

    if showFunc:
        if metadata.function.startswith('<'):
            s += 'Global Scope'
        else:
            s += f'{metadata.function}()'
    else:
        # Take out the comma and the space, if we're not using them
        s = s[:-5]
    s += '] '
    return s

def print_stack_trace(calls, showFunc, showFile, showPath):
    for i in reversed(stack()[3:]):
        print('\t', get_context(i, showFunc, showFile, showPath), style='trace')

def called_as_decorator(funcName, metadata=None, calls=1) -> 'Union[1, 2, 3, False]':
    """ Return 1 if being used as a function decorator, 2 if as a class decorator, 3 if not sure, and False if neither. """
    if metadata is None:
        metadata = get_metadata(calls+1)

    # print(metadata.code_context)
    context = metadata.code_context
    # I think this means we're using python from the command line
    if context is None:
        return False
    line = context[0]

    if funcName not in line:
        if 'def ' in line:
            return 1
        elif 'class ' in line:
            return 2
        elif '@' in line:
            return 3
    elif '@' in line:
        return 3

    return False

def print_context(calls=1, showFunc=True, showFile=True, showPath=True):
    print_debug_count()
    print(get_context(get_metadata(1 + calls),
                            showFunc or config.display_func,
                            showFile or config.display_file,
                            showPath or config.display_path),
                      end='', style='context')
#%%
def debug(
    var=_None,                # The variable to debug
    name: str=None,           # Don't try to get the name, use this one instead
    color=...,                # A number (0-5), a 3 item tuple/list, or None
    show: Literal['pprint', 'custom', 'repr']='custom',
    showFunc: bool=None,      # Expressly show what function we're called from
    showFile: bool=None,      # Expressly show what file we're called from
    showPath: bool=None,      # Show just the file name, or the full filepath
    # useRepr: bool=False,      # Whether we should print the repr of var instead of str
    calls: int=1,             # Add extra calls
    active: bool=True,        # If this is false, don't do anything
    background: bool=False,   # Whether the color parameter applies to the forground or the background
    # limitToLine: bool=True,   # When printing iterables, whether we should only print items to the end of the line
    # minItems: int=50,         # Minimum number of items to print when printing iterables (overrides limitToLine)
    # maxItems: int=-1,         # Maximum number of items to print when printing iterables, use None or negative to specify no limit
    depth: int=...,
    width: int=...,
    stackTrace: bool=False,   # Print a stack trace
    raiseError: bool=False,   # If var is an error type, raise it
    clr=...,                  # Alias of color
    # repr: bool=False,         # Alias of useRepr
    trace: bool=False,        # Alias of stackTrace
    bg: bool=False,           # Alias of background
    throwError: bool=False,   # Alias of raiseError
    throw: bool=False         # Alias of raiseError
    ) -> "var":
    """ Print variable names and values for easy debugging.

        Usage:
            debug()          -> Prints a standard message to just tell you that it's getting called
            debug('msg')     -> Prints the string along with metadata
            debug(var)       -> Prints the variable name, type, and value
            foo = debug(bar) -> Prints the variable name, type, and value, and returns the variable
            @debug           -> Use as a decorator to make note of when the function is called

        Args:
            var: The variable or variables to print
            name: Manully specify the name of the variable
            color: A number between 0-5, or 3 or 4 tuple/list of color data to print the debug message as
            showFunc: Ensure that the function the current call is called from is shown
            showFile: Ensure that the file the current call is called from is shown
            showPath: Show the full path of the current file, isntead of it's relative path
            useRepr: Use __repr__() instead of __str__() on the given variable
            limitToLine: If var is a list/tuple/dict/set, only show as many items as will fit on one terminal line, overriden by minItems
            minItems: If var is a list/tuple/dict/set, don't truncate more than this many items
            maxItems: If var is a list/tuple/dict/set, don't show more than this many items
            stackTrace: Prints a neat stack trace of the current call
            calls: If you're passing in a return from a function, say calls=2
            background: Changes the background color instead of the forground color
            active: Conditionally disables the function
            clr: Alias of color
            _repr: Alias of useRepr
            trace: Alias of stackTrace
            bg: Alias of background
    """
    if not active or not __debug__:
        return var

    # TODO:
    # Implement rich.inspect
    # implement inspect.ismodule, .ismethod, .isfunction, .isclass, etc.


    stackTrace = stackTrace or trace
    # useRepr = useRepr or repr
    background = background or bg
    throwError = throw or throwError or raiseError
    showFile = showFile or config.display_file
    showFunc = showFunc or config.display_func
    showPath = showPath or config.display_path
    useColor = ('default' if clr is Ellipsis else clr) if color is Ellipsis else color

    if isinstance(var, Warning):
        useColor = 'warn'
    elif isinstance(var, Exception):
        useColor = 'error'

    # if maxItems < 0 or maxItems is None:
        # maxItems = 1000000

    # +1 call because we don't want to get this line, but the one before it
    metadata = get_metadata(calls+1)

    _print_context = lambda: print(get_context(metadata, showFunc, showFile, showPath), end='', style='context')

    #* First see if we're being called as a decorator
    # inspect.
    if callable(var) and called_as_decorator('debug', metadata):
        def wrap(*args, **kwargs):
            # +1 call because we don't want to get this line, but the one before it
            metadata = get_metadata(2)
            print_debug_count()

            if stackTrace:
                print_stack_trace(2, showFunc, showFile, showPath)

            _print_context()  # was of style='note'
            print(f'{var.__name__}() called!', style='note')
            return var(*args, **kwargs)

        return wrap

    print_debug_count()

    if stackTrace:
        print_stack_trace(calls+1, showFunc, showFile, showPath)

    #* Only print the "HERE! HERE!" message
    if var is _None:
        # print(get_context(metadata, showFunc, showFile, showPath), end='', style=clr)
        _print_context()

        if not metadata.function.startswith('<'):
            print(f'{metadata.function}() called ', end='', style=useColor)

        print('HERE!', style=useColor)
        return

    #* Print the standard line
    # print(get_context(metadata, showFunc, showFile, showPath), end='', style='metadata')
    _print_context()

    #* Seperate the variables into a tuple of (typeStr, varString)
    varType = get_typename(var)
    if show == 'repr':
        varVal = _repr(var)
    else:
        if isinstance(var, (tuple, list, set, dict)):
            varVal  = get_iterable_str(var, method=show)
        else:
            varVal  = str(var)

    #* Actually get the name
    varName = get_varname(var, calls=calls, metadata=metadata) if name is None else name

    # It's a string literal
    if varName is None:
        print('<literal> ', end='', style='type')
        print(var, style='value')
        return var

    print(varType, end=' ', style='type')
    print(varName, end=' ', style='name')
    print('=',     end=' ', style='equals')
    print(varVal,           style='value')

    if isinstance(var, Exception) and throwError:
        raise var

    # Does the same this as debugged used to
    return var
#%% Tests
if __name__ == '__main__':
    import sys
    from os.path import join, dirname
    import sys
    sys.path.append(join(dirname( __file__ ), '..'))
    from Cope.debugging import *
    from Cope.colors import parse_color
    #%%
    var = 6
    debug(var)
    #%%

    # def test_getMetaData():
    # print('testing get_metadata')
    # print(get_metadata())

    # def test__debugGetLink():
    # print('testing get_link')
    # print(get_link())

    # def test__debugGetListStr():
    # get_iterable_str([1, 2, 3])

    # def test__debugGetTypename():
    # get_typename('test string literal')

    # def test__debugPrintLink():
    # print_link('testFile.py', 42)

    # def test__printDebugCount():
    # print_debug_count()

    # def test__debugManualGetVarName():
    # get_varname_manually(var)

    # def test__debugGetVarName():
    # get_varname(var)

    # def test__debugGetAdjustedFilename():
    # get_adjusted_filename('testFile.py')

    # def test__debugGetContext():
    # getContext()

    # def test__debugPrintStackTrace():
    # printStackTrace()

    # def test__debugBeingUsedAsDecorator():
    # called_as_decorator('testFunc')

    # def test_printContext():
    # print_context()

    # def test_debug():
    debug()
    a = 6
    s = 'test'
    j = None
    def testFunc():
        print('testFunc called')

    debug(a)
    debug(a, 'apple')

    debug("test3")
    debug(s)
    debug(6)
    debug(None)

    debug(j)
    debug()

    debug(testFunc)

    foo = debug(a)
    debug(foo)

    debug(parseColorParams((5, 5, 5)))

    debug(SyntaxError('Not an error'))
    try:
        debug(SyntaxError('Not an error'), raiseError=True)
    except SyntaxError:
        print('SyntaxError debug test passed!')
    else:
        print('SyntaxError debug test failed.')

    debug(UserWarning('Not a warning'))
    try:
        debug(UserWarning('Not a warning'), raiseError=True)
    except UserWarning:
        print('UserWarning debug test passed!')
    else:
        print('UserWarning debug test failed.')

    @debug
    def testFunc2():
        print('testFunc2 (decorator test) called')

    debug()

    testFunc2()

    debug(None)

    TUPLE = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    LIST  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    DICT  = {'a':1, 'b':2, 'c': 3}
    TYPE_LIST = ['a', 2, 7.4, 3]
    TYPE_TUPLE = ('a', 2, 7.4, 3)

    debug([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], raiseError=True)
    debug((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), raiseError=True)
    debug({'a':1, 'b':2, 'c': 3}, raiseError=True)
    debug(['a', 2, 7.4, 3], raiseError=True)
    debug(('a', 2, 7.4, 3), raiseError=True)
    debug()
    debug(TUPLE, raiseError=True)
    debug(LIST, raiseError=True)
    debug(DICT, raiseError=True)
    debug(TYPE_LIST, raiseError=True)
    debug(TYPE_TUPLE, raiseError=True)

    debug(())
    debug([])
    debug({})
    debug(set())


    # test()

    # CopeConfig.display_file=False
    CopeConfig.display_func=False
    # CopeConfig.display_path=True
    # CopeConfig.root_dir = './.pytest_cache'

    debug()

    # test()