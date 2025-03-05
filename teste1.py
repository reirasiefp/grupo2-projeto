from classes.gestores.gestor_tarefas import Gestor_Tarefas


gestorTarefas = Gestor_Tarefas("ficheiros/tarefas.csv")

gestorTarefas.ver_todas_tarefas()
print("#"*30)
gestorTarefas.listar_tarefas_projeto(2)
print("#"*30)
gestorTarefas.alterar_estado_tarefa(7)
print("#"*30)
gestorTarefas.listar_tarefas_projeto(2)