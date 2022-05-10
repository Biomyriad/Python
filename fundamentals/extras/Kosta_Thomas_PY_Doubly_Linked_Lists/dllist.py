class Dllist:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    def add(self, value):
        if self.head == None:
            self.length += 1
            self.head = Dlnode(value)
            self.tail = self.head
            return self
        self.length += 1
        node = Dlnode(value)
        node.prev = self.tail
        node.next = self.head
        self.tail.next = node
        self.tail = node
        self.head.prev = self.tail
        return self
    def remove_val(self, value):
        node = self.head
        for i in range(0, self.length):
            if node.value == value:
                self.length -= 1
                node.prev.next = node.next
                node.next.prev = node.prev
                return self
            node = node.next
        return self
    def incert_val(self, value, index):
        # consider allowing to insert at tail...
        node = self.head
        for i in range(0, self.length):
            if i == index:
                self.length += 1
                new_node = Dlnode(value)
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
                if i == 0:
                    self.head = new_node
                return self
            node = node.next
        return self
    def print_all(self):
        node = self.head
        for i in range(0, self.length):
            print(node.value)
            node = node.next
        return self

class Dlnode:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None