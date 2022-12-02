import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Criei o vinculo com a classe conexão
        self.db_connection = self.db_connection.conectar()#Conecto ao banco de dados
        self.con = self.db_connection.cursor()#Navega no meu banco
  
#abaixo é o diario
    def inserir(self,  conteudo):
        try:
            sql = "Insert into diario(codi, conteudo) values('','{}')".format(conteudo)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def consultar(self, codi):
        try:
            sql = "select * from diario where cod ='{}'".format(codi)
            self.con.execute(sql)
            msg = ""
            
            for(conteudo) in self.con:
                msg = msg + "\nCódigo: {}, Conteúdo: {}".format(conteudo, codi)
            return msg
        except Exception as erro:
            return erro
        
    def atualizar(self, codi, campo, novoDado):
        try:
            sql = "update diario set {} = '{}' where cod = '{}'".format(campo, novoDado, codi)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def excluir(self, codi):
        try:
            sql = "delete from diario where cod = '{}'".format(codi)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(codi) 
        except Exception as erro:
            return erro
        #abaixo é usuario        
    def cad(self, email, usuario, senha, telefone):
        try:
            sql = "Insert into cadastro(cod, email, usuario, senha, telefone) values('','{}','{}','{}','{}')".format(email, usuario, senha, telefone)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def loginInsert(self, email, senha, emailInput, senhaInput):
        try:
            sql = 'select * from cadastro'
            self.con.execute(sql)
            for (cod, email, senha) in self.con:
                if email and senha == emailInput and senhaInput:
                    return True
            else:
                print('\nUsuário ou senha incorretos!')
            return False
        except Exception as erro:
            return erro
        
    def loginValid(self, email, senha, emailInput, senhaInput):
        try:
            if self.loginInsert(email, senha, emailInput, senhaInput) == True:
                print('Logado com Sucesso !')
                print('\n')
            else:
                print('Login e Senha incorretos!')
                print('\n')
                return False
        except Exception as erro:
            return erro
            
            