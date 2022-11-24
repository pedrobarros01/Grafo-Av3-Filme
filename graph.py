from collections import defaultdict
from Filme import Filme

class Grafos:
    def __init__(self, vertice, listaGeneros, dirigido = False) -> None:
        self.vertice = vertice
        self.dirigido = dirigido
        self.adj = defaultdict(list)
        for genero in listaGeneros:
            self.adj[genero.name]
        print(self.adj)
        for genero in listaGeneros:
            if genero.name != 'genero':
                self.adj['genero'].append(genero)
        print(self.adj)
        print(len(self.adj['genero']))

    def adicionarAresta(self, filmeA, generoB):
        if filmeA.genre != generoB.genre:
            raise ValueError('Genero de <Filme> e <Genero> nao coincide')
        self.adj[generoB.genre].append(filmeA)
        if not self.dirigido:
            self.adj[filmeA.name].append(generoB)
    
    def printarGrafos(self):
        for vertice in self.adj:
            print(f'{vertice}: {self.adj.get(vertice)[0].name}')

    def dfs(self, fonte):
        lista = [False for i in self.vertice]
 
        def dfsAuxiliar(grafo, listaVisitado, vertice):
            #listaVisitado
            pass
        dfsAuxiliar(self.adj, lista, fonte)

            
        



class Grafo(Filme):
    """ Implementação básica de um grafo. """

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)


    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())


    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v in arestas:
            self.adiciona_arco(u, v)


    def adiciona_arco(self, u, v):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)


    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]


    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]

        

def dfs(grafo, vertice):
    visitados = set()

    def dfs_iterativa(grafo, vertice_fonte):
        visitados.add(vertice_fonte)
        falta_visitar = [vertice_fonte]
        while falta_visitar:
            vertice = falta_visitar.pop()
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    falta_visitar.append(vizinho)

    dfs_iterativa(grafo, vertice)

#Fonte: https://algoritmosempython.com.br/  
#https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/busca-profundidade/