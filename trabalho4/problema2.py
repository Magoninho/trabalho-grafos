def ler_grafo(arquivo):
    grafo = {}
    with open(arquivo, 'r') as f:
        for linha in f:
            cidade1, cidade2 = linha.strip().split()
            print(cidade1, cidade2)
            if cidade1 not in grafo:
                grafo[cidade1] = []
            if cidade2 not in grafo:
                grafo[cidade2] = []
            grafo[cidade1].append(cidade2)
            grafo[cidade2].append(cidade1)  
    # Se elas nao estiverem no grafo, nao terao vizinhos e ai a cidade x vai receber a cidade y do arquivo como vizinha e vice versa
    return grafo

def buscar_caminho(grafo, atual, destino, visitadas=None, caminho=None):
    
    # nenhuma cidade visitada, cria uma lista vazia pra armazenar as visitadas
    if visitadas is None:
        visitadas = set()
    
    #nenhum caminho criado, inicia uma lista vazia de caminho   
    if caminho is None:
        caminho = []

    # marcando a cidade atual como visitada e a adicionando ao caminho
    visitadas.add(atual)
    caminho.append(atual)

    # se a cidade atual for o destino, vai retornar o caminho
    if atual == destino:
        return caminho

    # tenta pegar as vizinhas da cidade atual no frafo, se ela n existir nele vai retornar um array vazio
    for vizinha in grafo.get(atual, []):
        # se a vizinha nao tiver sido visitada, vai fazer a chamada recursiva passando a vizinha como futura cidade atual tentando chegar ao destino
        if vizinha not in visitadas:
            resultado = buscar_caminho(grafo, vizinha, destino, visitadas, caminho)
            # se tiver achado o caminho, retorna ele
            if resultado:
                return resultado

    # Se nenhuma vizinha leva ao destino, tira a ultima cidade (atual) da pilha
    caminho.pop()
    return None


grafo = ler_grafo('caminhos.txt')
origem = input("Digite a cidade de origem: ").strip().upper()
destino = input("Digite a cidade de destino: ").strip().upper()

caminho = buscar_caminho(grafo, origem, destino)
if caminho:
    print("Caminho encontrado:", ' -> '.join(caminho))
    print("Largura do caminho:", (len(caminho)) - 1)
else:
    print("Nenhum caminho encontrado.")
