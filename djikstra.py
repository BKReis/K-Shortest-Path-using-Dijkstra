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
    # Valor muito alto
    infinito = 1000000
    menorDistanciaNodoInicial = None
    for menorDistancia in dictHeap:
        if dictHeap[menorDistancia] < infinito:
            infinito = dictHeap[menorDistancia]
            menorDistanciaNodoInicial = menorDistancia
    del dictHeap[menorDistanciaNodoInicial]

    return menorDistanciaNodoInicial


