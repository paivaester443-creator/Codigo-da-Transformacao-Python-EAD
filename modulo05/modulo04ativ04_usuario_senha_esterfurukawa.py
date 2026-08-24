usuarios_cadastrados = {
    "Ester": "ester123",
    "Isabelly": "isabelly123",
    "Sarah": "sarah123"
}

def fazer_login(usuario, senha, banco_dados):
    if banco_dados.get(usuario) == senha:
        return True, f"Bem-vindo(a), {usuario}!"
    return False, "Usuário ou senha incorretos."

user_input = input("Usuário: ")
senha_input = input("Senha: ")

sucesso, mensagem = fazer_login(user_input, senha_input, usuarios_cadastrados)
print(mensagem)