from enum import Enum
import matplotlib.pyplot as plt
from collections import Counter

class Vertices(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    



class Grafo:
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.adjacency_matrix = [[0] * self.number_of_vertices for _ in range(self.number_of_vertices)] 
        self.incidence_matrix = [[0] * number_of_vertices for _ in range(number_of_vertices)]
        self.states = [e.name for e in Vertices]
        self.edges = []
        self.index_list = []
        self.adjacency_list = []

    def add_edge(self, i, j):
        self.adjacency_matrix[i][j] = 1
        self.adjacency_matrix[j][i] = 1

        self.incidence_matrix[i][j] = 1
        self.incidence_matrix[j][i] = 1
        
        self.edges.append((i, j))


    def adjacency_matrix_to_list(self, matrix):
        n = len(matrix)
        graph = {}
        
        for i in range(n):
            graph[i] = []
            for j in range(n):
                if matrix[i][j] != 0:
                    graph[i].append(j)
    
        return graph
    
    def follows_dirac_theorem(self):
        graph = self.adjacency_matrix_to_list(self.adjacency_matrix)
        n = len(graph)
        if n < 3:
            return False
        threshold = n / 2
        for node in graph:
            if len(graph[node]) < threshold:
                return False
        return True

    def follows_ore_theorem(self):
        graph = self.adjacency_matrix_to_list(self.adjacency_matrix)
        n = len(graph)
        
        if n < 3:
            return False

        # Check all pairs of non-adjacent vertices
        for u in range(n):
            for v in range(u + 1, n):
                if v not in graph[u]:  # only check non-adjacent pairs
                    deg_u = len(graph[u])
                    deg_v = len(graph[v])
                    if deg_u + deg_v < n:
                        return False

        return True
    
    def is_complete_graph(self, graph):
        n = len(graph)
        for node, neighbors in graph.items():
            if len(neighbors) != n - 1:
                return False
        return True

    def bondy_chvatal_closure(self, graph):
        """
        Applies the Bondy-Chvátal closure to the graph.
        
        Parameters:
            graph (dict): Adjacency list.

        Returns:
            dict: Modified graph with closure applied.
        """
        n = len(graph)
        changed = True

        while changed:
            changed = False
            # Generate a set of current non-adjacent pairs
            for u in range(n):
                for v in range(u + 1, n):
                    if v not in graph[u]:
                        deg_u = len(graph[u])
                        deg_v = len(graph[v])
                        if deg_u + deg_v >= n:
                            # Add edge u-v
                            graph[u].append(v)
                            graph[v].append(u)
                            changed = True
        return graph

    def follows_bondy_chvatal_theorem(self):
        graph = self.adjacency_matrix_to_list(self.adjacency_matrix)
        if len(graph) < 3:
            return False

        closure = self.bondy_chvatal_closure(graph)
        return self.is_complete_graph(closure)

    
    def generate_indexed_list(self):
        cursor = 0
        for i in range(len(self.adjacency_matrix)):
            self.index_list.append(cursor)
            cursor = cursor + self.adjacency_matrix[i].count(1)

        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix[i])):
                if self.adjacency_matrix[i][j] == 1:
                    self.adjacency_list.append(j)

    def generate_histogram_data(self):
        histogram = []
        for row in self.adjacency_matrix:
            sum = 0
            for i in row:
                if i == 1:
                    sum += 1
            histogram.append(sum)
        
        return histogram
    
    def get_incidence_matrix(self):
        num_edges = len(self.edges)
        incidence_matrix = [[0] * num_edges for _ in range(self.number_of_vertices)]
        
        for edge_index, (start, end) in enumerate(self.edges):
            incidence_matrix[start][edge_index] = 1
            incidence_matrix[end][edge_index] = 1
        
        return incidence_matrix

    def get_adjacent_vertices(self, vertex):
        if vertex < 1 or vertex >= len(self.index_list):
            return []  # Retorna lista vazia se o vértice não for válido
        
        start = self.index_list[vertex]  # Obtém o índice inicial na lista B

        if vertex == len(self.index_list) - 1:
            end = -1
        else:
            end = self.index_list[vertex + 1]  # Obtém o índice final na lista B
        
        return self.adjacency_list[start:end]  # Retorna os vértices adjacentes
    

    def print_histogram(self):
        
        data = self.generate_histogram_data()
        max_height = max(data)
        canvas = []

        for h in range(max_height + 1):
            canvas.append([])
            for i in range(len(data)):
                current_max_height = data[i]
                if h < current_max_height:
                    canvas[h].append("##")
                elif h == current_max_height:
                    canvas[h].append(self.states[i])
                else:
                    canvas[h].append("  ")
        
        for row in reversed(canvas):
            for col in row:
                print(col, end=' ')
            print()
    
    def render_histogram(self):
        x = self.states
        y = self.generate_histogram_data()

        plt.bar(x, y)
        plt.show()
        
    def plot_grau_histogram(self):
        graus = self.generate_histogram_data()
        contagem = Counter(graus)
        graus_unicos = sorted(contagem.keys())
        quantidades = [contagem[g] for g in graus_unicos]
        
        plt.bar(graus_unicos, quantidades, tick_label=graus_unicos)
        plt.show()
    
    def render_adjacency_matrix(self):
        plt.matshow(self.adjacency_matrix)
        plt.show()

    def render_incidence_matrix(self):
        plt.matshow(self.get_incidence_matrix())
        plt.show()

    def print_adjacency_matrix(self):
        print('   ', end='')
        for i in self.states:
            print(i, end=' ')
        print()

        i = 0
        for row in self.adjacency_matrix:
            print(self.states[i], end=' ')
            for col in row:
                print(col, end='  ')
            print()
            i += 1

