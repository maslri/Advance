class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            else:
                temp.next = new_node
        else:
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index<=0:
            self.push(value)
        elif index>=self.length-1:
            self.append(value)
        else:
            temp = pre = self.head
            while index:
                pre = temp
                temp = temp.next
                index-=1
            else:
                new_node = Node(value)
                new_node.next = temp
                pre.next = new_node

    def setter(self, lst):
        self.head = None
        self.length = 0
        for value in lst[::-1]:
            self.push(value)
    
    def pop(self, index=0):
        if self.length:
            if index<=0:
                value = self.head.value
                self.head = self.head.next
            else:
                temp = pre = self.head
                while index and temp.next:
                    pre = temp
                    temp = temp.next
                    index-=1
                else:
                    value = temp.value
                    pre.next = temp.next
            self.length-=1
            return value
        else:
            return None
        
    def reverse(self) :
        pre = None
        current = self.head
        while current :
            _next = current.next
            current.next = pre
            pre = current
            current = _next
        self.head = pre

    def __len__(self):
        return self.length

    def isempty(self):
        return self.length == 0

    def __repr__(self):
        _str = ""
        temp = self.head
        while temp.next:
            _str += str(temp.value) + " -> "
            temp = temp.next
        else:
            _str += str(temp.value)
        return _str
    
    def hasLoop_old(self) :
        loop_set = set()
        temp = self.head
        while temp.next :
            if temp not in loop_set :
                loop_set.add(temp)
                temp = temp.next
            else :
                return True
        else :
            return False
    
    def hasLoop(self) :
        slow = fast = self.head
        while slow and fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
        else :
            return False
