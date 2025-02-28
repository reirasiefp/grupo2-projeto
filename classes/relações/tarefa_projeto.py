class Tarefa_Projeto:
    def __init__(self, id_tarefa, id_projeto):
        self.id_tarefa = id_tarefa
        self.id_projeto = id_projeto

    def to_string(self):
        return f"{self.id_tarefa};{self.id_projeto}"
    
    def from_string(string):
        idTarefa, idProjeto = string.strip().split(";")
        return Tarefa_Projeto(int(idTarefa),int(idProjeto))
