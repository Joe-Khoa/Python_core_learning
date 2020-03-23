import clear_shell_automatically as clear

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SLinklist:        # start_link_list
    def __init__(self):
        self.head_val = None

    # TRAVERSER
    def list_traverser(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next

    # Add_new_node
    def at_beginning(self,new_val):
        NewNode = Node(new_val)
        # UPDATE new_node_next to current head
        NewNode.next = self.head_val
        self.head_val = NewNode

    def at_the_end(self,new_val):
        NewNode = Node(new_val)
        if self.head_val is None:
            self.head_val = NewNode
        last = self.head_val
         # initial_1st_element
        while last.next:
            last = last.next # next_Node
        last.next = NewNode

    def at_between(self,between_node,new_val):
        if between_node.data == None:
            print('The note is absent!')
            return
        NewNode = Node(new_val)
        NewNode.next = between_node.next    # nextue_of_new !!!
        between_node.next = NewNode             # so : next_of_between

    def remove_a_node(self,Removekey):
        HeadVal = self.head_val
        if (HeadVal is not None):   # exist head
            if (HeadVal.data == Removekey):
                self.head_val = HeadVal.next    # assign data_head->2nd_element
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            print('head_val', HeadVal)
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        HeadVal = None


clear.clear()

list = SLinklist()
list.head_val = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')
# Link 1st to 2nd
list.head_val.next = e2
e2.next = e3
list.at_beginning('Sunday')
list.at_the_end('Fri')
list.at_between(list.head_val,'What a day')
list.remove_a_node('Tue')

list.list_traverser()
