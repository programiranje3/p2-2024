"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """


#%%
# Test demonstrate_lists()
demonstrate_lists()

#%%
def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """


#%%
# Test demonstrate_arrays()
demonstrate_arrays()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """


#%%
# Test populate_empty_list()
populate_empty_list()

#%%


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """


#%%
# Test duplicate_list()
duplicate_list()

#%%


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    # songs = ['Angie', 'No Expectations', 'Gimme Shelter', 'Ruby Tuesday', 'You Can\'t Always Get What You Want']


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()

