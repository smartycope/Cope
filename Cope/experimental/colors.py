import math
# import color-names
from typing import Tuple, Literal

def distinctColor(n: int) -> tuple:
    # First, ensure if it's 0, we return black
    if n == 0:
        return 0, 0, 0
    angle = n * 137.508
    r = int(math.sin(angle) * 127 + 128)
    g = int(math.sin(angle + 2 * math.pi / 3) * 127 + 128)
    b = int(math.sin(angle + 4 * math.pi / 3) * 127 + 128)
    return r, g, b

#todo Add support for openGL colors (-1.0 to 1.0)
#todo Consider changing the param paradigm to *rgba instead of all seperate parameters
#todo add support for QColor
def parse_color(*args, rtn:Literal[tuple, 'html', 'tuple']=tuple, **kwargs) -> Tuple[int, int, int, int]:
    """ One color function to rule them all!

        Parses given color parameters and returns a tuple of equalized
        3-4 item tuple of color data, and a bool for background.
        Can take 3-4 tuple/list of color data, or r, g, and b as induvidual parameters,
        and a single int (0-5) representing a preset unique color id.
        a and bg are always available as optional or positional parameters.

        Note: Seperate color specifications for foreground and background are not currently
        supported. bg is just a bool.
    """
    if isinstance(r, str):
        # We've been given a hex string
        if r.startswith('#'):
            r, g, b = map(lambda n: int(n, 16), r[1::2])
        # We've been given the name of a color
        else:
            raise NotImplementedError("parseColorParams does not yet support named colors")

    #* We've been given a list of values
    elif isinstance(r, (tuple, list)):
        if len(r) not in (3, 4):
            raise SyntaxError(f'Incorrect number ({len(r)}) of color parameters given')
        else:
            return (tuple(r), ((False if g is None else g) if not bg else bg))

    #* We've been given a single basic value
    elif isinstance(r, int) and b is None:
        return (distinctColor(r) + ((a,) if a is not None else ()), (False if g is None else g) if not bg else bg)

    #* We've been given 3 seperate parameters
    elif isinstance(r, int) and g is not None and b is not None:
        if isinstance(a, int):
            return ((r, g, b, a), bg)
        elif isinstance(a, bool) or a is None:
            return ((r, g, b), bool(a) if not bg else bg)

    #* We've probably been given a QColor
    elif hasattr(r, 'rgba'):
        return ((r.red(), r.green(), r.blue(), r.alpha()), bg)

    #* We've been given None
    elif r is None:
        return (DEFAULT, bg)

    # Now handle keyword args. If a keyword arg is specified, it should override other methods

    #* We're not sure how to interpret the parameters given
    else:
        raise SyntaxError(f'Incorrect color parameters {tuple(type(i) for i in (r, g, b, a, bg))} given')

def rgb2hex(rgb):
    """ Translates an rgb tuple of int to a hex color code """
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
