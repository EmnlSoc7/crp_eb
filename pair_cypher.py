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

        final_message = ""
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
