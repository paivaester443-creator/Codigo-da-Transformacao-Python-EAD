'''
Car
'''

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Autonomia: {self.autonomia_bateria}km"


class CarroAntigo(Carro):
    def __init__(self, marca, modelo, ano_fabricacao):
        super().__init__(marca, modelo)
        self.ano_fabricacao = ano_fabricacao

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Ano: {self.ano_fabricacao}"


carro_comum = Carro("Toyota", "Corolla")
print(carro_comum.exibir_info())

carro_eletrico = CarroEletrico("BYD", "Dolphin Mini", 291)
print(carro_eletrico.exibir_info())

carro_antigo = CarroAntigo("Volkswagen", "Fusca", 1972)
print(carro_antigo.exibir_info())