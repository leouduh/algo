def bellman_ford(graph, root, destination):
    status = True
    table = {node: float("inf") for node in graph.keys()}
    table[root] = 0
    relationships = {}
    while status:
        status = relax(graph, table, relationships)
    path = destination
    parent = ""
    while parent is not root:
        parent = relationships[destination]
        path += "==>" + parent
        destination = parent
    return path



def relax(graph, table, relationship):
    status = False
    for node in graph.keys():
        for child, weight in graph[node].items():
            if table[node] + weight < table[child]:
                status = True
                table[child] = table[node] + weight
                relationship[child] = node
    return status
            


graph = {
    "A": {"C": 35, "B":5, "D":40},
    "B": {"D": 20, "E": 25},
    "C": {"E": -30, "F": 30},
    "D": {"F": 20},
    "E": {"D": 45, "F": 25},
    "F": {}
    
}

print(bellman_ford(graph, "A", "F"))
