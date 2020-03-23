from clear_shell_automatically import *

class Queue:

    def __init__(self):
        self.queue = list()

    def insert(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return  True
        return ' exist in list '

    def queue_size(self):
        return int(len(self.queue))

    def print_queue(self):
        for i in range(0,self.queue_size()):
            print(self.queue[i])

    def pop(self):
        if self.queue_size() <= 0:
            return False
        self.queue.pop()
        return True


clear()
test_queue = Queue()
test_queue.insert('boy')
test_queue.insert('girls')
test_queue.insert('old man')
print(test_queue.queue_size())
test_queue.pop()
print(test_queue.queue_size())
test_queue.print_queue()
