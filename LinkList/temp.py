from NodeList import Linked_list, Node

ll = Linked_list()
first = Node(5)
first.next = Node(2)
first.next.next = Node(12)
first.next.next.next = Node(76)
first.next.next.next.next = first.next.next
ll.head = first

# print(ll.hasLoop())
print(ll.hasLoop_old())