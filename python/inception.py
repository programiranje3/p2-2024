"""The very first module in a more structured version of the project.
"""


#%%
# Moving code from main.py


#%%
# Printing with ' ' and printing without '\n'


#%%
# Printing with classical formatting (%)

print('The British Invasion started in %d in %s.' %(1964, 'America'))

#%%
# Keyboard input


#%%
# break and continue

for i in range(5):
    if i == 3:
        break
    print(i)


#%%
# A simple function and function call

def start():
    """
    A simple function
    """

    year = int(input('Year: '))
    return year


print('The British Invasion started in', start())

print()
print(__name__)
print()


#%%
# Printing docstrings

print(start.__doc__)
print(__doc__)

#%%
# Printing a list using enumerate()


#%%
# Importing from Standard Library

# Date format strings
# https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes

from datetime import date

d = date(1964, 2, 9)
print(d)
print(d.strftime('%b %d, %Y'))


#%%
# Testing print(__file__)

print(__file__)

#%%
# Taking care of the module __name__

if __name__ == '__main__':
    print('The British Invasion started in', start())
    print()
    print(__name__)
    print()


