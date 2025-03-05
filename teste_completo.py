from classes.gestores.gestor_membros import Gestor_Membros
from classes.gestores.gestor_pro_mem import Gestor_Pro_Mem
from classes.gestores.gestor_projetos import Gestor_Projetos
from classes.gestores.gestor_tar_mem import Gestor_Tar_Mem
from classes.gestores.gestor_tar_pro import Gestor_Tar_Pro
from classes.gestores.gestor_tarefas import Gestor_Tarefas
from classes.membro import Membro
from classes.projeto import Projeto
from classes.relações.projeto_membro import Projeto_Membro
from classes.relações.tarefa_membro import Tarefa_Membro
from classes.relações.tarefa_projeto import Tarefa_Projeto
from classes.tarefa import Tarefa
#APAGAR TODOS OS REGISTOS NOS FICHEIROS ANTES DE CORRER OS TESTES

#Criar 1 Projetos (confirmar no projetos.svc)
gestor_projetos = Gestor_Projetos("ficheiros/projetos.svc")

projeto = Projeto("Projeto Principal", gestor_projetos)
gestor_projetos.guardar_ficheiro(projeto)

#Criar 2 Membros (confirmar no membros.svc)
gestor_membros = Gestor_Membros("ficheiros/membros.svc")

membro1 = Membro("Antonio Silva","antonio@exemplo.com","Developer")
membro2 = Membro("Marta Oliveira","marta@exemplo.com","Designer")

gestor_membros.add_member(membro1)
gestor_membros.add_member(membro2)

#Criar 4 Tarefas (tarefas.svc)
gestor_tarefas = Gestor_Tarefas("ficheiros/tarefas.svc")

tarefa1 = Tarefa("Tarefa Dev",1,"Desenvolvimento","2025-04-04",gestor_tarefas)
gestor_tarefas.guardar_ficheiro(tarefa1)

tarefa2 = Tarefa("Tarefa Design",3,"Desenvolvimento","2025-05-05",gestor_tarefas)
gestor_tarefas.guardar_ficheiro(tarefa2)

tarefa3 = Tarefa("Tarefa Testes",5,"Desenvolvimento","2025-04-10",gestor_tarefas)
gestor_tarefas.guardar_ficheiro(tarefa3)

tarefa4 = Tarefa("Tarefa Dev 2",1,"Desenvolvimento","2025-04-25",gestor_tarefas)
gestor_tarefas.guardar_ficheiro(tarefa4)


#Associar Membros aos Projetos (confirmar no projeto_membro.svc)
gestorProMem = Gestor_Pro_Mem("ficheiros/projeto_membro.svc")

projeto_membro1 = Projeto_Membro(membro1.email,projeto.id)
projeto_membro2 = Projeto_Membro(membro2.email,projeto.id)

gestorProMem.guardar_registro(projeto_membro1)
gestorProMem.guardar_registro(projeto_membro2)

#Associar Tarefas ao Projetos (confirmar no tarefa_projeto.svc)
gestorTarPro = Gestor_Tar_Pro("ficheiros/tarefa_projeto.svc")

tarefa_projeto1 = Tarefa_Projeto(tarefa1.id,projeto.id)
gestorTarPro.guardar_registro(tarefa_projeto1)

tarefa_projeto2 = Tarefa_Projeto(tarefa2.id,projeto.id)
gestorTarPro.guardar_registro(tarefa_projeto2)

tarefa_projeto3 = Tarefa_Projeto(tarefa3.id,projeto.id)
gestorTarPro.guardar_registro(tarefa_projeto3)

tarefa_projeto4 = Tarefa_Projeto(tarefa4.id,projeto.id)
gestorTarPro.guardar_registro(tarefa_projeto4)

#Associar Membros às Tarefas (confirmar no tarefa_membro.svc)
gestorTarMem = Gestor_Tar_Mem("ficheiros/tarefa_membro.svc")

tarefa1_membro1 = Tarefa_Membro(tarefa1.id,membro1.email)
gestorTarMem.guardar_registro(tarefa1_membro1)

tarefa1_membro2 = Tarefa_Membro(tarefa1.id,membro2.email)
gestorTarMem.guardar_registro(tarefa1_membro2)

tarefa2_membro1 = Tarefa_Membro(tarefa2.id,membro1.email)
gestorTarMem.guardar_registro(tarefa2_membro1)

tarefa3_membro1 = Tarefa_Membro(tarefa3.id,membro1.email)
gestorTarMem.guardar_registro(tarefa3_membro1)

tarefa4_membro1 = Tarefa_Membro(tarefa4.id,membro1.email)
gestorTarMem.guardar_registro(tarefa4_membro1)
