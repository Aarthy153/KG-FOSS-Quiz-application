# Python program to find largest value
# on each level of binary tree.
 
""" Recursive function to find
the largest value on each level """
def helper(res, root, d):
 
    if ( not root):
        return
 
    # Expand list size
    if (d == len(res)):
        res.append(root.val)
 
    else:
 
        # to ensure largest value
        # on level is being stored
        res[d] = max(res[d], root.val)
 
    # Recursively traverse left and
    # right subtrees in order to find
    # out the largest value on each level
    helper(res, root.left, d + 1)
    helper(res, root.right, d + 1)
 
 
# function to find largest values
def largestValues(root):
 
    res = []
    helper(res, root, 0)
    return res
 
 
# Helper function that allocates a new
# node with the given data and None left
# and right pointers.                                    
class newNode:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
 
         
# Driver Code
if __name__ == '__main__':
    """ Let us construct the following Tree
        4
        / \
        9 2
    / \ \
    3 5 7 """
    root = newNode(4)
    root.left = newNode(9)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.right = newNode()