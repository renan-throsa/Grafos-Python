#pilha
class Stack :
  def __init__(self) :
    self.items = []

  def push(self, item) :
    self.items.apend(item)

  def pop(self) :
    return self.items.pop()

  def isEmpty(self) :
    return (self.items == [])

# Grafo
class Grafo:
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado
        self.tempo = 0

    def novo_Vertice(self, identificador):
        # string = input(str("Identificador do Vertice: "))
        self.lista_Vertices.append(Vertice(identificador))

    def busca_Aresta(self, u, v):  # Método recebe dois objetos do tipo Vértice
        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_Vertice(self, identificador):  # Método recebe um int
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def nova_Aresta(self, origem, destino, peso):
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        
        if self.direcionado == False:
                self.lista_Arestas.append(Aresta(destino_aux,origem_aux, peso))#Aresta(u,v) e Aresta(v,u)
        else:
            print("Um do Vertice ou ambos são invalidos")

    def esta_Vazio(self):
        if len(self.lista_Vertices) == 0:
            return True
        else:
            return False

    def busca_Adjacente(self, u):  # Método recebe um vertice
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True) #Para que não retorn o mesmo vertice seguidas veses
                return destino
        else:
            return None

    def Depth_first_search(self):
        for v in self.lista_Vertices:
            v.setVisitado(False)
            v.setImput(0)
            v.setOutput(0)
        for v in self.lista_Vertices:
            if not v.getVisitado():
                print("Visitando o vertice: %s" % v.getId())
                self.visita(v)

    def visita(self, u):
        u.setVisitado(True)
        grafo.tempo = +1
        u.setImput(grafo.tempo)
        v = self.busca_Adjacente(u)
        if v is not None:
            if not v.getVisitado():
                print("Predecessor de %s" % v.getId())
                print(u)
                v.predecessor.append(u)
                self.visita(v)
            else:
                u.setVisitado(True)
                grafo.tempo = +1
                u.setOutput(grafo.tempo)
                print(u)
        else:
            u.setVisitado(True)
            grafo.tempo = +1
            u.setOutput(grafo.tempo)
            print(u)

    def inicializa_Fonte(self, identificador):  # Função usado no BFS e Dijkstra
        for v in self.lista_Vertices:
            v.setEstimativa(99999)
            v.setVisitado(False)
        fonte = self.busca_Vertice(identificador)
        fonte.setVisitado(True)
        fonte.setEstimativa(0)

    def Breadth_first_search(self, identificador):
        self.inicializa_Fonte(identificador)
        fonte = self.busca_Vertice(identificador)
        lista = [fonte]
        while 0 != len(lista):
            u = lista[0]
            v = self.busca_Adjacente(u)  # retorna adjacente não visitado
            if v is None:
                lista.pop(0)  # retiro o vertice sem adjacentes

            else:
                grafo.tempo = +1
                v.setImput(grafo.tempo)
                v.predecessor.append(u.getId())
                v.setVisitado(True)
                lista.append(v)

            u.setVisitado(True)

    def imprime_Grafo(self, origem, destino):
        if origem == destino:
            print(origem)
        else:
            destino_Aux = self.busca_Vertice(destino)
            if len(destino_Aux.predecessor) == 0:
                print("Não ha caminho")
            else:
                print(destino_Aux.predecessor[0])
                self.imprime_Grafo(origem, destino_Aux.predecessor[0])

    def relaxa_Vertice(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId()) #guarda apenas o id
            
    def Dijkstra(self, origem):
        fonte = self.busca_Vertice(origem)
        self.inicializa_Fonte(origem)
        lista = []
        resposta = [] # conjunto resposta
        for i in self.lista_Vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()  # ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.busca_Adjacente(u)
            if v is None:
                for i in self.lista_Vertices:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                    i.setVisitado(
                        False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
                resposta.append(lista[0])
                lista.pop(0)  # retiro vertice sem adjacente da lista
                
            else:
                w = self.busca_Aresta(u, v)
                if w is not None:
                    self.relaxa_Vertice(u, v, w)
                


        print("Estimativas: ")
        for i in resposta:
            print(i) #imprimo as respostas

    def Bellman_Ford(self,origem):
        self.inicializa_Fonte(origem)
        for i in range(len(self.lista_Vertices)-1):
            for w in self.lista_Arestas:
                u = w.getOrigem()
                v = w.getDestino()
                self.relaxa_Vertice(u,v,w)

        for w in self.lista_Arestas:
            u = w.getOrigem()
            v = w.getDestino()
            if u.getEstimativa() > v.getEstimativa() + w.getPeso():
                return False # Não existe ciclo negativo
            else:
                return True #Exixte ciclo negatio


    def Minimum_spanning_tree(self,origem): #Prim
        fonte = self.busca_Vertice(origem)
        self.inicializa_Fonte(origem)
        lista = []
        arvore = []  # conjunto resposta
        for i in self.lista_Vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()# ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.busca_Adjacente(u)
            if v is None:
                for i in self.lista_Vertices:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                    i.setVisitado(False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
                lista.pop(0)  # retiro vertice sem adjacente
            else:
                w = self.busca_Aresta(u,v)
                if v.getEstimativa() > w.getPeso():
                    v.predecessor.append(u.getId())
                    arvore.append(w)

        for w in arvore:
            print(w)


# Grafo exemplo

"""
grafo = Grafo() #grafo não derecionado
grafo.novo_Vertice("u")
grafo.novo_Vertice("v")
grafo.novo_Vertice("x")
grafo.novo_Vertice("s")
grafo.novo_Vertice("y")
grafo.nova_Aresta("s", "u", 10)
grafo.nova_Aresta("s", "x", 5)
grafo.nova_Aresta("u", "v", 1)
grafo.nova_Aresta("u", "x", 2)
grafo.nova_Aresta("v", "y", 4)
grafo.nova_Aresta("x", "u", -3)
grafo.nova_Aresta("x", "y", 2)
grafo.nova_Aresta("x", "v", 9)
grafo.nova_Aresta("y", "s", 7)
grafo.nova_Aresta("y", "v", 6)
grafo.Dijkstra("s")
grafo.imprime_Grafo('s','y')
"""
grafo = Grafo(False)
grafo.novo_Vertice("A")
grafo.novo_Vertice("B")
grafo.novo_Vertice("C")
grafo.novo_Vertice("D")
grafo.novo_Vertice("E")
grafo.novo_Vertice("F")
grafo.novo_Vertice("G")

grafo.nova_Aresta("A", "B", 7)
grafo.nova_Aresta("A", "D", 5)
grafo.nova_Aresta("B", "C", 8)
grafo.nova_Aresta("B", "D", 9)
grafo.nova_Aresta("B", "E", 7)
grafo.nova_Aresta("C", "E", 5)
grafo.nova_Aresta("D", "F", 6)
grafo.nova_Aresta("D", "E", 15)
grafo.nova_Aresta("E", "F", 8)
grafo.nova_Aresta("E", "G", 9)
grafo.nova_Aresta("F", "G", 6)
#resposta desejada: G(V,A)[(A,B),(A,D),(B,E),(C,E),(D,F),(D,F),(E,G)]
