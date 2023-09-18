class Node :
    
    def __init__(self, value) :
        self.value = value
        self.next = None

class Customise_Stack :
    
    def __init__(self) :
        self.head = None
        self.length = 0
    
    def push(self, value) :
        new_node = Node(value)
        if self.length :
            new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def pop(self) :
        value = None
        if self.head :
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
        return value
    
    def __repr__(self) -> str:
        _str = ""
        if self.head :
            temp = self.head
            while temp.next :
                _str += str(temp.value) + " --> "
                temp = temp.next
            else :
                _str += str(temp.value)
        return _str
    
my_stack = Customise_Stack()
my_stack.push(21)
my_stack.push(31)
my_stack.push(41)
my_stack.push(51)
print(my_stack)
print(my_stack.pop())
print(my_stack)
print(my_stack.pop())
print(my_stack)
print(my_stack.pop())
print(my_stack)
print(my_stack.pop())
print(my_stack)
print(my_stack.pop())
print(my_stack)