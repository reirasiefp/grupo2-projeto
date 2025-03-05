def submenuProjetos():
    while True:
        print("\n============= Projetos =============")
        print("1 - Opção A")
        print("2 - Opção B")
        print("0 - Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Você escolheu a Opção A!")
        elif escolha == "2":
            print("Você escolheu a Opção B!")
        elif escolha == "0":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida, tente novamente.")

def submenuMembros():
    while True:
        print("\n============= Membros =============")
        print("1 - Opção A")
        print("2 - Opção B")
        print("0 - Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Você escolheu a Opção A!")
        elif escolha == "2":
            print("Você escolheu a Opção B!")
        elif escolha == "0":
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida, tente novamente.")

def submenuTarefas():
    while True:
        print("\n============= Tarefas =============")
        print("1 - Opção A")
        print("2 - Opção B")
        print("0 - Voltar")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Você escolheu a Opção A!")
        elif escolha == "2":
            print("Você escolheu a Opção B!")
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