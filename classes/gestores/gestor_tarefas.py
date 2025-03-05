class Gestor_Tarefas:
    def __init__(self, ficheiro):
        self.ficheiro = ficheiro
    
    def gerar_novo_id(self):
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()

        if not linhas:
            return 1
        
        ids = [int(linha.split(";")[0]) for linha in linhas if linha.strip()]
        return max(ids) + 1 if ids else 1
    
    def guardar_ficheiro(self, tarefa):
        with open(self.ficheiro, "a") as f:
            f.write(tarefa.to_string() + "\n")
        print("Tarefa adicionada com sucesso")
        return True
    
    #opção:
    # 0 = todos, 1 = em progresso, 2 = concluídos
    def ver_todas_tarefas(self, opcao = 0):
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()
        
        for linhas in linhas:
            id, nome, prioridade, tipo, data_inicio, data_fim, estado = linhas.strip().split(";")
            if opcao == 0:
                print(f"ID: {id}, Nome: {nome}, Tipo: {tipo}, Prioridade: {prioridade}, Data Inicio: {data_inicio}, Data Fim: {data_fim}, Status: {'Em progresso' if estado == '0' else 'Concluido'}")
            elif opcao == 1:
                if estado == '0':
                    print(f"ID: {id}, Nome: {nome}, Tipo: {tipo}, Prioridade: {prioridade}, Data Inicio: {data_inicio}, Data Fim: {data_fim}, Status: Em progresso")
            else:
                if estado == '1':
                    print(f"ID: {id}, Nome: {nome}, Tipo: {tipo}, Prioridade: {prioridade}, Data Inicio: {data_inicio}, Data Fim: {data_fim}, Status: Concluido")
            