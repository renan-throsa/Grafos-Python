class Vertice():
    def __init__(self, id):
        self.id = id
        self.estimativa = 999999
        self.input = 0
        self.output = 0
        self.visitado = False
        self.predecessor = []

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setImput(self, inp):
        self.input = inp

    def setOutput(self, out):
        self.output = out

    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa

    def __str__(self):
        return (" Vertice  : %s \n Estimativa: %i \n Tempo(%i\%i): " % (
        self.id, self.estimativa, self.input, self.output))  # imprimir o predecesso

    def __lt__(self, v):
        return self.estimativa < v.estimativa

    def __eq__(self, v):
        return self.estimativa == v.estimativa

    def __gt__(self, v):
        return self.estimativa > v.estimativa
