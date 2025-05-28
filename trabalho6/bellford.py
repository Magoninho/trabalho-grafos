class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.arestas = []

    def adicionar_aresta(self, u, v, peso):
        self.arestas.append((u, v, peso))

    def bellman_ford(self, origem):
        distancia = {v: float('inf') for v in self.V}
        predecessor = {v: None for v in self.V}
        distancia[origem] = 0

        # Relaxamento das arestas V-1 vezes
        for _ in range(len(self.V) - 1):
            for u, v, peso in self.arestas:
                if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                    distancia[v] = distancia[u] + peso
                    predecessor[v] = u

        # Verifica se há ciclo negativo
        for u, v, peso in self.arestas:
            if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                print("⚠️ Ciclo negativo detectado a partir da origem", origem)
                return

        print(f"🏁 Distâncias mínimas a partir de {origem}:")
        for v in self.V:
            print(f"{origem} -> {v}: {distancia[v]}")

# Grafo com ciclo negativo acessível apenas a partir de alguns vértices
g = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])
g.adicionar_aresta('A', 'B', 4)
g.adicionar_aresta('A', 'C', -3)
g.adicionar_aresta('B', 'D', 3)
g.adicionar_aresta('C', 'E', -6)
g.adicionar_aresta('E', 'F', 2)
g.adicionar_aresta('F', 'E', 2)  # ciclo negativo
g.adicionar_aresta('D', 'B', -2)
g.adicionar_aresta('D', 'F', 2)

origem = input("Digite o vértice de origem (A-F): ").upper()
g.bellman_ford(origem)
