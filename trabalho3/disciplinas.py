from enum import Enum
import math
import matplotlib.pyplot as plt
from collections import Counter

COLORS = ['#5390D9', '#72EFDD', '#7B2CBF', '#9D4EDD', '#C77DFF', '#E0AAFF', '#48BEF3','#5A189A']

class Subjects(Enum):
    Gerenciamento = 0
    Arquitetura = 1
    Grafos = 2
    Logica = 3
    TokyoGhoul = 4


class Grafo:
    def __init__(self, number_of_vertices):
        self.number_of_vertices = number_of_vertices
        self.adjacency_matrix = [[0] * self.number_of_vertices for _ in range(self.number_of_vertices)] 
        self.incidence_matrix = [[0] * number_of_vertices for _ in range(number_of_vertices)]
        self.subject = [e.name for e in Subjects]
        self.edges = []
        self.index_list = []
        self.adjacency_list = []

    def add_edge(self, i, j):
        self.adjacency_matrix[i][j] = 1
        self.adjacency_matrix[j][i] = 1

        self.incidence_matrix[i][j] = 1
        self.incidence_matrix[j][i] = 1
        
        self.edges.append((i, j))

        
    def get_adjacent_vertices(self, vertex):
        if vertex < 1 or vertex >= len(self.index_list):
            return []  # Retorna lista vazia se o vértice não for válido
        
        start = self.index_list[vertex]  # Obtém o índice inicial na lista B

        if vertex == len(self.index_list) - 1:
            end = -1
        else:
            end = self.index_list[vertex + 1]  # Obtém o índice final na lista B
        
        return self.adjacency_list[start:end]  # Retorna os vértices adjacentes
    
    
    def render_adjacency_matrix(self):
        plt.matshow(self.adjacency_matrix)
        plt.show()
        

    def print_adjacency_matrix(self):
        print('   ', end='')
        for i in self.subject:
            print(i, end=' ')
        print()

        i = 0
        for row in self.adjacency_matrix:
            print(self.subject[i], end=' ')
            for col in row:
                print(col, end='  ')
            print()
            i += 1
    
    def display_subjects(self, colored_graph):
        print("\nDisciplinas e horarios das provas finais:")  # Em que a ligação representam os alunos que estão matriculados nas disciplinas
        for posicao, coolor in enumerate(colored_graph):
            print(f"{Subjects(posicao).name}: {coolor + 1}° horario, cor correspondenter: ({COLORS[coolor]})")
            
    def coloring_subjects(self):
        coloracao = [-1] * self.number_of_vertices  # Inicialmente, nenhuma cor atribuída
        vertices = list(range(self.number_of_vertices))

        # Ordena os vértices por grau do vertice v decrescente
        vertices.sort(key=lambda v: sum(self.adjacency_matrix[v]), reverse=True)

        for v in vertices:
            # Coletar cores dos vizinhos já coloridos
            cores_vizinhos = set()
            for u in range(self.number_of_vertices):
                if self.adjacency_matrix[v][u] == 1 and coloracao[u] != -1:
                    cores_vizinhos.add(coloracao[u])

            # Atribuir a menor cor possível
            cor = 0
            while cor in cores_vizinhos:
                cor += 1
            coloracao[v] = cor

        return coloracao
    
    def plot_colored_graph(self, coloracao):
        # Posicionamento circular
        angulo = 2 * math.pi / self.number_of_vertices
        posicoes = {
            i: (math.cos(i * angulo), math.sin(i * angulo))
            for i in range(self.number_of_vertices)
        }

        plt.figure(figsize=(4, 4), num='E = Alunos, V = Disciplinas, C = Horarios')

        # Desenha arestas
        for a, b in self.edges:
            x_values = [posicoes[a][0], posicoes[b][0]]
            y_values = [posicoes[a][1], posicoes[b][1]]
            plt.plot(x_values, y_values, color='gray', zorder=1)

        # Desenha nós
        for i in range(self.number_of_vertices):
            x, y = posicoes[i]
            cor = COLORS[coloracao[i] % len(COLORS)]
            plt.scatter(x, y, color=cor, s=500, zorder=2)
            plt.text(x, y, self.subject[i], ha='center', va='center', fontsize=5, wrap=True, color='white')

        plt.axis('off')
        plt.show()
    

# Main
    
grafo = Grafo(5)

grafo.add_edge(Subjects.Gerenciamento.value, Subjects.TokyoGhoul.value)

grafo.add_edge(Subjects.Arquitetura.value, Subjects.Gerenciamento.value)
grafo.add_edge(Subjects.Arquitetura.value, Subjects.Grafos.value)
grafo.add_edge(Subjects.Arquitetura.value, Subjects.Logica.value)
grafo.add_edge(Subjects.Arquitetura.value, Subjects.TokyoGhoul.value)

grafo.add_edge(Subjects.Grafos.value, Subjects.TokyoGhoul.value)
grafo.print_adjacency_matrix()

coolorindo = grafo.coloring_subjects()

# Exibições 
grafo.display_subjects(coolorindo)
grafo.plot_colored_graph(coolorindo)