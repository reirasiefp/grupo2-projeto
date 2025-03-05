from classes.membro import Membro


class Gestor_Membros:
    def __init__(self, ficheiro):
        self.ficheiro = ficheiro
    
    def email_exists(self, email):
        with open(self.ficheiro, "r") as f:
            for line in f:
                _, existing_email, _ = line.strip().split(",")
                if existing_email == email:
                    return True
        return False
    
    def add_member(self, membro):
        if self.email_exists(membro.email):
            print("Este email já foi adicionado no sistema.")
            return False
        with open(self.ficheiro, "a") as f:
            f.write(membro.to_string() + "\n")
        print("Membro adicionado com sucesso!")
        return True
    
    def ver_todos_membros(self):
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()
        
        for linhas in linhas:
            nome, email, funcao = linhas.strip().split(",")
            print(f"Nome: {nome}, Email: {email}, Função: {funcao}")
    
    def get_membro_by_email(self, mail):
        with open(self.ficheiro, "r") as f:

            linhas = f.readlines()

            for linha in linhas:
                nome, email, funcao = linha.strip().split(",")
                if email == str(mail):
                    return Membro(nome, email, funcao)
        return None
    

