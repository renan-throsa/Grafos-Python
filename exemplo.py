from Grafo import Grafo
from Vertice import Vertice

grafo = Grafo()

grafo.novo_Vertice(1)
grafo.novo_Vertice(2)
grafo.novo_Vertice(3)
grafo.novo_Vertice(4)
grafo.novo_Vertice(5)
grafo.novo_Vertice(6)

grafo.nova_Aresta(1, 2, 0)
grafo.nova_Aresta(1, 3, 0)
grafo.nova_Aresta(1, 4, 0)
grafo.nova_Aresta(1, 5, 0)
grafo.nova_Aresta(1, 6, 0)
grafo.nova_Aresta(2, 3, 0)

for i in grafo.lista_Arestas:
    print(i)

print(grafo.busca_Aresta(Vertice(1), Vertice(3)))