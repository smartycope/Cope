<!-- <div align="center"> -->
<a href="https://github.com/smartycope/Cope/actions/workflows/unit-tests.yml">
    <img src="https://github.com/smartycope/Cope/actions/workflows/unit-tests.yml/badge.svg" alt="Unit Tests">
</a>
<a href="https://pypi.org/project/Cope/">
    <img src="https://img.shields.io/pypi/v/Cope.svg" alt="PyPI Latest Release">
</a>
<!-- </div> -->


# Cope
## NOTE:
```
The API is under active development, and is *not* stable. Make sure to freezed versions if you're going to use it, really at all.
Also, test coverage is mostly manual, and sparse.
```

This is my personal "standard library" of all the generally useful code I've written for various projects over the years. Pretty much any time I've written a function or class and thought "this might be useful later", I've stuffed it in here.


**Table of Contents**
* [Modules](#modules)
* [Documentation](#documentation)
* [Organization](#organization)
* [Installation](#installation)
* [License](#license)


## Modules
These are the currently available modules. In order to use any of them, you have to install the optional dependencies with `pip install Cope[module]`, which will install the required packages for that module.

The main `Cope` namespace is full of small, dependency-less functions and a couple classes that are generally useful for a number of applications.
* sympy
    * Some useful functions built on top of the sympy library
* plotly
    * Currently, just a single function to build a ridgeplot in plotly
* streamlit
    * Currently, just the `SS` class, which is a much simpler abstraction of st.session_state
* misc
    * Functions and classes that don't really fit anywhere else. Right now, it's just a function that runs notecards with you in the command line
* meme
    * Meme code! Right now, just a function that takes any graph, and automatically sticks it in the *look at that graph!* Nickleback meme.
* gym
    * Includes the SimpleGym class, which adds some features to the gymnasium (formerly gym) library
* debug
    * Code useful for debugging, including the `debug` function
* decorators
    * Some useful decorators
* pygame
    * Some functions relating to the pygame library
* boilerplate
    * Right now, just a class that holds a bunch of common responses. Not terribly useful.
* linalg
    * Some linear algebra functions & classes to make linear algebra easier, including a matrix() function to make inputting matricies easier. I wrote it all for a college class I took, and there's probably libraries out there that are much better. Most of it *probably* works?
* math
    * Doesn't have any external dependencies, but is a module. Has some extra math functions that are useful.


## Documentation
I don't have proper documentation yet. I need to learn a doc generator or two to learn to use those. Meanwhile, all the relevant documentation for each of the classes & functions should be in their doc strings.


## Installation
Cope is distributed on [PyPI](https://pypi.org) as a universal wheel and is available on Linux/macOS and Windows and supports Python 3.8+ and PyPy.

```bash
$ pip install Cope
$ pip install Cope[module]
```


## Why "Cope"?
My name is Copeland. Whenever I was learning a language, I would create a file called `Cope.*` for the language to import useful code I couldn't find in the standard libraries. As I learned to search for *libraries* before doing everything myself, a lot of it became less relevant. But some of it is still very useful, and eventually I decided to publish it, if only to make it easier to use for myself.


## License
Cope is distributed under the [MIT License](https://choosealicense.com/licenses/mit)
