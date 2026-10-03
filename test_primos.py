import unittest
from primos import es_primo


class TestEsPrimo(unittest.TestCase):
    def test_primos_conocidos(self):
        for n in (2, 3, 5, 7, 11, 13, 97):
            with self.subTest(n=n):
                self.assertTrue(es_primo(n))

    def test_compuestos(self):
        for n in (4, 6, 9, 15, 25, 100):
            with self.subTest(n=n):
                self.assertFalse(es_primo(n))

    def test_menores_que_dos_no_son_primos(self):
        for n in (1, 0, -7):
            with self.subTest(n=n):
                self.assertFalse(es_primo(n))


if __name__ == "__main__":
    unittest.main()
