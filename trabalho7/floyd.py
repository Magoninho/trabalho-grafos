import numpy as np
import time

n = 5
INF = float('inf')

W = [
    [0,   3,   INF, 7,   INF],
    [8,   0,   2,   INF, INF],
    [5,   INF, 0,   1,   INF],
    [2,   INF, INF, 0,   1],
    [INF, INF, 3,   INF, 0]
]

d_list = []
p_list = []

# Inicialização
d0 = np.array(W, dtype=float)
p0 = [[None if i == j or W[i][j] == INF else i for j in range(n)] for i in range(n)]

d_list.append(d0.copy())
p_list.append([row[:] for row in p0])

# Algoritmo Floyd-Warshall
for k in range(n):
    d_new = d_list[k].copy()
    p_new = [row[:] for row in p_list[k]]

    for i in range(n):
        for j in range(n):
            if d_list[k][i][j] > d_list[k][i][k] + d_list[k][k][j]:
                d_new[i][j] = d_list[k][i][k] + d_list[k][k][j]
                p_new[i][j] = p_list[k][k][j]

    d_list.append(d_new)
    p_list.append(p_new)

# Mostrar matrizes d0 a d5 com pausa
for k in range(n+1):
    print(f"\nd{k}:")
    for row in d_list[k]:
        print(["∞" if x == INF else int(x) for x in row])
    time.sleep(1.2)

# Mostrar matrizes p0 a p5 com pausa
for k in range(n+1):
    print(f"\np{k}:")
    for row in p_list[k]:
        print([None if x is None else x+1 for x in row])  # +1 para C1, C2...
    time.sleep(1.2)

# Reconstrução de caminhos
def reconstruir_caminho(i, j, p_final):
    if d_list[-1][i][j] == INF:
        return None
    caminho = [j]
    while i != j:
        j = p_final[i][j]
        caminho.append(j)
    caminho.reverse()
    return [f"C{v+1}" for v in caminho]

# Mostrar todos os caminhos com tempo total
print("\nCaminhos mais curtos e tempos totais entre todos os pares:")
time.sleep(1)

for i in range(n):
    for j in range(n):
        if i != j:
            caminho = reconstruir_caminho(i, j, p_list[-1])
            tempo = d_list[-1][i][j]
            if caminho:
                print(f"C{i+1} → C{j+1}: {' → '.join(caminho)} | Tempo: {int(tempo)}h")
            else:
                print(f"C{i+1} → C{j+1}: Sem caminho")
            time.sleep(0.5)
