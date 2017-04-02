from node import *
class Grafo:
    def __init__(self):
        self.listaDeNodos = {}
        self.numeroDeNodos = 0

    def adicionaNodo(self, nome):
        self.numeroDeNodos = self.numeroDeNodos + 1
        novoNodo = Nodos(nome)
        self.listaDeNodos[nome] = novoNodo

        return novoNodo

    def criaAresta(self, a, b, peso=0):
        self.listaDeNodos[a].adicionaVizinhos(self.listaDeNodos[b], peso)
        self.listaDeNodos[b].adicionaVizinhos(self.listaDeNodos[a], peso)

    def deletaMenorAresta(self,minimumPathList):
        initial_node = {}
        final_node = {}
        pesoFinal = 9999999

        #encontra aresta de menor peso entre as arestas relacionadas com elementos do menor caminho
        for x in minimumPathList:
            for y in self.listaDeNodos[x].conectadoCom:
                peso = self.listaDeNodos[x].conectadoCom[y]
                #print str(x) +" conecta com: " + str(y.nome) + " com peso: " +str(peso)
                if(pesoFinal> peso) and (existeNoPathMinimo(minimumPathList,y.nome)):
                    pesoFinal = peso
                    initial_node = x
                    final_node = y.nome
       #print "menor aresta: "+ str(initial_node) + "," + str(final_node) + "peso:" + str(pesoFinal)


        #apaga do grafo caminho de ida e volta da aresta de menor peso
        if final_node != {}:
            for j in self.listaDeNodos[initial_node].conectadoCom:
                if j.nome == final_node:
                    self.listaDeNodos[initial_node].conectadoCom.pop(j)
                    break
            for i in self.listaDeNodos[final_node].conectadoCom:
                if i.nome == initial_node:
                    self.listaDeNodos[final_node].conectadoCom.pop(i)
                    break


    def __iter__(self):
        return iter(self.listaDeNodos.values())


def existeNoPathMinimo(minimumPathList, a):
    if a in minimumPathList:
        return True
    else:
        return False