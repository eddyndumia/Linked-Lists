

# classes

class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.ref = None
        
class struct:
    
    def __init__(self):
        self.h = None
        self.t = None
        
    # make iterable
    
    def __iter__(self):
        object = self.h 
        while object:
            yield object
            object = object.ref  
    
    # create insertion method
    
    def insert(self, data, index):
        
        tempData = Node(data)
        # first check if list has items to determine insertion functions
        
        if self.h == None:
            self.h = tempData
            self.t = tempData
        else:
            
            
            #insertion at start 0
            
            if index == 0:
                
                tempData.ref = self.h
                self.h = tempData
                
            # insertion at the end 1
            
            elif index == 1:
                
                tempData.ref = None
                self.ref = tempData
                self.t = tempData
                
            # insertion at the middle 
            
            else:
                
                bin1 = self.h
                counter = 0
                while counter < index - 1:
                    bin1 = self.h.ref 
                    counter += 1
                tempAddress = bin1
                self.h.ref = tempData
                tempData.ref = tempAddress
                


# function to fill it with test data 
node = Node()

list1 = struct() 

def fillData(self, location, maxelems=100, maxint=1000):
    
    from random import randint
    for i in range(maxelems):
        elems = randint(0, maxint)
        struct.insert(self, elems, location)
        
        
# instance 

list002 = struct()
list001 = struct()

fillData(list1, 2)
fillData(list001, 0)
fillData(list002, 4)


# print



list2 = [node.data for node in list1]
list001 = [node.data for node in list001]
list002 = [node.data for node in list002]


list3 = []
list3 += list002 + list001
tupletest = tuple(list3)
print(tupletest)


                
                
        