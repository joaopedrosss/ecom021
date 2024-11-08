from model.server import Server

serverLivrosAqui = Server("Livros Aqui","0.0.0.0",80)
serverLivrosAqui.start()

"""
REQUISIÇÃO
{"Nome":"POetr","Sobrenome":"Pdededrk","Email":"jo","Titulo":"Carro Esportivo","Autor":"Desconhecido","Ano":"2020","Editora":"Editoradwd ABC","Edicao":"1","Preco":"35000","Genero":"Esportivo","Paginas":"200","Descricao":"Carro rapido e confortavel","Novo":"True","Foto":"capa.jpg"}

"""