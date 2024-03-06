"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print(25 // 13 - 12 % 5 + 3)


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()

#%%


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    # print(2 > 3)
    # print(2 <= 3)
    # print(not (2 > 3))
    # print(2 != 3)

    from datetime import date

    d1 = date(1964, 2, 7)
    d2 = date(1984, 2, 9)
    d3 = date(1984, 2, 9)

    # # print (d2 > d1)
    # print(d2 == d3)
    # print(d2 is d3)
    # print(id(d1), id(d2))

    # print(2 == None)
    # print(2 is None)

    # print(2 > None)
    print(type(None))


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()

#%%


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    # print(1 and 2)
    # print(1 and 0)
    # print(0 or 4)
    # print(1 and None)

    from datetime import date

    d1 = date(1964, 2, 7)
    d2 = date(1984, 2, 9)
    d3 = date(1984, 2, 9)

    print(d1 and 0)
    print(d1 and None)
    print(None and d1)
    print(d1 and d2)


#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()

