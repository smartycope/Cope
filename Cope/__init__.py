__version__ = '2.1.0'

# Make these submodules
from . import boilerplate
from . import experimental
from . import pygame
from . import plotly
# Dump everything in these directly into the main module
from .misc import *
from .decorators import *
