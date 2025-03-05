import re

from classes.gestores.gestor_membros import Gestor_Membros
from classes.relações.tarefa_membro import Tarefa_Membro
from classes.tarefa import Tarefa

def validar_data(data):
    padrao = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(padrao, data))

def validar_prioridade(num):
    return 1 <= num <= 9

def adicionar_tarefa(gestorTarefa):
    print("="*30)
    nome = input("Insira o nome da tarefa: ")

    while True:
        try:
            prioridade = int(input("Prioridade (1-9): "))
            if validar_prioridade(prioridade):
                break
            else:
                print("Valor para a prioridade incorrecto!")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro. (1-9)!")

    tipo = input("Tipo da tarefa: ")

    while True:
        data_fim = input("Data de fim (formato YYYY-MM-DD): ")
        if validar_data(data_fim):
            break
        else:
            print("Formato de data inválido")
    
    id_projeto = input("Id do projeto que quer adicionar a tarefa: ")
    
    tarefaNova = Tarefa(nome,prioridade,tipo,data_fim,id_projeto,gestorTarefa)
    gestorTarefa.guardar_ficheiro(tarefaNova)
    return tarefaNova

def associar_tarefa_membro(gestorTarMem, id_tarefa):
    gestorMembros = Gestor_Membros("ficheiros/membros.csv")
    
    email = input("Insira o email do membro: ")

    membro = gestorMembros.get_membro_by_email(email)

    if membro is None:
        print("Membro não encontrado!")
    else:
        tarefa_membro = Tarefa_Membro(id_tarefa,membro.email)
        gestorTarMem.guardar_registro(tarefa_membro)

    

