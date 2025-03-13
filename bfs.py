from collections import deque


# Implementation of bfs assuming that you use a dictionary to represent your
# graph. The key is the node and the value is a list of child nodes

class Node:
    def __init__(self, value):
        self.value = value
        self.distance = None
        self.explored = None



def bfs(graph, root):
    queue = deque([root])
    visited = []
    root.distance = 0
    
    while queue:
        node = queue.popleft()
        #only deal with nodes that have not been visited, if it has been visited simply
        #ignore and carry on with traversal. the next node in the queue.
        if node not in visited:
            visited.append(node)
            node.explored = True
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    if neighbour.distance is None:
                        neighbour.distance = node.distance + 1


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

#           1
#         /    \
#       2  ---  3
#      / \      | \
#     4   5 ----6   7
#    | 
#    8
#
#
#
#

graph = {
    a : [b, c],
    b : [c, a, d, e], 
    c : [b, a, f, g], 
    d : [b, h], 
    e : [f, b], 
    f : [e, c,],
    g : [c],
    h : [d]
}


bfs(graph, a)
print(f.value, f.distance, f.explored)


