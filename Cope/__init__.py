__version__ = '3.0.0'

msg = 'Dependencies for {0} are not installed. Have you run `pip install Cope[{0}]`?'

# Import submodules
try:
    from . import colors
except ImportError:
    raise ImportError(msg.format('colors'))

try:
    from . import debugging
except ImportError:
    raise ImportError(msg.format('debugging'))

try:
    from . import decorators
except ImportError:
    raise ImportError(msg.format('decorators'))

try:
    from . import gym
except ImportError:
    raise ImportError(msg.format('gym'))

try:
    from . import imports
except ImportError:
    raise ImportError(msg.format('imports'))

try:
    from . import pygame
except ImportError:
    raise ImportError(msg.format('pygame'))

try:
    from . import meme
except ImportError:
    raise ImportError(msg.format('meme'))

try:
    from . import debugging
except ImportError:
    raise ImportError(msg.format('debugging'))

try:
    from . import plotly
except ImportError:
    raise ImportError(msg.format('plotly'))

try:
    from . import streamlit
except ImportError:
    raise ImportError(msg.format('streamlit'))

try:
    from . import sympy
except ImportError:
    raise ImportError(msg.format('sympy'))

try:
    from . import misc
except ImportError:
    raise ImportError(msg.format('misc'))

# Has no dependencies
from . import boilerplate

# All the little stuff
from .util import *
