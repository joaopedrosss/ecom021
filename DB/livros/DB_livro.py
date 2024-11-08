import json

class DataBaseLivro:
    def __init__(self):
        self.path = "Data_livro.json"

    def setLivro(self, dict_data):
        with open(self.path) as file:
            lista_de_livros = json.load(file) # gets thecontent of the file and put that on a lista
        
        lista_de_livros.append(self.setJson(dict_data)) #take the list and converts to a object adn appends it to the list

        with open(self.path,"w") as file:
            json.dump(lista_de_livros, file)

    def setJson(self,dict_data): #gets a 'dict_data', a set of key:value items. like {"model":"bmw","year":1902} in, now, a STRING format.

    
    #example:
    #    "{'Nome':'John','Sobrenome':'Doe','Email':'john.doe@example.com','Titulo':'Carro Esportivo','Descricao':'Carro rápido e confortável'}"

    
        lista = []
        lista_len = len(lista)

        dict_data = dict_data[1:lista_len-1] #removes outer brackets
        dict_data = dict_data.split(",")

        for data in dict_data:
            data = data.split(":")[-1] # take the value of the key:value pair

            data = data[1:len(data)-1] #remove enclosing quotes(?) ; MUDAR ISSO (?)

            lista.append(data)

        print(lista) # tá tudo certo?

        obj = {
            "Nome": lista[0], #default: Joon
            "Sobrenome": lista[1], #default: Park
            "Email":lista[2], #default: jo
            "Titulo": lista[3],
            "Autor": lista[4],
            "Ano": lista[5],
            "Editora": lista[6],
            "Edicao": lista[7],
            "Preco": lista[8],
            "Genero": lista[9],
            "Paginas": lista[10],
            "Descricao": lista[11],
            "Novo": lista[12],
            "Foto": lista[13] 
            #adicionar um atributo id: mudar isso (?)
        }

        return obj
