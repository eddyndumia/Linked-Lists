

# this is a single linked list practice with little to no reference

# first i have to initialize the structure using two classes

# class 1:

class Node:

    # has two members, value and next

    # init

    def __init__(self, value=None):

        # next we initialize two values, value points to the address of the value, next points to the address of the next value
        self.value = value
        self.next = None

# class 2:


class SingleLinkedList:
    # this class holds two members,
    # head and tail, head points to the first Node object on the list and tail points to the last

    # init
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

        # next we create an insert method inside the Single Linkded List

    def insert(self, value, location):

        insertValue = Node(value)

        # check if the list has any value in it first by checking the value of the head

        # remember, to access any element in a linked list, you have to iterate over the list

        if self.head == None:
            self.head = insertValue
            self.tail = insertValue

            # if there exists values

        else:

            # insertion at the beginning of the list

            if location == 0:
                insertValue.next = self.head
                self.head = insertValue

            # insertion at the end of the list

            elif location == 1:

                self.tail.next = insertValue
                self.tail = insertValue
                insertValue.next = None

            # worst case scenario, insertion at the middle

            else:
                newNextNode = None
                counter = 0
                while counter < location - 1:
                    self.head.next = newNextNode
                    counter += 1

                # grab the memory location of the node we want to push to the bottom half
                nextAddress = newNextNode
                self.head.next = insertValue
                insertValue.next = nextAddress


# instantiate the list as an object, and also the node class for the head and tail members
node = Node()
mylinkedList = SingleLinkedList()


def insertData(self, maxelem=1000, maxint=100):
    from random import randint
    for i in range(maxint):
        elems = randint(0,maxelem)
        mylinkedList.insert(elems, 0)
    
    return "all data inserted successfully"
        
insertData(mylinkedList)


print([node.value for node in mylinkedList])
