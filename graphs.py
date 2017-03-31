#!/usr/bin/python
#-*-coding:utf-8-*-

class Nodos:
	def __init__(self,nome):
		self.nome = nome
		self.conectadoCom = {}
		self.distanciaDoNodoInicial = 1000000

	def adicionaVizinhos(self,vizinho,peso=0):
		self.conectadoCom[vizinho] = peso

	def removeVizinho(self):
		self.conectadoCom.pop()

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

class Grafo:
	def __init__(self):
		self.listaDeNodos = {}
		self.numeroDeNodos = 0
		

	def adicionaNodo(self,nome):
		self.numeroDeNodos = self.numeroDeNodos + 1
		novoNodo = Nodos(nome)
		self.listaDeNodos[nome] = novoNodo
		
		return novoNodo

	def criaAresta(self,a,b,peso=0):
		##Assume-se que o trâfego de dados e o custo seja o mesmo tanto para a ida quanto para a volta entre dois nós
		self.listaDeNodos[a].adicionaVizinhos(self.listaDeNodos[b],peso)

	def deletaUltimaAresta(self):
		self.listaDeNodos[-1].removeVizinho()

	def __iter__(self):
		return iter(self.listaDeNodos.values())

	
def Dijkstra(Grafo,nodoInicial):
	dictHeap = {}
	dictDistanciaDoNodoInicial = {}

	for x in Grafo.listaDeNodos:
		dictDistanciaDoNodoInicial[x] = 999999
		dictHeap[x] = dictDistanciaDoNodoInicial[x]

	dictDistanciaDoNodoInicial[nodoInicial] = 0
	dictHeap[nodoInicial] = 0

	while dictHeap:
		k = heapMinimo(dictHeap)
		#for j in Grafo.listaDeNodos[k].getConexoes():
		#	acrescimo = Grafo.listaDeNodos[k].getPeso(j)
		#	novaDistancia = dictDistanciaDoNodoInicial[k] + acrescimo
		#	aux = j.getNome()
		#	if (novaDistancia < dictDistanciaDoNodoInicial[aux]):
		#		dictDistanciaDoNodoInicial[j] = novaDistancia
		#		dictHeap[j] = novaDistancia
	return dictDistanciaDoNodoInicial

def heapMinimo(dictHeap):
	#Valor muito alto 
	infinito = 1000000
	menorDistanciaNodoInicial = None
	for menorDistancia in dictHeap:
		if dictHeap[menorDistancia] < infinito:
			infinito = dictHeap[menorDistancia]
			menorDistanciaNodoInicial = menorDistancia
	del dictHeap[menorDistanciaNodoInicial]
	
	return menorDistanciaNodoInicial



if __name__ == '__main__':


	Exemplo = Grafo()
	for i in range(6):
		Exemplo.adicionaNodo(i)
	Exemplo.criaAresta(0,1,6)
	Exemplo.criaAresta(0,2,8)
	Exemplo.criaAresta(1,4,11)
	Exemplo.criaAresta(2,3,9)
	Exemplo.criaAresta(4,5,3)
	Exemplo.criaAresta(5,2,7)
	Exemplo.criaAresta(5,3,4)


	Dijkstra(Exemplo,Exemplo.listaDeNodos[0].getNome())

	for v in Exemplo:
		for w in v.getConexoes():
			print("(%s,%s)" % (v.getNome(),w.getNome()))

	print "Shortest distance from each vertex:"
	for a in dictDistanciaDoNodoInicial: print "%s: %s" % (a, dictDistanciaDoNodoInicial[a])
