import unittest

class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b

class TestValidacaoEntradas(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero_lanca_excecao(self):
        # Verifica se o erro ValueError é lançado ao dividir por zero
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()