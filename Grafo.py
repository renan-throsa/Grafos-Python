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
class Grafo():
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado
        self.tempo = 0

    def add_Vertice(self, Identificador):
        # string = input(str("Identificador do Vertice: "))
        self.lista_Vertices.append(Vertice(Identificador))

    def busca_Vertice(self, identificador):  # Método recebe um int
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def add_Aresta(self, origem, destino, peso):
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if ((origem_aux is not None) and (destino_aux is not None)):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso=0))
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
                return destino
        else:
            return None

    def busca_profundidade(self):
        for v in self.lista_Vertices:
            v.setVisitado(False)
            v.setImput(0)
            v.setOutput(0)
        for v in self.lista_Vertices:
            if v.getVisitado() == False:
                print("Visitando o vertice: %s" % v.getId())
                self.visita(v)

    def visita(self, u):
        u.setVisitado(True)
        grafo.tempo = +1
        u.setImput(grafo.tempo)
        v = self.busca_Adjacente(u)
        if v is not None:
            if v.getVisitado() == False:
                print("Predecessor de %s" % v.getId())
                print(u)
                v.predecessor.append(u)
                self.visita(v)
            else:
                u.setVisitado(True)
                grafo.tempo=+1
                u.setOutput(grafo.tempo)
                print(u)
        else:
            u.setVisitado(True)
            grafo.tempo = +1
            u.setOutput(grafo.tempo)
            print(u)

    def inicializa_Fonte(self, identificador):
        for v in self.lista_Vertices:
            v.setEstimativa(99999)
            v.setVisitado(False)
        fonte = self.busca_Vertice(identificador)
        fonte.setVisitado(True)
        fonte.setEstimativa(0)

    def busca_Largura(self, identificador):
        self.inicializa_Fonte(identificador)
        fonte = self.busca_Vertice(identificador)
        lista = [fonte]
        while 0 != len(lista):
            u = lista[0]
            v = self.busca_Adjacente(u) #retorna adjacente não visitado
            if v is None:
                lista.pop(0) #retiro o vertice sem adjacentes

            else:
                grafo.tempo=+1
                v.setImput( grafo.tempo )
                v.predecessor.append(u.getId())
                v.setVisitado(True)
                lista.append(v)


            u.setVisitado(True)

    def imprime_Grafo(self,Origem,Destino):
        if Origem == Destino:
            print (Destino)
        else:
            destino_Aux = self.busca_Vertice(Destino)
            if len( destino_Aux.predecessor) == 0:
                print("Não ha caminho")
            else:
                print(destino_Aux.predecessor[0])
                self.imprime_Grafo(Origem, destino_Aux.predecessor[0])


    def relaxa_Vertice(self, u, v, w):
        """

		:type v: Vertice
		"""
        if v.getEstimativa() > u.getEstimativa() + w.getPeso:
            v.setEstimativa(u.getEstimativa() + w.getPeso)
            v.predecessor.append(u)


            """ def Dijkstra(self,Identificador):
				self.inicializa_Fonte(Identificador)
				fonte = self.busca_Vertice(Identificado)
				while( len(lista)!=0 ):
				u = lista.pop(0)
			"""
