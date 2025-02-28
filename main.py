from classes.gestores.gestor_tar_mem import Gestor_Tar_Mem
from classes.relações.tarefa_membro import Tarefa_Membro

#menus

gestorTarMem = Gestor_Tar_Mem("ficheiros/tarefa_membro.svc")

gestorTarMem.guardar_registro(Tarefa_Membro(1,"email1@gmail.com"))
gestorTarMem.guardar_registro(Tarefa_Membro(1,"email2@gmail.com"))
gestorTarMem.guardar_registro(Tarefa_Membro(2,"email1@gmail.com"))
gestorTarMem.guardar_registro(Tarefa_Membro(2,"email2@gmail.com"))



# Buscando registros por id
registros_por_id = gestorTarMem.procurar_por_id(2)
for r in registros_por_id:
    print(f"ID: {r.id_tarefa}, Email: {r.email_membro}")

print("#"*30)

# Buscando registros por email
registros_por_email = gestorTarMem.procurar_por_email("email1@gmail.com")
for r in registros_por_email:
    print(f"ID: {r.id_tarefa}, Email: {r.email_membro}")