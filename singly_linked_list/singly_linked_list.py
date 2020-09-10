
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def remove_head(self):
        # Empty list:
        if self.head is None:
            return None
        # One item:
        if self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        # More than one item:
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        # Empty:
        if self.tail is None:
            return None
        # One item:
        if self.head.get_next() is None:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        
        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value
