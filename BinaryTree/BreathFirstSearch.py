from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs_traversal(root):
    result = []
    if not root:
        return result

    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.val)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result

# Example usage:
# Construct a sample binary tree
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

# Perform BFS traversal
bfs_result = bfs_traversal(root)
print("BFS Traversal:", bfs_result)
