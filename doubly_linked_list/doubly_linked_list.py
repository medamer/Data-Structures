"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        if self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.value
            self.tail.prev = None
            self.head = self.tail
            self.length -= 1
            return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_tail = ListNode(value, None, None)
        if not self.head and not self.tail:
            self.head = new_tail
            self.tail = new_tail
            self.length += 1
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        if self.head is self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -=1
            return value
        else:
            value = self.tail
            self.tail.prev = self.tail.value
            self.tail.next = None
            self.length -=1
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if not self.head and self.tail:
            return None
        if self.head is self.tail:
            return None
        else:
            new_head = self.tail
            self.tail.next = self.head
            self.head.prev = new_head
            self.tail.prev = None
            self.head.next = None
            self.head = new_head
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if not self.head and self.tail:
            return None
        if self.head is self.tail:
            return None
        else:
            new_tail = self.head
            self.head.prev = self.tail
            self.tail.next = new_tail
            self.head.next = None
            self.tail = new_tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and node:
            return None
        elif self.head is node:
            self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev
            self.length -=1
        elif self.tail is node:
            self.tail = node.prev
            if node.prev is not None:
                node.prev.next = node.next
            self.lentgh -=1
        else:
            node = None
            self.length -=1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head and self.tail:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

