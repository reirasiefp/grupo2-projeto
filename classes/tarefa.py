from datetime import date, datetime

class Tarefa:

    def __init__(self, nome, prioridade, tipo, data_fim):
        self.nome = nome
        self.prioridade = prioridade
        self.membros = []
        self.tipo = tipo
        #0 = em progresso // 1 = concluido
        self.status = 0
        self.data_inicio = date.today()
        self.data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()

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
    
    def verificarStatus(self):
        if self.status == 0:
            return "Em progresso"
        else:
            return "Concluída"
        
    def __str__(self):
        return f"Nome: {self.nome}\nPrioridade: {self.prioridade} // Estado: {self.verificarStatus()}\nData Inicio: {self.data_inicio} // Data Fim: {self.data_fim}"