
################################### Geometry functions ###################################
def absdeg(angle):
    """ If an angle (in degrees) is not within 360, then this cuts it down to within 0-360 """
    angle = angle % 360.0
    if angle < 0:
        angle += 360
    return angle

def absrad(angle):
    """ If an angle (in radians) is not within 2Pi, then this cuts it down to within 0-2Pi """
    angle = angle % (pi*2)
    if angle < 0:
        angle += (pi*2)
    return angle

# Turns out there's already multiple implementations of these I just wasn't seeing
# def deg2rad(a, symbolic=False):
    # if symbolic:
    #     if ensureImported('sympy', 'pi', fatal=True):
    #         return (a * pi / 180).simplify()
    # else:
    #     return a * PI / 180.0

# def rad2deg(a, symbolic=False):
    # if symbolic:
    #     if ensureImported('sympy', 'pi', fatal=True):
    #         return (a * 180 / pi).simplify()
    # else:
    #     return a * 180.0 / PI

def dist(ax, ay, bx, by):
    return sqrt(((bx - ax)**2) + ((by - ay)**2))

def normalize2rad(a):
    # while a < 0: a += math.tau
    # while a >= math.tau: a -= math.tau
    return a % (PI * 2)

def normalize2deg(a):
    # while a < 0: a += 360
    # while a >= 360: a -= 360
    return a % 360

def constrainToUpperQuadrants(ang, deg=False):
    if deg:
        ang = radians(ang)
    # Oh duh
    return ang % PI

def negPow(num, exp):
    """ Raise num to exp, but if num starts off as negative, make the result negative """
    neg = num < 0
    return (num**exp) * (-1 if neg else 1)

def round2(num, digits=3, tostr=True, scinot:int=False):
    try:
        from sympy.core.evalf import N as evalf
        num = evalf(num)
    except ImportError:
        pass

    try:
        ans = round(num, digits)
    except:
        return '{:1f}'.format(num) if tostr else num

    if scinot:
        ensureImported('scinot', _as="scinotation")
        if not tostr:
            raise TypeError(f"Can't round using scientific notation and not return a string")
        return scinotation.format(ans, scinot)
    else:
        return '{:1f}'.format(ans) if tostr else ans
