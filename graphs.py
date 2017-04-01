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
		self.listaDeNodos[b].adicionaVizinhos(self.listaDeNodos[a], peso)

	def deletaUltimaAresta(self):
		self.listaDeNodos[-1].removeVizinho()

	def __iter__(self):
		return iter(self.listaDeNodos.values())

	
class Dijkstra:
	dictHeap = {}
	dictDistanciaDoNodoInicial = {}
	lastNodeTable = {}
	minimunPathList = []

	def __init__(self,Grafo,nodoInicial,finalNode):
		for x in Grafo.listaDeNodos:
			self.dictDistanciaDoNodoInicial[x] = 999999
			self.dictHeap[x] = self.dictDistanciaDoNodoInicial[x]
			self.lastNodeTable[x] = nodoInicial

		self.dictDistanciaDoNodoInicial[nodoInicial] = 0
		self.dictHeap[nodoInicial] = 0

		while self.dictHeap:
			source_node_name = heapMinimo(self.dictHeap)
			for dest_node in Grafo.listaDeNodos[source_node_name].getConexoes():
				acrescimo = Grafo.listaDeNodos[source_node_name].getPeso(dest_node)
				novaDistancia = self.dictDistanciaDoNodoInicial[source_node_name] + acrescimo
				dest_node_name = dest_node.getNome()
				if (novaDistancia < self.dictDistanciaDoNodoInicial[dest_node_name]):
					self.dictDistanciaDoNodoInicial[dest_node_name] = novaDistancia
					self.dictHeap[dest_node_name] = novaDistancia
					self.lastNodeTable[dest_node_name] = source_node_name

		#monta lista formando menor caminho a partir do node final percorrendo tabela de anteriores
		#ate chegar no node inicial
		self.minimunPathList.append(finalNode)
		nodeAnterior = self.lastNodeTable[finalNode]
		while nodoInicial != nodeAnterior:
			self.minimunPathList.append(nodeAnterior)
			nodeAnterior = self.lastNodeTable[nodeAnterior]
		self.minimunPathList.append(nodoInicial)
		self.minimunPathList = list(reversed(self.minimunPathList))



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

	dijkstra = Dijkstra(Exemplo,Exemplo.listaDeNodos[1].getNome(),Exemplo.listaDeNodos[3].getNome())

	for v in Exemplo:
		for w in v.getConexoes():
			print("(%s,%s)" % (v.getNome(),w.getNome()))

	print "Shortest distance from each vertex:"
	for a in dijkstra.dictDistanciaDoNodoInicial: print "%s: %s" % (a, dijkstra.dictDistanciaDoNodoInicial[a])

	print "Last node table:"
	for a in dijkstra.lastNodeTable: print "%s: %s" % (a, dijkstra.lastNodeTable[a])

	print "minimum path list" + str(dijkstra.minimunPathList)
