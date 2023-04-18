from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.key import *

def test_KeyStandard():
    KeyStandard()

def test_Key():
    debug(Key('one'))
    debug(Key('exclamation'))
    # debug(Key('exclamationmark'))
    debug(Key('exclamationPoint'))
    # These SHOULD work. __getattr__ is a fickle beast.
    # debug(Key.one)
    # debug(Key.s)
    # debug(Key.ctrl)

    from pynput import keyboard

    def on_press(key):
        debug(key)

        try:
            key = key.char
        except AttributeError:
            pass

        debug(key)
        debug(Key(key))
        debug(Key(key) == key)

    def on_release(key):
        try:
            key = key.char
        except AttributeError:
            pass
        if key == keyboard.Key.esc:
            return False

    debug(keyboard.Key.alt_r)
    debug(invertDict(KeyStandard.pynput)['rightAlt'])
    debug(KeyStandard.pynput[keyboard.Key.alt_r])

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def test_KeyShortcut():
    KeyShortcut()

def test_KeyChord():
    KeyChord()

def test_KeySequence():
    KeySequence()
