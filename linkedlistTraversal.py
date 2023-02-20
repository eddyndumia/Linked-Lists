

# make list struct

class Node:
    def __init__(self, data=None) -> None:
        self.data = data 
        self.next = None
        
class List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
      objects = self.head
      while objects:
          yield objects
          objects = objects.next
    
    def insert(self, data, index):
        rawData = Node(data)
        # check head first
        
        if self.head is not None:
            self.head = rawData 
            self.tail = rawData
        else:
            # insertion
            if index == 0:
                # at start
                rawData.next = self.head
                self.head = rawData
                
                
            elif index == 1:
                
                # at the end
                
                rawData.next = None
                self.tail.next = rawData
                self.tail = rawData
                
            else:
                
                # worst case, at middle
                tempBin = self.head
                counter = 0
                while counter < index - 1:
                    
                    self.head.next = tempBin
                    counter += 1
                tempAddress = tempBin
                rawData.next = tempAddress
                self.head = rawData
            
            
    def traverseList(self):
        if self.head is None:
            print("List is EMPTY!")
        else:
            node = self.head
            while node is not None:
                print(node.data)
                node = node.next
                
node = Node()
list1 = List()
list1.insert(2,0)
list1.insert(3,0)

list1.insert(4,0)
print([node.data for node in list1])
list1.traverseList()

            