from ._None import _None
from .decorators import todo
from typing import Union, Callable, Iterable

def isiterable(obj, includeStr=False):
    return isinstance(obj, Iterable) and (type(obj) is not str if not includeStr else True)

def isnumber(obj):
    # return isinstance(obj, (int, float))
    try:
        float(obj)
    except:
        return False
    else:
        return True

def ensureIterable(obj, useList=False):
    if not isiterable(obj):
        return [obj, ] if useList else (obj, )
    else:
        return obj

def ensureNotIterable(obj, emptyBecomes=_None):
    if isiterable(obj):
        # Generators are iterable, but don't inherantly have a length
        try:
            len(obj)
        except:
            obj = list(obj)

        if len(obj) == 1:
            try:
                return obj[0]
            except TypeError:
                return list(obj)[0]
        elif len(obj) == 0:
            return obj if emptyBecomes is _None else emptyBecomes
        else:
            return obj
    else:
        return obj

def flattenList(iterable, recursive=False, useList=True):
    if recursive:
        raise NotImplementedError

    useType = list if useList else type(iterable)
    rtn = useType()
    for i in iterable:
        rtn += useType(i)
    return rtn
    # print(flattenList(('a', 'b', [1, 2, 3]), useList=False))

def findIndex(iter, value):
    #Finds index in list l that is closest to value.
    #Uses a binary search.
    low = 0
    high = len(iter)-1
    while low+1 < high:
        mid = (low+high) // 2
        if iter[mid] > value:
            high = mid
        elif iter[mid] < value:
            low = mid
        else:
            return mid
    if abs(iter[high]-value) < abs(iter[low]-value):
        return high
    else:
        return low

def removeDuplicates(iterable, method='sorted set'):
    method = method.lower()
    if method == 'set':
        return type(iterable)(set(iterable))
    elif method == 'sorted set':
        return list(sorted(set(iterable), key=lambda x: iterable.index(x)))
    elif method == 'generator':
        seen = set()
        for item in seq:
            if item not in seen:
                seen.add(item)
                yield item
    elif method == 'manual':
        dups = {}
        newlist = []
        for x in biglist:
            if x['link'] not in dups:
                newlist.append(x)
                dups[x['link']] = None
    elif method == 'other':
        seen_links = set()
        for index in len(biglist):
            link = biglist[index]['link']
            if link in seen_links:
                del(biglist[index])
            seen_links.add(link)
    else:
        raise TypeError(f'Unknown removeDuplicates method: {method}. Options are: (set, sorted set, generator, manual, other)')

# def removeRedundant(iterable):
    # """ Remove any lists with only """
    # if len(iterable) == 1:

    # for i in iterable:
    #     if isiterable(i) and

# @confidence(10)
def normalizeList(iterable, ensureList=False):
    debug()
    if ensureList:
        return list(removeDuplicates(flattenList(ensureIterable(list(iterable), True))))
    else:
        return list(ensureNotIterable(removeDuplicates(flattenList(ensureIterable(list(iterable), True)))))

def getIndexWith(obj, key):
    """ Returns the index of the first object in a list in which key returns true to.
    Example: getIndexWith([ [5, 3], [2, 3], [7, 3] ], lambda x: x[0] + x[1] == 10) -> 2
    If none are found, returns None
    """
    for cnt, i in enumerate(obj):
        if key(i):
            return cnt
    return None

def invertDict(d):
    """ Returns the dict given, but with the keys as values and the values as keys. """
    return dict(zip(d.values(), d.keys()))

def addDicts(*dicts):
    """ Basically the same thing as Dict.update(), except returns a copy
        (and can take multiple parameters)
    """
    rtn = {}
    for d in dicts:
        rtn.update(d)
    return rtn

# @todo
class LoopingList(list):
    """ It's a list, that, get this, loops!
    """
    def __getitem__(self, index):
        if index > self.__len__():
            return super().__getitem__(index % self.__len__())
        else:
            return super().__getitem__(index)


