# normal_list = [2, 4, 5, 7, 9]
#
# class CustomSequence():
#     def __len__(self):
#         return 3
#     def __getitem__(self,index):
#         return "x{0}".format(index)
# class funkyback():
#     def __reversed__(self):
#         return 'backwards!'
# for seq in normal_list, CustomSequence(), funkyback():
#     print('\n{}: '.format(seq.__class__.__name__), end="")
#     for item in reversed(seq):
#         print(item, end=", ")


# Enumerate

# names = ['Rajesh', 'Rahul', 'Aarav', 'Sahil', 'Trevor']
# print(enumerate(names))
# print(list(enumerate(names)))
# # for i  in list(enumerate(names,2)):
# #     print(i[0])
# for i,n in enumerate(names):
#     print(str(i),'-',n) #   i is__ <class 'int'>

#   Functions Are Objects Too A function is the simplest callable object in Python

def my_fn():
   print('My function was called')
my_fn.description = 'A silly function'

def call_fn(fn):
    print(my_fn.description)
    print(my_fn.__name__)
    print(my_fn.__class__)

call_fn(my_fn)
