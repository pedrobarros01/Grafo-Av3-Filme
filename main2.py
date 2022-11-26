from graph import Grafos
from mocks import listaGeneros, filmes, filme3, filme4, filme5, filme19, filme18, genero
from Filme.filme import Filme
from middlewares import preecherAresta, preecherArestaLista
import igraph as ig
import matplotlib.pyplot as plt
numVertices = len(listaGeneros) + len(filmes)
digrafo = Grafos(numVertices, listaGeneros, filmes, True)
edges = []
vertice = None
for genero in listaGeneros:
    if genero.name == 'genero':
        vertice = genero
    if genero.name != 'genero':
        tupla = (vertice.id, genero.id)
        edges.append(tupla)

preecherArestaLista(filmes, listaGeneros, edges)
print(edges)    
g = ig.Graph(numVertices, edges)
g["title"] = 'Grafo dos Filmes'
lista = [vertice.name for vertice in listaGeneros]
lista.extend([vertice.name for vertice in filmes])
print(lista)
g.vs["name"] = lista
fig, ax = plt.subplots(figsize=(5,5))
ig.plot(
    g,
    target=ax,
    layout="circle", # print nodes in a circular layout
    vertex_size=0.1,
    vertex_frame_width=1.0,
    vertex_label=g.vs["name"],
    vertex_label_size=7.0,
)
plt.show()

'''preecherAresta(filmes, digrafo, listaGeneros)
digrafo.printarGrafos()
user = [filme3, filme4, filme5, filme19, filme18]
escala = Filme.distribuicaoEscala(user)
print('escala: ' + escala.__str__())
print(escala['acao'])
dicRecomendacao = digrafo.BuscaPorRecomendacao(escala, genero)
print(dicRecomendacao)'''
