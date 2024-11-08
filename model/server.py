import socket 
from threading import Thread

from DB.livros.DB_livro import DataBaseLivro

#socket: module that allows PC comunications in a network; a socket is a endpoint that receive and sends dat;in general, there is a *server sokect*, athat receives e servers requests, and a *client socket* (in this case, our site), that sends resquets.

# a classe Thread, do módulo threading, permite você executar várias tarefas ao mesmo tempo (importante num servidor Web)

class Server():
    def __init__(self, serve_nome,server_address,server_port):
        self.serve_nome = serve_nome
        self.server_address = server_address
        self.server_port = server_port
        self.server_socket = ''

    def start(self): # inicializar o socket do servidor
        print("Sever {} is open and running! Adress:{} Port:{}".format(self.serve_nome,self.server_address,self.server_port))
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        #crie o socket do servidor, de forma que ele use o endreçamento do ipv4 e o use o protocolo TCP/IP
        self.server_socket.bind((self.server_address,self.server_port))
         # o soekcet terá esse endereço (ex.: 0.0.0.0, endereço do servidro) e escutara essa porta (ex.:800,server_port)

        self.server_socket.listen(10) #começa a receber conexões; 10 no máximo
        self.active() 
        #self.active() -> permitir o multihtreading (a execução de várias tarefas ao mesmo tempo) dos processos do socket do servidor, que no caso seram 'methodGET' (ouvir uma requisção) e 'methodPOST' (servir uma requisição)

    def active(self):
        while True: #esteja sempre pronto para ouvir(GET) e servir (POST) uma requisição; para cada nova requisição/conexão, faça uma nova thread só para ela.
            client_socket, client_address = self.server_socket.accept() 
            # espere até ter uma conexão com um cliente. Quando isso acontecer, 'client_socket' recebe o socket do clinte e 'client_address' o endereço do cliente
            
            Thread(target=self.process,args=(client_socket,client_address)).start() 
            # execute tal ação com multihtreading; cire uma htread só para o processo do cliente, no caso 'process', cujos argumentos são 'client_socket' e 'client_address'
    
    def process(self,client_socket,client_address):
        client_data = client_socket.recv(1024) #espere até receber um pacote de 1024 bytes de dados
        client_data = client_data.decode() # converta esses bytes num string

        print("Requisição {} do cliente de endereço {}\nG:get\nP:post".format(client_data[0],client_address))

        if client_data.startswith("GET"):
            self.methodGET(client_data,client_socket)
        elif client_data.startswith("POST"):
            print("RESQUISIÇÃO POST")
            print("----------")
            print(client_data)
            print("-----")

        
            self.methodPOST(client_data,client_socket)

    def methodPOST(self,client_data,client_socket):
        
        headerPOST = client_data.split('\r\n')[0] #PEGUE O HEADER
        bodyPOST = client_data.split('\r\n')[-1] # pegue o body da requisição
        print("--- REQUEST ----")
        print(client_data.split('\r\n'))
        print("header:",headerPOST,"\n")
        print("body:",bodyPOST,"\n")
        
        try:
            path = self.get_request_path_POST(headerPOST)
            print("action:",path)
            if path == "setLivro":
                print("Inserindo livro no banco de dados...")
                livro_db = DataBaseLivro()

                livro_db.path = "DB\\livros\\Data_livro.json"
                
                livro_db.setLivro(bodyPOST) #CONSERTAR ISSO.
                print("Livro inserido com sucesso!")
                client_socket.sendall(b'HTTP/1.1 201 OK\r\n\r\nSucesso')
                 #mande uma resposta ao client. e mande tudo TUDO. 
                 #mande na forma de bytes - (b'')
            """
            if path == 'setUser': # IMPLEMENTAR ISSO
                db = DataBaseUser()

                db.path = "DB\\users\\UserData.json"

                db.setUser(data)
                print('Usuário setado com Sucesso!')                
                socketClient.sendall(b'HTTP/1.1 201 OK\r\n\r\nSucesso')
            
            """


            client_socket.close()
    
        except:
            client_socket.sendall(b'HTTP/1.1 404 File not found\r\n\r\nErro 404') # algo deu errado!
            return
            

    def get_request_path_POST(self,header):
        action = header.split(' ')[1][1:] # tá,uma requisição POST. mas o que ela deseja? (um setLivro, set Usario)? 
        return action

        """
            ex.:
            POST /test HTTP/1.1
            Host: example.com
            Content-Type: multipart/form-data;boundary="delimiter12345"

            --delimiter12345
        """


    def methodGET(self,client_data,client_socket):
        pass
