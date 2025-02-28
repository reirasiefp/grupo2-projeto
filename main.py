from classes.membro import Membro
from classes.projeto import Projeto
from classes.tarefa import Tarefa

#menus

tarefa = Tarefa("nome_da tarefa", 1, "tipo", "2025-02-28")
print(tarefa)

membro = Membro("nome", "email", "funcao")

projeto = Projeto("nome")


print("menu inicial:")
while True:
    print("1. Continuar:")
    print("2. Sair:")
    escolha = int(input("Escolha:"))

    if escolha == 1:
        continue
    elif escolha == 2:
        break
    else:
        print("Numero errado.")