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

    def encrypt(self):
        """
        Realiza a criptografia da mensagem inicializada
        Refência de execução
        limite maximo de caracteres definido pela area da chave 1
        e chave 2.

        8 * 8 = 64 (60)

        A cada coluna é percorrido todas as linhas na sequência,
        definida pelo total de caracteres da mensagem
        Necessário gerar Matriz de acordo com o tamanho da mensagem
        """
        message = self.prepare_text(self.message)

        first_key = self.convert_key(self.first_keyword)
        second_key = self.convert_key(self.second_keyword)

        # Verifica se a mensagem é maior que a quantidade de caracteres
        if len(message) >= (len(first_key) * len(second_key)):
            return ("FAILED", True)

        matrix = self.generate_matrix(message, first_key)

        print(matrix)

        first_key_indexes = self.enumerate_indexes(first_key)
        second_key_indexes = self.enumerate_indexes(second_key)

        temp_mat = []  # responsável pelas listas criptografadas
        line_encrypted_matrix = []
        encrypted_message = []  # lista de listas final da criptografia
        count_w = 1

        for head_index in second_key_indexes:
            if len(matrix) - 1 >= head_index:
                line_encrypted_matrix.append(matrix[head_index])

        for i in first_key_indexes:  # percorre os cabeçalhos

            for line in line_encrypted_matrix:  # lê cada linha da estrutura gerada
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
