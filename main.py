from classes.membro import Membro
from classes.projeto import Projeto
from classes.tarefa import Tarefa

#menus

tarefa = Tarefa("nome da tarefa", 1, "tipo", "2025-05-01")
print(tarefa)
print("#"*30)


membro = Membro("nome1", "email1", "funcao1")
tarefa.adicionar_membro(membro)
membro = Membro("nome1", "email1", "funcao1")
tarefa.adicionar_membro(membro)

membro2 = Membro("nome2", "email2", "funcao2")
tarefa.adicionar_membro(membro2)

tarefa.verListaMembros()

projeto = Projeto("nome")