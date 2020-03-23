
import pprint

class Animal(object):   # object is Parent of ALL class
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print('%s is eating %s' %(self.name,food))

class Dog(Animal):
    def fetch(self,thing):
        print( '%s goes after the %s' %(self.name,thing))
    def show_affection(self):
        print("Dog: {0} wags tail",format(self.name))

class Cat(Animal):
    def swat_string(self):
        print('%s shred the string' %(self.name))
    def show_affection(self):
        print("Cat: {0} purrs ",format(self.name))


# ***************** INHERITANCE *****************


"""Object.Attribute Lookup Hierarchy
    The instance
    The class
    Any class from which this class inherits"""

"""
What is an instance?

An object is created "using the constructor" of the class.
This object will then be called the instance of the class [1].
"""


# d = Dog('Ranger')
# c = Cat('Meow')
# d.fetch('ball')
# c.swat_string()
# d.eat('Dog food')
# d.swat_string() # error


# ***************** POLYMORPHISM *****************

# for a in [Dog('Rover'), Cat('precious'), Dog('Scout')]:
#     a.show_affection()

# built-in polymorphism (MANY SHAPES)
# print(dir('a'),end='')


#  *****************  OVERIDING  *****************

class Thought(object):
    def __init__(self):
        print('supper init')
    def message(self):
      print("SUPER__ Thought, always come and go")

class Advice(Thought):
   def __init__(self):
      # super(Advice, self).__init__()  # get Father constructor to make child_init
      super().__init__()    # same above
   def message(self):
      print('CHILD__ Warning: Risk is always involved when you are dealing with market!')

# me = Thought()
# me.message()
# you = Advice()
# you.message()


#   *****************  Inheriting the Constructor  *****************
"""
    Conclusion
        __init__ is like any other method; it can be inherited
            a class does not have a __init__ constructor,
        Python will check its parent class to see if it can find one.
        As soon as it finds one, Python calls it and stops looking
        We can use the super () function to call methods in the parent class.
        We may want to initialize in the parent as well as our own class.
"""
import random

class Animal():

    def __init__(self,name):
        self.name = name
        # print('Parent name')

class Dog(Animal):

    def __init__(self,name):
        # super(Dog,self).__init__(name)  # get to THIS Dog
        super().__init__(name)            # same
        self.breed = random.choice(['Dogberman','German Shepherd','Beagle'])

# d = Dog('Dog Name')
# print(d.name)
# print(d.breed)  # note breed is a attribute not argument


#   *****************  Multiple Inheritance and the Lookup Tree  *****************

class Mother():
    def __init__(self):
        print('Mother inherited')

class Father():
    def __init__():
        print('Father inherited')

class ChildA(Mother,Father):
    pass

class ChildB(Father,Mother):
    pass

# ca = ChildA()
# cb = ChildB()
# issubclass = issubclass(ChildA,Mother) and issubclass(ChildB,Father)
# print(issubclass)

# ****** Multiple inherited Cont... *******

class A(object):
    def dothis(self):
        print('do A')

class B(A):
    pass

class C(object):
    def dothis(self):
        print('do C')
    def dothat(self):
        print('do that C')

class D(B,C):
    pass

# d_ins = D()
# d_ins.dothis()
# d_ins.dothat()
# print(D.__mro__)
"""
# Python normally uses a “depth-first” order when searching inheriting classes.
    __mro__
    (<class '__main__.D'>,
     <class '__main__.B'>,        # first
      <class '__main__.A'>,
       <class '__main__.C'>,      # second
        <class 'object'>)
"""

#   *****************  Decorators, Static and Class Methods  *****************


def outside_func():
    print( """Simple method − defined outside of a class.
            This function can access class attributes
             by feeding instance argument:""")

def func(self):
    print('Instance method −')

# @classmethod
def cfunc(cls):
    print('The @classmethod decorator if we need to use class attributes')

# @staticmethod
def sfoo():
    print('Static method − do not have any info about the class')



# ************ 1.classmethod()____ Cont...

"""
The classmethod() is an inbuilt function
in Python which returns a class method for given function.

    Syntax:         classmethod(function)
    Parameter :     This function accept 'function' name as parameter.
    Return Type:    This function returns 'converted class method'.

    Uses of classmethod():
    used in "factory design pattern" where
    we want to call "many functions"
    with the class name rather than object.
"""
class Student:

    name = 'Geek4Geek'
    def printStuName(obj):
        print('the name is : ',obj.name)

# Called by Class
Student.printStuName = classmethod(Student.printStuName)
# Student.printStuName()
# s = Student()
# Called by obj/ instance
# s.printStuName()


# ************ 2. The @classmethod Decorator: ____ Cont...
"""
The @classmethod decorator, is a builtin function decorator
that is an expression that "gets evaluated after your function is defined".
The result of that evaluation "shadows your function definition".

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):

"""
# from datetime import date
#
# class Person:

# Static methods    ~ indepentdent method

"""
The main characteristics of a static method is that
they can be called without instantiating the class.
This methods are self contained,
meaning that they "cannot access any other attribute" or
"call any other method within that class".

"do not need an specific instance" in order to access that method.
For example if you have a class called Math
and you have a method called factorial (calculates the factorial of a number).
You probably won’t need an specific instance
to call that method so you could use a static method.
"""

class Math:

    @staticmethod
    def factorial(number):
        if (number == 0):
            return 1
        else :
            return number*Math.factorial(number-1)
factorial = Math.factorial(5)
# print(factorial)

# good example ALL_PYTHON_METHOD-TYPE

class MethodTypes:

    name = "Ragnar"
    hair = 'red'
    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname,'\n'+'*'*10)

    @classmethod
    def classMethod(cls):   # name_class varialbe compared to self_instance
        # Access a class atribute through keyword cls
        # cls.name = "Lagertha"
        print(cls.hair,'\n'+'*'*10)

    @staticmethod
    def staticMethod():
        print("This is a static method ans i am a independent GuY ",'\n'+'*'*10)

# # Creates an instance of the class
# m = MethodTypes()
# # Calls instance method
# m.instanceMethod()
#
# MethodTypes.classMethod()
# MethodTypes.staticMethod()


# Second example Static-classMethod

from datetime import date

class Person:
    test = '_test_class_method'
    def __init__(self, name, age):
        self.name = name
        self.age_= age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

person = Person('instance_name',18)
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print (person.name,person.age_, '')
print (person1.age_)
print (person1.test)
print (person2.age_)

print (Person.isAdult(22))
