"""Testar Criptografia"""

import unittest

from core_criptography import CoreCriptography
from simple_cypher import SimpleCypher


class TestCriptographyEBMethods(unittest.TestCase):
    """Responsável por testar Metodos de CriptograpyEB"""

    def test_convert_key(self):
        """Responsável por testar a conversão da chave para numérica"""

        cript_eb = CoreCriptography({"char_a1": ("E", 2), "char_a2": ("J", 8)})

        self.assertEqual(cript_eb.char_a1, "E")
        self.assertEqual(cript_eb.char_a1_pos, 2)

        self.assertEqual(cript_eb.char_a2, "J")
        self.assertEqual(cript_eb.char_a2_pos, 8)

        key = cript_eb.convert_key("banana")
        message = cript_eb.prepare_text("bem vindo à criptografia de transp")

        self.assertEqual(int(len(key)), int(max(key)))  # valida tamanho da chave
        self.assertListEqual(key, [4, 1, 5, 2, 6, 3])  # valida ordem da chave
        self.assertEqual("bemvindoacriptografiadetranspzzzz", message)

    def test_validate_autentication(self):
        """Responsável por validar a autenticação"""

        cript_eb = CoreCriptography({"char_a1": ("E", 2), "char_a2": ("J", 8)})
        message, autenticated = cript_eb.validate_autentication(
            "EEOTI AZJVC GDSNI ATZBD PFRZM AOANZ IRREP"
        )
        self.assertEqual(autenticated, True)
        self.assertEqual(message, "EOTIAZVCGDSNIATZBDPFRZMAOANZIRREP")


class TestSimpleCypherMethods(unittest.TestCase):
    """Responsável por testar Metodo SimpleCypher"""

    def test_encrypt(self):
        """Responsável por testar a encriptação da chave simples"""

        cript_eb = SimpleCypher(
            {"char_a1": ("E", 2), "char_a2": ("J", 8)},
            "bem vindo à criptografia de transp",
            "banana",
        )
        mensagem_data = cript_eb.encrypt()
        self.assertEqual(mensagem_data[0], "EEOTI AZJVC GDSNI ATZBD PFRZM AOANZ IRREP")

        cript_eb = SimpleCypher(
            {"char_a1": ("I", 4), "char_a2": ("G", 7)},
            "Combate eminente a 12 horas em 21142003",
            "metralhadora",
        )
        mensagem_data = cript_eb.encrypt()
        self.assertEqual(mensagem_data[0], "A14IE OG0EE MR3OT 2EH0T 22CNM IABA1 NSME1")

    def test_decrypt(self):
        """Responsável por testar a decriptação da chave simples"""
        decrypt_class_1 = SimpleCypher(
            {"char_a1": ("E", 2), "char_a2": ("J", 8)},
            "EEOTI AZJVC GDSNI ATZBD PFRZM AOANZ IRREP",
            "banana",
        )
        self.assertDictEqual(
            decrypt_class_1.decrypt(),
            {
                "status": "success",
                "message": "bemvindoacriptografiadetranspzzzz".upper(),
            },
        )

        decrypt_class_3 = SimpleCypher(
            {"char_a1": ("H", 4), "char_a2": ("R", 6)},
            "RAOHS RRNDZ ASAIA EEZEN MSZRC LRAOL FIVIE SEACO ZTIPZ",
            "compromisso",
        )
        self.assertDictEqual(
            decrypt_class_3.decrypt(),
            {
                "status": "success",
                "message": "realizaraTransferenciaomaiscedopossivelzzzz".upper(),
            },
        )

        decrypt_class_4 = SimpleCypher(
            {"char_a1": ("I", 4), "char_a2": ("G", 7)},
            "A14IE OG0EE MR3OT 2EH0T 22CNM IABA1 NSME1",
            "metralhadora",
        )
        self.assertDictEqual(
            decrypt_class_4.decrypt(),
            {
                "status": "success",
                "message": "COMBATEEMINENTEA12HORASEM21142003".upper(),
            },
        )


if __name__ == "__main__":
    unittest.main()
