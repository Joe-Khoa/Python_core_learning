"""
https://towardsdatascience.com/5-advanced-features-of-python-and-how-to-use-them-73bffa373c84

(1) Lambda functions - anonymous function
Python functions are typically defined
using the style of def a_function_name()
, but with lambda functions we don’t give it a name at all.

(2) Maps - like Map___:
Map() is a built-in Python function used to apply
applies to a sequence list or dictionary. very clean!

(3) Filtering - like a filter( filter-condition)___:
similar to the Map, applies to a sequence (list, tuple, dictionary)
only return the elements the applied returned as True.]


(4) Itertools___:
The Python Itertools "module" is a collection
of tools for handling iterators. An iterator is a data type
that can be used in a for loop including lists, tuples, and dictionaries.

(5) Generators___(just generate-no-loop):
Generator functions allow you to declare a function like an iterator,
i.e. it can be used in a for loop.
greatly simplifies code and much more "memory efficient" than a simple for loop.

    *********************************__Generator__ *************************************
    -   The range() function in Python does the same thing, it builds the list in memory
    -   A generator will create elements and store them in memory
     only as it needs them i.e one at a time.
    -   if you have to create 1 billion floating point numbers,
     you’ll only be storing them in memory "one at a time!"
     The xrange() function in Python uses generators to build lists.

            That being said, if you’d like to iterate over the list multiple times
     and it’s small enough to fit into memory, it will be better to use for loops
     and the range function. This is because generators and xrange will be freshly generating
     the list values every time you access them, whereas range is a static list
     and the integers already exist in memory for quick access.

(6) Function in funcion , func(func):

(7) Decorator ???  @function_x('param')


"""
# (1) Lambda

x = lambda a,b : (
        a+b
    )
y = lambda a,b : {
        a*b
    }   # return a set { result }
z = lambda x: x**2

# print(x(5,3))
# print(y(2,5))
# print(z(2))


# (2) Maps - like Map___:

def square_it(a):
    return a**3  #from math import pow # return pow(a,3)
l1 = [1,2,5,9]
l2 = [0,2,4,1,13]
l3 = []


x = map(square_it,l1)
# print(list(x))

def mutiplier(a,b):
    return a*b

x = map (mutiplier,l1,l2)
# print(list(x))
#   [0, 4, 20, 9]


# (3) Filtering : return_when_true

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def filter_odd(num):

    if num % 2 == 0:
        return True
    return False

filter_odd_number = filter(filter_odd,numbers)

# print(  list(filter_odd_number) )
#   [2, 4, 6, 8, 10, 12, 14]    this_take_only_true


# (4)
# https://docs.python.org/2/library/itertools.html
from itertools import *
import operator
# (4-1) izip  : Zip
""" Easy joining of two lists into a list of tuples"""
li_int = [1,2,3]
li_str = ['a','b','c']

ItemZip = zip(li_int,li_str)
# print(list(ItemZip))

# (4-2) count()  :
"""This one is great for adding indices next to your list
elements for readability and convenience"""

list_name = ['Bob','Emily','Joe']

add_index =  zip(count(1),list_name)
# print(tuple(add_index))

# (4-3) dropwhile()  drop_while_fail

def check_for_drop(x):
    # print('checking: ',x)
    return (x>5)    # 2 is return 2 show dropwhile let all the birds out

for i in dropwhile( check_for_drop,[2,4,6,8,10,12] ):
    # print('Result: ',i)
    pass


# (4-4) groupby()  retrieving bunches what is same

a = sorted([1, 2, 1, 3, 2, 1, 2, 3, 4, 5])
group_whats_same = groupby(a)
# for key,value in list(group_whats_same):
#     print(key, list(value), end = '\n')


# (4-5) Generators: create 1 billion floating point numbers,
#   you’ll only be storing them in memory "one at a time!"

""" Generator.py"""






# (6) function(param=function):

#program create tag
def make_tag(f):
    def wrapper(tag_name,text):
            return '<%(tag)s> %(text)s <%(tag)s>' %dict(tag=tag_name, text = text)
    return wrapper

def alias_fn():
    pass

if __name__ == '__main__':
    x = make_tag(alias_fn)     # now x is a function x =wrapper = x(tag_name,text)
    # print(
    #         x('div','this is text in tag!')
    #     )
    # print(
    #         x('b',x('div','this is text in tag!'))  # x('div','this is text in tag!') == %(text)s
    #     )


# (7)  decorator_function:

def make_tag(tag_name):
    def decor(f):
        def wrapper(text):
            return '<%(tag)s> %(text)s <%(tag)s>' %dict(tag = tag_name,text = f(text) )
        return wrapper
    return decor

@make_tag('div')
def fn(text_):
    return text_+'...'
# print(fn('this is text'))


# if __name__ =='__main__':
    # x = make_tag('div')(fn)('text inside tag')    # interesting
    # print( fn('data to be shown') )
