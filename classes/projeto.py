from datetime import date

from classes.gestores.gestor_projetos import Gestor_Projetos


class Projeto:

    def __init__(self, nome, gestor, id = None,data_inicio = None, status = None):

        if id is not None:
            self.id = id
        else:
            self.id = gestor.gerar_novo_id()

        self.nome = nome
        self.lista_membros = []
        self.lista_tarefas = []

        if data_inicio is not None:
            self.data_inicio = data_inicio
        else:
            self.data_inicio = date.today()

        #0 = em progresso // 1 = concluido
        if status is not None:
            self.status = status
        else:
            self.status = 0


    def adicionar_membros (self, membro):
        self.lista_membros.append(membro)

    def adicionar_tarefa(self, tarefa):
        self.lista_tarefas.append(tarefa)
    
    def tarefas_por_status(self, status):
        return [tarefa for tarefa in self.lista_tarefas if tarefa.status == status]
    
    #confirmar not sure se faz sentido e como a prioridade é definida
    def listar_tarefas_por_prioridade(self, prioridade):
        return [tarefa for tarefa in self.lista_tarefas if tarefa.prioridade == 10]
    
    #confirmar not sure
    def tarefas_por_responsavel(self, membro):
        return [tarefa for tarefa in self.lista_tarefas if tarefa.responsavel == membro]

    def produtividade(self):
        tarefas_concluidas = [tarefa for tarefa in self.lista_tarefas if tarefa.status == '1']
        return len(tarefas_concluidas) / len(self.lista_tarefas) * 100 if self.lista_tarefas else 0
    
    def terminar_projeto(self):
        if self.status == 1:
            print("Este Projeto já foi concluido!")
        else:
            print("Projeto concluido")
    
    def to_string(self):
        return f"{self.id};{self.nome};{self.data_inicio};{self.status}"
    
    def from_string(projeto_string):
        id, nome, data_inicio, status = projeto_string.strip().split(";")
        return Projeto(nome, None, id, data_inicio, status)

