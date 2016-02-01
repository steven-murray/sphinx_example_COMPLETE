"""
A module defining several objects aimed at showing different parts of the sphinx reportoire.
"""
import numpy as np

def a_one_liner(a):
    """Print a"""
    print "Result is: ", a

def a_math_func(a,b,hypot=True):
    """
    Return the hypotenuse of a right triangle with sides `a` and `b`, :math:`\sqrt{a^2 + b^2}`

    By default, returns the hypotenuse of the right triangle with sides `a` and `b`, and prints
    the result using :func:`a_one_liner`. Alternatively treats the larger of `a` and `b` as the
    hypotenuse and returns the other side.

    Parameters
    ----------
    a : array_like
        Length(s) of one side of the triangle

    b : array_like
        Length(s) of another side of the triangle. Must be a scalar, or same length as `a`.

    hypot : bool, optional
        If `True` the hypotenuse is to be calculated, otherwise, it is assumed to be the larger of `a` and `b`.

    Returns
    -------
    c : array_like
        The length(s) of the third side(s)

    Notes
    -----
    The result is calculated using Pythagoras' theorem:

    .. math:: c^2 = a^2 + b^2

    Examples
    --------
    Calculate the famous integer length right triangle:

    >>> a_math_func(3,4)
    Result is:  5.0
    5.0

    Alternatively, calculate the smaller side:

    >>> a_math_func(5,4,hypot=False)
    Result is:  3.0
    3.0
    """

    if hypot:
        c = np.sqrt(a**2 + b**2)
        a_one_liner(c)
        return c
    else:
        a = np.atleast_1d(a)
        b = np.atleast_1d(b)
        h = np.where(a>=b,a,b)
        s = np.where(a<b,a,b)
        c = np.sqrt(h**2 - s**2)
        if len(c)==1:
            c = c[0]
        a_one_liner(c)
        return c

class Klass(object):
    """
    A basic class.

    Parameters
    ----------
    thing : str
        Something that you like.

    Attributes
    ----------
    x : float
        How much I like `thing`.

    """
    x = 0

    def __init__(self,thing):
        self.thing = thing

    def tell_me(self):
        """ Print how much I like `thing`"""
        print "I like %s about %s"%(self.thing,self.x)

    @property
    def love_factor(self):
        """
        The love factor of `thing`.

        Equates to 4 times how much I like it.
        """
        return 4*self.x