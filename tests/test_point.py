from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.point import *

def test_findClosestXPoint():
    findClosestXPoint()

def test_getPointsAlongLine():
    getPointsAlongLine()

def test_rotatePoint():
    rotatePoint()

def test_getMidPoint():
    getMidPoint()

def test_findClosestPoint():
    findClosestPoint()

def test_collidePoint():
    collidePoint()

def test_getPointDist():
    getPointDist()
