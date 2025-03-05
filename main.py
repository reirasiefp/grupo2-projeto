from classes.gestores.gestor_membros import Gestor_Membros
from classes.gestores.gestor_projetos import Gestor_Projetos
from classes.gestores.gestor_tar_mem import Gestor_Tar_Mem
from classes.gestores.gestor_tarefas import Gestor_Tarefas
import funcoes_main


def listagemProjetos(gestorProjetos):
    while True:
        print("\n============= Listar Projetos =============")
        print("1 - Listar todos os Projetos")
        print("2 - Listar Projetos em progresso")
        print("3 - Listar Projetos concluidos")
        print("0 - Voltar")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            print("="*30)
            print("Lista de todos os projetos:")
            gestorProjetos.ver_todos_projetos()
            
        elif escolha == "2":
            print("="*30)
            print("Lista dos projetos em progresso:")
            gestorProjetos.ver_todos_projetos(1)
            print("="*30)
        elif escolha == "3":
            print("="*30)
            print("Lista dos projetos concluidos:")
            gestorProjetos.ver_todos_projetos(2)
            print("="*30)
        elif escolha == "0":
            print("="*30)
            print("A sair do menu...")
            print("="*30)
            break
        else:
            print("Opção inválida, tente novamente.")

def submenuProjetos():
    gestorProjetos = Gestor_Projetos("ficheiros/projetos.csv")
    while True:
        print("\n============= Projetos =============")
        print("1 - Listar Projetos")
        print("2 - Adicionar novo Projeto")
        print("3 - Gestão de Projetos")
        print("0 - Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listagemProjetos(gestorProjetos)
        elif escolha == "2":
            print("Você escolheu a Opção B!")
        elif escolha == "0":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida, tente novamente.")

def submenuMembros():
    gestorMembros = Gestor_Membros("ficheiros/membros.csv")
    while True:
        print("\n============= Membros =============")
        print("1 - Listar Membros")
        print("2 - Adicionar novo Membro")
        print("3 - Gestão de Membro")
        print("0 - Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            gestorMembros.ver_todos_membros()
        elif escolha == "2":
            print("Você escolheu a Opção B!")
        elif escolha == "0":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida, tente novamente.")

def listagemTarefas(gestorTarefas):
    while True:
        print("\n============= Listar Tarefas =============")
        print("1 - Listar todas as Tarefas")
        print("2 - Listar Tarefas de um projeto")
        print("0 - Voltar")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            print("="*30)
            print("Lista de todos as tarefas:")
            gestorTarefas.ver_todas_tarefas()
            print("="*30)
        elif escolha == "2":
            id_projeto = input("Inisira o id do projeto: ")
            print("="*30)
            print(f"Lista de todas as tarefas do projecto: {id_projeto}")
            gestorTarefas.listar_tarefas_projeto(id_projeto)
            print("="*30)
            print("="*30)
        elif escolha == "0":
            print("="*30)
            print("A sair do menu...")
            print("="*30)
            break
        else:
            print("Opção inválida, tente novamente.")

def gestaoTarefa(gestorTarefas, novaTarefa=None):
    gestorTarMem = Gestor_Tar_Mem("ficheiros/tarefa_membro.csv")

    id = None
    tarefa = None
    if novaTarefa is not None:
        id = novaTarefa.id
        tarefa = novaTarefa
    else:
        id = int(input("Insira o id da tarefa: "))
        tarefa = gestorTarefas.get_tarefa_by_id(id)
        if tarefa is None:
            print("Tarefa não encontrada")
            return
        
    print(f"\n============= Tarefa: {tarefa.id} =============")
    print("1 - Associar Membros")
    print("2 - Editar tarefa")
    print("3 - Ver todos os membros responsáveis")
    print("0 - Voltar")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        funcoes_main.associar_tarefa_membro(gestorTarMem, tarefa.id)
    elif escolha == "2":
        print()
    elif escolha == "3":
        gestorTarMem.ver_todos_membros_by_tarefaId(tarefa.id)
    elif escolha == "0":
        print("Voltar ao menu Tarefas...")
        return
    else:
        print("Opção inválida, tente novamente.")


def submenuTarefas():
    gestorTarefas = Gestor_Tarefas("ficheiros/tarefas.csv")
    while True:
        print("\n============= Tarefas =============")
        print("1 - Listar Tarefas")
        print("2 - Adicionar nova Tarefa")
        print("3 - Gestão de Tarefa")
        print("0 - Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listagemTarefas(gestorTarefas)
        elif escolha == "2":
            nova_tarefa = funcoes_main.adicionar_tarefa(gestorTarefas)
            gestaoTarefa(gestorTarefas, nova_tarefa)
        elif escolha == "3":
            gestaoTarefa(gestorTarefas)
        elif escolha == "0":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_principal():
    while True:
        print("\n============= Menu Principal =============")
        print("1 - Projetos")
        print("2 - Membros")
        print("3 - Tarefas")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            submenuProjetos()
        elif escolha == "2":
            submenuMembros()
        elif escolha == "3":
            submenuTarefas()
        elif escolha == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu_principal()