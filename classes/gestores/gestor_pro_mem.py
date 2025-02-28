from classes.relações.projeto_membro import Projeto_Membro

class Gestor_Pro_Mem:
    def __init__(self, ficheiro):
        self.ficheiro = ficheiro
        self.registros = self.carregar_ficheiro()

    def guardar_registro(self, registro):
        self.registros.append(registro)
        self._guardar_no_ficheiro()
        
    def carregar_ficheiro(self):
        try:
            with open(self.ficheiro, "r") as f:
                return [Projeto_Membro.from_string(linha) for linha in f.readlines()]
        except FileNotFoundError:
            return []

    def _guardar_no_ficheiro(self):
         with open(self.ficheiro, "w") as f:
            for registro in self.registros:
                f.write(registro.to_string() + "\n")
    
    def procurar_por_id(self, id):
        # Buscar todos os registros com o mesmo id de projeto
        return [registro for registro in self.registros if registro.id_projeto == id]
    
    def procurar_por_email(self, email):
        # Buscar todos os registros com o mesmo email
        return [registro for registro in self.registros if registro.email_membro == email]