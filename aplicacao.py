from Grafo import Grafo

option = 1
grafo = Grafo()
while(option):
    print("\nOpções:\n1-Adicionar vértice\n2-Adicionar aresta\n3-Remover vértice\n4-Remover aresta",
        "\n5-Realizar Cobertura Mínima de Vértices\n6-Mostrar Grafo\n0-Sair da Aplicação\n")
    option = int(input("O que deseja fazer ? "))

    if option == 1:
        v = int(input("Digite o numero correspondente ao vértice: "))
        if not grafo.novo_Vertice(v):
            print("Selecione outro numero, esse vértice ja existe.")
        else:
            print("Vértice {} adicionado com sucesso.".format(v))
    elif option == 2:
        v = int(input("Digite o numero correspondente ao primeiro vértice: "))
        w = int(input("Digite o numero correspondente ao segundo vértice: "))
        if grafo.nova_Aresta(v, w, 0):
            print("Aresta {}-{} adicionada com sucesso.".format(v, w))
        else:
            print("Não foi possível adicionar a aresta. Verifique o índice dos vértices.")
    elif option == 3:
        v = int(input("Digite o numero correspondente ao vértice: "))
        if grafo.novo_Vertice(v) is None:
            print("Não existe vértice com esse identificador.")
        else:
            grafo.remove_vertice(v)
    elif option == 4:
        v = int(input("Digite o numero correspondente ao primeiro vértice da aresta: "))
        w = int(input("Digite o numero correspondente ao segundo vértice da aresta: "))
        if not grafo.remove_Aresta(v, w):
            print("Não existe aresta com esses vértices.")
        else:
            grafo.remove_Aresta(v, w)
            print("Aresta {}-{} removida com sucesso.".format(v, w))
    elif option == 5:
        print("ainda nao, amigo.")
    elif option == 6:
        print(grafo.printa_grafo())