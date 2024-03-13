"""Demonstrates sets.
"""


#%%
def demonstrate_sets():
    """Creating and using sets.
    - create a set and make an attempt to duplicate items
    - demonstrate some typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    the_beatles = {'John', 'Paul', 'George', 'Ringo'}
    # the_beatles.add('John')
    # print(the_beatles)

    print(the_beatles | {'John', 'George Martin'})
    print(the_beatles & {'John', 'George Martin'})
    print(the_beatles - {'John', 'George Martin'})
    print(the_beatles ^ {'John', 'George Martin'})


#%%
# Test demonstrate_sets()
demonstrate_sets()


