'''
Como criar e ler um arquivo em txt:

Para abrir use "arquivo = open("nome_do_arquivo.txt", "modo")

Para ler use "arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read() 
print(conteudo)"
'''

def manipular_arquivo(nome_arquivo, texto):
    # 1. Escrevendo no arquivo (modo 'w' cria o arquivo ou sobrescreve seu conteúdo)
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)
    print(f"Conteúdo salvo com sucesso em '{nome_arquivo}'.\n")

    # 2. Lendo o arquivo (modo 'r' lê todo o conteúdo)
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    
    return conteudo

# Exemplo de uso:
nome = "dados.txt"
conteudo_para_salvar = "Linha 1: Aprendendo manipulacao de arquivos em Python.\nLinha 2: Arquivo .txt lido com sucesso!"

# Executa e exibe o resultado
resultado = manipular_arquivo(nome, conteudo_para_salvar)

print("--- Conteúdo Lido do Arquivo ---")
print(resultado)