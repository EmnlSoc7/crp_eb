"""Módulo principal de criptografia"""

from core_criptography import CoreCriptography


class SimpleCypher(CoreCriptography):
    """
    Módulo de criptografia de chave simples (chave unica).

    Métodos:
        encrypt(): Método de encryptação.
        decrypt(): Método de decriptação.

    Parametros:
        char_au (dict: tuple(str, int)): Caracteres de autenticação.
        message (str): Mensagem em claro.

    Retorno:
        tuple(message, bool): Tupla com a mensagem e o status da
        criptografia realizada.
    """

    def __init__(
        self,
        char_au: dict[str, tuple[str, int], str, tuple[str, int]],
        message: str,
        keyword: str,
    ):
        super().__init__(char_au)
        self.message = message
        self.keyword = keyword

    def encrypt(self) -> tuple[str, bool]:
        """
        Faz a encriptação da mensagem fornecida em
        self.message, usando a as chaves char_au, com a senha
        em self.keyword.

        Parametros:
            message (str): Mensagem em claro.

        Retorno:
            tuple(message, bool): Tupla com a mensagem e o status da
            criptografia realizada.
        """

        # Formata mensagem para mult de 5 + 2 au
        message = self.prepare_text(self.message)
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
        return (final_message.strip().upper(), True)

    def decrypt(self) -> dict[str, str]:
        """
        Realiza a descriptografia da mensagem fornecida
        """

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

        message, validation = self.autenticate_message(self.message)

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
    pass
