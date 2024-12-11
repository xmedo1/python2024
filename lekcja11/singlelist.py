class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return not self == other


class SingleList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("Lista jest pusta")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("Lista jest pusta")

        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next

        if previous is None:
            self.head = None
            self.tail = None
        else:
            previous.next = None
            self.tail = previous

        self.length -= 1
        return current

    def join(self, other):
        if other.is_empty():
            return self

        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail

        self.length += other.length
        other.clear()

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def find_min(self):
        if self.is_empty():
            return None

        current = self.head
        minimum = current

        while current is not None:
            if current.data < minimum.data:
                minimum = current
            current = current.next

        return minimum

    def find_max(self):
        if self.is_empty():
            return None

        current = self.head
        maximum = current

        while current is not None:
            if current.data > maximum.data:
                maximum = current
            current = current.next

        return maximum

    def reverse(self):
        current = self.head
        previous = None

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.tail = self.head
        self.head = previous
