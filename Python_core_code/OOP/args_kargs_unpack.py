# có thể viết là *var và **vars
 # giúp chúng ta có thể truyền bao nhiêu tham số vào hàm cũng được.

# def foo(x, y):
#     return print(x + y)
# foo(1, 2)

# Bây giờ, nếu muốn tính tổng của nhiều số hơn
# use list -> ok but NOT GOOD => not know how many varible

def foo(a,b,*vars):
    result = a+b
    for x in vars:
        result += x
    return print(result)
# foo(1,2)
# foo(1,2,3,4,4,4)    # TOO good

# args is a tuple not a list | args* always in the end LIKE defaul
# list là mutable còn tuple là immutable.


# ******************************************************

""" Cách sử dụng **kwargs cũng tương tự như như *args
->mà nó được sử dụng cho các tham số đặt tên
 named arguments hoặc keyword arguments)."""

def foo(a=0, b=1):
    return a + b
# foo()

def foo(a): # a is a Dict
    for key, value in a.items():
        print(key, value)
# foo({'a': 1, 'b': 2}) # too complicated

def foo(**named_vars):  # named_vars same a Dict
    for key,value in named_vars.items():
        print(key,':',value)
# foo(a=1,b=2)

"""
Thứ tự đúng sẽ là:
    Các tham số bình thường
    *args
    **kwargs
"""

def foo(a, b, *args, **kwargs):
    return a + b



# ************************# Sử dụng để UNPACK #******************************

"""
 * được xử dụng với một đối tượng iterable,
  còn ** chỉ có thể dùng được với dict mà thôi.
"""
x = (1, 2, 3)
# print(x)
# print(*x)

def foo(a,b,c):
    print("a = %d, b = %d, c = %d" % ( int(a), int(b), int(c) ))
# foo(1,2,3)
# foo(*x)    # TOO better
y = {'1': 7, '2': 8, '3': 9}
""" số lượng các tham số của hàm và số lượng giá trị unpack được phải khớp nhau,
y = {'a': 7, 'b': 8, 'c': 9}    #  error"""

# foo(**y)
# foo(*y) # just KEY


# ************************# Unpack khi gán biến #******************************

x = [1, 2, 3, 4, 5, 6]
a, b, c  = x[0], x[1:-1], x[-1] # hard
a, *b, c = x    # so  cleaner !
# print(a)

# dict  ->  SyntaxError: can't assign to literal
# o = {p: 42, q: true}
# {p: foo, q: bar} = o


# ************************# làm "phẳng" các list #******************************


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
a = (*list1,*list2,*list3)
# print(*list1,*list2,*list3)
# print(a)

dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}
merge_dict = {**dict1, **dict2}
# print(merge_dict)
