"""Módulo principal de criptografia"""

from unidecode import unidecode


class CriptographyEB:
    """Responsável pelo controle da criptografia"""

    def __init__(self, char_au):
        """Inicializacao da classe"""

        if char_au["char_a1"][1] == char_au["char_a2"][1]:
            print("Autenticação com posição duplicada")
            exit()
        self.char_a1 = char_au["char_a1"][0]
        self.char_a1_pos = int(char_au["char_a1"][1])

        self.char_a2 = char_au["char_a2"][0]
        self.char_a2_pos = int(char_au["char_a2"][1])

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

    def sumarize_text(self, message: str, gap=2, base=5, ghost="z"):
        """Realiza a sumarização matemática de um texto"""

        message = unidecode("".join(e for e in message if e.isalnum()))
        qtd_ghost = (
            0
            if base - ((len(message) + gap) % base) >= base
            else base - ((len(message) + gap) % base)
        )

        for _ in range(qtd_ghost):
            message = message + ghost

        return message

    def lists_to_string(self, list_message):
        """Separa lista de listas em forma de String"""
        message = ""
        for lists in list_message:
            for head, char in enumerate(lists):
                if head == 0:
                    message += " "
                message += char

        return message

    def generate_matrix(self, message: str, key: list[int]) -> list:
        """Cria uma matriz com maximo de colunas de uma chave especifica"""

        matrix = []
        temp_mat = []

        for head, char in enumerate(message):
            temp_mat.append(char)

            if len(temp_mat) == max(key) or head + 1 == len(message):
                matrix.append(temp_mat)
                temp_mat = []

        return matrix

    def encrypt(self, message, keyword):
        """Realiza a criptografia da mensagem fornecida"""

        message = self.sumarize_text(message)
        key = self.convert_key(keyword)

        # bemvindoacriptografiadetransp
        # 29 caracteres
        # [4, 1, 5, 2, 6, 3]

        matrix = self.generate_matrix(message, key)

        # Criado sem numpy, enumerado os indexes na ordem de criptografia
        key_indexes = [i[0] for i in sorted(enumerate(key), key=lambda x: x[1])]

        temp_mat2 = []
        encrypted_message = []
        count_w = 1
        for i in key_indexes:
            for line in matrix:
                for head, column in enumerate(line):

                    if count_w == self.char_a1_pos:
                        temp_mat2.append(self.char_a1)
                        count_w += 1
                    elif count_w == self.char_a2_pos:
                        temp_mat2.append(self.char_a2)
                        count_w += 1

                    if head == i:
                        if len(temp_mat2) == 5:
                            encrypted_message.append(temp_mat2)
                            temp_mat2 = []

                        temp_mat2.append(column)
                        count_w += 1

                    if len(temp_mat2) == 5:
                        encrypted_message.append(temp_mat2)
                        temp_mat2 = []

        final_message = self.lists_to_string(encrypted_message)
        return final_message.strip().upper()

    def decrypt(self, message):
        """Realiza a descriptografia da mensagem fornecida"""

        return message


if __name__ == "__main__":
    ##################################################################
    # Criado testes unitários para testar o código de forma dinamica #
    #                Não utilizar Módulo diretamente                 #
    ##################################################################
    pass
