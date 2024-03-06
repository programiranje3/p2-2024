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

    british_invasion = [1964, 1967, True, 'Rock \'n\' Roll']
    # print(british_invasion)
    # print(british_invasion[3])
    # print(british_invasion[-3:])

    # gods = ['The Beatles', 'The Rolling Stones']
    # the_essence = gods + british_invasion
    # print(the_essence)

    for e in british_invasion:
        print(e)


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

    british_invasion = [1964, 1967, True, 'Rock \'n\' Roll']

    print(british_invasion.append('The Beatles'))
    print(british_invasion)
    print(british_invasion.remove(True))
    print(british_invasion)
    print(british_invasion.pop(1))
    print(british_invasion)
    print(british_invasion.extend(['The Rolling Stones', 'The Kinks']))
    print(british_invasion)
    print(british_invasion.count('The Beatles'))
    print(british_invasion.index('The Beatles'))
    print(british_invasion.reverse())
    print(british_invasion)
    print(len(british_invasion))
    print('The Kinks' not in british_invasion)


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array

    a = array('i', [1, 2, 3])
    print(a)
    print(type(a))
    print([1, 2, 3])
    print(type([1, 2, 3]))


#%%
# Test demonstrate_arrays()
demonstrate_arrays()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import randint, seed

    # seed(12)
    l1 = []
    for _ in range(10):
        l1.append(randint(10, 20))
    print(l1)


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

    british_invasion = [1964, 1967, True, 'Rock \'n\' Roll']
    # b = british_invasion
    # b = british_invasion.copy()
    # b = british_invasion[:]
    b = british_invasion + []
    print(british_invasion is b)


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

    songs = ['Angie', 'No Expectations', 'Gimme Shelter', 'Ruby Tuesday', 'You Can\'t Always Get What You Want']

    print(''.join([s[0] for s in songs]))
    print(''.join([s[0] for s in songs]).capitalize() + '!')
    print()

    songs = ['Angie', 'No Expectations', 'Gimme Shelter',
             'Angie', 'Ruby Tuesday', 'You Can\'t Always Get What You Want']
    print([t[0] for t in enumerate(songs) if t[1] == 'Angie'])


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()

