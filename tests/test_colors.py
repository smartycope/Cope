from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.colors import *

def test_resetColor():
    resetColor()

def test_parseColorParams():
    debug(parseColorParams((5, 5, 5)) )
    debug(parseColorParams((5, 5, 5), True) )
    debug(parseColorParams((5, 5, 5, 6)) )
    debug(parseColorParams((5, 5, 5, 6), True) )
    debug(parseColorParams([5, 5, 5, 6]) )
    debug(parseColorParams(5, 5, 5) )
    debug(parseColorParams(5, 5, 5, True) )
    debug(parseColorParams(5, 5, 5, 6) )
    debug(parseColorParams(5, 5, 5, bg=True) )
    debug(parseColorParams(5, 5, 5, 6, True) )
    debug(parseColorParams(3) )
    debug(parseColorParams(3, bg=True))
    debug(parseColorParams((3,)) ) # Succeeded
    debug(parseColorParams(3, a=6) )
    debug(parseColorParams(3, a=6, bg=True) )
    debug(parseColorParams(None) )
    debug(parseColorParams(None, bg=True) )

def test_rgbToHex():
    rgbToHex()

def test_darken():
    darken()

def test_lighten():
    lighten()

def test_clampColor():
    clampColor()

def test_invertColor():
    invertColor()

def test_printColor():
    printColor()

def test_coloredOutput():
    coloredOutput