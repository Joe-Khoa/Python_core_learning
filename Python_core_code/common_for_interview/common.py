from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']

# shuffle(x)
print(x)
x.sort()
print(x)
# delete_a_file
import os
try :
    # os.remove(r"C:\Users\Lilti\Documents\Python\Python_ATOM\Django\Python_core_code\common_for_interview\test.py")
    os.unlink(r"C:\Users\Lilti\Documents\Python\Python_ATOM\Django\Python_core_code\common_for_interview\test.py")    # or this_line_to_remove
    print('deleled successfully!')
except:
    print('not exist file!')

# dir (print)      #   : Hàm dir () hiển thị các ký hiệu(defined symbols).
# help ()     #   : Hàm help () chuỗi tài liệu và trợ giúp liên quan đến mô-đun, từ khóa, thuộc tính, v.v.

list_mutable_obj = ['a','b','1']
print('ORIGIN_list_mutable_obj: ', list_mutable_obj)
list_mutable_obj[1] = 'xyzabcd'
print('list_mutable_obj: ',list_mutable_obj)

print('*'*40)

tuple_IMmutable_obj = ('a','b','1')
print('ORIGIN_list_mutable_obj: ', list_mutable_obj)
try:
    tuple_IMmutable_obj[1] = 'xyzabcd'
    print('list_mutable_obj: ',list_mutable_obj)
except:
    print(' !!! (^_^) python_said:  a tupple is IMMUTABLE')

try:
    fz = frozenset([1,2,3])
    fz[1] = 1
    print(fz)
except:
    print(" !!! (^_^) TypeError: 'frozenset' object does not support item assignment")
