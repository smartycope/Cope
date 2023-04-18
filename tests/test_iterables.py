from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.iterables import *

def test_isiterable():
    isiterable()

def test_isnumber():
    isnumber()

def test_ensureIterable():
    ensureIterable()

def test_ensureNotIterable():
    ensureNotIterable()

def test_flattenList():
    flattenList()

def test_removeDuplicates():
    removeDuplicates()

def test_normalizeList():
    normalizeList()

def test_getIndexWith():
    getIndexWith()

def test_invertDict():
    invertDict()

def test_addDicts():
    addDicts()

def test_LoopingList():
    LoopingList()

def test_MappingList():
    debug(MappingList())
    debug(MappingList(1, 2, 3))
    debug(MappingList((1, 2, 3)))
    debug(MappingList([1, 2, 3]))
    m = MappingList(1, 2, 3)
    debug(m)
    debug(m+3)
    debug(m-3)
    m += 4
    debug(m)

    m = MappingList('hello', 'world')
    debug(m)
    m += '!'
    debug(m)
    try:
        debug(m / 4)
    except AttributeError:
        print('First Error test worked')
    else:
        print('First Error test failed')

    debug(MappingList(1, 2, 3) * MappingList(2, 2, 4))
    # try:
        # debug(MappingList(1, 2, 3) * MappingList(2, 2))
    # except TypeError:
        # print('Second error test worked')
    # else:
        # print('Second error test failed')
    # debug(MappingList(1, 2, 3) * MappingList(2))
    debug(MappingList(1, 2, 3) * 2)

    t = MappingList('testing')
    debug(t)
    debug(t+' success')
    debug(t.istitle)
    debug(t.replace('t', '|'))
    debug(t.upper())
    t += ' tests'
    debug(t)

def test_ZerosDict():
    ZerosDict

def test_MultiAccessDict():
    MultiAccessDict

def test_ZerosMultiAccessDict():
    ZerosMultiAccessDict
