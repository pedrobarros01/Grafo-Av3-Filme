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

def preecherArestaLista(listaFilme, listaDeGenero, lista):
    for i in range(0, len(listaFilme)):
        tupla = ()
        if(i < 5):
            verticeGenero = procurarPorGenero(listaDeGenero, 'acao')
            tupla = (verticeGenero.id, listaFilme[i].id)
            lista.append(tupla)
        elif(i < 10):
            verticeGenero = procurarPorGenero(listaDeGenero, 'comedia')
            tupla = (verticeGenero.id, listaFilme[i].id)
            lista.append(tupla)
        elif(i < 15):
            verticeGenero = procurarPorGenero(listaDeGenero, 'terror')
            tupla = (verticeGenero.id, listaFilme[i].id)
            lista.append(tupla)
        elif(i < 20):
            verticeGenero = procurarPorGenero(listaDeGenero, 'suspense')
            tupla = (verticeGenero.id, listaFilme[i].id)
            lista.append(tupla)
        elif(i < 25):
            verticeGenero = procurarPorGenero(listaDeGenero, 'ficcao')
            tupla = (verticeGenero.id, listaFilme[i].id)
            lista.append(tupla)
        elif(i < 30):
            verticeGenero = procurarPorGenero(listaDeGenero, 'romance')
            tupla = (verticeGenero.id, listaFilme[i].id)
            lista.append(tupla)