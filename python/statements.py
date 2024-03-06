"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    a = 1.3
    b = 1.3
    #
    # a = [1.3, 2.3]
    # b = [1.3, 2.3]
    #
    c = 'ccc'
    d = 'ccc'
    #
    # # print(d is c)
    # print(a is b)
    # print(a == b)

    # # if a == b:
    # if a:
    #     print(True)
    # else:
    #     print(False)

    if a > b:
        print('>')
    elif a < b:
        print('<')
    elif a != b:
        print('!=')
    else:
        print('==')


#%%
# Test demonstrate_branching()
demonstrate_branching()

#%%


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    # s = 'qwerty'
    # # for i in s:
    # #     print(i)
    # for _ in s:
    #     print(1964)

    # for i in range(0, 13, 2):
    #     print(i)

    for i in range(13):
        if i == 3:
            # continue
            break
        print(i)


#%%
# Test demonstrate_loops()
demonstrate_loops()

