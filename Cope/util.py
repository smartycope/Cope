"""
A bunch of miscellaneous functions and classes that might be useful
"""
__version__ = '2.0.0'

from random import randint
import os
import io
import sys
from typing import *
from itertools import chain
from inspect import isgenerator
from math import pi
from warnings import warn

def percentage(percentage:Union[int, float]) -> float:
    if isinstance(percentage, bool):
        return float(percentage)
    elif percentage > 1:
        return percentage / 100
    return percentage
_percentage = percentage

def percent(percentage:int|float):
    ''' Usage:
        if (percent(50)):
            <code that has a 50% chance of running>
        NOTE: .5 works as well as 50
    '''
    return randint(1, 100) < percentage(percentage)*100

def randbool() -> bool:
    """ Returns, randomly, either True or False """
    return bool(randint(0, 1))

def close_enough(a, b, tolerance):
    """ Returns True if a is within tolerance range of b """
    return a <= b + tolerance and a >= b - tolerance

def closest(target:SupportsInt, compare:Iterable[SupportsInt], index=False) -> int:
    """ Finds the value in `compare` that is closest to `target`.
        Returns the index (if `index` is True), or the value.
        Uses the - operator.
        If there are multiple closest values in the list, it returns the first one
    """
    val = min(compare, key=lambda i: abs(target - i))
    if index:
        return compare.index(val)
    return val

def furthest(target:SupportsInt, compare:Iterable[SupportsInt], index=False) -> int:
    """ Finds the value in `compare` that is furthest from `target`.
        Returns the index (if `index` is True), or the value.
        If there are multiple furthest values in the list, it returns the first one
        Uses the - operator.
    """
    val = max(compare, key=lambda i: abs(target - i))
    if index:
        return compare.index(val)
    return val

def is_power_of_2(x:int) -> bool:
    """ Returns true if x is a power of 2 """
    return (x != 0) and ((x & (x - 1)) == 0)

def between(target, start, end, left_open=False, right_open=False) -> bool:
    """ Returns True if `target` is between start and end """
    return (target >= start if left_open  else target > start) and \
           (target <= end   if right_open else target < end)

def insert_str(string:str, index:int, inserted:str) -> str:
    """ Returns the string with `inserted` inserted into `string` at `index` """
    return string[:index] + inserted + string[index+1:]

def clip(val, low, high):
    """ Constrains `val` to be within `low` and `high` """
    return min(high, max(low, val))

def rescale(
    value:SupportsAbs,
    from_start:SupportsAbs, from_end:SupportsAbs,
    to_start:SupportsAbs,   to_end:SupportsAbs
    ) -> SupportsAbs:
    """ Proportionally maps `value` from being within the `from` range to the `to` range """
    return ((abs(value - from_start) / abs(from_end - from_start)) * abs(to_end - to_start)) + to_start

def frange(start:float, stop:float, skip:float=1.0, accuracy:int=10000000000000000):
    for x in range(int(start*accuracy), int(stop*accuracy), int(skip*accuracy)):
        yield x / accuracy

def confirm(
    prompt:str='Continue?',
    quit:bool=False,
    quit_msg:str='Exiting...',
    return_if_invalid:bool=False,
    include_YN:bool=True,
    ) -> bool:
    """ Prompt the user to confirm via terminal whether to continue or not. If given an invalid response,
        it will continue to ask, unless `return_if_invalid` is set to True.
    """
    response = input(prompt + (" (y/N): " if include_YN else '')).lower()
    if response in ('y', 'yes'):
        return True
    elif response in ('n', 'no'):
        if quit:
            print(quit_msg)
            exit(1)
        return False
    else:
        print('Invalid Input')
        if return_if_invalid:
            return None
        else:
            confirm(prompt, include_YN=include_YN, quit=quit, quit_msg=quit_msg)

def cat_file(f:str) -> str:
    """ Simply return whatever is in the given file path. Just like the Unix `cat` command. """
    with open(f, 'r') as f:
        return f.read()

def ordinal(i:int) -> str:
    """ Return the string name, i.e. 1st, 2nd, 3rd, etc. for the given integer """
    # Wow, English does not make any sense.
    i = str(i)
    if i[-1] == '1' and not i.endswith('11'):
        return i + 'st'
    elif i[-1] == '2' and not i.endswith('12'):
        return i + 'nd'
    elif i[-1] == '3' and not i.endswith('13'):
        return i + 'rd'
    else:
        return i + 'th'

