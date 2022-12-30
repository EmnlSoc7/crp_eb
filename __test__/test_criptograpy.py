"""Testar Criptografia"""

import unittest
from crp_eb.criptography import CriptographyEB


class TestCriptographyEBMethods(unittest.TestCase):
    """Responsável por testar Metodo CriptograpyEB"""

    def test_encrypt(self):
        """Responsável por testar a encriptação"""

        cript_eb = CriptographyEB({"char_a1": ("E", "2"), "char_a2": ("J", "8")})
        mensagem_data = cript_eb.encrypt("bem vindo à criptografia de transp", "banana")

        self.assertEqual(cript_eb.char_a1, "E")
        self.assertEqual(cript_eb.char_a1_pos, "2")

        self.assertEqual(cript_eb.char_a2, "J")
        self.assertEqual(cript_eb.char_a2_pos, "8")

        self.assertTrue(
            (len(mensagem_data) + 2) % 5 == 0
        )  # Verifica se gerou multiplo de 5
        # self.assertEqual( messagem_data, "EEOTI AZJVC GDSNI ATZBD PFRZM AOANZ IRREP")

    def test_convert_key(self):
        """Responsável por testar a conversão da chave para numérica"""

        cript_eb = CriptographyEB({"char_a1": ("E", "2"), "char_a2": ("J", "8")})
        key = cript_eb.convert_key("banana")

        self.assertEqual(cript_eb.char_a1, "E")
        self.assertEqual(cript_eb.char_a1_pos, "2")

        self.assertEqual(cript_eb.char_a2, "J")
        self.assertEqual(cript_eb.char_a2_pos, "8")

        self.assertEqual(int(len(key)), int(max(key)))
        self.assertListEqual(key, [4, 1, 5, 2, 6, 3])


if __name__ == "__main__":
    unittest.main()
