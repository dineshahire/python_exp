import random class Node:
def init (self, data=None):
self.data = data self.next = None
class LinkedList: def
    init    (self):
self.head = None
# Adding a node to the end of the linked list def append (self, data): new_node = Node(data) if self.head is None: self.head = new_node return last_node = self.head while last_node.next: last_node = last_node.next last_node.next = new_node def print_list (self): current_node = self.head while current_node:
print (current_node.data, end=" -> ") current_node = current_node.next print ("None")

class Stack:
def init (self):
self.items = []
# Adding an element to the top of the stack def push (self, item): self.items.append(item)
# Removing the top element from the stack def pop (self): if not self.is_empty (): return self.items.pop() def is_empty (self): return len (self.items) ==
0 def peek (self): if not




self.is_empty (): return self.items[-1] def print_stack (self):
print (self.items)

from collections import deque class Queue:
def init (self):
self.items = deque ()
# Adding an element to the end of the queue def enqueue (self, item): self.items.append(item)
# Removing the front element from the queue def dequeue (self): if not self.is_empty(): return self.items.popleft () # Checking if the queue is empty
def is_empty (self):
return len (self.items) == 0
# Returning the front element of the queue without removing it def peek (self): if not self.is_empty (): return self.items[0] # Printing the queue
def print_queue (self):
print (self.items)

# Creating an instance of the linked list llist = LinkedList ()
# Appending random values to the linked list for i in range (10): llist.append(random.randint(1, 100))
# Printing the linked list print("Linked List:") llist.print_list()
# Creating an instance of the stack




stack = Stack () for i in range (5): stack.push(random.randint (1, 100)) print ("\nStack:") stack.print_stack () queue = Queue () for i in range (5): queue.enqueue(random.randint (1, 100)) print ("\n Queue:")
queue.print_queue ()
