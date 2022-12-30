"""Módulo principal de criptografia"""

from unidecode import unidecode


class CriptographyEB:
    """Responsável pelo controle da criptografia"""

    def __init__(self, char_au):
        """Inicializacao da classe"""

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

        matrix = []
        temp_mat = []
        # matrix = [[b, e ,m , v, i, n], [d,o,a,c,r], ...]
        for i, char in enumerate(message):
            temp_mat.append(char)

            if len(temp_mat) == max(key) or i + 1 == len(message):
                matrix.append(temp_mat)
                temp_mat = []

        # Criado sem numpy, enumerado os indexes na ordem de criptografia
        key_indexes = [i[0] for i in sorted(enumerate(key), key=lambda x: x[1])]
        print(key_indexes)
        print(matrix)

        temp_mat2 = []
        encrypted_message = []
        count_w = 1
        for i in key_indexes:
            print(i)
            for line in matrix:
                for head, column in enumerate(line):

                    if len(temp_mat2) == 5:
                        encrypted_message.append(temp_mat2)
                        temp_mat2 = []

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
                        print(f"char: {column}")

        return matrix

    def decrypt(self, message):
        """Realiza a descriptografia da mensagem fornecida"""

        return message


if __name__ == "__main__":
    cript_eb = CriptographyEB({"char_a1": ("E", 2), "char_a2": ("J", 8)})
    mensagem_data = cript_eb.encrypt("bem vindo à criptografia de transp", "banana")

    print(mensagem_data)
