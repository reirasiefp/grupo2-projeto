from datetime import date, datetime

class Tarefa:

    def __init__(self, nome, prioridade, tipo, data_fim, id_projeto, gestor, id = None, data_inicio = None, status = None):
        
        if id is not None:
            self.id = id
        else:
            self.id = gestor.gerar_novo_id()
        
        self.nome = nome
        self.prioridade = prioridade
        self.membros = []
        self.tipo = tipo
        #0 = em progresso // 1 = concluido
        if status is not None:
            self.status = status
        else:
            self.status = 0
        
        if data_inicio is not None:
            self.data_inicio = data_inicio
        else:
            self.data_inicio = date.today()

        self.data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()

        self.id_projeto = id_projeto
    

    def setPrioridade(self, nova_prioridade):
        if 1 <= nova_prioridade <= 10:
            self.prioridade = nova_prioridade
            print("Prioridade atualizada!")
        else:
            print("Valor para a prioridade incorrecto")

    def setDataFim(self, data_fim):
        datatmp = datetime.strptime(data_fim, "%Y-%m-%d").date()
        if datatmp > date.today():
            self.data_fim = datatmp
            print(f"Data para finalizar a tarefa foi actualizada para {self.data_fim}!")
        else:
            print("Data inválida!")

    def terminar_tarefa(self):
        if self.status == 0:
            self.status = 1
            print("Tarefa terminada!")
        else:
            print("Tarefa já foi concluida!")
    
    def adicionar_membro(self, membro):
        emails = [membro.email for membro in self.membros]
        if membro.email in emails:
            print(f"Tarefa já tinha sido atribuida ao {membro.nome}")
        else:
            self.membros.append(membro)
            print(f"Tarefa atribuida ao {membro.nome}")
    
    def verListaMembros(self):
        print("Lista de membros:") 
        for membro in self.membros:
            print(f"Nome: {membro.nome}, Email: {membro.email}")

    def to_string(self):
        return f"{self.id},{self.nome},{self.prioridade},{self.tipo},{self.data_inicio},{self.data_fim},{self.status},{self.id_projeto}"
    
    def from_string(tarefa_string):
        id, nome, prioridade, tipo, data_inicio, data_fim, status, id_projeto = tarefa_string.strip().split(",")
        return Tarefa(nome, prioridade, tipo, data_fim, id_projeto, None, id, data_inicio, status)

    def __str__(self):
        return f"Id: {self.id} Nome: {self.nome}\nPrioridade: {self.prioridade}\nData Inicio: {self.data_inicio} // Data Fim: {self.data_fim}"
