class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    result = []
    if root:
        result.append(root.val)
        result += preorder_traversal(root.left)
        result += preorder_traversal(root.right)
    return result

# Example usage:
# Construct a sample binary tree
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

# Perform DFS preorder traversal
preorder_result = preorder_traversal(root)
print("Preorder Traversal:", preorder_result)
