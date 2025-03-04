# Criar 5 membros
# Criar 2 Projectos

from classes.gestores.gestor_projetos import Gestor_Projetos
from classes.projeto import Projeto


gestorProjetos = Gestor_Projetos("ficheiros/projetos.svc")

projeto1 = Projeto("Projeto1 - Teste do mal",gestorProjetos)
#gestorProjetos.guardar_ficheiro(projeto1)

projeto2 = Projeto("Projeto2 - Teste do bem",gestorProjetos)
#gestorProjetos.guardar_ficheiro(projeto2)

projeto3 = Projeto("Projeto3 - Teste do assim-assim",gestorProjetos)
#gestorProjetos.guardar_ficheiro(projeto3)

print("#"*30)
print("TODOS OS PROJETOS")
print("#"*30)
gestorProjetos.ver_todos_projetos()

print("#"*30)
print("TODOS OS PROJETOS EM PROGRESSO")
print("#"*30)
gestorProjetos.ver_todos_projetos(1)

print("#"*30)
print("TODOS OS PROJETOS CONCLUIDOS")
print("#"*30)
gestorProjetos.ver_todos_projetos(2)


#Listar todos os membros
#Listar todos os projetos

#Associar membro 1, 2, 3 ao projecto 1
#Associar membro 4, 5 ao projecto 2

#Listar todos os membros do projeto 1
#Listar todos os membros do projeto 2