from graph import Grafos
from mocks import listaGeneros, filmes, genero, filme7, filme10, filme12
from Filme.filme import Filme
from middlewares import preecherAresta, preecherArestaLista
'''import igraph as ig
import matplotlib.pyplot as plt'''
numVertices = len(listaGeneros) + len(filmes)
digrafo = Grafos(numVertices, listaGeneros, filmes, True)
preecherAresta(filmes, digrafo, listaGeneros)
digrafo.printarGrafos()
user = [filme7, filme10, filme12]
escala = Filme.distribuicaoEscala(user)
print('escala: ' + escala.__str__())
dicRecomendacao = digrafo.BuscaPorRecomendacao(escala, genero)
print(dicRecomendacao)
'''edges = []
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
fig, ax = plt.subplots(figsize=(10,10))
ig.plot(
    g,
    target=ax,
    vertex_size=0.95,
    vertex_label=g.vs["name"],
    vertex_label_size=6.0
    
)
plt.show()
fig.savefig('graph.svg')'''

'''
preecherAresta(filmes, digrafo, listaGeneros)
digrafo.printarGrafos()
user = [filme3, filme4, filme5, filme19, filme18]
escala = Filme.distribuicaoEscala(user)
print('escala: ' + escala.__str__())
print(escala['acao'])
dicRecomendacao = digrafo.BuscaPorRecomendacao(escala, genero)
print(dicRecomendacao)
'''


