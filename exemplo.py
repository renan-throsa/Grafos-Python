from Grafo import Grafo

grafo = Grafo()

grafo.novo_Vertice(1)
grafo.novo_Vertice(2)
grafo.novo_Vertice(3)
grafo.novo_Vertice(4)
grafo.novo_Vertice(5)
grafo.novo_Vertice(6)

grafo.nova_Aresta(1, 2, 0)
grafo.nova_Aresta(1, 3, 0)
grafo.nova_Aresta(2, 3, 0)
grafo.nova_Aresta(2, 4, 0)
grafo.nova_Aresta(2, 5, 0)
grafo.nova_Aresta(2, 6, 0)

print(grafo.printa_grafo())

result = grafo.bruteForce()

for item in result:
    for vertice in item:
        print(vertice.getId(), end=" ")
    print()
