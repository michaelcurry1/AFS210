from itertools import count
from operator import indexOf
from threading import currentThread


class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        node0 = Node (data)
        node0.next = self.head
        if self.head:
            self.head.prev = node0
        self.head = node0
            
        self.count += 1
        if self.count == 1:
            self.tail = self.head
        # print(self.head.data)
        # print(self.head.prev)
        # print(self.head.next.data)
        # print(node0.data)
        # print(node0.next.data)

    def addLast(self, data) -> None:
        # Add a node at the end of the list
        node4 = Node (data)

        self.tail.next = node4
        node4.prev = self.tail

        # print(self.tail.data)
        # print(self.tail.prev.data)
        # print(self.tail.next.data)
        # print(node4.data)
        # print(node4.prev.data)
        self.tail = node4
        self.count += 1


    def addAtIndex(self, data, index):
        newNode = Node(data)
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        if self.count == index:
            self.addLast(newNode)
            # return self.tail
        # If index is greater than the length, the data will not be inserted.
        if index > self.count:
            return None
        if index == 0:
            self.addFirst(newNode)
            # return self.head
        # Add a node to the list at the given index position
        # This function does not replace the data at the index, but pushes everything else down.
        else:
            n = 0
            current = self.head
            
            for _ in range (index -1):
                current = current.next
            newNode.next = current.next
            newNode.prev = current
            current.next = newNode
            current.next.prev = newNode
            self.count += 1

            # print(current.data)
            # print(next.data)
            
                    
                
      
       

      


        # self.count += 1
    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1  
        pos = -1

        for node in self.iter():
            pos += 1
            if data == node:
                return pos  
        


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr



# class Node:
#     # A doubly-linked node.
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#         self.prev = None
    
# class DoublyLinkedList:
#     # A doubly-linked list.
#     def __init__(self):
#         # Create an empty list.
#         self.tail = None
#         self.head = None
#         self.count = 0
# node1 = Node (7)
# node2 = Node (8)
# node3 = Node (9)

list = DoublyLinkedList()

list.addFirst("May")
list.add("the")
list.add("force")
list.add("be")
list.add("with")
list.add("you")
list.add("!")
print(list)
print(list.indexOf("with"))
list.delete("you")
list.addAtIndex("us",5)
list.addAtIndex("all",6)
print(list)

# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# list.head = node1
# list.tail = node3
# list.count = 3
# list.addFirst(6)
# list.addLast(10)
# list.addAtIndex(11,5)
# list.addAtIndex(20,9)
# list.addAtIndex(5,0)
# list.addAtIndex(8.5,3)

# print(list.count) 
# print(list.head.data)
# print(list.head.next.data)
# print(list.head.next.next.data)
# print(list.head.next.next.next.data)
# print(list.head.next.next.next.next.data)
# print(list.head.next.next.next.next.next.data) 
# print(list.head.next.next.next.next.next.next.data) 
# print(list.head.next.next.next.next.next.next.next.data) 
# # print(list.head.next.next.next.next.next.next.next.next.data) 
# # print(list.head.next.next.next.next.next.data) 
# # print(list.head.next.next.next.next.next.data) 

# print(list.tail.data)
# print(list.tail.prev.data)
# print(list.tail.prev.prev.data)
# print(list.tail.prev.prev.prev.data)
# print(list.tail.prev.prev.prev.prev.data) 
# print(list.tail.prev.prev.prev.prev.prev.data) 
# # print(list.tail.prev.prev.prev.prev.prev.data) 
# # print(list.tail.prev.prev.prev.prev.prev.data) 
# # print(list.tail.prev.prev.prev.prev.prev.data) 
# # print(list.tail.prev.prev.prev.prev.prev.data) 
# print(list)
# print(list.indexOf(8.5))