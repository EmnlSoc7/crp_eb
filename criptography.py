"""Módulo principal de criptografia"""

from unidecode import unidecode


class CriptographyEB:
    """Responsável pelo controle da criptografia"""

    def __init__(self, char_au):
        """Inicializacao da classe"""

        self.char_a1 = char_au["char_a1"][0]
        self.char_a1_pos = char_au["char_a1"][1]

        self.char_a2 = char_au["char_a2"][0]
        self.char_a2_pos = char_au["char_a2"][1]

    def convert_key(self, keyword):
        """Converte Chave de Caractere para Ordem Numérica"""

        alfa = "abcdefghijklmnopqrstuvwxyz"

        keyword = keyword.lower()
        key = [0 for _ in range(len(keyword))]
        key_char = keyword

        count = 1
        for letter in alfa:
            for index, char in enumerate(key_char):
                if letter == char:
                    key[index] = count
                    count += 1

        return key

    def encrypt(self, message, keyword):
        """Realiza a criptografia da mensagem fornecida"""

        message = unidecode("".join(e for e in message if e.isalnum()))
        key = self.convert_key(keyword)

        # bemvindoacriptografiadetransp
        # 29 caracteres
        # [4, 1, 5, 2, 6, 3]

        if len(message) % 5 == 4:
            char_ghost = 4
        else:
            char_ghost = 3 - (len(message) % 5)

        for _ in range(char_ghost):
            message = message + "z"

        message_encrypted = len(message) % 5

        return message

    def decrypt(self, message):
        """Realiza a descriptografia da mensagem fornecida"""

        return message


if __name__ == "__main__":
    pass
