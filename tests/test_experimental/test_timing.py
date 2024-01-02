from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.timing import *

def test_timeFunc():
    timeFunc()

def test__printTimingData():
    _printTimingData()

def test_getTime():
    getTime()

def test_psleep():
    psleep()
