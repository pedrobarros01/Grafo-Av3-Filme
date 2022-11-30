import random

class Filme:
    def __init__(self, name, genre, tipo) -> None:
        self._name = name
        self._genre = genre
        self._tipo = tipo
        self._peso = 0
        self._id = 0

    def ligar(self, filmeB):
        if self.genre.upper() == filmeB.genre.upper():
            return True
        return False
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    

    def __str__(self) -> str:
        return f'===Filme===\nNome: {self._name}\nGenero: {self._genre}'

    ## Quantidade de recomendação dos filmes
    @classmethod
    def saberEscala(cls, reccomendationVector):
        dicGenero = {
            'acao': 0,
            'comedia': 0,
            'terror': 0,
            'suspense': 0,
            'ficcao': 0,
            'romance': 0
        }
        for filme in reccomendationVector:
            if filme.genre == 'acao':
                dicGenero["acao"] += 1
            if filme.genre == 'comedia':
                dicGenero["comedia"] += 1
            if filme.genre == 'terror':
                dicGenero["terror"] += 1
            if filme.genre == 'suspense':
                dicGenero["suspense"] += 1
            if filme.genre == 'ficcao':
                dicGenero["ficcao"] += 1
            if filme.genre == 'romance':
                dicGenero["romance"] += 1
        return dicGenero

    
    @classmethod
    def distribuicaoEscala(cls, userVector):
        totalRecommedation = 6
        dicEscala = cls.saberEscala(userVector)
        totalUservector = len(userVector)
        dicFilmes = {
            'acao': 0,
            'comedia': 0,
            'terror': 0,
            'suspense': 0,
            'ficcao': 0,
            'romance': 0
        }
        dicResposta = dicFilmes.copy()
        for chave in dicEscala:
            peso = dicEscala[chave] / totalUservector
            dicFilmes[chave] = peso
        for chave in dicResposta:
            dicResposta[chave] = round(dicFilmes[chave] * totalRecommedation)
        return dicResposta
    


'''class RecommendationVector:
    def __init__(self) -> None:
        self.acao = 0
        self.romance = 0
        self.terror = 0
        self.ficcao = 0
        self.comedia = 0
        self.suspense = 0
        self.totalCount = 0

    def setQuantities(self, genre):
        if(genre == "acao"):
            self.totalCount+=1
            self.acao+=1
        elif(genre == "romance"):
            self.totalCount+=1
            self.romance+=1
        elif(genre == "terror"):
            self.totalCount+=1
            self.terror+=1
        elif(genre == "ficcao"):
            self.totalCount+=1
            self.ficcao+=1
        elif(genre == "comedia"):
            self.totalCount+=1
            self.comedia+=1
        elif(genre == "suspense"):
            self.totalCount+=1
            self.suspense+=1

    def getMoviesPercentage(self, genre):
        return genre/self.totalCount

    def fullfillRecommendationVector(self, watchedMovie, genreVector, recommendationVector):
        del(genreVector.index(watchedMovie))
        multiplier=0
        list = []
        if(len(recommendationVector) > 0):
            if(self.getMoviesPercentage(self.acao) > 1/6):
                multiplier = self.getMoviesPercentage(self.acao) * 6
                for i in range(multiplier):
                    sortedMovieIndex = random.randint(0, len(genreVector))
                    list.append(genreVector[sortedMovieIndex])
                    del(genreVector.index(sortedMovieIndex))
            elif(self.getMoviesPercentage(self.romance) > 1/6):
                 multiplier = self.getMoviesPercentage(self.romance) * 6
                 for i in range(multiplier):
                    sortedMovieIndex = random.randint(0, len(genreVector))
                    list.append(genreVector[sortedMovieIndex])
                    del(genreVector.index(sortedMovieIndex))
            elif(self.getMoviesPercentage(self.terror) > 1/6):
                multiplier = self.getMoviesPercentage(self.terror) * 6
                for i in range(multiplier):
                    sortedMovieIndex = random.randint(0, len(genreVector))
                    list.append(genreVector[sortedMovieIndex])
                    del(genreVector.index(sortedMovieIndex))
            elif(self.getMoviesPercentage(self.ficcao) > 1/6):
                 multiplier = self.getMoviesPercentage(self.ficcao) * 6
                 for i in range(multiplier):
                    sortedMovieIndex = random.randint(0, len(genreVector))
                    list.append(genreVector[sortedMovieIndex])
                    del(genreVector.index(sortedMovieIndex))
            elif(self.getMoviesPercentage(self.comedia) > 1/6):
                 multiplier = self.getMoviesPercentage(self.comedia) * 6
                 for i in range(multiplier):
                    sortedMovieIndex = random.randint(0, len(genreVector))
                    list.append(genreVector[sortedMovieIndex])
                    del(genreVector.index(sortedMovieIndex))
            elif(self.getMoviesPercentage(self.suspense) > 1/6):
                 multiplier = self.getMoviesPercentage(self.suspense) * 6
                 for i in range(multiplier):
                    sortedMovieIndex = random.randint(0, len(genreVector))
                    list.append(genreVector[sortedMovieIndex])
                    del(genreVector.index(sortedMovieIndex))
        return list'''
