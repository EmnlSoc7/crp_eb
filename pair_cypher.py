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
        self.fist_keyword = str(first_keyword)
        self.second_keyword = str(second_keyword)

    def encrypt(self):
        """Realiza a criptografia da mensagem inicializada"""

        final_message = ""
        return (final_message.strip().upper(), True)

    def decrypt(self):
        """Realiza a descriptografia da mensagem inicializada"""

        final_message = ""
        return (final_message.strip().upper(), True)
