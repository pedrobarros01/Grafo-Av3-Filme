
class Filme:
    def __init__(self, name, genre) -> None:
        self._name = name
        self._genre = genre
    
    def ligar(self, filmeB):
        if self.genre.upper() == filmeB.genre.upper():
            return True
        return False
    
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
            'ação': 0,
            'comédia': 0,
            'terror': 0,
            'suspense': 0,
            'ficção': 0,
            'romance': 0
        }
        for filme in reccomendationVector:
            if filme.genre == 'ação':
                dicGenero["ação"] += 1
            if filme.genre == 'comédia':
                dicGenero["comédia"] += 1
            if filme.genre == 'terror':
                dicGenero["terror"] += 1
            if filme.genre == 'suspense':
                dicGenero["suspense"] += 1
            if filme.genre == 'ficção':
                dicGenero["ficção"] += 1
            if filme.genre == 'romance':
                dicGenero["romance"] += 1
        return dicGenero
    


