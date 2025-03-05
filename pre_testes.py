import os

#Apaga todo o conteudo dos ficheiros .svc dentro da pasta "ficheiros"

for root, _, files in os.walk("ficheiros"):
    for file in files:
         if file.endswith(".svc"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'w') as f:
                    f.write("")
                print(f"Cleared content of: {file_path}")
            except Exception as e:
                print(f"Error clearing {file_path}: {e}")