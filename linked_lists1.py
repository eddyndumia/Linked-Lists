

class Node:
    def __init__(self, value=None):

        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):

        # this is the head of the singly linked list, it points to the first item in the
        self.head = None

        # this is the tail of the singly linked list, it points to the last item in the list
        self.tail = None

    # create a function that makes it iterable for you to print

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                # at the beginning of the list
                newNode.next = self.head
                self.head = newNode

            elif location == 1:

                # at the end of the linkedlist
                # 1. update newnode reference to null as it is the last one on the list
                newNode.next = None
            # 2. reference next of lastnode to point to newnode as next
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0

                # traverse through the items up to the position just before the position we want to insert
                # thats why there is a - 1 in the while loop.
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next

                # update the next.node variable of the item before the position you want to insert to point to the node you are
                # inserting

                # tempNode.next is the variable that points to the-next-node-in-the-list's memory location

                tempNode.next = newNode

                # after updating the previous_node.next variable, now you can update the current_node.next to te

                newNode.next = nextNode


    # init object of SLinkdList()
singlelinkedlist = SLinkedList()

# init object of class node which has members value and next

# think of this node as a balloon filled up with air and tied up with a

# the balloon represents the  data value and the string points to the memory address of the next item in the list

node1 = Node(1)

node2 = Node(2)

# sets the tail data member to point to the memory location of object node1 as the first item in the singly linked list
singlelinkedlist.head = node1
# through OOP we can access the data members of class node and update the pointer firstnode.next to point to
singlelinkedlist.head.next = node2
# the memory location of node2


singlelinkedlist.tail = node2
# sets the tail data member to point to the memory location of item/object node2 as it is the last item in the list


singlyLinkedList = SLinkedList()

singlyLinkedList.insert(9, 1)

print([node.value for node in singlyLinkedList])
