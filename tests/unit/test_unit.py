import unittest
from projeto_aula.main import buscar_fato_aleatorio


class FakeResponse:
    def json(self):
        return {"text": "Fato interessante de teste"}


class TestBuscarFatoAleatorio(unittest.TestCase):

    def setUp(self):
        import projeto_aula.main as main
        main.requests.get = lambda url: FakeResponse()

    def test_fato_retornado(self):
        resultado = buscar_fato_aleatorio()
        self.assertEqual(resultado["fato"], "Fato interessante de teste")

    def test_retornadicionario(self):
        resultado = buscar_fato_aleatorio()
        self.assertIsInstance(resultado, dict)

    def test_chaves_presentes(self):
        resultado = buscar_fato_aleatorio()
        self.assertIn("fato", resultado)
        self.assertIn("sistema", resultado)
        self.assertIn("diretorio", resultado)
        self.assertIn("data", resultado)

if __name__ == "__main__":
    unittest.main()