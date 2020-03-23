
""" when we design a class,
 we decide which data belongs to the instance and
 which data should be stored into the overall class.
"""

# class InstanceCounter(object):
#    count = 0 # *****class attribute, will be accessible to ALL INSTANCE
#    def __init__(self, val):
#       self.val = val
#       InstanceCounter.count +=1 #      Increment the value of class attribute,
# #     accessible through class name
# #     In above line, class ('InstanceCounter') act as an object
#    def set_val(self, newval):
#       self.val = newval
#
#    def get_val(self):
#       return self.val
#
#    def get_count(self):
#       return InstanceCounter.count
# a = InstanceCounter(9)
# b = InstanceCounter(18)
# c = InstanceCounter(27)
# # now the InstanceCounter.count = 3 times (class)
#
# for obj in (a, b, c):
#    print ('val of obj: %s' %(obj.get_val())) # Initialized value ( 9, 18, 27)
#    print ('count: %s' %(obj.get_count())) # always 3

class myClass:
    class_attr = 99

    def class_method(self):
        self.instance_attr = 'I am an instance of this attribute not overall class'

print(myClass.__dict__,'\n')

a = myClass()
a.class_method()
print(a.__dict__)
