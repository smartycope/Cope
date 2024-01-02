# from .decorators import todo, confidence
from .imports import dependsOnPackage
from .debugging import get_varname, called_as_decorator, debug, get_metadata
# from .colors import ERROR
import re
import subprocess
from os.path import join
from random import randint
import sys
# from math import floor
from unicodedata import normalize

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

def isPowerOf2(x):
    """ Returns true if x is a power of 2 """
    return (x != 0) and ((x & (x - 1)) == 0)

def isBetween(val, start, end, beginInclusive=False, endInclusive=False):
    """ Returns true if val is between start and end """
    return (val >= start if beginInclusive else val > start) and \
           (val <= end   if endInclusive   else val < end)

def insertChar(string, index, char):
    """ Returns the string with char inserted into string at index. Freaking python string are immutable. """
    return string[:index] + char + string[index+1:]

def constrain(val, low, high):
    """ Constrains val to be within low and high """
    return min(high, max(low, val))

def translate(value, fromStart, fromEnd, toStart, toEnd):
    return ((abs(value - fromStart) / abs(fromEnd - fromStart)) * abs(toEnd - toStart)) + toStart

def frange(start, stop, skip=1.0, accuracy=10000000000000000):
    return [x / accuracy for x in range(int(start*accuracy), int(stop*accuracy), int(skip*accuracy))]

def portFilename(filename):
    return join(*filename.split('/'))

def insert_newlines(string, max_line_length):
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

def assertValue(param, *values, blocking=True):
    paramName = get_varname(param)
    if not called_as_decorator('assertValue'):
        if param not in values:
            err = TypeError(f"Invalid value for {paramName}, must be one of: {values}")
            if blocking:
                raise err
            else:
                debug(err)
    else:
        print('TODO: AssertValue usage as a decorator')

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

def comment(comment='', char='#', start='', end='', line_limit=80):
    """ Replaces the call with a nicely formatted comment line next time the line is run
        CAVIAT: This is a terrible, terrible function that you should NOT use.
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

def confirm(prompt='Continue?', returnIfInvalid=False, failedFunc=lambda: None, includeYN=True, quit=False, quitMsg='Okay then, exiting...'):
    response = input(prompt + (" (y/N): " if includeYN else '')).lower()
    if response in ('y', 'yes'):
        return True
    elif response in ('n', 'no'):
        if quit:
            print(quitMsg)
            exit(1)
        else:
            failedFunc()
        return False
    else:
        print('Invalid Input')
        if returnIfInvalid:
            return None
        else:
            confirm(prompt, failedFunc=failedFunc, includeYN=includeYN, quit=quit, quitMsg=quitMsg)

def slugify(value, allow_unicode=False, allow_space=False, convert_case=True):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    from unicodedata import normalize
    value = str(value)
    if allow_unicode:
        value = normalize('NFKC', value)
    else:
        value = normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower() if convert_case else value)
    return re.sub(r'[-\n\r\t\v\f]+' if allow_space else r'[-\s]+', '-', value).strip('-_')

def catFile(f):
    with open(f, 'r') as f:
        return f.read()

# No, English does not make any sense.
def umpteenthName(i:int) -> "1st, 2nd, 3rd, etc.":
    i = str(i)
    if i[-1] == '1' and (i != '11'):
        return i + 'st'
    elif i[-1] == '2' and (i[0] != '1'):
        return i + 'nd'
    elif i[-1] == '3' and (i[0] != '1'):
        return i + 'rd'
    else:
        return i + 'th'

def letterGrade(percentage):
    # If we're given a decimal instead of a percentage
    if percentage < 1:
        percentage *= 100

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
    # else:
        # unreachableState()

def cp(thing=None, rnd=3, show=False, notIterable=True, evalf=True):
    from sympy import latex
    from clipboard import copy
    if thing is None:
        thing = _

    if notIterable:
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

def inIPython(return_instance=True):
    try:
        import IPython
    except ImportError:
        return False
    else:
        if (instance := IPython.get_ipython()) is not None:
            return instance if return_instance else True
        else:
            return False
