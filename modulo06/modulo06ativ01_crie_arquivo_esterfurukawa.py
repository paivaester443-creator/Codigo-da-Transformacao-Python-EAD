'''
Como criar e ler um arquivo em txt:

Para abrir use "arquivo = open("nome_do_arquivo.txt", "modo")

Para ler use "arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read() 
print(conteudo)"
'''


# 1 . Criando um arquivo TXT com o nome "nome_arquivo.txt" 
# e escrevendo algumas informações nele.
nome_arquivo = "dados_arquivo.txt"


# 2 . Conteúdo a ser escrito no arquivo
# --- ESCRITA ---
conteudo = [
    "Ester Furukawa;16 anos;02899-000;947541;esterfurukawa@mail.com\n",
    "Isabelly Castelo;17 anos;057193-000;978786;isabellycastelo@mail.com\n",
    "Sarah Santos;15 anos;089880-100;98799;sarahsantos@gmail.com\n"
]


# 3 . Escrevendo no arquivo
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(conteudo)
print(f"✅ Arquivo '{nome_arquivo}' criado e escrito com sucesso!")



# 4 . Lendo o conteúdo do arquivo
# --- LEITURA ---
print("\n--- Lendo o conteúdo do arquivo TXT ---")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    print(texto)