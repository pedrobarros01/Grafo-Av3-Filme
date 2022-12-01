from collections import defaultdict
from random import randint
from auxiliares import preecherArestaLista, procurarPorGenero
import igraph as ig
import matplotlib.pyplot as plt
class Grafos: 
    def __init__(self, vertice, listaGeneros, listaFilmes, dirigido = False) -> None:
        
        self._vertice = vertice
        self.dirigido = dirigido
        self.adj = defaultdict(list)
        self.arestas = []
        for genero in listaGeneros:
            if genero.name == 'genero':
                vertice = genero
            if genero.name != 'genero':
                tupla = (vertice.id, genero.id)
                self.arestas.append(tupla)

        preecherArestaLista(listaFilmes, listaGeneros, self.arestas)
        for genero in listaGeneros:
            self.adj[genero.name]
        for filme in listaFilmes:
            self.adj[filme.name]
        for genero in listaGeneros:
            if genero.name != 'genero':
                self.adj['genero'].append(genero)
        self.listaGenero = listaGeneros
        self.listaFilme = listaFilmes
        
    def adicionarAresta(self, filmeA, generoB):
        if filmeA.genre != generoB.genre:
            raise ValueError('Genero de <Filme> e <Genero> nao coincide')
        self.adj[generoB.genre].append(filmeA)
        if not self.dirigido:
            self.adj[filmeA.name].append(generoB)
    
    def printarGrafos(self):
        for vertice in self.adj:
            print(f'{vertice}: {self.adj.get(vertice)}')
    
    def visualizarGrafoFilmes(self):
        g = ig.Graph(self._vertice, self.arestas)
        g["title"] = 'Grafo dos Filmes'
        lista = [vertice.name for vertice in self.listaGenero]
        lista.extend([vertice.name for vertice in self.listaFilme])
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
        fig.savefig('graph.svg')

    def visualizarGrafoRecomendacao(self, objRecomendacao):
        # 6 generos + 1 usuario + filmes que estao na recomendacao
        vertices = 7
        id_usuario = 0
        idAux = 7
        for chave in objRecomendacao:
            if len(objRecomendacao[chave]) != 0:
                for filme in objRecomendacao[chave]:
                    vertices += 1
        arestasAux = []
        for genero in self.listaGenero:
            if genero.name != 'genero':
                tupla = (id_usuario, genero.id)
                arestasAux.append(tupla)
        
        for chave in objRecomendacao:
            if len(objRecomendacao[chave]) != 0:
                generoID = procurarPorGenero(self.listaGenero, chave).id
                for filme in objRecomendacao[chave]:
                    tupla = (generoID, idAux)
                    idAux += 1
                    arestasAux.append(tupla)
        listaNomes = ['Usuário']
        listaNomes.extend([vertices.name for vertices in self.listaGenero if vertices.name != 'genero'])
        for chave in objRecomendacao:
            if len(objRecomendacao[chave]) != 0:
                listaAux = objRecomendacao[chave]
                listaNomes.extend(listaAux)
        g = ig.Graph(vertices, arestasAux)
        g["title"] = "Grafo de Recomendacao"
        g.vs["name"] = listaNomes
        fig, ax = plt.subplots(figsize=(10,10))
        ig.plot(
            g,
            target=ax,
            vertex_size=0.65,
            vertex_label=g.vs["name"],
            vertex_label_size=6.0
            
        )
        plt.show()
        fig.savefig('graphRecomendation.svg')

    def dfs(self, fonte, genero):

        lista = []
        dicVisitado = {}
        for vertice in self.adj:
            dicVisitado[vertice] = False
        def dfsAuxiliar(grafo, dicionarioVisitado, vertice, genero, listaAux):
            dicionarioVisitado[vertice.name] = True
            if vertice.peso == 1:
                listaAux.append(vertice.name)
            for vizinho in self.adj[vertice.name]:
                if not dicionarioVisitado[vizinho.name] and genero == vizinho.genre:
                    dfsAuxiliar(grafo, dicionarioVisitado, vizinho, genero, listaAux)
        dfsAuxiliar(self.adj, dicVisitado, fonte, genero, lista)
        return lista
    
    def modificarPeso(self, genero, escala):
        subgrafo = self.adj[genero]
        lista = [(filme, indice) for indice, filme in enumerate(subgrafo)]
        print(lista)
        for vertice, ind in enumerate(subgrafo):
            self.adj[genero][vertice].peso = 0
        peso = []
        while len(peso) != escala and len(lista) != 0:
            vertice, ind = lista.pop(0)
            colocaEle = randint(0, 1)
            if colocaEle and not vertice.peso:
                self.adj[genero][ind].peso = colocaEle
                peso.append(vertice)
            else:
                lista.append((vertice, ind))
            
    def BuscaPorRecomendacao(self, escalaDic, raiz):
        for chave in escalaDic:
             if escalaDic[chave] != 0:
                self.modificarPeso(chave, escalaDic[chave])
        dicRecommendacao = {
            'acao': [],
            'comedia': [],
            'terror': [],
            'suspense': [],
            'ficcao': [],
            'romance': []
        }
        for chave in dicRecommendacao:
            lista = self.dfs(raiz, chave)
            dicRecommendacao[chave] = lista
        return dicRecommendacao

            
                
        
            
        


    @property
    def vertice(self):
        return self._vertice

    @vertice.setter
    def vertice(self, vertice):
        self._vertice = vertice
            
        

#Fonte: https://algoritmosempython.com.br/  
#https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/busca-profundidade/