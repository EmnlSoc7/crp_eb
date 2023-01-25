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

    def test_encrypt(self):
        """Realiza o teste unitário da criptografia"""

        pair_cypher = PairCypher(
            {"char_a1": ("M", 2), "char_a2": ("D", 8)},
            message="enviada gasolina solicitada pt",
            first_keyword=1367524,
            second_keyword=31745682,
        )
        self.assertDictEqual(
            pair_cypher.encrypt(),
            {
                "status": "success",
                "message": "GMETA IDDTC ANASN AZILA PISVD OOIAL",
            },
        )

        pair_cypher = PairCypher(
            {"char_a1": ("M", 2), "char_a2": ("D", 8)},
            message="exercito de ocupacao saqueando cidades pt",
            first_keyword=1367524,
            second_keyword=31745682,
        )
        self.assertDictEqual(
            pair_cypher.encrypt(),
            {
                "status": "success",
                "message": "OMEUI TADUI OSADX EDZCP TCPQC CDESE EAAZA ORNDO",
            },
        )

        pair_cypher = PairCypher(
            {"char_a1": ("M", 2), "char_a2": ("D", 8)},
            message="confirmada tentativa terrorista pt civis simpaticos nossa causa",
            first_keyword=12345,
            second_keyword=65423,
        )

        self.assertDictEqual(
            pair_cypher.encrypt(),
            {
                "status": "fail",
                "message": "Mensagem maior que a matriz das chaves",
            },
        )

    def test_decript(self):
        """Realiza o teste unitário da descriptografia"""

        # Primeiro teste, sucesso
        pair_cypher = PairCypher(
            {"char_a1": ("M", 2), "char_a2": ("D", 8)},
            message="GMETA IDDTC ANASN AZILA PISVD OOIAL",
            first_keyword=1367524,
            second_keyword=31745682,
        )

        self.assertDictEqual(
            pair_cypher.decrypt(),
            {
                "status": "success",
                "message": "enviadagasolinasolicitadaptz".upper(),
            },
        )

        # Segundo teste, sucesso
        pair_cypher = PairCypher(
            {"char_a1": ("M", 2), "char_a2": ("D", 8)},
            message="OMEUI TADUI OSADX EDZCP TCPQC CDESE EAAZA ORNDO",
            first_keyword=1367524,
            second_keyword=31745682,
        )

        self.assertDictEqual(
            pair_cypher.decrypt(),
            {
                "status": "success",
                "message": "exercitodeocupacaosaqueandocidadesptzz".upper(),
            },
        )

        # Autenticação falhando
        pair_cypher = PairCypher(
            {"char_a1": ("M", 5), "char_a2": ("D", 8)},
            message="OMEUI TADUI OSADX EDZCP TCPQC CDESE EAAZA ORNDO",
            first_keyword=1367524,
            second_keyword=31745682,
        )

        self.assertDictEqual(
            pair_cypher.decrypt(),
            {
                "status": "fail",
                "message": "Autenticação Invalida",
            },
        )


if __name__ == "__main__":
    unittest.main()
