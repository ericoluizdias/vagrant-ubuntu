import os
import time

def delete_old_files(folder_path):
    # Obtém o tempo atual
    current_time = time.time()
    
    # Itera sobre todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Verifica se é um arquivo (não um diretório)
        if os.path.isfile(file_path):
            # Obtém o tempo da última modificação do arquivo
            file_mod_time = os.path.getmtime(file_path)
            
            # Se o arquivo foi modificado antes de hoje, deleta-o
            if file_mod_time < current_time - 86400:  # 86400 segundos em um dia
                os.remove(file_path)
                print(f"Deleted {file_path}")

# Especifica o caminho da pasta
folder_path ="C:\temp\sgile"

# Verifica se a pasta existe antes de chamar a função
if os.path.exists(folder_path):
    # Chama a função para deletar arquivos antigos
    delete_old_files(folder_path)
else:
    print(f"A pasta {folder_path} não existe.")
