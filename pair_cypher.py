"""Módulo de criptografia de chave dupla"""

from typing import Union
from core_criptography import CoreCriptography


class PairCypher(CoreCriptography):
    def __init__(
        self,
        char_au: dict[str, tuple[str, int], str, tuple[str, int]],
        message: str,
        first_keyword: Union[str, int],
        second_keyword: Union[str, int],
    ):
        super().__init__(char_au)
        self.message = message
        self.first_keyword = str(first_keyword)
        self.second_keyword = str(second_keyword)

    def matrix_refactory_by_index(self, matrix: list, key_indexes: list):
        """Realiza a refatoração de uma matriz de acordo com a lista de headers fornecidas

        Args:
            matrix (list): Matriz inicial
            key_indexes (list): lista numérica da ordem dos indices

        Returns:
            list: Matriz Inicial formatada de acordo com a ordem dos indices
        """
        line_encrypted_matrix = []  # matriz na ordem da chave secundária
        for head_index in key_indexes:
            if len(matrix) - 1 >= head_index:
                line_encrypted_matrix.append(matrix[head_index])

        return line_encrypted_matrix

    def encrypt(self) -> tuple[str, bool]:
        """
        Realiza a criptografia da mensagem com as chaves e letras
        de autenticação fornecidas

        Returns:
            tuple (str, bool): Mensagem de retorno, Sucesso/Falha
        """
        message = self.prepare_text(self.message)

        first_key = self.convert_key(self.first_keyword)
        second_key = self.convert_key(self.second_keyword)

        # Verifica se a mensagem é maior que a quantidade de caracteres
        if len(message) >= (len(first_key) * len(second_key)):
            return ("FAILED", False)

        matrix = self.generate_matrix(message, first_key)

        first_key_indexes = self.enumerate_indexes(first_key)
        second_key_indexes = self.enumerate_indexes(second_key)

        temp_mat = []  # responsável pelas listas criptografadas
        encrypted_message = []  # lista de listas final da criptografia
        count_w = 1

        line_refactored_matrix = self.matrix_refactory_by_index(
            matrix, second_key_indexes
        )

        for i in first_key_indexes:  # percorre os cabeçalhos

            for line in line_refactored_matrix:  # lê cada linha da estrutura gerada
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

        encrypted_message = self.lists_to_string(encrypted_message)
        return (encrypted_message.strip().upper(), True)

    def decrypt(self):
        """Realiza a descriptografia da mensagem inicializada"""

        final_message = ""
        return (final_message.strip().upper(), True)


if __name__ == "__main__":
    ##################################################################
    # Criado testes unitários para testar o código de forma dinamica #
    #                Não utilizar Módulo diretamente                 #
    ##################################################################
    pass
