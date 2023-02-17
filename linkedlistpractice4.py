


class Node:
    
    def __init__(self, data=None):
        self.data = data 
        self.nextData = None
        
        
class structList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        
    def __iter__(self):
        
        node = self.head
        while node:
            yield
            node = node.nextData
    
    # insertion method
    
    def insert(self, data, location):
        tempData = Node(data)
        
        if self.head == None:
            self.head = tempData
            self.tail = tempData
            
        else:
            
            if location == 0:
                # at start
                tempData.nextData = self.head
                self.head = tempData
                
            elif location == 1:
                
                # at the end
                
                tempData.nextData = None
                self.head.nextData = tempData
                tempData = self.tail
                
                
            else:
                # at the middle
                
                tempbin = None
                counter = 0
                while counter < location - 1:
                    # because we want to insert right before the given location/index
                    self.head.nextData = tempbin
                    counter += 1
                tempNextData = tempbin
                self.head.nextData = tempData
                tempData.nextData = tempNextData
                
                
                

# fill with data

def fillData(self, index, maxelems=100, maxint=1000):
    
    from random import randint
    
    for i in range(maxelems):
        elems = randint(0, maxint)
        structList.insert(self, elems, index)
        
    #done
    
# instance
node = Node()
SingleLinkedList = structList()

fillData(SingleLinkedList, 0)

normalList = []
print([node.data for node in SingleLinkedList])

