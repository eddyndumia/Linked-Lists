
# linked list data strcuture

 #start by two classes 
 
class Node:
    # takes value, ref
    def __init__(self, data=None):
         self.data = data
         self.ref = None
         
         
class SingleLinkedList:
    # init the class memebers head tail
    
    def __init__(self):
        self.head = None  
        self.tail = None 

    # make it iterable
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.ref

          
      
      
    # create insert function  --> takes parameters (self, data and location)
    
    def insert(self, data, location):
        tempData = Node(data)
        
        
        # check if list has items by checking if head is non
        if self.head == None:
            self.head = tempData
            self.tail = tempData
        
        else: # insert data at at start, middle and end
            
            # insertion at the start
            if location == 0:
                tempData.ref = self.head
                self.head = tempData
                
            # insertion at the end
            
            elif location == 1:
                
                # reference tempData to tail
                tempData.ref = self.tail
                self.tail = tempData
                self.tail.ref = None
                
            # wost case scenario insertion at the middle 
            
            else:
                fetchAddress = self.head
                counter = 0
                
                while counter < location - 1:
                    fetchAddress = self.head.ref
                    counter += 1
                tempAddress = fetchAddress
                self.head.ref = tempData
                tempData.ref = tempAddress
                


# instantiate both classes as objects

node = Node()

mytestList = SingleLinkedList()

# fill list with random integers


def fillData(self):
    from random import randint
    for i in range(1000):
        elems = randint(0, 1000)
        SingleLinkedList.insert(self, elems, 1)
        
# call the function to insert

fillData(mytestList)

mytestListWithData = [node.data for node in mytestList]


print(mytestListWithData)
        
                
                
                
                
                
                
                
                
                
            
            
            
        
    