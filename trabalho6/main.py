def bellman_ford(graph, start):
    # Inicializa as distâncias
    distance = {v: float('inf') for v in graph}
    distance[start] = 0
    predecessor = {v: None for v in graph}

    # Relaxa todas as arestas |V| - 1 vezes
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u

    # Verifica ciclos negativos
    for u in graph:
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                print("Ciclo negativo detectado no vértice", v)
                return None, None

    return distance, predecessor

def print_path(predecessor, v):
    path = []
    while v:
        path.append(v)
        v = predecessor[v]
    print(" -> ".join(reversed(path)))


def main():
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 3), ('D', 2), ('E', 3)],
        'C': [('B', 1), ('D', 4), ('F', 5)],
        'D': [('E', -5)],
        'E': [('C', -3)],
        'F': [('D', 1)]
    }

    origem = input("Digite o vértice de origem (A-F): ").upper()
    if origem not in graph:
        print("Vértice inválido.")
        return

    distancia, predecessor = bellman_ford(graph, origem)

    if distancia is None:
        print("Não é possível calcular os caminhos mais curtos devido a um ciclo negativo.")
    else:
        print(f"\nMenores custos a partir do vértice {origem}:")
        for v in sorted(graph.keys()):
            print(f"{origem} -> {v} = {distancia[v]}")
            print_path(predecessor, v)

if __name__ == "__main__":
    main()
