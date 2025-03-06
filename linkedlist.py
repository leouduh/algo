class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node | None = None
        self.prev: Node | None = None

    def __repr__(self):
        return str(f"{self.val}--->{self.next}")

class linked_list:
    def __init__(self, node: Node):
        self.head: Node = node
        self.tail: Node | None = None

    def prepend(self, node: Node):
        node.next = self.head
        self.head = node

    def append(self, node: Node):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node
        return self

    def insert_node(self, node: Node, loc: int):
        if loc > self.length():
            raise ValueError("You are trying to insert out of bounds of the linkedlist")
        if loc == 0:
            self.prepend(node)
        curr = self.head
        for _ in range(loc - 1):
            curr = curr.next
        curr.next, node.next = node, curr.next

    def length(self):
        count = 0
        curr = self.head
        while curr.next:
            count +=  1
            curr = curr.next
        count += 1
        return count


    def __repr__(self):
        curr = self.head
        rep = ""
        while curr.next != None:
            rep += f"{curr.val}-->"
            curr = curr.next
        rep += f"{curr.val}-->NULL"
        return rep

l = linked_list(Node(2))
a = Node(4)
b = Node(6)
c = Node(8)
l.append(a).append(b).append(c)
print(l)
l.insert_node(Node(100), 5 )
print(l)
