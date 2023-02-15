



class Node:
    def __init__(self, value=None):
        
        self.value = value
        self.next = None
        

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
singlelinkedlist = SLinkedList()

node1 = Node(1)
node2 = Node(2)

singlelinkedlist.head = node1
singlelinkedlist.head.next = node2
singlelinkedlist.tail = node2



""