


### Linked List Data Structure


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SLinkedStructure:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def insert(self, data, index):
        
        data = Node(data)
        # check list
        if self.head is None:
            self.head = data
            self.tail = data
            
        else:
            
            if index == 0:
                # at the start
                
                data.next = self.head
                self.head = data
            elif index == 1:
                
                # at the end
                
                data.next = None
                
                # self.tail.next represents the previously last node, right before where we are inserting
                self.tail.next = data
                self.tail = data
                
            else:
                tempBin = self.head
                counter = 0
                while counter < index - 1:
                    self.head.next = tempBin
                    counter += 1
                tempAddr = tempBin
                data.next = tempAddr
                self.tail.next = data
                
    def traverseList(self):
            # check node
            node = self.head
            if node is None:
                return "list empty"
            else:#
                #to do 
                
                
                
        