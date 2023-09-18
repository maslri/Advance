class Node :
    
    def __init__(self, value) :
        self.value = value
        self.next = None

class Customise_Queue :
    
    def __init__(self) :
        self.head = None
        self.length = 0
        self.first = None

    def enqueue(self, value) :
        new_node = Node(value)
        if self.head == None :
            self.head = new_node
            self.first = new_node
            self.length = 1
        else :
            self.first.next = new_node
            self.first = new_node
            self.length += 1
    
    def dequeue(self) :
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

mq = Customise_Queue()
mq.enqueue(2)
mq.enqueue(22)
mq.enqueue(222)
mq.enqueue(2222)
print(mq)
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())
print(mq.dequeue())