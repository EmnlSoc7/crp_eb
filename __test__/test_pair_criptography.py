"""Realiza o test unitário da criptografia de chave dupla"""

import unittest
from pair_cypher import PairCypher


class TestPairCriptographyMethods(unittest.TestCase):
    """Responsável por testar os metodos de pair_cypher"""

    def test_initialization(self):
        """Realiza o teste unitário da inicialização do metodo principal"""

        # maximo de 42 caracteres
        cript = PairCypher(
            {"char_a1": ("M", 2), "char_a2": ("D", 8)},
            message="solicito envio de armamento tatico em 39201",
            first_keyword=1367524,
            second_keyword=216345,
        )

        self.assertEqual(cript.char_a1, "M")
        self.assertEqual(cript.char_a1_pos, 2)
        self.assertEqual(cript.char_a2, "D")
        self.assertEqual(cript.char_a2_pos, 8)


if __name__ == "__main__":
    unittest.main()