def grade(percentage:Union[float, int]) -> str:
    """ This returns the letter grade given, based on the percentage you have in a class
        NOTE: This is one scale, that represents general accuracy. Your institution may
        use a different scale. As far as I know, there isn't a standardized scale for letter grades.
        Also, come to find out, this is for American grades. The European grade scales are *wildly* different.
    """
    # If we're given a decimal instead of a percentage
    percentage = _percentage(percentage)

    if percentage < .60:
        return 'F'
    elif percentage < .62:
        return 'D-'
    elif percentage < .68:
        return 'D'
    elif percentage < .70:
        return 'D+'
    elif percentage < .73:
        return 'C-'
    elif percentage < .78:
        return 'C'
    elif percentage < .80:
        return 'C+'
    elif percentage < .83:
        return 'B-'
    elif percentage < .88:
        return 'B'
    elif percentage < .90:
        return 'B+'
    elif percentage < .93:
        return 'A-'
    # elif percentage <= 100:
    else:
        return 'A'

def isiterable(obj, include_str:bool=True) -> bool:
    """ Returns True if you can iterate over obj. Optionally excludes strings """
    if isinstance(obj, str):
        return include_str
    # A tuple type, for instance has __iter__, but isn't iterable
    if isinstance(obj, type):
        return False
    return (
        isinstance(obj, Iterable) or
        isgenerator(obj) or
        getattr(obj, '__iter__', False) or
        getattr(obj, '__next__', False)
    )

def ensure_iterable(iter:Iterable, cast:type=list, ensure_cast_type:bool=True):
    """ Ensures that `iter` is an iterable, if it isn't already.
        If `iter` is not an iterable, it'll make it one of type `cast`, and if `ensure_cast_type` is
        True, it will cast `iter` to `cast` as well. Otherwise it returns `iter` unchanged.
        Strings, in this context, don't count as iterables.
    """
    if not isiterable(iter, include_str=False):
        print(iter)
        print(cast)
        return cast((iter, ))
    else:
        if ensure_cast_type:
            return cast(iter)
        else:
            return iter
ensureIterable = ensure_iterable

# TODO Figure out how to test for non-terminating generators
def ensure_not_iterable(iter:Iterable):
    """ Ensures that `iter` is *not* an iterable, IF `iter` only has one element.
        If `iter` has 0 or more than 1 elements, it returns iter unchanged.
        This function works with generators, but they must self-terminate.
        DO NOT PASS INFINITE ITERATORS TO THIS FUNCTION.
        There is no good way to test for them, and they will cause an infinite loop
    """
    if not isiterable(iter):
        return iter

    if isgenerator(iter):
        iter = list(iter)

    if len(iter) == 1:
        return list(iter)[0]

    return iter
ensureNotIterable = ensure_not_iterable


# TODO: Test manually
def in_IPython(return_instance=True):
    try:
        import IPython
    except ImportError:
        return False
    else:
        if (instance := IPython.get_ipython()) is not None:
            return instance if return_instance else True
        else:
            return False

def flatten(iter:Iterable, recursive:bool=True) -> list:
    """ Denest either 1 or all lists inside of `iter` into one big 1 dimentional list. """
    rtn = list(chain(*[ensure_iterable(i) for i in iter]))
    if recursive and any(map(isiterable, rtn)):
        rtn = flatten(rtn, recursive)
    return rtn

def invert_dict(d:dict) -> dict:
    """ Returns the dict given, but with the keys as values and the values as keys. """
    return dict(zip(d.values(), d.keys()))

# Tested manually elsewhere
# TODO: Add tests for this
class RedirectStd:
    def __init__(self, stdout=None, stderr=None):
        if isinstance(stdout, io.TextIOBase):
            self._stdout = stdout
        else:
            self._stdout = open(stdout or os.devnull, 'w')
        if isinstance(stderr, io.TextIOBase):
            self._stderr = stderr
        else:
            self._stderr = open(stderr or os.devnull, 'w')

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        self._stdout.close(); self._stderr.close()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

def unreachable_state(message=''):
    if not __debug__: return
    if message:
        warn(f'Unreachable State Reached: {message}')
    else:
        warn('Unreachable State Reached!')
unreachable = unreachable_state



