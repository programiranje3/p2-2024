"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


#%%
# Setup / Data
song = 'My Generation'
year = 1965

pete = 'Pete Townshend'
roger = 'Roger Daltrey'
john = 'John Entwistle'
keith = 'Keith Moon'
the_who = [pete, roger, john, keith]


#%%
# def demonstrate_annotations(title, year):
def demonstrate_annotations(title: str, year: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """

    print(f'{title}, {year}')
    print(demonstrate_annotations.__annotations__)
    print(demonstrate_annotations.__name__)
    print(demonstrate_annotations.__doc__)
    return f'demonstrate_annotations(\'{title}\', year)'


#%%
# Test demonstrate_annotations(title, year)
print(demonstrate_annotations(song, year))


#%%
# def show_song(title, author='Pete Townshend', year: int = 1965):
def show_song(title, author='Pete Townshend', year: int = 1965):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """

    # a = 2
    print(locals())
    print(f'title: {title}, author: {author}, year: {year}')


#%%
# Test show_song(title, author='Pete Townshend', year: int = 1965)
show_song(song)


#%%
def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    # print(members)
    # print(*members)
    # print()

    print(f'Band: {band}, members: {"not specified" if not members else ", ".join([m for m in members])}')


#%%
# Test use_flexible_arg_list(band: str, *members)
use_flexible_arg_list('The Who', *the_who)
use_flexible_arg_list('The Who')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    print(details)
    print(*details)
    # print(**details)
    print()

    m = "not specified" if not members else ", ".join([m for m in members])
    a = 'active' if is_active else 'not active'
    d = '' if not details else ', '.join([str(k) + ': ' + str(v) for k, v in details.items()])
    print(f'Band: {band}; members: {m}; {a}; {d}')


#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
use_all_categories_of_args('The Who', is_active=True, start=1962, end=1983)
use_all_categories_of_args('The Who', *the_who, is_active=False,
                           start=1964, end=1983)


