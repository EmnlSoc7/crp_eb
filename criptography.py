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

    def enumerate_indexes(self, key: list[int]) -> list:
        """Retorna os indices em ordem crescente de uma lista de inteiros"""
        return [i[0] for i in sorted(enumerate(key), key=lambda x: x[1])]

    def encrypt(self, message, keyword):
        """Realiza a criptografia da mensagem fornecida"""

        message = self.sumarize_text(message)  # Formata mensagem para mult de 5 + 2 au
        key = self.convert_key(keyword)  # pega a ordem numérica da chave criptografica
        matrix = self.generate_matrix(message, key)  # gera matriz da chave

        # Criado sem numpy, enumerado os indexes da ordem numérica
        key_indexes = self.enumerate_indexes(key)

        temp_mat = []  # responsável pelas listas criptografadas
        encrypted_message = []  # lista de listas final da criptografia
        count_w = 1
        for i in key_indexes:
            for line in matrix:
                for head, column in enumerate(line):

                    if len(temp_mat) == 5:
                        encrypted_message.append(temp_mat)
                        temp_mat = []

                    if count_w == self.char_a1_pos:
                        temp_mat.append(self.char_a1)
                        count_w += 1
                    elif count_w == self.char_a2_pos:
                        temp_mat.append(self.char_a2)
                        count_w += 1

                    if head == i:
                        if len(temp_mat) == 5:
                            encrypted_message.append(temp_mat)
                            temp_mat = []

                        temp_mat.append(column)
                        count_w += 1

        final_message = self.lists_to_string(encrypted_message)
        return final_message.strip().upper()

    def decrypt(self, message):
        """Realiza a descriptografia da mensagem fornecida"""

        # TODO: Descriptografar mensagem
        # Verificar as chaves de autenticação e remove-las da mensagem
        # converter index da chave
        # identificar quantidade de letras na mensagem
        # distribuir mensagem por coluna

        return message


if __name__ == "__main__":
    ##################################################################
    # Criado testes unitários para testar o código de forma dinamica #
    #                Não utilizar Módulo diretamente                 #
    ##################################################################
    pass
