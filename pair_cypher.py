"""Módulo de criptografia de chave dupla"""

from typing import Union
from core_criptography import CoreCriptography


class PairCypher(CoreCriptography):
    """Módulo de criptografia de chave dupla.

    Métodos:
        encrypt(): Método de encryptação
        decrypt(): Método de decriptação

    Parametros:
        char_au (dict: tuple(str, int)): Caracteres de autenticação
        message (str): Mensagem em claro
        first_keyword: Primeira chave
        second_keyword: Segunda chave
    """

    def __init__(
        self,
        char_au: dict[str, tuple[str, int]],
        message: str,
        first_keyword: Union[str, int],
        second_keyword: Union[str, int],
    ):
        super().__init__(char_au)
        self.message = message
        self.first_keyword = str(first_keyword)
        self.second_keyword = str(second_keyword)

    def matrix_refactory_by_index(
        self, matrix: list[list[str]], key_indexes: list[int]
    ) -> tuple[list[int], list[list[str]]]:
        """Realiza a refatoração de uma matriz de acordo com a lista de headers fornecidas

        Args:
            matrix (list): Matriz inicial
            key_indexes (list): lista numérica da ordem dos indices

        Returns:
            tuple (list, list): Chave Reversa, Matriz Inicial formatada
        """
        line_encrypted_matrix = []  # matriz na ordem da chave secundária
        reverse_key = []
        for head_index in key_indexes:
            if len(matrix) > head_index:

                line_encrypted_matrix.append(matrix[head_index])
                reverse_key.append(head_index)

        return (reverse_key, line_encrypted_matrix)

    def encrypt(self) -> dict[str, str]:
        """
        Realiza a criptografia da mensagem com as chaves e letras
        de autenticação fornecidas

        Returns:
            dict ("status": str, "message": str): Status da operação, mensagem de retorno
        """
        message = self.prepare_text(self.message)

        first_key = self.convert_key(self.first_keyword)
        second_key = self.convert_key(self.second_keyword)

        # Verifica se a mensagem é maior que a quantidade de caracteres
        if len(message) >= (len(first_key) * len(second_key)):
            return {
                "status": "fail",
                "message": "Mensagem maior que a matriz das chaves",
            }

        matrix = self.generate_matrix(message, first_key)

        first_key_indexes = self.enumerate_indexes(first_key)
        second_key_indexes = self.enumerate_indexes(second_key)

        temp_mat = []  # responsável pelas listas criptografadas
        encrypted_message = []  # lista de listas final da criptografia
        count_w = 1

        _, line_refactored_matrix = self.matrix_refactory_by_index(matrix, second_key_indexes)

        for i in first_key_indexes:  # percorre os cabeçalhos

            for line in line_refactored_matrix:  # lê cada linha da estrutura gerada
                # separa em uma nova lista de acordo com o head e adiciona autenticação
                for head, column in enumerate(line):

                    # Adiciona autenticações
                    if count_w == self.char_a1_pos:
                        temp_mat.append(self.char_a1)
                        count_w += 1
                    elif count_w == self.char_a2_pos:
                        temp_mat.append(self.char_a2)
                        count_w += 1

                    # se é a coluna alvo
                    if head == i:
                        if len(temp_mat) == 5:
                            encrypted_message.append(temp_mat)  # adiciona a linha
                            temp_mat = []

                        temp_mat.append(column)  # adiciona caractere
                        count_w += 1

                    if len(temp_mat) == 5:
                        encrypted_message.append(temp_mat)  # adiciona linha
                        temp_mat = []

        encrypted_message = self.lists_to_string(encrypted_message)

        return {
            "status": "success",
            "message": encrypted_message.strip().upper(),
        }

    def decrypt(self) -> dict[str, str]:
        """Realiza a descriptografia da mensagem inicializada

        Returns:
            dict ("status": str, "message": str): Status da operação, mensagem de retorno
        """

        autenticated_message = self.autenticate_message(self.message)

        if autenticated_message[1] is False:
            return {"status": "fail", "message": "Autenticação Invalida"}

        first_key = self.convert_key(self.first_keyword)
        second_key = self.convert_key(self.second_keyword)
        first_key_indexes = self.enumerate_indexes(first_key)
        second_key_indexes = self.enumerate_indexes(second_key)

        # -----------------------------------------------------------
        # Descrição:
        # Gera uma matriz com a quantidade de caracteres da mensagem
        # e com maximo de colunas igual à chave criptografica.
        # * Usada para estruturar a descriptografia coluna a coluna
        # -----------------------------------------------------------
        matrix = self.generate_matrix(autenticated_message[0], first_key, blank=True)

        reverse_key, matrix_refactored = self.matrix_refactory_by_index(matrix, second_key_indexes)
        # -----------------------------------------------------------
        # Descrição:
        # Percorre toda a mensagem letra por letra, verifica
        # a coluna de cada linha e preenche a primeira linha
        # a estar com a coluna vazia.
        # Interrompe o loop toda vez que preencher
        # -----------------------------------------------------------
        column_key = 0  # Contador para definir a coluna alvo

        for _, char in enumerate(autenticated_message[0]):

            # Verifica se ainda há posição disponivel na coluna
            found = False
            for lines_check in matrix_refactored:
                if len(lines_check) >= (first_key_indexes[column_key] + 1):
                    if "" == lines_check[first_key_indexes[column_key]]:
                        found = True
                        break

            # Troca a coluna alvo se não localizar posição vazia
            column_key = column_key + 1 if found is False else column_key

            # preenche a primeira coluna da linha que estiver vazia
            for _, line in enumerate(matrix_refactored):

                if len(line) > first_key_indexes[column_key]:
                    if (line[first_key_indexes[column_key]]) == "":
                        line[first_key_indexes[column_key]] = char
                        break

        _, decrypted_message = self.matrix_refactory_by_index(
            matrix_refactored, self.enumerate_indexes(reverse_key)
        )

        # Converte a matriz em string
        decrypted_message = self.lists_to_string(decrypted_message).replace(" ", "")
        return {"status": "success", "message": decrypted_message}


if __name__ == "__main__":
    ##################################################################
    # Criado testes unitários para testar o código de forma dinamica #
    #                Não utilizar Módulo diretamente                 #
    ##################################################################
    pass
