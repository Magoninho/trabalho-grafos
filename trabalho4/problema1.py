rede_social = {
    'Alice': ['Bob', 'Carol', 'Frank'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Carol': ['Alice', 'Eve', 'Grace'],
    'David': ['Bob', 'Henry'],
    'Eve': ['Bob', 'Carol', 'Ivy'],
    'Frank': ['Alice', 'Grace', 'Jack'],
    'Grace': ['Carol', 'Frank', 'Ivy'],
    'Henry': ['David', 'Jack'],
    'Ivy': ['Eve', 'Grace', 'Jack'],
    'Jack': ['Frank', 'Henry', 'Ivy']
}


def bfs(graph, start, end):
    if end not in graph:
        raise ValueError('Esse usuario não existe na base de dados')
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop()
        node = path[-1]
        if node == end:
            return path

        for adjacent in graph.get(node):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
    return None

path = bfs(rede_social, 'Alice', 'Jack')
print(path)
print(len(path) - 1, "arestas de distancia")