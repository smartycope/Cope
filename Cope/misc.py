"""
Some command-line utilities that can be useful
"""

__version__ = '1.0.0'

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from random import choice
from sympy import latex, Basic, Float
from clipboard import copy
from Cope.util import ensure_not_iterable

# TODO: add tests
def run_notecards(cards:dict):
    """ A quick function for helping you practice notecards. `cards` is a dict of
        {card front: card back}.
    """
    console = Console()
    cur_front = ''
    cur_back = ''
    print('Press enter for the next card, f to flip the card, b to flip back, and q to quit')
    while (resp := input()) != 'q':
        console.clear()
        if resp == '':
            while (front := choice(list(cards.keys()))) == cur_front: pass
            cur_front = front
            cur_back = cards[front]
            rprint(Panel(front))
        elif resp == 'f':
            rprint(Panel(cur_back))
        elif resp == 'b':
            rprint(Panel(front))

# TODO: add the sigfigs library to include sigfigs
# TODO: change sympy to be an optional dependancy for this (it should still run without it)
def cp(thing=None, rnd:int=3, show=False, not_iterable=True, evalf=True):
    """ Quick shortcut for notebooks for copying things to the clipboard in an easy way"""
    if thing is None:
        thing = _

    if not_iterable:
            thing = ensure_not_iterable(thing)

    if isinstance(thing, Basic) and not isinstance(thing, Float) and not evalf:
        copy(latex(thing))
        if show:
            print('latexing')
    else:
        try:
            if evalf:
                try:
                    thing = thing.evalf()
                except: pass
            if rnd:
                copy(str(round(thing, rnd)))
                if show:
                    print('rounding')
            else:
                raise Exception()
        except:
            copy(str(thing))
            if show:
                print('stringing')
    return thing
