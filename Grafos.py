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


#Verice
class Vertice():
	def __init__(self,id):
		self.id = id
		self.estimativa = 0
		self.input = 0
		self.output = 0
		self.visitado = False
		self.predecessores = []
		
	def setVisitado(self,valor ):
		self.visitado = valor

	def getVisitado(self):
		return self.visitado
	
	def setId(self,id):
		self.id = id
	
	def getId(self):
		return self.id
		
	def setImput(self,inp ):
		self.input = inp

	def setOutput(self,out):
		self.output = out

	def setEstimativa(self,estimativa ):
		self.estimativa = estimativa
	
	def getEstimativa(self):
		return self.estimativa
	def __str__(self):
		return(" Vertice  : %s \n Estimativa: %i \n Tempo(%i\%i): "%(self.id,self.estimativa,self.input,self.output))#imprimir o predecesso

	def __lt__(self,v):
		return self.estimativa < v.estimativa
	
	def __eq__(self,v):
		return self.estimativa == v.estimativa
	
	def __gt__(self,v):
		return self.estimativa > v.estimativa
	
#Aresta

class Aresta():
	def __init__(self,origem,destino,peso = 0):
		self.origem = origem
		self.destino = destino
		self.peso = peso
				
	def getOrigem(self):
		return self.origem
		
	def getDestino(self):
		return self.destino
	
	def setpeso(self,peso):
		self.peso = peso
		
	def	getPeso(self):
		return self.peso
		
	def setOrigem(self,vertice):
		self.origem = vertice
		
	def setDestino(self,vertice):
		self.destino = vertice
	
	def __str__(self):
		return("Origem : %s \n Destino: %s \n Peso: %i"%(self.origem.getId(),self.destino.getId(),self.peso))

#Grafo
class Grafo():
	def __init__(self,direcionado = True):
		self.lista_Vertices = []
		self.lista_Arestas = []
		self.direcionado = direcionado
		self.tempo = 0

	def add_Vertice(self,Identificador):
		#string = input(str("Identificador do Vertice: "))
		self.lista_Vertices.append(Vertice(Identificador))
	
	def busca_Vertice(self,identificador): #Método recebe um int
			for i in self.lista_Vertices:
				if identificador == i.getId():
					return i
			else:
				return None
			
	def add_Aresta(self,origem,destino,peso):
			origem_aux = self.busca_Vertice(origem)
			destino_aux= self.busca_Vertice(destino)
			if ( (origem_aux is not None) and (destino_aux is not None)):
				self.lista_Arestas.append(Aresta(origem_aux,destino_aux,peso=0))
			else:
				print ("Um do Vertice ou ambos são invalidos")
			
	def esta_Vazio(self):
		if (len(self.lista_Vertices) == 0 ):
			return True
		else:
			return False
	
	def busca_Adjacente(self,u): #Método recebe um vertice 
		for i in range(len(self.lista_Arestas)):
			origem = self.lista_Arestas[i].getOrigem()
			destino = self.lista_Arestas[i].getDestino()
			if ( (u.getId() == origem.getId()) and (destino.getVisitado() == False) ):
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
				print("Visitando o vertice: %s" %v.getId())
				self.visita(v)
	
	def visita(self,u):
		u.setVisitado(True)
		self.tempo=+1
		u.setImput(self.tempo)
		v = self.busca_Adjacente( u )
		if  ( (v is not None) and (v.getVisitado() == False)):
			print("Predecessor de %s"%v.getId())
			print(u)
			v.predecessores.append(u)
			self.visita(v)
		else:
			u.setVisitado(True)
			self.tempo=+1
			u.setOutput(self.tempo)
			print(u)
	
	def inicializa_Fonte(self,Identificador):# Busca em largura e Dijkstra
                for v in self.lista_Vertices:
                    v.setEstimativa(99999)
                fonte = self.busca_Vertice(Identificador)
                fonte.setVisitado(True)
                fonte.setEstimativa(0)
                
                
            
        
	def busca_Largura(self,Identificador):
                self.inicializa_Fonte(Identificador)
		fonte = self.busca_Vertice(Identificador)
		fila = [fonte]
		while ( len(lista)!=0):
			u = lista.pop(0)
			v = self.busca_Adjacente( u )
			if ((v is not None) and (v.getVisitado == False)):
				v.setVisitado(True)
                                v.setImput(self.tempo)
                                lista.append(v)
                                lista.sort()
			else:
				u.setVisitado(True)
		
	

			
	def inicializa_Fonte(self,Identificador):
	for v in self.lista_Vertices:
		v.setEstimativa(99999)
	fonte = self.busca_Vertice(Identificador)
	fonte.setVisitado(True)
	fonte.setEstimatima(0)
	
	def Dijkstra(self,Identificador):
	self.inicializa_Fonte(Identificador)
	fonte = self.busca_Vertice(Identificado)
	while( len(lista)!=0 ):
		u = lista.pop(0)
	
	
	
