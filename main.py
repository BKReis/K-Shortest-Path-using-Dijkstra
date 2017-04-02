import sys
from graph import *
from djikstra import *
if __name__ == '__main__':

	infinito = 999999

	#graph declaration
	graph = Grafo()
	for i in range(6):
		graph.adicionaNodo(i)
	graph.criaAresta(0,1,6)
	graph.criaAresta(0,2,8)
	graph.criaAresta(1,4,11)
	graph.criaAresta(2,3,9)
	graph.criaAresta(4,5,3)
	graph.criaAresta(5,2,7)
	graph.criaAresta(5,3,4)

	if len(sys.argv) == 4:
		#receive arguments from command line
		k = int(sys.argv[1])
		initial_node_number = int(sys.argv[2])
		dest_node_number = int(sys.argv[3])
		u = 0
		while u < k:
			if dest_node_number in graph.listaDeNodos:
				dijkstra = Dijkstra(graph, graph.listaDeNodos[initial_node_number].getNome(), graph.listaDeNodos[dest_node_number].getNome())
				if dijkstra.dictDistanciaDoNodoInicial[dest_node_number] < infinito:
					print "Shortest Path "+str(u+1) +": "+ str(dijkstra.minimunPathList)
					print "Path Total Weight: "+str(dijkstra.dictDistanciaDoNodoInicial[dest_node_number])
					graph.listaDeNodos.pop(dijkstra.minimunPathList[1])
					#graph.deletaMenorAresta(dijkstra.minimunPathList)
				else:
					u = k
					print "All Possible Paths Found"
			u = u+1
	else:
		print "Enter the correct number of arguments!!"



	# dijkstra = Dijkstra(Exemplo,Exemplo.listaDeNodos[1].getNome(),Exemplo.listaDeNodos[3].getNome())

	# for v in Exemplo:
	# 	for w in v.getConexoes():
	# 		print("(%s,%s)" % (v.getNome(),w.getNome()))
	#
	# print "Shortest distance from each vertex:"
	# for a in dijkstra.dictDistanciaDoNodoInicial: print "%s: %s" % (a, dijkstra.dictDistanciaDoNodoInicial[a])
	#
	# print "Last node table:"
	# for a in dijkstra.lastNodeTable: print "%s: %s" % (a, dijkstra.lastNodeTable[a])
	#
	# print "minimum path list" + str(dijkstra.minimunPathList)
