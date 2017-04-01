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
    # Valor muito alto
    infinito = 1000000
    menorDistanciaNodoInicial = None
    for menorDistancia in dictHeap:
        if dictHeap[menorDistancia] < infinito:
            infinito = dictHeap[menorDistancia]
            menorDistanciaNodoInicial = menorDistancia
    del dictHeap[menorDistanciaNodoInicial]

    return menorDistanciaNodoInicial

def printPath(exemplo,dictDistanciaDoNodoInicial):
    for v in exemplo:
        for w in v.getConexoes():
            print("(%s,%s)" % (v.getNome(), w.getNome()))

    print "Shortest distance from each vertex:"
    for a in dictDistanciaDoNodoInicial: print "%s: %s" % (a, exemplo.dictDistanciaDoNodoInicial[a])