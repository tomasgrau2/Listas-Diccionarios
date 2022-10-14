import unittest
import main


class BuscarRepetidos(unittest.TestCase):

    def test_simple(self):
        resultado = main.buscar_repetidos([7, 8, 101])
        self.assertEqual(resultado, {7: 1, 8: 1, 101: 1})

    def test_complex(self):
        resultado = main.buscar_repetidos([8, 8, 7, 8, 101])
        self.assertEqual(resultado, {7: 1, 8: 3, 101: 1})

if __name__ == '__main__':
    unittest.main()