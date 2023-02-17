


# start

class Node:
    
    def __init__(self,data=None):
      self.data = data
      self.nextData = None
      
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.nextData 
    
    # insert function
    
    def insert(self, data, location):
        tempData = Node(data)
        
        if self.head == None:
            self.head = tempData
            self.tail = tempData
            
        else:
            
            if location == 0:
                # insetion at the start ,0
                tempData.nextData = self.head
                self.head = tempData
                
            elif location == 1:
                
                # insertion at the end, 1
                tempData.nextData = None
                self.tail.nextData = tempData
                self.tail = tempData
                
            else:
                
                # insertion at the middle
                tempBin = self.head
                counter = 0
                while counter < location:
                    self.head.nexData = tempBin
                    counter += 1
                tempAddrNextData = tempBin
                tempData = tempAddrNextData
                self.tail.nextData = tempData
                tempData.nextData = tempAddrNextData
                
                
                
# data fill function

def fillWithData(self, index, maxelems=100, maxint=100):
    from random import randint
    
    for i in range(maxelems):
        elems = randint(0, maxint)
        SingleLinkedList.insert(self,elems, index)
        

# instance 

node = Node()
list1 = SingleLinkedList()
fillWithData(list1, 1)

print([node.data for node in list1])

