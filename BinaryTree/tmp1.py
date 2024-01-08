class Binary_Tree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    ## Error !?
    def add_child(self, data) :
        if type(data) != Binary_Tree :
            data = Binary_Tree(data)
        if self.left is None :
            self.left = data
        elif self.right is None :
            self.right = data
        else :
            self.left.add_child(data)
    
def isStrict(root : Binary_Tree) -> bool:
    if root is None :
        return True
    if root.left == None and root.right == None :
        return True
    if root.left is not None and root.right is not None :
       return isStrict(root.left) and isStrict(root.right)
    return False

def countNodes(root : Binary_Tree) -> int :
    if root is None :
        return 0
    return ( 1 + countNodes(root.left) + countNodes(root.right))

def isComplete(root : Binary_Tree, index : int, number_nodes : int) -> bool:
    if root is None :
        return True
    if index >= number_nodes :
        return False
    return (isComplete(root.left, 2*index+1, number_nodes) 
                and isComplete(root.right, 2*index+2, number_nodes))

root = Binary_Tree(5)
root.add_child(3)
root.add_child(4)
root.add_child(1)
root.add_child(2)
root.add_child(6)
root.add_child(8)
root.add_child(9)

print(isStrict(root))
print(isStrict(root))