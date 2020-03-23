from clear_shell_automatically  import *

class Stack:

    def __init__(self):
        self.stack = []

    def add(self,data):
        if data not in self.stack:
            return self.stack.append(data)
            return True
        else :
            return False

    def pop(self):
        if len(self.stack) <= 0:
            return 'no element'
        return self.stack.pop()

    def traveser(self):
        print('stack list : ')
        for i in range(0,len(self.stack)):
            print(self.stack[i])
        print('\n')
    def peek(self):
        try :
            return self.stack[-1]
        except:
            return 'empty stack'


clear()

day_stack = Stack()
day_stack.add('Mon')
day_stack.add('Tue')
day_stack.add('between day!')
day_stack.add('Tue')
day_stack.traveser()
# day_stack.pop()
# day_stack.pop()


print('peek : ',day_stack.peek())
