



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


def insert (self, value, location):
    newNode = Node(value)
    
    if self.head is None:
        self.head = newNode 
        self.tail = newNode
    else:
        if location is 0:
            newNode.next = self.head 
            self.head = newNode
        elif location is 1:
            
            # at the end of the linkedlist
            # 1. update newnode reference to null as it is the last one on the list
            newNode.next = None
            # 2. 
            
            
            
            
            
            
            
            
            
            
            
            