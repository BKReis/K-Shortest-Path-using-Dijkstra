from dijkstra import *
from graph import *


if __name__ == "__main__":
    exemplo = Grafo()
    for i in range(6):
        exemplo.adicionaNodo(i)
        exemplo.criaAresta(0,1,6)
        exemplo.criaAresta(0,2,8)
        exemplo.criaAresta(1,4,11)
        exemplo.criaAresta(2,3,9)
        exemplo.criaAresta(4,5,3)
        exemplo.criaAresta(5,2,7)
        exemplo.criaAresta(5,3,4)

    dictDistanciaDoNodoInicial = Dijkstra(exemplo,exemplo.listaDeNodos[0].getNome())
    printPath(exemplo,dictDistanciaDoNodoInicial)