# TODO: I think this broke
def replace_line(line, offset=0, keepTabs=True, convertTabs=True, calls=0):
    """ Replaces the line of code this is called from with the give line parameter.
        This is a very bad idea and you should not use it
        Automatically adds a newline to the end, but does not automatically add tabs.
    """
    meta = get_metadata(calls=calls+2)

    with open(meta.filename, 'r') as f:
        file = f.readlines()

    # Not really sure of the reason for the -1.
    if file[meta.lineno-1] == meta.code_context[0]:
        if keepTabs:
            tabs = re.match(r'([\t ]+)', file[meta.lineno-1 + offset])
            if tabs:
                line = tabs.group(1) + line

        if convertTabs:
            line = line.replace('\t', '    ')

        file[meta.lineno-1 + offset] = line + '\n'

    else:
        debug(f"Error: lines don't match, not replacing line.\n\tMetadata: \"{meta.code_context}\"\n\tFile: \"{file[meta.lineno-1]}\"", clr=-1)
        return

    with open(meta.filename, 'w') as f:
        f.writelines(file)

# TODO Unfinished
def comment(comment='', line_limit=80, char='=', start='', end='#', capitalize=False):
    """ Replaces the call with a nicely formatted comment line next time the line is run
        NOTE: This is a terrible, terrible function that you should NOT use.
                I'm pretty confident it won't overwrite your source code.
                And it's surprisingly useful.
                But still, use at your own risk.
    """
    if capitalize:
        comment = comment.upper()

    meta = get_metadata(calls=2)

    with open(meta.filename, 'r') as f:
        file = f.readlines()

    # Not really sure of the reason for the -1.
    if file[meta.lineno-1] == meta.code_context[0]:
        tabs = re.match(r'([\t ]+)', file[meta.lineno-1])
        if tabs is None:
            tabs = ''
        else:
            tabs = tabs.group(1)

        if not len(char):
            replace_line('# ' + comment, calls=1)
            return
        if not len(start):
            start = char
        if not len(end):
            end = char

        # Calculate half the distance - comment
        half = (((line_limit // len(char)) - len(comment) - (len(tabs) // 2) - 1 - (2 if len(comment) else 0) - len(end)) // 2) - 1
        # We want the comment to be nicely seperated
        seperateChar = ' ' if len(comment) else ''
        # Add them all together
        c = '#' + start + (char * half) + seperateChar + comment + seperateChar + (char * half)
        # If it doesn't quite reach the max number of characters, make sure it does
        c += ((line_limit - len(c) - len(end)) // len(char)) * char
        c = tabs + c + end
        file[meta.lineno-1] = c + '\n'

    else:
        debug(f"Error: lines don't match, not replacing line.\n\tMetadata: \"{meta.code_context}\"\n\tFile: \"{file[meta.lineno-1]}\"", clr=-1)
        return

    with open(meta.filename, 'w') as f:
        f.writelines(file)


# @todo('Make this use piping and return the command output', False)
def runCmd(args):
    """ Run a command and terminate if it fails. """
    try:
        ec = subprocess.call(' '.join(args), shell=True)
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)
        ec = 1
    if ec:
        sys.exit(ec)

def center(string):
    """ Centers a string for printing in the terminal """
    from os import get_terminal_size
    for _ in range(int((get_terminal_size().columns - len(string)) / 2)): string = ' ' + string
    return string


# TODO: Failing
def insert_newlines(string:str, max_line_length:int) -> str:
    """ Inserts newline characters into `string` in order to keep `string` under `max_line_length`
        characters long, while not inserting a newline in the middle of a word
    """
    # split the string into a list of words
    words = string.split()
    # initialize the result as an empty string
    result = ""
    # initialize the current line as an empty string
    current_line = words[0]
    # iterate over the words in the list
    for word in words[1:]:
        # if the current line plus the next word would exceed the maximum line length,
        # add a newline character to the result and reset the current line
        if len(current_line) + 1 + len(word) > max_line_length:
            result += current_line + "\n"
            current_line = word
        else:
            # add the word to the current line and a space character after it
            current_line += " " + word
    return result

def assertValue(param, *values, blocking=True):
    paramName = get_varname(param)
    if not called_as_decorator('assertValue'):
        if param not in values:
            err = ValueError(f"Invalid value for {paramName}, must be one of: {values}")
            if blocking:
                raise err
            else:
                debug(err)
    else:
        print('TODO: AssertValue usage as a decorator')
