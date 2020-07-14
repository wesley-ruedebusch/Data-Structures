"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_value(self):
        # returns node's data
        return self.data

    def get_next(self):
        # returns the thing pointed at by the node's `next` reference
        return self.next

    def set_next(self, new_next):
    # set this node's next reference to `new_next`
        self.next = new_next

# this is bad
# node = Node(1)
# node.set_next(Node(2))
# node.get_next().set_next(Node(3))
# node.get_next().get_next().set_next(Node(4))

class LinkedList:
    def __init__(self):
        # first node in linked list
        self.head = None
        # last node in linked list
        self.tail = None
# O(1) b/c operation does not depend on size of linked list
    def add_to_tail(self, data):
        # adds 'data' to the end of linked list
        # wrap 'data' in a Node instance
        new_node = Node(data)

        # what about the empty case when self.head = None 
        # and self.tail = None 
        if not self.head and not self.tail:
            # list is empty
            # update both head and tail to point to new node
            self.head = new_node
            self.tail = new_node
        # non-empty linked list case
        else:
            # call set_next with the new_node on the current tail node
            self.tail.set_next(new_node)
            # update self.tail to point to the new last Node in the linked list
            self.tail = new_node

    def remove_from_head(self):
        # removes the Node that self.head is refering to
        # returns the Node's data
        if self.head is None:
            return None

        # # save head node's data,
        data = self.head.get_data()

        if self.head is self.tail:
            # if both head and tail refer to same node
            # there's only one node in teh linked list
            self.head = None
            self.tail = None
        else:
            # if we have more than one node in liked list
            # # delete head node, 
                # python's runtime will automatically delete this
                # once nothing refers to the node
            # # update self.head to the node AFTER the one we just deleted
            self.head = self.head.get_next()
        return data
"""
To hopefully summarise some of the things he’s gone over so far:
A linked list is comprised of nodes that have a value and next property. The value is the data associated with that node, and the next property points to whatever value (if any) comes after it.
Hence it is represented as values (contained in a circle/node) and arrows:
1 -> 2 -> 3 -> 4
To keep track of an entire “list” of nodes, the linked list class itself has head and tail properties that point to the starting and ending nodes.
Because there is a pointer to the tail node, it makes it much easier to create another node and then set the tail’s pointer to that new node.
"""
