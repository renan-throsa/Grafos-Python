from Vertice import Vertice
from Aresta import Aresta

# Grafo
class Grafo:
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado
        self.tempo = 0

    def novo_Vertice(self, identificador):
        # string = input(str("Identificador do Vertice: "))
        if self.busca_Vertice(identificador) is None:
            self.lista_Vertices.append(Vertice(identificador))
            return True
        return False

    def busca_Aresta(self, u, v):  # Método recebe dois objetos do tipo Vértice
        if not u or not v:
            return None

        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w
        return None

    def busca_aresta_vertice(self, u):  # Método recebe um objeto do tipo Vértice
        a = []
        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u or destino.getId() == u:
                a.append(w)
        return a

    def busca_Vertice(self, identificador):  # Método recebe um int

        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def remove_vertice(self, identificador): #Método recebe um int
        v = self.busca_Vertice(identificador)
        if v is None:
            return None
        else:
            self.lista_Vertices.remove(v)
            arestas = self.busca_aresta_vertice(identificador)
            if len(arestas) != 0:
                for x in arestas:
                    self.lista_Arestas.remove(x)
            else:
                return None

    def nova_Aresta(self, origem, destino, peso):  # Método recebe dois identificadores
        if self.busca_Aresta(self.busca_Vertice(origem), self.busca_Vertice(destino)):
            return False

        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            return False

        if not self.direcionado:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))  # Aresta(u,v) e Aresta(v,u)
        return True

    def remove_Aresta(self, origem, destino):
        v = self.busca_Vertice(origem)
        w = self.busca_Vertice(destino)
        if v is None or w is None:
            return False

        x = self.busca_Aresta(v, w)
        y = self.busca_Aresta(w, v)
        #Verifica se encontrou a aresta
        if x is None and y is None:
            return False
        #Remove todas as arestas correspondentes
        try:
            while True:
                try:
                    self.lista_Arestas.remove(x)
                except ValueError:
                    self.lista_Arestas.remove(y)
        except ValueError:
            pass

        return True

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
                destino.setVisitado(True)  # Para que não retorn o mesmo vertice seguidas veses
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
        self.tempo += 1
        u.setImput(self.tempo)
        v = self.busca_Adjacente(u)  # retorna apenas não visitado ou nulo
        while v is not None:
            v.predecessor.append(u.getId())
            self.visita(v)
            v = self.busca_Adjacente(u)

        self.tempo += 1
        u.setOutput(self.tempo)
        print("Voltando para: ", u.predecessor)

    def inicializa_Fonte(self, fonte):  # Função usado no BFS e Dijkstra Método recebe um Objeto
        for v in self.lista_Vertices:
            v.setEstimativa(99999)
            v.setVisitado(False)
        fonte.setVisitado(True)
        fonte.setEstimativa(0)

    def Breadth_first_search(self, identificador):
        fonte = self.busca_Vertice(identificador)
        if fonte is None:
            return "Vertce Nulo"
        self.inicializa_Fonte(fonte)
        lista = [fonte]
        while 0 != len(lista):
            u = lista[0]
            v = self.busca_Adjacente(u)  # retorna adjacente não visitado
            if v is None:
                lista.pop(0)  # retiro o vertice sem adjacentes

            else:
                self.tempo += 1
                v.setImput(self.tempo)
                v.predecessor.append(u.getId())
                v.setVisitado(True)
                lista.append(v)

            u.setVisitado(True)

    def imprime_Grafo_com_Destino(self, origem, destino):
        destino_Aux = self.busca_Vertice(destino)
        if len(destino_Aux.predecessor) == 0:
            print("Não ha caminho")
        else:
            print(destino)
            self.imprime_Grafo(origem, destino)

    def imprime_Grafo(self, origem, destino):
        if origem == destino:
            print("Fim")
        else:
            destino_Aux = self.busca_Vertice(destino)
            print(destino_Aux)
            if len(destino_Aux.predecessor) == 0:
                print("Não ha caminho")
            else:
                print(destino_Aux.predecessor[0])
                self.imprime_Grafo(origem, destino_Aux.predecessor[0])

    def printa_grafo(self):
        lista_formatada = ""
        for i in self.lista_Arestas:
            lista_formatada += str(i)
            lista_formatada += "\n"
        if len(self.lista_Vertices) == 0:
            return "============= O grafo ainda nao possui nenhum vertice ============="
        if lista_formatada == "":
            return "============= O grafo ainda nao possui nenhuma aresta ============="
        return lista_formatada

    def relaxa_Vertice(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId())  # guarda apenas o id

    def generate_subsets(self, set_, curr_subset, subsets_, k, next_index):
        if len(curr_subset) == int(k):
            subsets_.append(curr_subset)
            return
        if next_index + 1 <= len(set_):
            curr_subset_exclude = curr_subset.copy()
            curr_subset.append(set_[next_index])
            self.generate_subsets(set_, curr_subset, subsets_, k, next_index+1)
            self.generate_subsets(set_, curr_subset_exclude, subsets_, k, next_index+1)

    def verify_vertex_cover(self, cover, edges):
        # check that atleast one vertice from each edge appears in cover
        for edge in edges:

            in_cover = False
            for vertex in cover:
                if edge.getOrigem() == vertex or edge.getDestino() == vertex:
                    in_cover = True
            # stop processing as soon as one edge found not in cover
            if not in_cover:
                return False
    # return true if all edges have atleast one endpoint in cover
        return True

    def gen_subsets(self, set_, k):
        curr_subset = []
        res = []
        self.generate_subsets(set_, curr_subset, res, k, 0)
        return res

    def bruteForce(self):
        vertices = self.lista_Vertices
        k = len(vertices)
        res = []
        min_vertices_lenght = len(vertices)
        # generate all edges present in graph
        edges = self.lista_Arestas

        for i in range(1, k):
            # generate all subset of size i from set vertices
            subsets_ = self.gen_subsets(vertices, i)

            for s in subsets_:
                # check if subset s is a cover for graph

                if self.verify_vertex_cover(s, edges) is True and len(s) <= min_vertices_lenght:
                    min_vertices_lenght = len(s)
                    # since subsets are generated in  increasing size, the first
                    # subset that is cover can be returned as the minimal one
                    res.append(s)

        return res
