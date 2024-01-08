class Binary_search_tree :

    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def search(self, val) -> bool :
        if self.data == val :
            return True
        elif self.data > val :
            if self.left :
                return self.left.search(val)
            else :
                return False
        else :
            if self.right :
                return self.right.search(val)
            else :
                return False

    def add(self, val) :
        if self.data == val :
            return
        elif self.data > val :
            if self.left == None :
                self.left = Binary_search_tree(val)
            else :
                self.left.add(val)
        else :
            if self.right == None :
                self.right = Binary_search_tree(val)
            else :
                self.right.add(val)
    
    def inorder_traversal(self) :
        elements = []
        if self.left :
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements
    
    def preorder_traversal(self) :
        elements = []
        elements.append(self.data)
        if self.left :
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()
        return elements
    
    def postorder_traversal(self) :
        elements = []
        if self.left :
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()
        elements.append(self.data)
        return elements
    
    def reverse(self) :
        self.right, self.left = self.left, self.right
        if self.left :
            self.left.reverse()
        if self.right :
            self.right.reverse()
    

elements = [15, 12, 27, 7, 14, 20, 88, 23]
root = Binary_search_tree(elements[0])
for i in elements[1:] :
    root.add(i)
