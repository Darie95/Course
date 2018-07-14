""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

min = 0
max =10**6

def checkBST(root):
    return additional_check(root, min, max)

def additional_check(root, min, max):
    if root is None:
        return True
    elif root.data > min and root.data < max:
        return additional_check(root.left, min, root.data) and additional_check(root.right, root.data, max)
    else:
        return False


# why it doesn't work???
# def checkBST(root):
#     if root is None or (root.left is None and root.right is None):
#         return True
#     elif root.left is None and root.right and  root.data < root.right.data:
#         return checkBST(root.right)
#     elif root.right is None and root.left and root.data > root.left.data:
#         return checkBST(root.left)
#     elif root.data > root.left.data and root.data < root.right.data:
#         return checkBST(root.right) and checkBST(root.right)
#     else:
#         return False
