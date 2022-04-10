class stack:
    # A doubly-linked list.
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items = []

    def enqueue(self, data):
        self.items.insert(0, data) 

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items [-1]

    def size(self):
        return len(self.items) 

class queue:
    # A doubly-linked list.
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items [-1]

    def size(self):
        return len(self.items)        