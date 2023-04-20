import math
# from .misc import constrain
# Default color constants
DEFAULT = (204, 204, 204)
ALERT   = (220, 0, 0)
WARN    = (150, 30, 30)
ERROR   = ALERT

# Default colors for debugging -- None for using the previously set color
NOTE_CALL          = (211, 130, 0)
EMPTY              = NOTE_CALL
CONTEXT            = None
COUNT              = (34, 111, 157)
DEFAULT_DEBUG      = (34, 179, 99)
TODO               = (128, 64, 64)
STACK_TRACE        = (159, 148, 211)
CONFIDENCE_WARNING = (255, 190, 70)
DEPRICATED_WARNING = WARN
LOG_COLOR          = (100, 130, 140)

DEBUG_EQUALS          = DEFAULT
DEBUG_METADATA_DARKEN = 70
DEBUG_TYPE_DARKEN     = 10
DEBUG_NAME_DARKEN     = -60
DEBUG_VALUE_DARKEN    = 0


def distinctColor(n: int) -> tuple:
    # First, ensure if it's 0, we return black
    if n == 0:
        return 0, 0, 0
    angle = n * 137.508
    r = int(math.sin(angle) * 127 + 128)
    g = int(math.sin(angle + 2 * math.pi / 3) * 127 + 128)
    b = int(math.sin(angle + 4 * math.pi / 3) * 127 + 128)
    return r, g, b

def resetColor():
    print('\033[0m',  end='')
    print('\033[39m', end='')
    print('\033[49m', end='')
    # print('', end='')

#todo Add support for openGL colors (-1.0 to 1.0)
#todo Consider changing the param paradigm to *rgba instead of all seperate parameters
#todo add support for QColor
def parseColorParams(r, g=None, b=None, a=None, bg=False) -> "((r, g, b, a), background)":
    """ Parses given color parameters and returns a tuple of equalized
        3-4 item tuple of color data, and a bool for background.
        Can take 3-4 tuple/list of color data, or r, g, and b as induvidual parameters,
        and a single int (0-5) representing a preset unique color id.
        a and bg are always available as optional or positional parameters.

        Note: Seperate color specifications for foreground and background are not currently
        supported. bg is just a bool.
    """
    #* We've been given the name of a color
    if type(r) is str:
        raise NotImplementedError("parseColorParams does not yet support named colors")
    #* We've been given a list of values
    elif isinstance(r, (tuple, list)):
        if len(r) not in (3, 4):
            raise SyntaxError(f'Incorrect number ({len(r)}) of color parameters given')
        else:
            return (tuple(r), ((False if g is None else g) if not bg else bg))

    #* We've been given a single basic value
    elif type(r) is int and b is None:
        return (distinctColor(r) + ((a,) if a is not None else ()), (False if g is None else g) if not bg else bg)

    #* We've been given 3 seperate parameters
    elif type(r) is int and g is not None and b is not None:
        if type(a) is int:
            return ((r, g, b, a), bg)
        elif type(a) is bool or a is None:
            return ((r, g, b), bool(a) if not bg else bg)

    #* We've probably been given a QColor
    elif hasattr(r, 'rgba'):
        return ((r.red(), r.green(), r.blue(), r.alpha()), bg)

    #* We've been given None
    elif r is None:
        return (DEFAULT, bg)

    #* We're not sure how to interpret the parameters given
    else:
        raise SyntaxError(f'Incorrect color parameters {tuple(type(i) for i in (r, g, b, a, bg))} given')

class coloredOutput:
    """ A class to be used with the 'with' command to print colors.
        Resets after it's done.
        @Parameters:
            Takes either a 3 or 4 list/tuple of color arguements, 3 seperate
            color arguements, or 1 color id between 0-5 representing a distinct
            color. Set the curColor parameter (must be a 3 or 4 item list/tuple)
            to have the terminal reset to that color instead of white.
        https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
    """
    def __init__(self, r, g=None, b=None, foreground=True, curColor=DEFAULT):
        color, bg = parseColorParams(r, g, b, bg=foreground)
        self.fg = bg
        self.r, self.g, self.b = color
        self.doneColor = curColor

    def __enter__(self):
        try:
            if self.fg:
                print(f'\033[38;2;{self.r};{self.g};{self.b}m', end='')
            else:
                print(f'\033[48;2;{self.r};{self.g};{self.b}m', end='')
        except:
            self.reset()

    def __exit__(self, *args):
        self.reset()

    def reset(self):
        print(f'\033[38;2;{self.doneColor[0]};{self.doneColor[1]};{self.doneColor[2]}m', end='')

def rgbToHex(rgb):
    """ Translates an rgb tuple of int to a tkinter friendly color code """
    return f'#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}'

def darken(amount, r, g=None, b=None, a=None):
    """ Returns the given color, but darkened. Make amount negative to lighten """
    # Constrain isn't defined yet and I don't feel like moving it
    return tuple([min(255, max(0, i - amount)) for i in parseColorParams(r, g, b, a)[0]])

def lighten(amount, r, g=None, b=None, a=None):
    """ Returns the given color, but darkened. Make amount negative to darken """
    return tuple([min(max(i + amount, 0), 255) for i in parseColorParams(r, g, b, a)[0]])

def clampColor(r, g=None, b=None, a=None):
    """ Clamp a 0-255 color to a float between 1 and 0.
        Helpful for openGL commands.
    """
    rgba = parseColorParams(r, g, b, a)[0]
    return tuple(c / 255 for c in rgba)

def invertColor(r, g=None, b=None, a=None):
    """ Inverts a color """
    rgba = parseColorParams(r, g, b, a)[0]
    # print(rgba)
    # return tuple(255 - c for c in rgba[0])
    return tuple(255 - c for c in rgba)

def printColor(s, color=DEFAULT, **kwargs):
    with coloredOutput(color):
        print(s, **kwargs)
