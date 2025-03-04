from classes.gestores.gestor_pro_mem import Gestor_Pro_Mem
from classes.gestores.gestor_projetos import Gestor_Projetos
from classes.projeto import Projeto
from classes.gestores.gestor_membros import Gestor_Membros
from classes.membro import Membro
from classes.relações.projeto_membro import Projeto_Membro


gestorProjetos = Gestor_Projetos("ficheiros/projetos.svc")
gestorMembros = Gestor_Membros("ficheiros/membros.svc")

projeto1 = Projeto("Projeto1 - Teste do mal",gestorProjetos)
gestorProjetos.guardar_ficheiro(projeto1)

projeto2 = Projeto("Projeto2 - Teste do bem",gestorProjetos)
gestorProjetos.guardar_ficheiro(projeto2)

membro1 = Membro("Rafael", "rafael@example.com", "Developer")
membro2 = Membro("Sofia", "sofia@example.com", "Designer")

gestorMembros.add_member(membro1)
gestorMembros.add_member(membro2)

gestorProMem = Gestor_Pro_Mem("ficheiros/projeto_membro.svc")

projeto1_membro1 = Projeto_Membro(membro1.email,projeto1.id)
projeto2_membro1 = Projeto_Membro(membro1.email,projeto2.id)
projeto2_membro2 = Projeto_Membro(membro2.email,projeto2.id)

gestorProMem.guardar_registro(projeto1_membro1)
gestorProMem.guardar_registro(projeto2_membro1)
gestorProMem.guardar_registro(projeto2_membro2)