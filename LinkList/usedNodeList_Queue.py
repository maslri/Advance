class Node :
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

# Two-Sided NodeList
class Customise_Queue :
    
    def __init__(self) :
        self.head = None
        self.length = 0
        self.front = None

    def enqueue(self, value) :
        new_node = Node(value)
        if self.head :
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else :
            self.head = new_node
            self.front = new_node
        self.length += 1

    def dequeue(self) :
        if self.length <= 1 :
            if self.length == 0 :
                print("Queue is Empty!")
                return ""
            else :
                value = self.front.value
                self.head = None
                self.front = None
                self.length -= 1
                return value
        else :
            value = self.front.value
            self.front = self.front.prev
            self.front.next = None
            self.length -= 1
            return value
    
    def __repr__(self) :
        if self.length :
            _str = ""
            temp = self.head
            while temp.next :
                _str += str(temp.value) + " <--> "
                temp = temp.next
            else :
                _str += str(temp.value)
            return _str
        else :
            return ""

my_que = Customise_Queue()
my_que.enqueue(1)
my_que.enqueue(2)
my_que.enqueue(3)
my_que.enqueue(4)
my_que.enqueue(5)

print(my_que)
print(my_que.dequeue())
print(my_que)
print(my_que.dequeue())
print(my_que)
my_que.enqueue(11)
print(my_que)