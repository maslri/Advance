class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Clod:

    def __init__(self):
        self.head = None
        self.length = 0
         
    def push(self, value) :
        new_node = Node(value)
        if self.head :
            temp = self.head
            while temp.next != self.head :
                temp = temp.next
            else :
                new_node.next = self.head
                self.head = new_node
                temp.next = new_node
                self.length += 1
        else :
            self.head = new_node
            new_node.next = new_node
            self.length = 1

    def pop(self, index=-1) :
        if index == -1 :
            if self.head :
                temp = self.head
                while temp.next.next != self.head :
                    temp = temp.next
                else :
                    value = temp.next.value
                    if self.length == 1 :
                        self.head = None
                    else :
                        temp.next = self.head
                    self.length -= 1
                    return value
            else :
                return None
        else :
            if self.head :
                temp = self.head
                if index > self.length - 1 :
                    index = self.length - 1
                elif index < 0 :
                    temp = self.head
                    while temp.next != self.head :
                        temp = temp.next
                    else :
                        value = self.head.value
                        temp.next = self.head.next
                        self.head = self.head.next
                        self.length -= 1
                        return value
                index -= 1
                while index :
                    temp = temp.next
                    index -= 1
                else :
                    value = temp.next.value
                    temp.next = temp.next.next
                    self.length -= 1
                    return value
            else:
                return None

    def __repr__(self) -> str:
        _str = ""
        if self.head :
            temp = self.head
            while temp.next != self.head :
                _str += str(temp.value) + " --> "
                temp = temp.next
            else :
                _str += str(temp.value) + " --> [LOOP]"
        return _str
    

ml = Clod()
ml.push(1)
ml.push(2)
ml.push(3)
ml.push(4)
ml.push(5)
print(ml)
print(ml.pop(-9))
print(ml)
# print(ml.pop())
# print(ml)
# print(ml.pop())
# print(ml)
# print(ml.pop())
# print(ml)
# print(ml.pop())
# print(ml)
# print(ml.pop())