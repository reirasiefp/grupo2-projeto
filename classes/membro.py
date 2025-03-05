class Membro:
    def __init__(self, nome, email, funcao):
        self.nome = nome
        self.email = email
        self.funcao = funcao

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_email(self, novo_email):
        self.email = novo_email
    
    def alterar_funcao(self, nova_funcao):
        self.funcao = nova_funcao

    def to_string(self):
        return f"{self.nome},{self.email},{self.funcao}"
    
    def from_string(membro_string):
        nome, email, funcao = membro_string.strip().split(",")
        return Membro(nome, email, funcao)

    
