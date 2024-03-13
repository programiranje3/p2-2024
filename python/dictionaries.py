"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


#%%
def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - access dictionary values by the corresponding keys (syntax: value = d[key])
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    # print(list.__dict__)
    # the_who = {}
    # print(type(the_who))

    the_glimmer_twins = {1: 'Mick Jagger', 2: 'Keith Richards'}
    # print(the_glimmer_twins[1])
    # print(the_glimmer_twins.items())
    # for k in the_glimmer_twins.keys():
    #     print(str(k) + ':', the_glimmer_twins[k])

    # from pprint import pprint
    # pprint(the_glimmer_twins, width=1)
    # pprint(the_glimmer_twins, )

    # the_glimmer_twins['birth_place'] = 'Dartford'
    # print(the_glimmer_twins)
    # del the_glimmer_twins['birth_place']
    # print(the_glimmer_twins)

    # the_glimmer_twins.update({'birth_place': 'Darthford'})
    the_glimmer_twins.update([('birth_place', 'Darthford')])
    print(the_glimmer_twins)


#%%
# Test demonstrate_dictionaries()
demonstrate_dictionaries()


#%%
def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if (by == 'k') or (by == 'K'):
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif (by == 'v') or (by == 'V'):
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # from operator import itemgetter
    #
    # if (by == 'k') or (by == 'K'):
    #     return dict(sorted(d.items(), key=itemgetter(0)))
    # elif (by == 'v') or (by == 'V'):
    #     return dict(sorted(d.items(), key=itemgetter(1)))
    # else:
    #     return None

    if by == 'k' or by == 'K':
        return dict(sorted(d.items(), key=lambda x: x[0]))
    elif by == 'v' or by == 'V':
        return dict(sorted(d.items(), key=lambda x: x[1]))
    else:
        return None


#%%
def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    from pprint import pprint

    songs = {2: 'Angry', 1: 'Brown Sugar', 3: 'Jumpin\' Jack Flash'}
    glimmer_twins = {'mick': 'Mick Jagger', 'keith': 'Keith Richards', 'birth_year': 1943}
    glimmer_twins = {'mick': 'Mick Jagger', 'keith': 'Keith Richards', 'birth_year': '1943'}
    # d = {2: 38, 5: 19, 1: 20}

    # print(sort_dictionary(d, by='v'))
    # print(sort_dictionary(songs, by='k'))
    print(sort_dictionary(songs, by='v'))
    # print(sort_dictionary(glimmer_twins, by='k'))
    print(sort_dictionary(glimmer_twins, by='v'))
    # print(sort_dictionary(glimmer_twins, 'k'))
    # print(sort_dictionary(glimmer_twins, 'v'))


#%%
# Test demonstrate_dict_sorting()
demonstrate_dict_sorting()


#%%
# Just testing; pprint sometimes doesn't show the sorted dictionary correctly when sorting by value

import operator
from pprint import pprint
# my_dict = {'a': 2, 'b': 1, 'c': 3}
my_dict = {'mick': 'Mick Jagger', 'keith': 'Keith Richards', 'birth_year': '1943'}
sorted_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
print(sorted_dict)
pprint(sorted_dict)
print()

# Output:
# {'b': 1, 'a': 2, 'c': 3}

d = {2: 38, 5: 19, 1: 20}

sort_dictionary(my_dict, by='v')

# from pprint import pprint
#
# songs = {2: 'Angry', 1: 'Brown Sugar', 3: 'Jumpin\' Jack Flash'}
# glimmer_twins = {'mick': 'Mick Jagger', 'keith': 'Keith Richards', 'birth_year': 1943}
# glimmer_twins = {'mick': 'Mick Jagger', 'keith': 'Keith Richards', 'birth_year': '1943'}
# d = {2: 38, 5: 19, 1: 20}
#
# print(sort_dictionary(d, by='v'))
# # pprint(sort_dictionary(songs, by='k'))
# # pprint(sort_dictionary(songs, by='v'))
# # pprint(sort_dictionary(glimmer_twins, by='k'))
# # pprint(sort_dictionary(glimmer_twins, by='v'))
# # pprint(sort_dictionary(glimmer_twins, 'k'))
# # pprint(sort_dictionary(glimmer_twins, 'v'))

