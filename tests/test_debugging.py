from Cope import *


# def test_import():
var = 6
debug(var)

import sys
from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.debugging import *
from Cope.colors import parseColorParams

# def test_getMetaData():
getMetaData()

# def test__debugGetLink():
getLink()

# def test__debugGetListStr():
getListStr([1, 2, 3])

# def test__debugGetTypename():
getTypename('test string literal')

# def test__debugPrintLink():
printLink('testFile.py', 42)

# def test__printDebugCount():
debugCount()

# def test__debugManualGetVarName():
manualGetVarName(var)

# def test__debugGetVarName():
getVarName(var)

# def test__debugGetAdjustedFilename():
getAdjustedFilename('testFile.py')

# def test__debugGetContext():
# getContext()

# def test__debugPrintStackTrace():
# printStackTrace()

# def test__debugBeingUsedAsDecorator():
beingUsedAsDecorator('testFunc')

# def test_printContext():
printContext()

# def test_debug():
debug()
a = 6
s = 'test'
j = None
def testFunc():
    print('testFunc called')

debug(a)
debug(a, 'apple')

debug('test3')
debug(s)

debug(j)
debug()

debug(testFunc)

foo = debug(a)
debug(foo)

debug(parseColorParams((5, 5, 5)) )

debug(SyntaxError('Not an error'))
try:
    debug(SyntaxError('Not an error'), raiseError=True)
except SyntaxError:
    print('SyntaxError debug test passed!')
else:
    print('SyntaxError debug test failed.')

debug(UserWarning('Not a warning'))
try:
    debug(UserWarning('Not a warning'), raiseError=True)
except UserWarning:
    print('UserWarning debug test passed!')
else:
    print('UserWarning debug test failed.')

@debug
def testFunc2():
    print('testFunc2 (decorator test) called')

debug()

testFunc2()

debug(None)

TUPLE = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
LIST  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
DICT  = {'a':1, 'b':2, 'c': 3}
TYPE_LIST = ['a', 2, 7.4, 3]
TYPE_TUPLE = ('a', 2, 7.4, 3)

debug([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], raiseError=True)
debug((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), raiseError=True)
debug({'a':1, 'b':2, 'c': 3}, raiseError=True)
debug(['a', 2, 7.4, 3], raiseError=True)
debug(('a', 2, 7.4, 3), raiseError=True)
debug()
debug(TUPLE, raiseError=True)
debug(LIST, raiseError=True)
debug(DICT, raiseError=True)
debug(TYPE_LIST, raiseError=True)
debug(TYPE_TUPLE, raiseError=True)

debug(())
debug([])
debug({})
debug(set())
