class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(f"{self.val}--->{self.next}")

class linked_list:
    def __init__(self, node: Node):
        self.head: Node = node
        self.tail = None

    def prepend(self, node: Node):
        node.next = self.head
        self.head = node

    def append(self, node: Node):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node

    def __repr__(self):
        curr = self.head
        rep = ""
        while curr.next != None:
            rep += f"{curr.val}-->"
            curr = curr.next
        rep += f"{curr.val}-->NULL"
        return rep

