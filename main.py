from Filme.filme import Filme
from mocks import filmes, listaGeneros, genero
from graph import Grafos
from middlewares import preecherAresta
if __name__ == '__main__':
    user = []
    reccomendationVector = []
    operacao = True
    numVertices = len(listaGeneros) + len(filmes)
    grafo = Grafos(numVertices, listaGeneros, filmes, True)
    preecherAresta(filmes, grafo, listaGeneros)
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