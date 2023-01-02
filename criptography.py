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

    def sumarize_text(self, message: str, gap=2, base=5, ghost="z") -> str:
        """Formata string e adiciona letras fantasmas equiparar ao multiplo da base"""

        message = unidecode("".join(e for e in message if e.isalnum()))
        qtd_ghost = (
            0
            if base - ((len(message) + gap) % base) >= base
            else base - ((len(message) + gap) % base)
        )

        for _ in range(qtd_ghost):
            message = message + ghost
        print(message)
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

    def validate_autentication(self, message: str) -> tuple[str, bool]:
        """
        Faz a autenticação dos caracteres na mensagem e retorna
        uma tupla com a mensagem formatada sem os caracteres especificos
        e o status booleano da autenticação True ou retorna a propria
        mensagem e o status booleano False.

        Parametros:
            message (str): Mensagem criptografada previamente.

        Retorno:
            tuple(message, bool): Tupla com a mensagem e o status da
            validação da mensagem.
        """

        message = message.replace(" ", "")
        message_autenticated = ""
        char_a1_index = self.char_a1_pos - 1
        char_a2_index = self.char_a2_pos - 1

        if (
            message[char_a1_index] == self.char_a1
            and message[char_a2_index] == self.char_a2
        ):
            message_autenticated = (
                message[:char_a1_index] + message[char_a1_index + 1 :]
            )
            message_autenticated = (
                message_autenticated[: char_a2_index - 1]
                + message_autenticated[char_a2_index:]
            )
            return (message_autenticated, True)
        return (message, False)


class SimpleCypher(CriptographyEB):
    """Classe de criptografia de chave simples"""

    def __init__(self, char_au, message: str, keyword: str):
        super().__init__(char_au)
        self.message = message
        self.keyword = keyword

    def encrypt(self):
        """Realiza a criptografia da mensagem fornecida"""

        # Formata mensagem para mult de 5 + 2 au
        message = self.sumarize_text(self.message)
        # pega a ordem numérica da chave criptografica
        key = self.convert_key(self.keyword)
        # gera matriz da chave
        matrix = self.generate_matrix(message, key)

        # Criado sem numpy, enumerado os indexes da ordem numérica
        key_indexes = self.enumerate_indexes(key)

        temp_mat = []  # responsável pelas listas criptografadas
        encrypted_message = []  # lista de listas final da criptografia
        count_w = 1
        for i in key_indexes:  # percorre os cabeçalhos
            for line in matrix:  # lê cada linha da estrutura gerada
                # separa em uma nova lista de acordo com o head e adiciona autenticação
                for head, column in enumerate(line):

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

                    if len(temp_mat) == 5:
                        encrypted_message.append(temp_mat)
                        temp_mat = []

        final_message = self.lists_to_string(encrypted_message)
        return final_message.strip().upper()

    def decrypt(self) -> dict[str, str]:
        """Realiza a descriptografia da mensagem fornecida"""

        ##### identificar o tamanho da mensagem sem aut
        ##### Distribui-la em igual conforme o tamanho
        # ----------------------------------------------------------- #
        #       EEOTI AZJVC GDSNI ATZBD PFRZM AOANZ IRREP             #
        #          EOTIAZVCGDSNIATZBDPFRZMAOANZIRREP                  #
        #    usar um for contando cada passagem e gerando a lista     #
        # em cada linha e quando atingir 33, encerra o processo e     #
        #                       armazena                              #
        #   output:   BEMVINDOACRIPTOGRAFIADETRANSPZZZZ               #
        #
        # Nomenclaturas descritivas:
        # letra = char
        # linha = line
        # mensagem = message
        # coluna = key_indexes[column_key]
        # -----------------------------------------------------------

        message, validation = self.validate_autentication(self.message)

        if validation is False:
            return {"status": "error", "message": "Autenticação Invalida"}

        key = self.convert_key(self.keyword)
        key_indexes = self.enumerate_indexes(key)

        # -----------------------------------------------------------
        # Descrição:
        # Gera uma matriz com a quantidade de caracteres da mensagem
        # e com maximo de colunas igual à chave criptografica.
        # * Usada para estruturar a descriptografia coluna a coluna
        # -----------------------------------------------------------
        mat_temp = []
        matrix = []
        for i in range(len(message)):
            mat_temp.append("")
            if len(mat_temp) >= len(key) or i + 1 == len(message):
                matrix.append(mat_temp)
                mat_temp = []

        # -----------------------------------------------------------
        # Descrição:
        # Percorre toda a mensagem letra por letra, verifica
        # a coluna de cada linha e preenche a primeira linha
        # a estar com a coluna vazia.
        # Interrompe o loop toda vez que preencher
        # -----------------------------------------------------------
        column_key = 0  # Contador para definir a coluna alvo

        for _, char in enumerate(message):

            # Verifica se ainda há posição disponivel na coluna
            found = False
            for lines_check in matrix:
                if len(lines_check) >= (key_indexes[column_key] + 1):
                    if "" == lines_check[key_indexes[column_key]]:
                        found = True
                        break

            # Troca a coluna alvo se não localizar posição vazia
            column_key = column_key + 1 if found is False else column_key

            # preenche a primeira coluna da linha que estiver vazia
            for _, line in enumerate(matrix):

                if (line[key_indexes[column_key]]) == "":
                    line[key_indexes[column_key]] = char
                    break

        # Converte a matriz em string
        decrypted_message = self.lists_to_string(matrix).replace(" ", "")
        return {"status": "success", "message": decrypted_message}


if __name__ == "__main__":
    ##################################################################
    # Criado testes unitários para testar o código de forma dinamica #
    #                Não utilizar Módulo diretamente                 #
    ##################################################################

    testing = SimpleCypher(
        {"char_a1": ("H", 4), "char_a2": ("R", 6)},
        "Realizar a Transferencia o mais cedo possivel",
        "compromisso",
    )

    encrypted = testing.encrypt()
    print(encrypted)
    pass
