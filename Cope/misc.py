# from .decorators import todo, confidence
from .imports import dependsOnPackage
from .debugging import getVarName, beingUsedAsDecorator, debug, getMetaData
from .colors import ERROR
import re
import subprocess
from os.path import join
from random import randint
import sys

from unicodedata import normalize

def available(*args, fail_if_none=True):
    """ Returns the parameter passed to it which is not None, failing if more than one is None,
        and optionally failing if none of them are None """
    from varname import argname

    rtn = None
    name = ''
    for i in args:
        if i is not None:
            if rtn is not None:
                # raise TypeError(f'Please dont specify both {nameof(i, frame=2)} and {name} at the same time')
                raise TypeError(f'Please only specify one of {argname("args")} at a time')
            else:
                rtn = i
    if rtn is None and fail_if_none:
        raise TypeError(f'Please specify at least of one of {argname("args")}')
    return rtn

def have(*obj):
    """ Returns true if all of the parameters are not None """
    yes = True
    for i in obj:
        if i is None:
            yes = False
    return yes

def need(*obj):
    """ Returns true if all of the parameters are None """
    yes = True
    for i in obj:
        if i is not None:
            yes = False
    return yes

def involves(*obj):
    """ Returns true if there's no more than 1 None parameter """
    unknowns = 0
    for i in obj:
        if i is None:
            unknowns += 1
    return unknowns <= 1

def unknown(d: dict, *obj: str):
    """ Returns the only parameter equal to None (or None if there are more or less than 1) """
    # if Counter(d.values())[None] != 1:
    count = 0
    for key in obj:
        if d[key] is None:
            count += 1
            thing = key
    if count != 1:
        return None
    else:
        return thing
        # return debug(invertDict(d)[None], clr=2)
        # return

def known(d: dict, *obj: str):
    """ Returns the dict d without any of the stuff equal to None in it """
    newd = {}
    for key, val in d.items():
        if val is not None:
            newd[key] = val
    return newd

def only1(*args):
    """ Returns true only  if there is only 1 non-None parameter """
    cnt = 0
    for i in args:
        if i is not None:
            cnt += 1
    return cnt == 1


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

def percent(percentage):
    ''' Usage:
        if (percent(50)):
            <code that has a 50% chance of running>
    '''
    return randint(1, 100) < percentage

def randbool():
    """ Returns, randomly, either True or False """
    return bool(randint(0, 1))

def closeEnough(a, b, tolerance):
    """ Returns True if a is within tolerance range of b """
    return a <= b + tolerance and a >= b - tolerance

def findClosestValue(target, comparatorList) -> "value":
    """ Finds the value in comparatorList that is closest to target """
    # dist = max_distance
    # value = None
    # index = 0
    # for cnt, current in enumerate(comparatorList):
    #     currentDist = abs(target - current)
    #     if currentDist < dist:
    #         dist = currentDist
    #         value = current
    #         index = cnt
    # return (value, index)
    return min(comparatorList, key=lambda x: abs(target - x))

def findFurthestValue(target, comparatorList) -> "value":
    """ Finds the value in comparatorList that is furthest from target """
    return max(comparatorList, key=lambda x: abs(target - x))

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
    paramName = getVarName(param)
    if not beingUsedAsDecorator('assertValue'):
        if param not in values:
            err = TypeError(f"Invalid value for {paramName}, must be one of: {values}")
            if blocking:
                raise err
            else:
                debug(err)
    else:
        print('TODO: AssertValue usage as a decorator')

# @confidence(72)
def replaceLine(line, offset=0, keepTabs=True, convertTabs=True, additionalCalls=0):
    """ Replaces the line of code this is called from with the give line parameter.
        This is probably a very bad idea to actually use.
        Don't forget to add tabs! Newline is already taken care of (unless you want to add more).
    """
    meta = getMetaData(calls=2 + additionalCalls)

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
        debug(f"Error: lines don't match, not replacing line.\n\tMetadata: \"{meta.code_context}\"\n\tFile: \"{file[meta.lineno-1]}\"", clr=ERROR)
        return

    with open(meta.filename, 'w') as f:
        f.writelines(file)

# @confidence(85)
def fancyComment(title='', char='#', endChar='#', lineLimit=80):
    """ Replaces the call with a nicely formatted comment line """
    halfLen = ((lineLimit / len(char)) - len(title) - 1 - (2 if len(title) else 0) - len(endChar)) / 2
    seperateChar = ' ' if len(title) else ''

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

@dependsOnPackage('unicodedata', 'normalize')
def slugify(value, allow_unicode=False, allow_space=False, convert_case=True):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
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
