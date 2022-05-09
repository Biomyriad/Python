class SList:
    def __init__(self, value=None):
        self.head = None
        self.lnode = None
        self.length = 0
    def append(self, value):
        self.length += 1
        if self.head == None:
            self.head = Slnode(value)
            self.lnode = self.head
            return self
        new_node = Slnode(value)
        self.lnode.nnode = new_node
        self.lnode = new_node
        return self
    def incert_front(self, value):
        self.length += 1
        if self.head == None:
            self.head = Slnode(value)
            self.lnode = self.head
            return self
        new_node = Slnode(value)
        new_node.nnode = self.head
        self.head = new_node
        return self
    def remove_front(self):
        if self.head == None:
            return self
        self.length -= 1
        self.head = self.head.nnode
        return self
    def remove_back(self):
        if self.head == None:
            return self
        if self.head.nnode == None:
            self.remove_front()
            return self
        node = self.head
        while not node.nnode.nnode == None:
            node = node.nnode
        node.nnode = None
        self.length -= 1
        return self
    def remove_val(self, value):
        if self.head == None:
            return self
        if self.head.value == value:
            self.remove_front()
            return self
        if self.lnode.value == value:
            self.remove_back()
            return self
        node = self.head.nnode
        pre_node = self.head
        while not node.value == value:
            pre_node = node
            node = node.nnode
        pre_node.nnode = node.nnode
        self.length -= 1
        return self
    def insert_at(self, value, n):
        if n > self.length:
            return self
        if n == 0:
            self.incert_front(value)
            return self
        if n == self.length:
            self.append(value)
            return self
        self.length += 1
        idx = 0
        node = self.head
        pre_node = None
        while True:
            pre_node = node
            node = node.nnode
            idx += 1
            if idx == n:
                new_node = Slnode(value)
                new_node.nnode = node
                pre_node.nnode = new_node
                return self
    def print_all(self):
        last_node = self.head
        if not self.head == None:
            while True:
                print(last_node.value)
                if not last_node.nnode == None:
                    last_node = last_node.nnode
                else:
                    break
        return self

class Slnode:
    def __init__(self, value):
        self.nnode = None
        self.value = value