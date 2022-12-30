"""Módulo principal de criptografia"""

from unidecode import unidecode


class CriptographyEB:
    """Responsável pelo controle da criptografia"""

    def __init__(self, chave, char_au):
        """Inicializacao da classe"""
        self.chave = chave

        self.char_a1 = char_au["char_a1"][0]
        self.char_a1_pos = char_au["char_a1"][1]

        self.char_a2 = char_au["char_a2"][0]
        self.char_a2_pos = char_au["char_a2"][1]

    def convert_key(self):
        """Converte Chave de Caractere para Ordem Numérica"""

        alfa = "abcdefghijklmnopqrstuvwxyz"
        key = ['_' for _ in range(len(self.chave))]
        key_char = self.chave

        count = 1
        for letter in alfa:
            for index, char in enumerate(key_char):
                if letter == char:
                    key[index] = count
                    count += 1

        return key

    def encrypt(self, message):
        """Realiza a criptografia da mensagem fornecida"""

        message = unidecode(''.join(e for e in message if e.isalnum()))

        message_encrypted = message

        return message_encrypted

    def decrypt(self, message):
        """Realiza a descriptografia da mensagem fornecida"""

        return message


if __name__ == '__main__':
    pass
