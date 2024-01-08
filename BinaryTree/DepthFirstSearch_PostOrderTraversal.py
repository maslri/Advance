class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root):
    result = []
    if root:
        result += postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.val)
    return result

# Example usage:
# Construct a sample binary tree
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

# Perform DFS postorder traversal
postorder_result = postorder_traversal(root)
print("Postorder Traversal:", postorder_result)
