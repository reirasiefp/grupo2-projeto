from datetime import date

class Tarefa:

    def __init__(self, nome, prioridade, tipo, data_fim):
        self.nome = nome
        self.prioridade = prioridade
        self.membros = []
        self.tipo = tipo

        #0 = em progresso // 1 = concluido
        self.status = 0

        self.data_inicio = date.today()
        self.data_fim = data_fim

    def __str__(self):
        return f"Data Inicio: {self.data_inicio}"