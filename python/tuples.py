"""Demonstrates tuples.
"""


#%%
def demonstrate_tuples():
    """Creating and using tuples.
    - create and print empty tuple, 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    # t0 = ()
    # print(type(t0))

    # t1 = 'Pete',
    # print(t1)
    # print(type(t1))
    # print(len(t1))

    the_who = ('Pete', 'Roger', 'John', 'Keith', True)
    for i in range(5):
        print(the_who[i])
    for member in the_who:
        print(member)
    # the_who[1] = ''


#%%
# Test demonstrate_tuples()
demonstrate_tuples()


#%%
def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    the_who = ('Pete', 'Roger', 'John', 'Keith', True)
    pete, roger, john, keith, b = the_who
    print(pete, roger, john, keith, b)


#%%
# Test demonstrate_packing()
demonstrate_packing()


#%%
def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    members = ('Mick Jagger', 'Keith Richards', 'Bill Wyman', 'Charlie Watts', 'Brian Jones')
    birth_years = (1940, 1942, 1936, 1941, 1942)
    birth_places = ('Dartford', 'Dartford', 'London', 'London', 'Cheltenham')

    the_rolling_stones = zip(members, birth_years, birth_places)
    print(the_rolling_stones)
    print()
    for m, y, p in the_rolling_stones:
        print(', '.join([m, str(y), p]))


#%%
# Test demonstrate_zip
demonstrate_zip()

