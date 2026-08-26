#Criando classe do carro, qual a marca, o modelo e o ano dos carros
# previamente inseridos
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}"


# Testando a representação em string (__str__)
carro1 = Carro("Ford", "Mustang", 2022)
carro2 = Carro("Volkswagen", "Fusca", 1972)

print(carro1)
print(carro2)