from .decorators import todo, confidence
from .imports import dependsOnPackage

@todo('Make this use piping and return the command output', False)
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

def assertValue(param, *values, blocking=True):
    paramName = _debugGetVarName(param)
    if not _debugBeingUsedAsDecorator('assertValue'):
        if param not in values:
            err = TypeError(f"Invalid value for {paramName}, must be one of: {values}")
            if blocking:
                raise err
            else:
                debug(err)
    else:
        todo('usage as a decorator')

@confidence(72)
def replaceLine(line, offset=0, keepTabs=True, convertTabs=True, additionalCalls=0):
    """ Replaces the line of code this is called from with the give line parameter.
        This is probably a very bad idea to actually use.
        Don't forget to add tabs! Newline is already taken care of (unless you want to add more).
    """
    meta = _debugGetMetaData(calls=2 + additionalCalls)

    with open(meta.filename, 'r') as f:
        file = f.readlines()

    # Not really sure of the reason for the -1.
    if file[meta.lineno-1] == meta.code_context[0]:
        if keepTabs:
            tabs = rematch(file[meta.lineno-1 + offset], r'\s+')
            if tabs:
                line = tabs.string + line

        if convertTabs:
            line = line.replace('\t', '    ')

        file[meta.lineno-1 + offset] = line + '\n'

    else:
        debug(f"Error: lines don't match, not replacing line.\n\tMetadata: \"{meta.code_context}\"\n\tFile: \"{file[meta.lineno-1]}\"", clr=Colors.ERROR)
        return

    with open(meta.filename, 'w') as f:
        f.writelines(file)

@confidence(85)
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
    value = resub(r'[^\w\s-]', '', value.lower() if convert_case else value)
    return resub(r'[-\n\r\t\v\f]+' if allow_space else r'[-\s]+', '-', value).strip('-_')

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
