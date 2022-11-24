from mocks import filmes, listaGeneros
from graph import Grafos

def preecherAresta(listaFilme, grafo):
    for i in range(0, len(listaFilme)):
        if(i < 5):
            grafo.adj['acao'].append(listaFilme[i])
        elif(i < 10):
            grafo.adj['comedia'].append(listaFilme[i])
        elif(i < 15):
            grafo.adj['terror'].append(listaFilme[i])
        elif(i < 20):
            grafo.adj['suspense'].append(listaFilme[i])
        elif(i < 25):
            grafo.adj['ficcao'].append(listaFilme[i])
        elif(i < 30):
            grafo.adj['romance'].append(listaFilme[i])

if __name__ == '__main__':
    user = []
    reccomendationVector = []
    operacao = True
    grafo = Grafos(len(listaGeneros), listaGeneros)
    preecherAresta(filmes, grafo)
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
            user.append(filmeAdd)
        elif opc.upper().strip() == 'L':
            for filme in filmes:
                print(filme)
        elif opc.upper().strip() == 'R':
            print('>>> Listar Recomendacoes')
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
            user.remove(filmeDelete)
        elif opc.upper().strip() == 'F':
            print('>>> Terminando operacao')
            operacao = False
        else:
            print(f'>>> Digitou errado: {opc}')
    print('ola mundo')