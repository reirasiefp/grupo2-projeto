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
    

