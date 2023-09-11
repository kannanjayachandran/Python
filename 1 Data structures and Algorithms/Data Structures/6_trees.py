class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

"""
     1
    / \
   2   3
  / \
 4   5
 
"""


# In-Order Traversal
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)


# To start the traversal from the root node
print("In-Order Traversal: ")
in_order_traversal(root)


# Pre-Order Traversal
def pre_order_traversal(node):
    if node:
        print(node.data, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


# To start the traversal from the root node
print("\nPre-Order Traversal: ")
pre_order_traversal(root)
# Output: 1 2 4 5 3


# Post-Order Traversal
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")


# To start the traversal from the root node
print("\nPost-Order Traversal: ")
post_order_traversal(root)
# Output: 4 5 2 3 1
