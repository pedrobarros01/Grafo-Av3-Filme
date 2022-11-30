
from filme import Filme
FILME = 1
GENERO = 0
id = 0
filmes = []
arestas = []
listaGeneros = []
# Generos 
genero = Filme("genero", "genero", GENERO)
genero.id = id
listaGeneros.append(genero)

acao = Filme("acao", "acao", GENERO)
id += 1
acao.id = id
listaGeneros.append(acao)

comedia = Filme("comedia", "comedia", GENERO)
id += 1
comedia.id = id
listaGeneros.append(comedia)

ficcao = Filme("ficcao", "ficcao", GENERO)
id += 1
ficcao.id = id
listaGeneros.append(ficcao)

terror = Filme("terror", "terror", GENERO)
id += 1
terror.id = id
listaGeneros.append(terror)

suspense = Filme("suspense", "suspense", GENERO)
id += 1
suspense.id = id
listaGeneros.append(suspense)

romance = Filme("romance", "romance", GENERO)
id += 1
romance.id = id
listaGeneros.append(romance)


# Filmes
filme1 = Filme("drive(2011)", "acao", FILME)
id += 1
filme1.id = id
filmes.append(filme1)

filme2 = Filme("truque de mestre", "acao", FILME)
id += 1
filme2.id = id
filmes.append(filme2)

filme3 = Filme("vingadores", "acao", FILME)
id += 1
filme3.id = id
filmes.append(filme3)

filme4 = Filme("morbius", "acao", FILME)
id += 1
filme4.id = id
filmes.append(filme4)
filme5 = Filme("trem-bala", "acao", FILME)
id += 1
filme5.id = id
filmes.append(filme5)

filme6 = Filme("se beber nao case", "comedia", FILME)
id += 1
filme6.id = id
filmes.append(filme6)

filme7 = Filme("minions", "comedia", FILME)
id += 1
filme7.id = id
filmes.append(filme7)

filme8 = Filme("meu malvado favorito 2", "comedia", FILME)
id += 1
filme8.id = id
filmes.append(filme8)

filme9 = Filme("luck", "comedia", FILME)
id += 1
filme9.id = id
filmes.append(filme9)

filme10 = Filme("cidade perdida", "comedia", FILME)
id += 1
filme10.id = id
filmes.append(filme10)
filme11 = Filme("jogos mortais", "terror", FILME)
id += 1
filme11.id = id
filmes.append(filme11)

filme12 = Filme("a freira", "terror", FILME)
id += 1
filme12.id = id
filmes.append(filme12)

filme13 = Filme("invocacao do mal", "terror", FILME)
id += 1
filme13.id = id
filmes.append(filme13)

filme14 = Filme("a avo", "terror", FILME)
id += 1
filme14.id = id
filmes.append(filme14)

filme15 = Filme("tempo", "terror", FILME)
id += 1
filme15.id = id
filmes.append(filme15)

filme16 = Filme("se7en", "suspense", FILME)
id += 1
filme16.id = id
filmes.append(filme16)

filme17 = Filme("aguas profundas", "suspense", FILME)
id += 1
filme17.id = id
filmes.append(filme17)
filme18 = Filme("o telefone preto", "suspense", FILME)
id += 1
filme18.id = id
filmes.append(filme18)

filme19 = Filme("a fera", "suspense", FILME)
id += 1
filme19.id = id
filmes.append(filme19)

filme20 = Filme("voce pertence a mim", "suspense", FILME)
id += 1
filme20.id = id
filmes.append(filme20)

filme21 = Filme("interstellar", "ficcao", FILME)
id += 1
filme21.id = id
filmes.append(filme21)

filme22 = Filme("matrix", "ficcao", FILME)
id += 1
filme22.id = id
filmes.append(filme22)

filme23 = Filme("inception", "ficcao", FILME)
id += 1
filme23.id = id
filmes.append(filme23)

filme24 = Filme("a origem", "ficcao", FILME)
id += 1
filme24.id = id
filmes.append(filme24)

filme25 = Filme("perdido em marte", "ficcao", FILME)
id += 1
filme25.id = id
filmes.append(filme25)


filme26 = Filme("o melhor de mim", "romance", FILME)
id += 1
filme26.id = id
filmes.append(filme26)

filme27 = Filme("diario de uma paixao", "romance", FILME)
id += 1
filme27.id = id
filmes.append(filme27)


filme28 = Filme("365 dias", "romance", FILME)
id += 1
filme28.id = id
filmes.append(filme28)


filme29 = Filme("atraves da minha janela", "romance", FILME)
id += 1
filme29.id = id
filmes.append(filme29)

filme30 = Filme("espontanea", "romance", FILME)
id += 1
filme30.id = id
filmes.append(filme30)


