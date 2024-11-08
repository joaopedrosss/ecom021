
"""
{
"Nome":"João",
"Sobrenome":"Matheus",
"Email": "a@gmail.com",
"Password": "8989w"
}
"""

"""
import json
import smtplib
from email.message import EmailMessage
from model.user import User

"""
{
"Nome":"João",
"Sobrenome":"Matheus",
"Email": "a@gmail.com",
"Password": "8989w"
}


class DataBaseUser:
    def __init__(self):
        self.path = "UserData.json"
        self.addressEmail = "projetosoft24@gmail.com"
        self.passwordEmail = "tblgioxnsitoeaig"

    def setUser(self,data): # SÓ PRECISA DESSE CARA AQUI
        with open(self.path) as file:
            listFile = json.load(file)
        listFile.append(self.setJson(data))
        with open(self.path,"w") as file:
            json.dump(listFile, file)

    def setJson(self,data): #USAR ISSO ARA
        Lista = []
        size = len(data)
        data = data[1:size-1]

        """
        "Zahav"
          "Alkmir" 
         "al@gmail"
        "Titulo","O caminho para vencer",
        "Autor":"Desconhecido",
        "Ano":"2020",
        "Editora":"Editordedadwd ABC"

        """
        
        data = data.split(',')
        for dt in data:
            dt = dt.split(':')[-1]
            s = len(dt)
            dt = dt[1:s-1]
            Lista.append(dt)
        Obj = {
            "Nome": Lista[0], 
            "Sobrenome": Lista[1], 
            "Email": Lista[2], 
            "Celular": Lista[3], 
            "Password": Lista[4]
        }
        
        OBJ = {
            "Nome":"João",
            "Sobrenome":"Matheus",
            "Email": "a@gmail.com",
            "Password": "8989w"
            }
        return Obj

