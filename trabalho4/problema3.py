from collections import deque

def dfs(graph, node):
    visited = set()
    stack = deque() # criando uma stack vazia

    visited.add(node)
    stack.append(node)

    while stack:
        s = stack.pop()

        for n in reversed(graph[s]):
            if n not in visited:
                visited.add(n)
                stack.append(n)
    todos_visitados = visited == set(graph.keys())
                
    return todos_visitados, visited



# 1. Rede Totalmente Conectada
#    R1 -- R2 -- R4
#    |    |    /
#    R3 -- R5
rede_conectada = {
    'R1': ['R2', 'R3'],
    'R2': ['R1', 'R4', 'R5'],
    'R3': ['R1', 'R5'],
    'R4': ['R2', 'R5'],
    'R5': ['R2', 'R3', 'R4']
}

# 2. Rede com Roteadores Desconectados
#    R1 -- R2    R4 -- R5 (R4 e R5 estão isolados)
#    |
#    R3
rede_desconectada = {
    'R1': ['R2', 'R3'],
    'R2': ['R1'],
    'R3': ['R1'],
    'R4': ['R5'],  # Grupo isolado
    'R5': ['R4']   # Grupo isolado
}

roteador_central = 'R1'

# Teste com a rede conectada
print("="*40)
print("Verificando conectividade da rede CONECTADA...")
print("="*40)
conectada, visitados_conectada = dfs(rede_conectada, roteador_central)
print(f"\nA rede CONECTADA está totalmente conectada a partir de {roteador_central}? {conectada}")
print("="*40)

# Teste com a rede desconectada
print("\n\n" + "="*40)
print("Verificando conectividade da rede DESCONECTADA...")
print("="*40)
desconectada, visitados_desconectada = dfs(rede_desconectada, roteador_central)
print(f"\nA rede DESCONECTADA está totalmente conectada a partir de {roteador_central}? {desconectada}")
print("="*40)

# Teste com um ponto de partida diferente na rede desconectada
roteador_central_isolado = 'R4'
print("\n\n" + "="*40)
print(f"Verificando conectividade da rede DESCONECTADA a partir de {roteador_central_isolado}...")
print("="*40)
desconectada_isolado, visitados_isolado = dfs(rede_desconectada, roteador_central_isolado)
print(f"\nA rede DESCONECTADA está totalmente conectada a partir de {roteador_central_isolado}? {desconectada_isolado}")
print(f"(Esperado: False, pois {roteador_central_isolado} não alcança R1, R2, R3)")
print("="*40)