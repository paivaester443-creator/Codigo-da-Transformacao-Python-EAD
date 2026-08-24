class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} [{status}]"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        return f"Livro '{livro.titulo}' adicionado ao acervo."

    def emprestar_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    return f"✅ Empréstimo de '{livro.titulo}' realizado!"
                return f"⚠️ O livro '{livro.titulo}' já está emprestado."
        return f"❌ Livro '{titulo}' não encontrado."

    def devolver_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    return f"✅ Livro '{livro.titulo}' devolvido!"
                return f"⚠️ O livro '{livro.titulo}' já estava disponível."
        return f"❌ Livro '{titulo}' não encontrado."

    def __str__(self):
        cabecalho = f"=== Acervo da {self.nome} ===\n"
        if not self.acervo:
            return cabecalho + "Nenhum livro cadastrado."
        itens = "\n".join([f"- {livro}" for livro in self.acervo])
        return cabecalho + itens


# Testando a estrutura do desafio
bib = Biblioteca("Biblioteca Central")

livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Alquimista", "Paulo Coelho")

print(bib.adicionar_livro(livro1))
print(bib.adicionar_livro(livro2))
print()
print(bib)

print()
print(bib.emprestar_livro("Dom Casmurro"))
print(bib)

print()
print(bib.devolver_livro("Dom Casmurro"))
print(bib)