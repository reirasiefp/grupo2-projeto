class Projeto_Membro:
    def __init__(self, id_projeto, email_membro):
        self.id_projeto = id_projeto
        self.email_membro = email_membro

    def to_string(self):
        return f"{self.id_projeto},{self.email_membro}"

    def from_string(string):
        id, email = string.strip().split(",")
        return Projeto_Membro(int(id),email)