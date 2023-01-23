"""Realiza o test unitário da criptografia de chave dupla"""

import unittest

from pair_cypher import PairCypher


class TestPairCriptographyMethods(unittest.TestCase):
    """Responsável por testar os metodos de pair_cypher"""

    def test_initialization(self):
        """Realiza o teste unitário da inicialização do metodo principal"""

        cript = PairCypher(
            {"char_a1": ("E", 2), "char_a2": ("J", 8)},
            message="solicito envio de armamento tatico em 39201",
            first_keyword="metralhadora",
            second_keyword="petardo",
        )

        self.assertEqual(cript.char_a1, "E")
        self.assertEqual(cript.char_a1_pos, 2)
        self.assertEqual(cript.char_a2, "J")
        self.assertEqual(cript.char_a2_pos, 8)


if __name__ == "__main__":
    unittest.main()
