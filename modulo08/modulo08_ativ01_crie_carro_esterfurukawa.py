class carro:
    def __init__(self, marca, modelo):
        return f"marca: {self.marca} | modelo: {self.modelo}"

    meu_carro = ("fiat", "uno")
    print(meu_carro.exibir_info())