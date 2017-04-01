#!/usr/bin/python
#-*-coding:utf-8-*-
from nodos import *
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
