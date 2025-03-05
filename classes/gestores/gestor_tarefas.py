import csv

from classes.tarefa import Tarefa

class Gestor_Tarefas:
    def __init__(self, ficheiro):
        self.ficheiro = ficheiro

    def gerar_novo_id(self):
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()

        if not linhas:
            return 1
        
        ids = [int(linha.split(",")[0]) for linha in linhas if linha.strip()]
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
            id, nome, prioridade, tipo, data_inicio, data_fim, estado, id_projeto = linhas.strip().split(",")
            if opcao == 0:
                print(f"ID: {id}, Nome: {nome}, Tipo: {tipo}, Prioridade: {prioridade}, Data Inicio: {data_inicio}, Data Fim: {data_fim}, Status: {'Em progresso' if estado == '0' else 'Concluido'}, Id Projeto: {id_projeto}")
            elif opcao == 1:
                if estado == '0':
                    print(f"ID: {id}, Nome: {nome}, Tipo: {tipo}, Prioridade: {prioridade}, Data Inicio: {data_inicio}, Data Fim: {data_fim}, Status: Em progresso, Id Projeto: {id_projeto}")
            else:
                if estado == '1':
                    print(f"ID: {id}, Nome: {nome}, Tipo: {tipo}, Prioridade: {prioridade}, Data Inicio: {data_inicio}, Data Fim: {data_fim}, Status: Concluido, Id Projeto: {id_projeto}")


    def listar_tarefas_projeto(self, id_projeto):
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()
        
        for linhas in linhas:
            id, nome, prioridade, tipo, data_inicio, data_fim, estado, id_proj = linhas.strip().split(",")
            if str(id_projeto) == id_proj:
                print(f"ID: {id}, Nome: {nome}, Tipo: {tipo}, Prioridade: {prioridade}, Data Inicio: {data_inicio}, Data Fim: {data_fim}, Status: {'Em progresso' if estado == '0' else 'Concluido'}")
 

    def concluir_tarefa(self, id_tarefa):
        tarefas = []
        tarefa_encontrada = False
        
        with open(self.ficheiro, "r") as f:
            leitor_csv = csv.reader(f)
            for linha in leitor_csv:
                if int(linha[0]) == id_tarefa:
                    linha[6] = '1'
                    tarefa_encontrada = True
                tarefas.append(linha)
        
        if not tarefa_encontrada:
            print(f"Tarefa com ID {id_tarefa} não encontrada.")
            return
        
        with open(self.ficheiro, "w", newline='') as f:
            escrita_csv = csv.writer(f)
            escrita_csv.writerows(tarefas)
        
        print("Estado da tarefa foi atualizado!")

    def get_tarefa_by_id(self, id_tarefa):
        with open(self.ficheiro, "r") as f:

            linhas = f.readlines()

            for linha in linhas:
                id, nome, prioridade, tipo, data_inicio, data_fim, estado, id_proj = linha.strip().split(",")
                if id == str(id_tarefa):
                    return Tarefa(nome,prioridade,tipo,data_fim,id_proj,None,id,data_inicio,estado)
        return None