from classes.relações.tarefa_projeto import Tarefa_Projeto

class Gestor_Tar_Pro:
    def __init__(self, ficheiro):
        self.ficheiro = ficheiro
        self.registros = self.carregar_ficheiro()

    def guardar_registro(self, registro):
        self.registros.append(registro)
        self._guardar_no_ficheiro()
        
    def carregar_ficheiro(self):
        try:
            with open(self.ficheiro, "r") as f:
                return [Tarefa_Projeto.from_string(linha) for linha in f.readlines()]
        except FileNotFoundError:
            return []

    def _guardar_no_ficheiro(self):
         with open(self.ficheiro, "w") as f:
            for registro in self.registros:
                f.write(registro.to_string() + "\n")
    
    def procurar_por_id_tarefa(self, id):
        # Buscar todos os registros com o mesmo id tarefa
        return [registro for registro in self.registros if registro.id_tarefa == id]
    
    def procurar_por_id_projeto(self, id):
        # Buscar todos os registros com o mesmo id projeto
        return [registro for registro in self.registros if registro.id_projeto == id]