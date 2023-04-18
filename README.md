# Cope

This is my personal "standard library" of all the generally useful code I've written for various projects over the years. Pretty much any time I've written a function or class and thought "this might be useful later", I've stuffed it in here. As such, a lot of it is super useful, a lot of it is garbage, and a lot of it has become obsoleted as I've learned more and found new libraries. I've tried to keep it clean and organized, but there is a lot of it.
I also have tests written for a bunch of it, but not all.
The debug function in particular I'm especially proud of. I've spent more time than is reasonable on it.






## Ignore this
This needs to go somewhere eventually

DECORATOR SYNTAX:

def decorator(*decoratorArgs, **decoratorKwArgs):
    def wrap(functionBeingDecorated):
        def innerWrap(*decoratedArgs, **decoratedKwArgs):
            return functionBeingDecorated(*decoratedArgs, **decoratedKwArgs)
        return innerWrap
    return wrap

COPY version:

def decorator(*decoratorArgs, **decoratorKwArgs):
    def wrap(func):
        def innerWrap(*funcArgs, **funcKwArgs):
            return func(*funcArgs, **funcKwArgs)
        return innerWrap
    return wrap
