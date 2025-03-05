from classes.gestores.gestor_membros import Gestor_Membros
from classes.gestores.gestor_projetos import Gestor_Projetos
from classes.gestores.gestor_tarefas import Gestor_Tarefas


gestorTarefas = Gestor_Tarefas("ficheiros/tarefas.csv")
gestorProjetos = Gestor_Projetos("ficheiros/projetos.csv")
gestorMembros = Gestor_Membros("ficheiros/membros.csv")

gestorTarefas.ver_todas_tarefas()
print("#"*30)
gestorTarefas.listar_tarefas_projeto(1)
print("#"*30)
gestorTarefas.concluir_tarefa(3)
print("#"*30)
gestorTarefas.listar_tarefas_projeto(1)
print("#"*30)
print(gestorTarefas.get_tarefa_by_id(3))
print("#"*30)
print(gestorProjetos.get_projeto_by_id(1))
print("#"*30)
print(gestorMembros.get_membro_by_email("antonio@exemplo.com"))
print("#"*30)

