from heapq import heapify, heappop, heappush

def dijkstra(graph, root):
    """
    The graph argument here is a graph dictionary, while the root here is simply a string.

    """ 
    visited = []
    distances = {node: (0 if node is root else float("inf")) for node in graph.keys()}
    p_queue = [(0, root)]
    heapify(p_queue)
    while p_queue:
        node_distance, node = heappop(p_queue)
        if node not in visited:
            visited.append(node)
            for neighbour, distance in graph[node].items():
                if node_distance + distance < distances[neighbour]:
                    distances[neighbour] = node_distance + distance
                    heappush(p_queue, ((node_distance + distance) , neighbour))
    return distances
    
# Dict of dicts used to represent the graph and weighted relationships

graph = {
    "A": {"B": 2, "C":2},
    "B": {"A": 2, "C": 6, "D": 1, "E": 1, "F": 5},
    "C": {"A": 2, "B": 6, "G": 6, "H": 2},
    "D": {"B": 1, "E": 1},
    "E": {"B": 1, "D": 1, "G":1},
    "F": {"B": 5, "G": 1}, 
    "G": {"F": 1, "E": 1, "C": 6, "H": 3},
    "H": {"C": 2, "G": 3},
}




print(dijkstra(graph, "A"))





