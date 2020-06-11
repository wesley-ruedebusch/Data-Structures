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
class BSTNode:
    def __init__(self, value):
        if value < self.value:
            # go left
            # check for another node
            if self.left:
                #then self.left is a node
               self.left.insert(value)
            else:
                self.left = BSTNode(value)
        # if greater than or equal, 
        else:
            # go right
            # check for another node
            if self.right:
                #then self.right is a node
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Insert the given value into the tree
    def insert(self, value):
        # check if tree is empty
        if self is None:
            return False
        # check if self is the target
        elif self.value == target:
            return True
        elif target < self.value:
            if self.left:
               return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
               return self.right.contains(target)
            else:
                return False 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
