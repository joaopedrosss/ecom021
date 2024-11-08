from DB.livros.DB_livro import DataBaseLivro

obj = DataBaseLivro()

"""
obj.setLivro("{'Nome':'Joon','Sobrenome':'Park','Email':'jo','Titulo':'Carro Esportivo','Autor':'Desconhecido','Ano':'2020','Editora':'Editora ABC','Edicao':'1','Preco':'35000','Genero':'Esportivo','Paginas':'200','Descricao':'Carro rapido e confortavel','Novo':'True','Foto':'capa.jpg'}")
"""
obj.path = "DB\\livros\\Data_livro.json"
obj.setLivro('{"Nome":"T5","Sobrenome":"Pdededrk","Email":"jo","Titulo":"Carro Esportivo","Autor":"Desconhecido","Ano":"2020","Editora":"Editordedadwd ABC","Edicao":"1","Preco":"35000","Genero":"Esportivo","Paginas":"200","Descricao":"Carro rapido e confortavel","Novo":"True","Foto":"capa.jpg"}')
