from classes.projeto import Projeto


class Gestor_Projetos:
    def __init__(self, ficheiro):
        self.ficheiro = ficheiro
    
    def gerar_novo_id(self):
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()

        if not linhas:
            return 1
        
        ids = [int(linha.split(",")[0]) for linha in linhas if linha.strip()]
        return max(ids) + 1 if ids else 1
    
    def guardar_ficheiro(self, projeto):
        with open(self.ficheiro, "a") as f:
            f.write(projeto.to_string() + "\n")
        print("Projeto adicionado com sucesso")
        return True
    
    #opção:
    # 0 = todos, 1 = em progresso, 2 = concluídos
    def ver_todos_projetos(self, opcao = 0):
        with open(self.ficheiro, "r") as f:
            linhas = f.readlines()
        
        for linhas in linhas:
            id, nome, data_inicio, estado = linhas.strip().split(",")
            if opcao == 0:
                print(f"ID: {id}, Nome: {nome}, Data Inicio: {data_inicio}, Status: {'Em progresso' if estado == '0' else 'Concluido'}")
            elif opcao == 1:
                if estado == '0':
                    print(f"ID: {id}, Nome: {nome}, Data Inicio: {data_inicio}, Status: Em progresso")
            else:
                if estado == '1':
                    print(f"ID: {id}, Nome: {nome}, Data Inicio: {data_inicio}, Status: Concluido")


    def get_projeto_by_id(self, id_projeto):
        with open(self.ficheiro, "r") as f:

            linhas = f.readlines()

            for linha in linhas:
                id, nome, data_inicio, estado = linha.strip().split(",")
                if id == str(id_projeto):
                    return Projeto(nome, None, id, data_inicio, estado)
        return None
    