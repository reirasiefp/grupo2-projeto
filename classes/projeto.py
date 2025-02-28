class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.lista_membros = []
        self.lista_tarefas = []
        
        #0 = em progresso // 1 = concluido
        # self.status = 0



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
    
    
    

