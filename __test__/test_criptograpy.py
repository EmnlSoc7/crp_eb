"""Testar Criptografia"""

import unittest
from crp_eb.criptography import CriptographyEB
from crp_eb.criptography import SimpleCypher


class TestCriptographyEBMethods(unittest.TestCase):
    """Responsável por testar Metodos de CriptograpyEB"""

    def test_convert_key(self):
        """Responsável por testar a conversão da chave para numérica"""

        cript_eb = CriptographyEB({"char_a1": ("E", 2), "char_a2": ("J", 8)})

        self.assertEqual(cript_eb.char_a1, "E")
        self.assertEqual(cript_eb.char_a1_pos, 2)

        self.assertEqual(cript_eb.char_a2, "J")
        self.assertEqual(cript_eb.char_a2_pos, 8)

        key = cript_eb.convert_key("banana")
        message = cript_eb.sumarize_text("bem vindo à criptografia de transp")

        self.assertEqual(int(len(key)), int(max(key)))  # valida tamanho da chave
        self.assertListEqual(key, [4, 1, 5, 2, 6, 3])  # valida ordem da chave
        self.assertEqual("bemvindoacriptografiadetranspzzzz", message)


class TestSimpleCypherMethods(unittest.TestCase):
    """Responsável por testar Metodo SimpleCypher"""

    def test_encrypt(self):
        """Responsável por testar a encriptação"""

        cript_eb = SimpleCypher(
            {"char_a1": ("E", 2), "char_a2": ("J", 8)},
            "bem vindo à criptografia de transp",
            "banana",
        )
        mensagem_data = cript_eb.encrypt()

        self.assertEqual(cript_eb.char_a1, "E")
        self.assertEqual(cript_eb.char_a1_pos, 2)

        self.assertEqual(cript_eb.char_a2, "J")
        self.assertEqual(cript_eb.char_a2_pos, 8)

        # self.assertTrue((len(mensagem_data) + 2) % 5 == 0)  # Verifica se gerou multiplo de 5 na Mensagem

        self.assertEqual(mensagem_data, "EEOTI AZJVC GDSNI ATZBD PFRZM AOANZ IRREP")
        # Valida resultado


if __name__ == "__main__":
    unittest.main()
