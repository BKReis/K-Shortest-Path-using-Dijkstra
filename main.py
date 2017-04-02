#!/usr/bin/python
#-*-coding:utf-8-*-
from graph import *
from djikstra import *
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
