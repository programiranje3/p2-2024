"""Demonstrates working with strings in Python.
"""

import string

import settings


#%%
def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    # print('This is an int %d, and it denotes an important %s.' % (1964, 'year'))
    # print('C:\nobody')
    # print(r'C:\nobody')
#     print("""
# 1964
# 1967
# """)
#     print('The British Invasion ' * 3)
    print('The British Invasion'[4:12])
    print('The British Invasion'[-8:])


#%%
# Test demonstrate_formatting()
demonstrate_formatting()

#%%


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('The British Invasion, {0}-{1}'.format(1964, 1967))


#%%
# Test demonstrate_fancy_formatting()
demonstrate_fancy_formatting()

#%%


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    start = 1963
    end = 1967
    print(f'The British Invasion, {start + 1}-{end}.')


#%%
# Test demonstrate_fancy_formatting_with_f_strings()
demonstrate_fancy_formatting_with_f_strings()

#%%


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    print('The British Invasion'.endswith('Invasion'))
    print('The British Invasion'.split())
    print('The British Invasion'.split(' British '))
    print('Invasion' in 'The British Invasion')
    print(len('The British Invasion'))
    print('   The British Invasion')
    print('   The British Invasion'.strip())
    print('   The British Invasion'.lstrip())


#%%
# Test demonstrate_string_operations()
demonstrate_string_operations()
