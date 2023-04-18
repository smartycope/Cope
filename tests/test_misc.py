from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.misc import *

def test_runCmd():
    runCmd()

def test_percent():
    percent()

def test_randbool():
    randbool()

def test_closeEnough():
    closeEnough()

def test_findClosestValue():
    findClosestValue()

def test_findFurthestValue():
    findFurthestValue()

def test_center():
    center()

def test_isPowerOf2():
    isPowerOf2()

def test_isBetween():
    isBetween()

def test_insertChar():
    insertChar()

def test_constrain():
    constrain()

def test_translate():
    translate()

def test_frange():
    frange()

def test_portFilename():
    portFilename()

def test_assertValue():
    assertValue()

def test_replaceLine():
    replaceLine("\t\t# This Line has been replaced! 1", -1)
    replaceLine("\t\t# This Line has been replaced! 2")
    replaceLine("# This Line has been replaced! 3")

    # replaceLine("\t\t# This Line has been replaced! 1", -1)
    # replaceLine("\t\t# This Line has been replaced! 2")
    # replaceLine("# This Line has been replaced! 3")


def test_fancyComment():
    fancyComment()
    fancyComment(char='~')
    fancyComment(lineLimit=30)
    fancyComment('Seperator!')
    fancyComment('Seperator!', '~')
    fancyComment('Seperator!', '~', '{')
    fancyComment('Seperator!', '~', '{', 50)

    # fancyComment()
    # fancyComment(char='~')
    # fancyComment(lineLimit=30)
    # fancyComment('Seperator!')
    # fancyComment('Seperator!', '~')
    # fancyComment('Seperator!', '~', '{')
    # fancyComment('Seperator!', '~', '{', 50)


def test_confirm():
    confirm()

def test_slugify():
    slugify()

def test_umpteenthName():
    umpteenthName()
