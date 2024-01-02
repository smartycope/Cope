from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.log import *

def test_log():
    log()

def test_warn():
    warn()

def test_unreachableState():
    unreachableState()
