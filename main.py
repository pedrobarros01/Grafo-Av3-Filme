from Filme.filme import Filme
from mocks import filmes, listaGeneros, genero
from graph import Grafos

def procurarPorGenero(listaDeGenero, genero):
    for genre in listaDeGenero:
        if genre.name == genero:
            return genre

def preecherAresta(listaFilme, grafo, listaDeGenero):
    for i in range(0, len(listaFilme)):
        if(i < 5):
            grafo.adicionarAresta(listaFilme[i], procurarPorGenero(listaDeGenero, 'acao'))
        elif(i < 10):
            grafo.adicionarAresta(listaFilme[i], procurarPorGenero(listaDeGenero, 'comedia'))
        elif(i < 15):
            grafo.adicionarAresta(listaFilme[i], procurarPorGenero(listaDeGenero, 'terror'))
        elif(i < 20):
            grafo.adicionarAresta(listaFilme[i], procurarPorGenero(listaDeGenero, 'suspense'))
        elif(i < 25):
            grafo.adicionarAresta(listaFilme[i], procurarPorGenero(listaDeGenero, 'ficcao'))
        elif(i < 30):
            grafo.adicionarAresta(listaFilme[i], procurarPorGenero(listaDeGenero, 'romance'))

if __name__ == '__main__':
    user = []
    reccomendationVector = []
    operacao = True
    grafo = Grafos(len(listaGeneros) + len(filmes), listaGeneros)
    preecherAresta(filmes, grafo, listaGeneros)
    grafo.printarGrafos()
    '''
    R -> buscar recomendação
    V -> Ver filme, adicionar no vetor User
    L -> listar catalogo de filme
    '''
    while operacao:
        opc = input('>>> O que deseja fazer: (V/L/R/U/D/F)')
        if opc.upper().strip() == 'V':
            nomeFilme = input('>>> Qual o nome do filme: ')
            filmeAdd = None
            for filme in filmes:
                if nomeFilme.upper() == filme.name.upper():
                    filmeAdd = filme
                    break
            if filmeAdd:
                user.append(filmeAdd)
            else:
                print('>>> Nao encontrado filme na lista de filmes')
        elif opc.upper().strip() == 'L':
            for filme in filmes:
                print(filme)
        elif opc.upper().strip() == 'R':
            print('>>> Listar Recomendacoes')
            dicEscala = Filme.distribuicaoEscala(user)
            print(dicEscala)
            dicRecomendacao = grafo.BuscaPorRecomendacao(dicEscala, genero)
            print(dicRecomendacao)
        elif opc.upper().strip() == 'U':
            print('>>> Listando filmes marcados para ver')
            for filmeVisto in user:
                print(filmeVisto)
        elif opc.upper().strip() == 'D':
            print('>>> Delete um filme')
            nomeFilme = input('>>> Nome do filme Visto: ')
            filmeDelete = None
            for filme in filmes:
                if nomeFilme.upper() == filme.upper():
                    filmeDelete = filme
                    break
            if filmeDelete:
                user.remove(filmeDelete)
            else:
                print('>>> Filme nao encontrado na sua lista')
        elif opc.upper().strip() == 'F':
            print('>>> Terminando operacao')
            operacao = False
        else:
            print(f'>>> Digitou errado: {opc}')