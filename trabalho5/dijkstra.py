import heapq  # utiliza da biblioteca padrao do python pra fazer a fila de prioridade


grafo = {
    'Centro': [('Aldeota', 10), ('Benfica', 7)],
    'Aldeota': [('Centro', 10), ('Meireles', 5), ('Cocó', 15)],
    'Benfica': [('Centro', 7), ('Parangaba', 12)],
    'Meireles': [('Aldeota', 5), ('Cocó', 8)],
    'Cocó': [('Aldeota', 15), ('Meireles', 8), ('Papicu', 6)],
    'Parangaba': [('Benfica', 12), ('Papicu', 14)],
    'Papicu': [('Cocó', 6), ('Parangaba', 14)],
}
# o set permite descobrir significantemente mais rapido se um objeto tá dentro do set ou nao
def dijkstra(grafo, origem, destino):
    fila = [(0, origem, [])] # a fial é uma tupla que recebe o custo atual (inicialmente 0), a cidade de origem e o caminho q foi percorrido
    visitados = set() #Cria um conjunto para guardar os nós que já foram visitados. 

    while fila: # enquanto tiver que nos p visitar, continua executando
        
        (custo, atual, caminho) = heapq.heappop(fila) # recebe e tira da fila o melhor caminho(menor custo) o heap garante que o menor sempre sera o primeiro

        if atual in visitados: # Se o nó já foi visitado antes, pula ele para não repetir
            continue # break da cobra

        caminho = caminho + [atual] # adicionando atual ao caminho
        visitados.add(atual) # marcando como visitado

        if atual == destino:
            return caminho, custo # se o atual ja for o destino, retorna logo caminho e custo

        for vizinho, peso in grafo.get(atual, []): #p cada vizinho do no atual (usa essa formatacao pq se digitar o nome da cidade errado, retorna uma lista vazia), em suma mais otimizado e previne erros
            if vizinho not in visitados: # se o vizinho ainda nao tiver sido visitado, adiciona ele na fila de prioridade e calcula o novo custo respectio
                heapq.heappush(fila, (custo + peso, vizinho, caminho))

    return None, float('inf') # se nao der p chegar no infeliz retorna nenhum caminho e custo infinito


origem = 'Benfica'
destino = 'Papicu'
caminho, custo = dijkstra(grafo, origem, destino)

try:
    print(f"Menor caminho de {origem} até {destino}: {' -> '.join(caminho)}")
    print(f"Custo total: {custo} minutos")
except TypeError:
    print("Nenhum caminho encontrado, custo ∞")
    print("Você provavelmente cometeu um erro ao digitar ou o bairro nao ta presente no grafo 😡 🤬")
