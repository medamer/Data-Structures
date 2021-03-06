"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
# sys.path.append('./queue/queue.py')
# from queue import Queue
# sys.path.append('./stack/stack.py')
# from stack import Stack
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList

######## IMPORT QUEUE AND STACK CLASS ############
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()

########################

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()

######################################################

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if new_node.value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                return self.right.insert(value)
        elif new_node.value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if the LL us empty:
        if not self.value:
            return None
        # Check if the target == the root:
        elif self.value == target:
            return True
        # check if the target smaller than root:
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # check if the target is greater than root:
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return None
        elif self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        node = self
        while node:
            if node is None:
                return
            if node is not None:
                print(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
            node = queue.dequeue()


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()
        node = self
        while node:
            if node is None:
                return
            if node is not None:
                print(node.value)
            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)
            node = stack.pop()
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft()
        if self.right is not None:
            self.right.pre_order_dft()
        

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left is not None:
            self.left.post_order_dft()
        if self.right is not None:
            self.right.post_order_dft()
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""

bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  