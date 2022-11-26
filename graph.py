from collections import defaultdict
from random import randint
class Grafos: 
    def __init__(self, vertice, listaGeneros, listaFilmes, dirigido = False) -> None:
        
        self._vertice = vertice
        self.dirigido = dirigido
        self.adj = defaultdict(list)
        for genero in listaGeneros:
            self.adj[genero.name]
        for filme in listaFilmes:
            self.adj[filme.name]
        print(self.adj)
        for genero in listaGeneros:
            if genero.name != 'genero':
                self.adj['genero'].append(genero)
    def adicionarAresta(self, filmeA, generoB):
        if filmeA.genre != generoB.genre:
            raise ValueError('Genero de <Filme> e <Genero> nao coincide')
        self.adj[generoB.genre].append(filmeA)
        if not self.dirigido:
            self.adj[filmeA.name].append(generoB)
    
    def printarGrafos(self):
        for vertice in self.adj:
            print(f'{vertice}: {self.adj.get(vertice)}')
        

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
        lista = [(vertice, ind) for ind, vertice in enumerate (subgrafo)]
        operacao = True
        peso = []
        while operacao:
            vertice, ind = lista.pop(0)
            colocaEle = randint(0, 1)
            print(colocaEle)
            if colocaEle and not vertice.peso:
                self.adj[genero][ind].peso = colocaEle
                peso.append(vertice)
            else:
                lista.append((vertice, ind))
            if len(peso) == escala:
                operacao = False
            
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