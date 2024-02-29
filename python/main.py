"""The very first Python script - main.py.
"""


# #%%
# # Hello world: the print() built-in function and the + operator.
#
# print('British Invasion')
# print('British invasion', 'started in', 1964)
# print('British invasion ' + 'started in ' + str(1964) + '.')
# print('British invasion ' + 'started in ' + '\n' + str(1964) + '.')
#
# #%%
# # The input() built-in function
#
# # input('The British Invasion started in: ')
# print('Year: ', end='')
# # print('Year: ', end='')
# year = input()
# print('The British Invasion started in ' + year + '.')
#
#
# #%%
# # A simple function and function call
#
# def start():
#     """
#     A simple function
#     """
#
#     year = int(input('Year: '))
#     return year
#
#
# print('The British Invasion started in', start())
#
#
# #%%
# # A simple loop and the range() built-in function
#
# # for i in range(5):
# #     print(i)
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# #%%
# # A simple list, accessing list elements, printing lists
#
# british_invasion = [1964, 'Feb 09', 1967, 'The Beatles']
# print(british_invasion)
# print(british_invasion[0])
# print(british_invasion[0:2])
# print(british_invasion[-2:])
#
# #%%
# # Looping through list elements - for and enumerate()
#
# # for i in range(len(british_invasion)):
# #     print(british_invasion[i])
#
# for i, j in enumerate(british_invasion):
#     print(str(i + 1) + ':', j)
# print()
#
# print(enumerate(british_invasion))
# print(list(enumerate(british_invasion)))
#
# #%%
# # Global variables: __name__, __file__, __doc__,...
#
# print(__name__)
# # print(__file__)
# print(start.__doc__)
# print(start.__dict__)

#%%
# Importing from another script

print(__name__)
print()

from python.inception import start
# print()
# print(__name__)
# print()
# print(start())
