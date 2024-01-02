import re
from random import randint
from typing import *
from .debugging import get_metadata

def available(*args, null=None) -> list:
    """ Of the parameters passed, returns the parameters which are not `null` """
    return list(filter(lambda i: i != null, args))

# TODO: Tests
def only1(*args, null=None) -> bool:
    """ Returns true only if there is only 1 non-`null` parameter """
    return len(available(*args, null=null)) == 1

# TODO: Tests
def interpret_percentage(percentage:Union[int, float]) -> float:
    if percentage > 1:
        return percentage / 100
    return percentage

# TODO: Tests
def percent(percentage:Union[int, float]):
    ''' Usage:
        if (percent(50)):
            <code that has a 50% chance of running>
        NOTE: .5 works as well as 50
    '''
    return randint(1, 100) < interpret_percentage(percentage)*100

# TODO: Tests
def randbool() -> bool:
    """ Returns, randomly, either True or False """
    return bool(randint(0, 1))

# TODO: Tests
def close_enough(a, b, tolerance):
    """ Returns True if a is within tolerance range of b """
    return a <= b + tolerance and a >= b - tolerance

# TODO: Tests
def closest_index(target:SupportsInt, compare:Iterable[SupportsInt], index=False) -> int:
    """ Finds the value in `compare` that is closest to `target`.
        Returns the index (if `index` is True), or the value.
        Uses the - operator.
    """
    val = min(compare, key=lambda i: abs(target - i))
    if index:
        return compare.index(val)
    return val

# TODO: Tests
def furthest_index(target:SupportsInt, compare:Iterable[SupportsInt], index=False) -> int:
    """ Finds the value in `compare` that is furthest from `target`.
        Returns the index (if `index` is True), or the value.
        Uses the - operator.
    """
    val = max(compare, key=lambda i: abs(target - i))
    if index:
        return compare.index(val)
    return val

# TODO: Tests
def isPowerOf2(x:int) -> bool:
    """ Returns true if x is a power of 2 """
    return (x != 0) and ((x & (x - 1)) == 0)

# TODO: Tests
def between(target, start, end, left_open=False, right_open=False) -> bool:
    """ Returns True if `target` is between start and end """
    return (target >= start if left_open  else target > start) and \
           (target <= end   if right_open else target < end)

# TODO: Tests
def insert_str(string:str, index:int, inserted:str) -> str:
    """ Returns the string with `inserted` inserted into `string` at `index` """
    return string[:index] + inserted + string[index+1:]

# TODO: Tests
def constrain(val, low, high):
    """ Constrains `val` to be within `low` and `high` """
    return min(high, max(low, val))

# TODO: Tests
def translate(
    value:SupportsAbs,
    from_start:SupportsAbs, from_end:SupportsAbs,
    to_start:SupportsAbs,   to_end:SupportsAbs
    ) -> SupportsAbs:
    """ Proportionally maps `value` from being within the `from` range to the `to` range """
    return ((abs(value - from_start) / abs(from_end - from_start)) * abs(to_end - to_start)) + toStart

# TODO: Tests
def frange(start:float, stop:float, skip:float=1.0, accuracy:int=10000000000000000):
    # return (x / accuracy for x in range(int(start*accuracy), int(stop*accuracy), int(skip*accuracy)))
    for x in range(int(start*accuracy), int(stop*accuracy), int(skip*accuracy)):
        yield x / accuracy

# TODO: Tests
def insert_newlines(string:str, max_line_length:int) -> str:
    """ Inserts newline characters into `string` in order to keep `string` under `max_line_length`
        characters long, while not inserting a newline in the middle of a word
    """
    # split the string into a list of words
    words = string.split()
    # initialize the result as an empty string
    result = ""
    # initialize the current line as an empty string
    current_line = ""
    # iterate over the words in the list
    for word in words:
        # if the current line plus the next word would exceed the maximum line length,
        # add a newline character to the result and reset the current line
        if len(current_line) + len(word) > max_line_length:
            result += "\n"
            current_line = ""
        # add the word to the current line and a space character after it
        current_line += word + " "
        # add the current line to the result
        result += current_line
    return result

def replaceLine(line, offset=0, keepTabs=True, convertTabs=True, calls=0):
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
            tabs = re.match(file[meta.lineno-1 + offset], r'\s+')
            if tabs:
                line = tabs.string + line

        if convertTabs:
            line = line.replace('\t', '    ')

        file[meta.lineno-1 + offset] = line + '\n'

    else:
        debug(f"Error: lines don't match, not replacing line.\n\tMetadata: \"{meta.code_context}\"\n\tFile: \"{file[meta.lineno-1]}\"", clr=-1)
        return

    with open(meta.filename, 'w') as f:
        f.writelines(file)

