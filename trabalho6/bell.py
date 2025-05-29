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

        # Relaxamento
        for _ in range(len(self.V) - 1):
            for u, v, peso in self.arestas:
                if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                    distancia[v] = distancia[u] + peso
                    predecessor[v] = u

        # Detecta vértices afetados por ciclo negativo
        ciclo_negativo_vertices = set()
        for u, v, peso in self.arestas:
            if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                ciclo_negativo_vertices.add(v)

        # Propaga afetação
        afetados = set()

        def dfs(v):
            if v in afetados:
                return
            afetados.add(v)
            for u_, v_, _ in self.arestas:
                if u_ == v:
                    dfs(v_)

        for v in ciclo_negativo_vertices:
            dfs(v)

        # Reconstrução do caminho
        def reconstruir_caminho(v):
            caminho = []
            atual = v
            while atual is not None:
                caminho.append(atual)
                atual = predecessor[atual]
            return caminho[::-1]

        # Imprime resultado
        print(f"\n🏁 Resultados a partir da origem {origem}:")
        for v in self.V:
            if v in afetados:
                print(f"{origem} -> {v}: inacessível (afetado por ciclo negativo)")
            elif distancia[v] == float('inf'):
                print(f"{origem} -> {v}: inacessível (sem caminho)")
            else:
                caminho = reconstruir_caminho(v)
                caminho_str = " → ".join(caminho)
                print(f"{origem} -> {v}: custo {distancia[v]} | caminho: {caminho_str}")
                
                
gn = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

#com ciclo negativo
gn.adicionar_aresta('A', 'B', 4)
gn.adicionar_aresta('A', 'C', 2)
gn.adicionar_aresta('B', 'D', 3)
gn.adicionar_aresta('C', 'E', 2)
gn.adicionar_aresta('E', 'F', 2)
gn.adicionar_aresta('F', 'E', -5)  # ciclo negativo
gn.adicionar_aresta('D', 'B', 1)
gn.adicionar_aresta('D', 'F', 2)

origem1 = input("Digite o vértice de origem (vai ter ciclo negativo) (A-F): ").upper()
gn.bellman_ford(origem1)

g = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

#sem ciclo negativo
g.adicionar_aresta('A', 'B', 4)
g.adicionar_aresta('A', 'C', 2)
g.adicionar_aresta('B', 'D', 3)
g.adicionar_aresta('C', 'E', 2)
g.adicionar_aresta('E', 'F', 2)
g.adicionar_aresta('F', 'E', -2)  
g.adicionar_aresta('D', 'B', 1)
g.adicionar_aresta('D', 'F', 2)

origem2 = input("Digite o vértice de origem (A-F): ").upper()
g.bellman_ford(origem2)