grafo = Grafo(7)


#padrão de todos
grafo.add_edge(Vertices.A.value, Vertices.B.value)
grafo.add_edge(Vertices.B.value, Vertices.C.value)
grafo.add_edge(Vertices.C.value, Vertices.D.value)
grafo.add_edge(Vertices.D.value, Vertices.E.value)
grafo.add_edge(Vertices.F.value, Vertices.G.value)
grafo.add_edge(Vertices.G.value, Vertices.A.value)


#caso 1
grafo.add_edge(Vertices.A.value, Vertices.C.value)
grafo.add_edge(Vertices.C.value, Vertices.G.value)
grafo.add_edge(Vertices.B.value, Vertices.D.value)
grafo.add_edge(Vertices.B.value, Vertices.E.value)
grafo.add_edge(Vertices.D.value, Vertices.F.value)
grafo.add_edge(Vertices.E.value, Vertices.G.value)
grafo.add_edge(Vertices.A.value, Vertices.F.value)

#caso 2
# grafo.add_edge(Vertices.A.value, Vertices.C.value)
# grafo.add_edge(Vertices.A.value, Vertices.F.value)
# grafo.add_edge(Vertices.B.value, Vertices.D.value)
# grafo.add_edge(Vertices.B.value, Vertices.E.value)
# grafo.add_edge(Vertices.C.value, Vertices.G.value)
# grafo.add_edge(Vertices.E.value, Vertices.G.value)

# #caso 3
# grafo.add_edge(Vertices.A.value, Vertices.C.value)
# grafo.add_edge(Vertices.A.value, Vertices.F.value)
# grafo.add_edge(Vertices.B.value, Vertices.D.value)

# #caso 4
# grafo.add_edge(Vertices.A.value, Vertices.C.value)
# grafo.add_edge(Vertices.A.value, Vertices.F.value)



# grafo.print_adjacency_matrix()
# grafo.plot_histogram()
# grafo.print_histogram()
# grafo.render_histogram()
# grafo.render_adjacency_matrix()
# grafo.render_incidence_matrix()
# grafo.plot_grau_histogram()

# grafo.generate_indexed_list()

print("dirac: ", grafo.follows_dirac_theorem())
print("ore: ", grafo.follows_ore_theorem())
print("bondy: ", grafo.follows_bondy_chvatal_theorem())