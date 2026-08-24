import os
import shutil

origem = "pasta_origem"
destino = "pasta_destino"

# Cria a pasta de origem e um arquivo de teste caso não existam
if not os.path.exists(origem):
    os.makedirs(origem)
    with open(os.path.join(origem, "exemplo.txt"), "w", encoding="utf-8") as f:
        f.write("Conteúdo para o backup automático.")

def realizar_backup(pasta_origem, pasta_destino):
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não existe.")
        return

    # Substitui o backup anterior se a pasta de destino já existir
    if os.path.exists(pasta_destino):
        shutil.rmtree(pasta_destino)
        
    shutil.copytree(pasta_origem, pasta_destino)
    print(f"✅ Backup concluído! Conteúdo de '{pasta_origem}' copiado para '{pasta_destino}'.")

realizar_backup(origem, destino)