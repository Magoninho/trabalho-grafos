import heapq  # utiliza da biblioteca padrao do python (fila de prioridade)


grafo = {
    'Centro': [('Aldeota', 10), ('Benfica', 7)],
    'Aldeota': [('Centro', 10), ('Meireles', 5), ('Cocó', 15)],
    'Benfica': [('Centro', 7), ('Parangaba', 12)],
    'Meireles': [('Aldeota', 5), ('Cocó', 8)],
    'Cocó': [('Aldeota', 15), ('Meireles', 8), ('Papicu', 6)],
    'Parangaba': [('Benfica', 12), ('Papicu', 14)],
    'Papicu': [('Cocó', 6), ('Parangaba', 14)],
}

def dijkstra(grafo, origem, destino):
    fila = [(0, origem, [])] 
    visitados = set()

    while fila:
        (custo, atual, caminho) = heapq.heappop(fila)

        if atual in visitados:
            continue

        caminho = caminho + [atual]
        visitados.add(atual)

        if atual == destino:
            return caminho, custo

        for vizinho, peso in grafo.get(atual, []):
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, vizinho, caminho))

    return None, float('inf')


origem = 'Benfica'
destino = 'Papicu'
caminho, custo = dijkstra(grafo, origem, destino)

print(f"Menor caminho de {origem} até {destino}: {' -> '.join(caminho)}")
print(f"Custo total: {custo} minutos")