# TODO add the __roperator__ functions
class MappingList(list):
    """ An iterable that functions exactly like a list, except any operators applied to it
        are applied equally to each of it's memebers, and return a mapping list instance.
    """
    unmatchedLenError = TypeError('Cannot evaluate 2 MappingLists of differing length')

    def __init__(self, *args):
        super().__init__(ensureIterable(ensureNotIterable(args)))

    def apply(self, func:Union[Callable, 'MappingList'], *args, **kwargs):
        """ Call a function with parameters on each item """
        if type(func) is MappingList and len(func) == len(self):
            self = MappingList([i(k, *args, **kwargs) for i, k in (func, self)])
        else:
            for i in range(len(self)):
                self[i] = func(self[i], *args, **kwargs)
        return self

    def call(self, func:Union[str, 'MappingList'], *args, **kwargs):
        """ Call a member function with parameters on each item """
        if type(func) is MappingList and len(func) == len(self):
            self = MappingList([i.__getattribute__(k)(*args, **kwargs) for i, k in (func, self)])
        else:
            for i in range(len(self)):
                self[i] = self[i].__getattribute__(func)(*args, **kwargs)
        return self

    def attr(self, attr:Union[str, 'MappingList']):
        """ Replace each item with it's attribute """
        if type(attr) is MappingList and len(attr) == len(self):
            self = MappingList([i.__getattribute__(k) for i, k in (attr, self)])
        else:
            for i in range(len(self)):
                self[i] = self[i].__getattribute__(attr)
        return self

    def lengths(self):
        return ensureNotIterable(MappingList([len(i) for i in self]))

    def __getattr__(self, name):
        self = MappingList([i.__getattribute__(name) for i in self])
        return self

    def __call__(self, *args, **kwargs):
        for i in range(len(self)):
            self[i] = self[i](*args, **kwargs)
        return self

    def __hash__(self):
        return hash(tuple(self))

    def __cmp__(self, other):
        if type(other) is MappingList:
            if len(other) == len(self):
                return MappingList([i.__cmp__(k) for i, k in (other, self)])
            else:
                raise MappingList.unmatchedLenError
        else:
            return super().__cmp__(other)

    def __pos__(self):
        for i in range(len(self)):
            self[i] = +self[i]
        return self

    def __neg__(self):
        for i in range(len(self)):
            self[i] = -self[i]
        return self

    def __abs__(self):
        for i in range(len(self)):
            self[i] = abs(self[i])
        return self

    def __invert__(self):
        for i in range(len(self)):
            self[i] = ~self[i]
        return self

    def __round__(self, n):
        for i in range(len(self)):
            self[i] = round(self[i], n)
        return self

    def __floor__(self):
        for i in range(len(self)):
            self[i] = self[i].__floor__()
        return self

    def __ceil__(self):
        for i in range(len(self)):
            self[i] = self[i].__ceil__()
        return self

    def __add__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__add__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__add__(other) for i in self])

    def __sub__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__sub__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__sub__(other) for i in self])

    def __mul__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__mul__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__mul__(other) for i in self])

    def __floordiv__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__floordiv__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__floordiv__(other) for i in self])

    def __truediv__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__truediv__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__truediv__(other) for i in self])

    def __mod__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__mod__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__mod__(other) for i in self])

    def __divmod__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__divmod__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__divmod__(other) for i in self])

    def __pow__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__pow__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__pow__(other) for i in self])

    def __lshift__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__lshift__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__lshift__(other) for i in self])

    def __rshift__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__rshift__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__rshift__(other) for i in self])

    def __and__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__and__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__and__(other) for i in self])

    def __or__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__or__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__or__(other) for i in self])

    def __xor__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            return MappingList(*[i.__xor__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            return MappingList(*[i.__xor__(other) for i in self])

    def __iadd__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__add__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__add__(other) for i in self])
        return self

    def __isub__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__sub__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__sub__(other) for i in self])
        return self

    def __imul__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__mul__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__mul__(other) for i in self])
        return self

    def __ifloordiv__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__floordiv__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__floordiv__(other) for i in self])
        return self

    def __itruediv__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__truediv__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__truediv__(other) for i in self])
        return self

    def __imod__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__mod__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__mod__(other) for i in self])
        return self

    def __idivmod__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__divmod__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__divmod__(other) for i in self])
        return self

    def __ipow__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__pow__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__pow__(other) for i in self])
        return self

    def __ilshift__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__lshift__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__lshift__(other) for i in self])
        return self

    def __irshift__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__rshift__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__rshift__(other) for i in self])
        return self

    def __iand__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__and__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__and__(other) for i in self])
        return self

    def __ior__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__or__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__or__(other) for i in self])
        return self

    def __ixor__(self, other):
        if type(other) is MappingList and len(other) == len(self):
            self = MappingList(*[i.__xor__(k) for i, k in zip(other, self)])
        elif type(other) is MappingList:
            raise MappingList.unmatchedLenError
        else:
            self = MappingList(*[i.__xor__(other) for i in self])
        return self

    def __int__(self):
        for i in range(len(self)):
            self[i] = self[i].__int__()
        return self

    def __long__(self):
        for i in range(len(self)):
            self[i] = self[i].__long__()
        return self

    def __float__(self):
        for i in range(len(self)):
            self[i] = self[i].__float__()
        return self

    def __complex__(self):
        for i in range(len(self)):
            self[i] = self[i].__complex__()
        return self

    def __oct__(self):
        for i in range(len(self)):
            self[i] = self[i].__oct__()
        return self

    def __hex__(self):
        for i in range(len(self)):
            self[i] = self[i].__hex__()
        return self

    def __index__(self):
        for i in range(len(self)):
            self[i] = self[i].__index__()
        return self

    def __trunc__(self):
        for i in range(len(self)):
            self[i] = self[i].__trunc__()
        return self

    def __coerce__(self, other):
        for i in range(len(self)):
            self[i] = self[i].__coerce__(other)
        return self

class ZerosDict(dict):
    """ Exactly the same thing as a regular dict, except if you try to get an item that
        doesn't exist, it just returns None instead of raising an error (but does not create
        that index)
    """
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        else:
            return None

class MultiAccessDict(dict):
    """ Exactly the same thing as a regular dict, except you can get and set multiple items
        at once, and it returns a list of the asked for items, or sets all of the items to
        the specified value
    """
    def __getitem__(self, *keys):
        if len(keys) == 0:
            raise KeyError("No input parameters given")
        return [super().__getitem__(key) for key in keys]

    def __setitem__(self, *keys, value):
        todo('figure out how the setitem parameters work')
    #     return [super().__setitem__(key) for key in keys]

class ZerosMultiAccessDict(ZerosDict):
    """ A combonation of a ZerosDict and a MultiAccessDict """
    def __getitem__(self, keys):
        if len(keys) == 0:
            raise KeyError("No input parameters given")
        rtn = []
        if not isiterable(keys):
            return super().__getitem__(keys)
        else:
            for key in keys:
                rtn.append(super().__getitem__(key))
            return ensureNotIterable(rtn)
