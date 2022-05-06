import random

class Node:
    # A doubly_linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # create empty list.
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
        # Returns the number of elements in the list.
        return self.count

    def getStart(self):
        return self.head

    def getEnd(self):
        return self.tail

    def addFirst(self, data) -> None:
        # Add a node at front of list.
        node = Node(data)
        node.next = self.head
        self.head = node
        if not self.tail:
            # first node on the list
            self.tail = node
        self.count += 1

    def addLast(self, data) -> None:
        # Add a node at end of the list.
        node = Node(data)
        self.count += 1

        # first node on the list.
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def add(self, data) -> None:
            # Append an item to the end of the list.
            self.addLast(data)

    def addAtIndex(self, data, index):
            # Add a node to the list at the given index position.
            # If index equals to the length of linked list, the node will be appended to the end of the linked list.
            # I f index is greater than length, the data will not be inserted.

            if index > self.count:
                return

            if (index == self.count):
                self.addLast(data)
                return

            curr = self.head
            prev = self.head

            for n in range(index):
                prev = curr
                curr = curr.next

            node = Node(data)
            prev.next = node
            node.prev = prev
            node.next = curr
            curr.prev = node
            self.count = 0

            return

    def clear(self) -> None:
            # Remove all of the items from list.
            self.head = None
            self.tail = None
            self.count = 0

    def deleteAtIndex(self, index) -> None:
            #Delete the node at the index-th in the linked list, if the index is valid.

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
            # Delete a node from the list Who's value matches the supplied value.
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

    def indexOf(self, data):
        # Search through the list. Return the index position if data found, otherwise return -1
        pos = -1

        for node in self.iter():
            pos += 1
            if data == node:
                return pos
        return pos

    # Bubblesort
    def sortList(self):
        # Check whether list is empty.
        if(self.head == None):
            return
        else:
            # Current will point to head.
            current = self.head
            while(current.next != None):
                # I f currtnt's data is greater than index's data, swap the data of current and index.
                if(current.data > index.data):
                    temp = current.data
                    current.data = index.data
                    index.data = temp
                index = index.next
            current = current.next
    
    # Modified version of a Bubble sort.
    # Instead of comparing elements and sorting based on value.
    # Swap randomly while traversing the list.
    def shuffleList(self):
        # Check if list is empty.
        if(self.head == None):
            return
        else:
            # Current will point to head.
            current = self.head
            while(current.next != None):
                # Index will point to node next to current.
                index = current.next
                while(index != None):
                    # If current's data is greater than index's data, swap the data of current and index.
                    if (random.randint(0, 1) == 1):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index Out Of Range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index Out Of Range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        pos = 0
        for node in self.iter():
            myStr += str(pos) + ", " + str(node)+ "\n"
            pos += 1
        return myStr

        



        




    