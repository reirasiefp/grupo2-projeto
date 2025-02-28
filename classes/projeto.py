class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.lista_membros = []
        self.lista_tarefas = []
        
        #0 = em progresso // 1 = concluido
        self.status = 0