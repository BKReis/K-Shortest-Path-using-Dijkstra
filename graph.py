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

    def deletaUltimaAresta(self):
        self.listaDeNodos[-1].removeVizinho()

    def __iter__(self):
        return iter(self.listaDeNodos.values())