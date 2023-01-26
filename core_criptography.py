"""Modulo principal de criptografia"""

from unidecode import unidecode


class CoreCriptography:
    """Responsável pelo controle da criptografia"""

    def __init__(self, char_au: dict[str, tuple[str, int]]):
        """Inicializacao da classe"""

        if char_au["char_a1"][1] == char_au["char_a2"][1]:
            raise ValueError("Autenticação com posição duplicada!")

        self.char_a1 = char_au["char_a1"][0]
        self.char_a1_pos = int(char_au["char_a1"][1])

        self.char_a2 = char_au["char_a2"][0]
        self.char_a2_pos = int(char_au["char_a2"][1])

    def convert_key(self, keyword: str) -> list[int]:
        """
        Retorna uma lista numérica representando a posição
        alfabética de cada caractere de uma palavra especifica.

        Parametros:
            keyword (str): Palavra única

        Retorno:
            keyword_order (list[int]): lista numérica da ordem alfabética
        """

        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

        keyword = keyword.lower()
        keyword_order = [0 for _ in range(len(keyword))]  # lista de zeros
        keyword_lower = keyword

        count = 1
        for letter in alphabet:  # percorre o alfabeto
            for index, char in enumerate(keyword_lower):  # percorre a palavra
                if letter == char:
                    keyword_order[index] = count  # substitui 0 pela posição
                    count += 1  # aumenta o contador

        return keyword_order

    def prepare_text(self, message: str, gap=2, base=5, ghost="z") -> str:
        """
        Prepara a mensagem, adicionando as letras mortas ao final, removendo
        os caracteres especiais e espaços.

        Parametros:
            message (str): Mensagem desejada
            gap (int): Quantidade de caracteres para considerar a mais no calculo,
            util para inserir novos caracteres posteriormente.
            base (int): Multiplo de referência para formatar a mensagem com caracteres
            fantasmas.
            ghost (str): caractere fantasma comum

        Retorno:
            message (str): Mensagem no formatada de acordo com parametros
        """

        if len(ghost) > 1:
            raise ValueError("ghost não é um caractere único")

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
        """Transforma as listas de uma lista, em palavras individuais"""

        message = ""
        for lists in list_message:
            for head, char in enumerate(lists):
                if head == 0:
                    message += " "
                message += char

        return message

    def generate_matrix(
        self, message: str, key: list[int], blank=False
    ) -> list[list[str]]:
        """Cria uma matriz com maximo de colunas de uma chave especifica"""

        matrix = []  # matriz final
        temp_mat = []  # matriz temporaria

        for head, char in enumerate(message):
            if blank:
                temp_mat.append("")
            else:
                temp_mat.append(char)

            # Registra linha na matriz final caso chegue ao tamanho em colunas
            if len(temp_mat) == max(key) or head + 1 == len(message):
                matrix.append(temp_mat)
                temp_mat = []

        return matrix

    def enumerate_indexes(self, key: list[int]) -> list[int]:
        """Retorna os indices em ordem crescente de uma lista de inteiros"""
        return [i[0] for i in sorted(enumerate(key), key=lambda x: x[1])]

    def autenticate_message(self, message: str) -> tuple[str, bool]:
        """
        Realiza a autenticação das duas letras nas posições especificas

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


if __name__ == "__main__":
    ##################################################################
    # Criado testes unitários para testar o código de forma dinamica #
    #                Não utilizar Módulo diretamente                 #
    ##################################################################
    pass
