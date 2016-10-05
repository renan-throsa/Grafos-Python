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

    def nova_Aresta(self, origem, destino, peso): #Método recebe dois identificadores
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

        if self.direcionado == False:
                self.lista_Arestas.append(Aresta(destino_aux,origem_aux, peso))#Aresta(u,v) e Aresta(v,u)

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
        self.tempo = 0
        for v in self.lista_Vertices:
            v.setVisitado(False)
            v.input = 0
            v.output = 0
        for v in self.lista_Vertices:
            if not v.getVisitado():
                self.visita(v)

    def visita(self, u):
        print("Visitando o vertice: %s" % u.getId())
        u.setVisitado(True)
        grafo.tempo += 1
        u.setImput(grafo.tempo)
        v = self.busca_Adjacente(u)#retorna apenas não visitado ou nulo
        while v is not None:
            v.predecessor.append(u.getId())
            self.visita(v)
            v = self.busca_Adjacente(u) 
            
        grafo.tempo += 1
        u.setOutput(grafo.tempo)
        print("Voltando para: ",u.predecessor)

        
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
                grafo.tempo += 1
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
        for i in self.lista_Vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()# ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.busca_Adjacente(u)

            if v is None:
                for i in lista:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                    i.setVisitado(False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
                  # retiro vertice sem adjacente
                grafo.tempo += 1
                u.setImput(grafo.tempo)
                lista.remove(u)
            else:
                w = self.busca_Aresta(u,v)
                if lista.count(v) > 0:
                    if v.getEstimativa() > w.getPeso():
                        v.predecessor.append(u.getId())
                        v.setEstimativa(w.getPeso())


        for u in self.lista_Vertices:
            if len(u.predecessor) > 0:
                print(u.predecessor,"------",u.getId())
        self.lista_Vertices.sort(key=lambda u: u.input, reverse=False)
        for i in self.lista_Vertices:
            print(i)
                



    def is_Cyclic(self,u):
        if (self.lista_Arestas > len(self.lista_Vertices) - 1):
            return "Erro,grafo não eh DAG (directed acyclic graph)."

    def grafo_Transposto(self):#w(u,v) passa a ser w(v,u)
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[0].getOrigem()
            destino = self.lista_Arestas[0].getDestino()
            self.lista_Arestas.pop(0)
            self.lista_Arestas.append(Aresta(destino, origem, 0))


    def Strong_component_algorithm(self):
        print("Busca em Profundidade")
        self.Depth_first_search()
        self.lista_Vertices.sort(key=lambda u: u.output, reverse=True) #ordena a lista em ralação a vertice.output
        for w in grafo.lista_Arestas:
            print(w)
        self.grafo_Transposto()
        print("Grafo Transposto:")
        for w in grafo.lista_Arestas:
            print(w)
        for i in self.lista_Vertices:
            i.input = 0
            i.output = 0
            i.setVisitado(False)
        print("\nComponetes fortemente Conexos\n")
        for i in self.lista_Vertices:
            if not i.getVisitado():
                self.visita(i)

    def euleriano(self):
        for u in self.lista_Vertices:
            if self.grau(u) % 2 is not 0:
                return False
        return True


    def grau(self,u):
        grau = 0
        for w in self.lista_Arestas:
            if u == w.getOrigem():
                grau += 1
        return grau

    def ehPonto(self,u):
        for v in self.lista_Vertices:
            v.setVisitado(False)

        u.setVisitado(True)
        self.visita(self.busca_Adjacente(u))
        for v in self.lista_Vertices:
            if v.getVisitado() == False:
                return True

    def Articulation(self):
        art = []
        for u in self.lista_Vertices:
            if self.ehPonto(u):
                art.append(u.getId())
        print("Pontos de Articulação",art)
# Grafo exemplo
#Exemplo Componentes fortemente conexos
"""
grafo = Grafo()
#Exemplo componente fortemente conexo
grafo.novo_Vertice(0)
grafo.novo_Vertice(1)
grafo.novo_Vertice(2)
grafo.novo_Vertice(3)
grafo.nova_Aresta(0,1,0)
grafo.nova_Aresta(0,3,0)
grafo.nova_Aresta(1,2,0)
grafo.nova_Aresta(2,0,0)
grafo.nova_Aresta(2,3,0)
grafo.Strong_component_algorithm()

#Exemplo Dijkstra
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
grafo.nova_Aresta("x", "u", 3)
grafo.nova_Aresta("x", "y", 2)
grafo.nova_Aresta("x", "v", 9)
grafo.nova_Aresta("y", "s", 7)
grafo.nova_Aresta("y", "v", 6)
grafo.Dijkstra("s")
grafo.imprime_Grafo('s','y')

#Exemplo Busca em profundidade
grafo = Grafo()
grafo.novo_Vertice(0)
grafo.novo_Vertice(1)
grafo.novo_Vertice(2)
grafo.novo_Vertice(3)
grafo.novo_Vertice(4)
grafo.novo_Vertice(5)
grafo.nova_Aresta(0,1,0)
grafo.nova_Aresta(0,4,0)
grafo.nova_Aresta(1,2,0)
grafo.nova_Aresta(1,4,0)
grafo.nova_Aresta(2,3,0)
grafo.nova_Aresta(3,1,0)
grafo.nova_Aresta(4,3,0)
grafo.nova_Aresta(5,4,0)
grafo.nova_Aresta(5,0,0)


#Exemplo Árovre geradora mínima
grafo = Grafo()
grafo.novo_Vertice("A")
grafo.novo_Vertice("B")
grafo.novo_Vertice("C")
grafo.novo_Vertice("D")
grafo.novo_Vertice("E")
grafo.novo_Vertice("F")
grafo.novo_Vertice("G")
#A
grafo.nova_Aresta("A", "B", 7)
grafo.nova_Aresta("A", "D", 5)
#B
grafo.nova_Aresta("B", "A", 7)
grafo.nova_Aresta("B", "D", 9)
grafo.nova_Aresta("B", "C", 8)
grafo.nova_Aresta("B", "E", 7)
#C
grafo.nova_Aresta("C", "B", 8)
grafo.nova_Aresta("C", "E", 5)
#D
grafo.nova_Aresta("D", "A", 5)
grafo.nova_Aresta("D", "B", 9)
grafo.nova_Aresta("D", "E",15)
grafo.nova_Aresta("D", "F", 6)
#E
grafo.nova_Aresta("E", "B", 7)
grafo.nova_Aresta("E", "C", 5)
grafo.nova_Aresta("E", "D",15)
grafo.nova_Aresta("E", "F", 8)
grafo.nova_Aresta("E", "G", 9)
#F
grafo.nova_Aresta("F", "D", 6)
grafo.nova_Aresta("F", "E", 8)
grafo.nova_Aresta("F", "G",11)
#G
grafo.nova_Aresta("G", "F",11)
grafo.nova_Aresta("G", "E", 9)

grafo.Minimum_spanning_tree("D")



#Exemplo Ciclo Euleriano
grafo = Grafo(False)
grafo.novo_Vertice('v')
grafo.novo_Vertice('x')
grafo.novo_Vertice('u')
grafo.novo_Vertice('y')
grafo.novo_Vertice('w')
grafo.novo_Vertice('z')

grafo.nova_Aresta('v','x',0)
grafo.nova_Aresta('v','u',0)
grafo.nova_Aresta('x','u',0)
grafo.nova_Aresta('x','y',0)
grafo.nova_Aresta('x','w',0)
grafo.nova_Aresta('u','y',0)
grafo.nova_Aresta('u','w',0)
grafo.nova_Aresta('y','z',0)
grafo.nova_Aresta('y','w',0)
grafo.nova_Aresta('w','z',0)

print(grafo.euleriano())
"""
#exemplo ponto de articulação
grafo = Grafo(False)
grafo.novo_Vertice('a')
grafo.novo_Vertice('b')
grafo.novo_Vertice('c')
grafo.novo_Vertice('d')
grafo.novo_Vertice('e')
grafo.novo_Vertice('f')
grafo.novo_Vertice('g')

grafo.nova_Aresta('a','d',0)
grafo.nova_Aresta('a','e',0)
grafo.nova_Aresta('b','e',0)
grafo.nova_Aresta('b','f',0)
grafo.nova_Aresta('c','f',0)
grafo.nova_Aresta('c','g',0)
grafo.nova_Aresta('d','e',0)
grafo.nova_Aresta('e','f',0)
grafo.nova_Aresta('f','g',0)

grafo.Articulation()
