# Puxa as informações da marca e modelo do carros para exibi-lás
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"

# Pega as informações do carro eletrico e exibe
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Autonomia: {self.autonomia_bateria}km"


# Instanciando e testando a subclasse
carro_eletrico = CarroEletrico("BYD", "Dolphin Mini", 291)
print(carro_eletrico.exibir_info())