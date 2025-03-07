from enum import Enum
import matplotlib.pyplot as plt
from collections import Counter

class Estados(Enum):
    AC = 0
    AL = 1
    AP = 2
    AM = 3
    BA = 4
    CE = 5
    DF = 6
    ES = 7
    GO = 8
    MA = 9
    MT = 10
    MS = 11
    MG = 12
    PA = 13
    PB = 14
    PR = 15
    PE = 16
    PI = 17
    RJ = 18
    RN = 19
    RS = 20
    RO = 21
    RR = 22
    SC = 23
    SP = 24
    SE = 25
    TO = 26



class GrafoEstados:
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.adjacency_matrix = [[0] * self.number_of_vertices for _ in range(self.number_of_vertices)] 
        self.incidence_matrix = [[0] * number_of_vertices for _ in range(number_of_vertices)]
        self.states = [e.name for e in Estados]
        self.edges = []
        self.index_list = []
        self.adjacency_list = []

    def add_edge(self, i, j):
        self.adjacency_matrix[i][j] = 1
        self.adjacency_matrix[j][i] = 1

        self.incidence_matrix[i][j] = 1
        self.incidence_matrix[j][i] = 1
        
        self.edges.append((i, j))


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
        plt.xlabel("Grau do Estado")
        plt.ylabel("Quantidade de Estados")
        plt.title("Distribuição dos Graus dos Estados")
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

if __name__ == "__main__":
    grafo = GrafoEstados(27)

    grafo.add_edge(Estados.AC.value, Estados.AM.value)
    grafo.add_edge(Estados.AC.value, Estados.RO.value)
    grafo.add_edge(Estados.AL.value, Estados.SE.value)
    grafo.add_edge(Estados.AL.value, Estados.PE.value)
    grafo.add_edge(Estados.AL.value, Estados.BA.value)
    grafo.add_edge(Estados.AP.value, Estados.PA.value)
    grafo.add_edge(Estados.AM.value, Estados.PA.value)
    grafo.add_edge(Estados.AM.value, Estados.RO.value)
    grafo.add_edge(Estados.AM.value, Estados.RR.value)
    grafo.add_edge(Estados.AM.value, Estados.MT.value)
    grafo.add_edge(Estados.BA.value, Estados.TO.value)
    grafo.add_edge(Estados.BA.value, Estados.SE.value)
    grafo.add_edge(Estados.BA.value, Estados.PI.value)
    grafo.add_edge(Estados.BA.value, Estados.MG.value)
    grafo.add_edge(Estados.BA.value, Estados.GO.value)
    grafo.add_edge(Estados.BA.value, Estados.AL.value)
    grafo.add_edge(Estados.BA.value, Estados.PE.value)
    grafo.add_edge(Estados.CE.value, Estados.RN.value)
    grafo.add_edge(Estados.CE.value, Estados.PB.value)
    grafo.add_edge(Estados.CE.value, Estados.PI.value)
    grafo.add_edge(Estados.CE.value, Estados.PE.value)
    grafo.add_edge(Estados.ES.value, Estados.RJ.value)
    grafo.add_edge(Estados.ES.value, Estados.MG.value)
    grafo.add_edge(Estados.ES.value, Estados.BA.value)
    grafo.add_edge(Estados.GO.value, Estados.TO.value)
    grafo.add_edge(Estados.GO.value, Estados.MT.value)
    grafo.add_edge(Estados.GO.value, Estados.MS.value)
    grafo.add_edge(Estados.GO.value, Estados.MG.value)
    grafo.add_edge(Estados.MA.value, Estados.PI.value)
    grafo.add_edge(Estados.MA.value, Estados.TO.value)
    grafo.add_edge(Estados.MA.value, Estados.PA.value)
    grafo.add_edge(Estados.MT.value, Estados.MS.value)
    grafo.add_edge(Estados.MT.value, Estados.RO.value)
    grafo.add_edge(Estados.MT.value, Estados.TO.value)
    grafo.add_edge(Estados.MT.value, Estados.PA.value)
    grafo.add_edge(Estados.MS.value, Estados.MG.value)
    grafo.add_edge(Estados.MS.value, Estados.SP.value)
    grafo.add_edge(Estados.MS.value, Estados.PR.value)
    grafo.add_edge(Estados.MG.value, Estados.RJ.value)
    grafo.add_edge(Estados.MG.value, Estados.SP.value)
    grafo.add_edge(Estados.PA.value, Estados.TO.value)
    grafo.add_edge(Estados.PB.value, Estados.RN.value)
    grafo.add_edge(Estados.PB.value, Estados.PE.value)
    grafo.add_edge(Estados.PR.value, Estados.SC.value)
    grafo.add_edge(Estados.PR.value, Estados.SP.value)
    grafo.add_edge(Estados.PE.value, Estados.AL.value)
    grafo.add_edge(Estados.PE.value, Estados.PI.value)
    grafo.add_edge(Estados.PI.value, Estados.TO.value)
    grafo.add_edge(Estados.RJ.value, Estados.SP.value)
    grafo.add_edge(Estados.RS.value, Estados.SC.value)
    grafo.add_edge(Estados.RR.value, Estados.PA.value)
    grafo.add_edge(Estados.SC.value, Estados.PR.value)
    grafo.add_edge(Estados.DF.value, Estados.MG.value)
    grafo.add_edge(Estados.DF.value, Estados.GO.value)


    # grafo.print_adjacency_matrix()
    # grafo.plot_histogram()
    # grafo.print_histogram()
    # grafo.render_histogram()
    # grafo.render_adjacency_matrix()
    # grafo.render_incidence_matrix()
    grafo.plot_grau_histogram()

    grafo.generate_indexed_list()

    print(grafo.get_adjacent_vertices(26))