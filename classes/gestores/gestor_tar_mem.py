from classes.gestores.gestor_membros import Gestor_Membros
from classes.gestores.gestor_tarefas import Gestor_Tarefas
from classes.relações.tarefa_membro import Tarefa_Membro

class Gestor_Tar_Mem:
    def __init__(self, ficheiro):
        self.ficheiro = ficheiro
        self.registros = self.carregar_ficheiro()

    def guardar_registro(self, registro):
        self.registros.append(registro)
        self._guardar_no_ficheiro()
        
    def carregar_ficheiro(self):
        try:
            with open(self.ficheiro, "r") as f:
                return [Tarefa_Membro.from_string(linha) for linha in f.readlines()]
        except FileNotFoundError:
            return []

    def _guardar_no_ficheiro(self):
         with open(self.ficheiro, "w") as f:
            for registro in self.registros:
                f.write(registro.to_string() + "\n")

    def ver_todos_membros_by_tarefaId(self,tarefa_id):
        gestorMembros = Gestor_Membros("ficheiros/membros.csv")
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()
        
        for linhas in linhas:
            id_tarefa, email = linhas.strip().split(",")
            if id_tarefa == tarefa_id:
                print(gestorMembros.get_membro_by_email(email))

    def ver_todas_tarefas_by_email(self,mail):
        gestorTarefas = Gestor_Tarefas("ficheiros/tarefas.csv")
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()
        
        for linhas in linhas:
            id_tarefa, email = linhas.strip().split(",")
            if email == mail:
                print(gestorTarefas.get_tarefa_by_id(id_tarefa))