# TODO: make this respect tabs at the beginning of a line
def comment(comment='', char='#', start='', end='', line_limit=80):
    """ Replaces the call with a nicely formatted comment line next time the line is run
        NOTE: This is a terrible, terrible function that you should NOT use.
                I'm pretty confident it won't overwrite your source code.
                And it's surprisingly useful.
                But still, use at your own risk.
    """
    if not len(char):
        replaceLine('# ' + comment, calls=1)
        return
    if not len(start):
        start = char
    if not len(end):
        end = char

    # Calculate half the distance - comment
    half = (((line_limit // len(char)) - len(comment) - 1 - (2 if len(comment) else 0) - len(end)) // 2) - 1
    # We want the comment to be nicely seperated
    seperateChar = ' ' if len(comment) else ''
    # Add them all together
    c = '#' + start + (char * half) + seperateChar + comment + seperateChar + (char * half)
    # If it doesn't quite reach the max number of characters, make sure it does
    c += ((line_limit - len(c) - len(end)) // len(char)) * char
    replaceLine(c + end, calls=1)

# TODO: Tests
def confirm(
    prompt:str='Continue?',
    quit:bool=False,
    quit_msg:str='Exiting...',
    return_if_invalid:bool=False,
    include_YN:bool=True,
    ) -> bool:
    """ Promt the user to confirm via terminal whether to continue or not. If given an invalid response,
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

# TODO: Tests
def cat_file(f:str) -> str:
    """ Simply return whatever is in the given file path. Just like the Unix `cat` command. """
    with open(f, 'r') as f:
        return f.read()

# TODO: Tests
def umpteenth(i:int) -> str:
    """ Return the string name, i.e. 1st, 2nd, 3rd, etc. for the given integer """
    # Wow, English does not make any sense.
    i = str(i)
    if i[-1] == '1' and (i != '11'):
        return i + 'st'
    elif i[-1] == '2' and (i[0] != '1'):
        return i + 'nd'
    elif i[-1] == '3' and (i[0] != '1'):
        return i + 'rd'
    else:
        return i + 'th'

# TODO: Tests
def grade(percentage:Union[float, int]) -> str:
    """ This returns the letter grade given, based on the percentage you have in a class """
    # If we're given a decimal instead of a percentage
    percentage = interpret_percentage(percentage)

    if percentage < 61:
        return 'F'
    elif percentage < 64:
        return 'D-'
    elif percentage < 67:
        return 'D'
    elif percentage < 70:
        return 'D+'
    elif percentage < 74:
        return 'C-'
    elif percentage < 77:
        return 'C'
    elif percentage < 80:
        return 'C+'
    elif percentage < 84:
        return 'B-'
    elif percentage < 87:
        return 'B'
    elif percentage < 90:
        return 'B+'
    elif percentage < 94:
        return 'A-'
    elif percentage < 100:
        return 'A'

# TODO
def sigfigs(num:float, sigfigs=3) -> str:
    """ After all the STEM classes I've taken, I *still* don't understand how sigfigs work. """
    NotImplemented

# TODO: Tests, and make this use sigfigs instead
def cp(thing=None, rnd:int=3, show=False, not_iterable=True, evalf=True):
    """ Quick shortcut for notebooks for copying things to the clipboard in an easy way"""
    from sympy import latex, Basic, Float
    from clipboard import copy

    if thing is None:
        thing = _

    if not_iterable:
            thing = ensureNotIterable(thing)

    if isinstance(thing, Basic) and not isinstance(thing, Float) and not evalf:
        copy(latex(thing))
        if show:
            print('latexing')
    else:
        try:
            if evalf:
                try:
                    thing = thing.evalf()
                except: pass
            if rnd:
                copy(str(round(thing, rnd)))
                if show:
                    print('rounding')
            else:
                raise Exception()
        except:
            copy(str(thing))
            if show:
                print('stringing')
    return thing


class CommonResponses:
    """ A collection of default responses for inputs. Make sure to use .lower() when testing agaisnt these.
        Note: There is some overlap between them, so testing order matters.
    """
    YES   = ('y', 'yes', 'ya', 'yeah', 'si', 'true', 'definitely', 'accurate', 'totally')
    NO    = ('n', 'no', 'not', 'nien', 'false', 'nope', 'not really', 'nah')
    MAYBE = ('sure', 'kinda', 'i guess', 'kind of', 'maybe', 'ish', 'sorta')
    NA    = ('none', 'na', 'n/a', 'not applicable')
    HIGH_AMOUNT = ('very', 'much', 'very much', 'extremely', 'quite', 'quite a bit', 'lot', 'a lot', 'lots',
                   'super', 'high', 'ton', 'a ton', 'bunch', 'a bunch')
    MODERATE_AMOUNT = ('fairly', 'somewhat', 'enough')
    SOME_AMOUNT = ('a little bit', 'a bit', 'a little', 'ish', 'not a lot', 'not a ton', 'some', 'mostly')
    LOW_AMOUNT  = ("not at all", 'not very', 'not much', 'low', 'none', 'none at all', 'not terribly')

# TODO: Tests... somehow?
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
