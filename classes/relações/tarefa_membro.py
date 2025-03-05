class Tarefa_Membro:
    def __init__(self, id_tarefa, email_membro):
        self.id_tarefa = id_tarefa
        self.email_membro = email_membro

    def to_string(self):
        return f"{self.id_tarefa},{self.email_membro}"

    def from_string(string):
        id, email = string.strip().split(",")
        return Tarefa_Membro(int(id),email)