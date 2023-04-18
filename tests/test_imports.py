from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.imports import *

def test_ensureImported():
    ensureImported()

def test_checkImport():
    checkImport()

def test_dependsOnPackage():
    dependsOnPackage()

def test_importpath():
    importpath()
