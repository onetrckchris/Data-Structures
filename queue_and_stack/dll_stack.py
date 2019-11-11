import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        # print("This is the tail: ", self.storage.tail.value)
        # print("This is the head: ", self.storage.head.value)

    def pop(self):
        if self.storage.head:
            self.storage.remove_from_head()
        # print("This is the tail I'm trying to pop(): ", self.storage)

    def len(self):
        return self.storage.length

test_stack = Stack()
test_stack.push(5)
test_stack.push(10)
test_stack.push(52)
test_stack.pop()
test_stack.pop()
print("Test stack: ", test_stack.storage)
