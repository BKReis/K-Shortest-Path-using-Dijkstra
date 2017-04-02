class Nodos:
	def __init__(self,nome):
		self.nome = nome
		self.conectadoCom = {}
		self.distanciaDoNodoInicial = 1000000

	def adicionaVizinhos(self,vizinho,peso=0):
		self.conectadoCom[vizinho] = peso

	def removeVizinho(self,a):
		self.conectadoCom[a].pop()

	def setDistanciaDoNodoInicial(self,distancia):
		self.distanciaDoNodoInicial = distancia

	def getConexoes(self):
		return self.conectadoCom.keys()

	def getNome(self):
		return self.nome

	def getPeso(self,vizinho):
		return self.conectadoCom[vizinho]

	def getDistanciaDoNodoInicial(self):
		return self.distanciaDoNodoInicial