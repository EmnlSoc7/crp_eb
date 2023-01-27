"""Modulo de interface da criptografia"""

import re
import tkinter as tk
from tkinter import ttk

# Modulos locais
from simple_cypher import SimpleCypher
from pair_cypher import PairCypher


class KeywordsFrame(ttk.Frame):
    """Interface de Criptografia

    Parameters
    ----------
    ttk : Frame()
        root de acesso da interface do tkinter
    """

    def __init__(self, container):
        super().__init__(container)

        # ----------------------------------------------------
        # Opções Padrões
        # ----------------------------------------------------
        options = {"padx": 5, "pady": 5}

        # ----------------------------------------------------
        # Seleção do tipo de chave criptografica e de modo
        # ----------------------------------------------------

        self.cript_label = ttk.Label(self, text="Tipo de Chave:")
        self.cript_label.grid(column=0, row=0, sticky=tk.W, **options)

        self.cript_type = tk.StringVar(value="Chave Simples")

        self.criptography_type = ttk.Combobox(self, textvariable=self.cript_type)
        self.criptography_type["values"] = ("Chave Simples", "Chave Dupla")
        self.criptography_type["state"] = "readonly"
        self.criptography_type.grid(column=1, row=0, sticky=tk.E, **options)

        self.operation = tk.StringVar()
        self.operation.set("Criptografar")
        self.operation_selection = ttk.Combobox(self, textvariable=self.operation)
        self.operation_selection["values"] = ("Criptografar", "Descriptografar")
        self.operation_selection["state"] = "readonly"
        self.operation_selection.grid(column=0, row=4, columnspan=2, sticky=tk.EW, **options)

        # ---------------------------------------------------
        # Grid para as chaves criptograficas
        # ---------------------------------------------------

        # -----------------
        # Primeira chave
        # -----------------
        self.first_keyword = tk.StringVar()
        self.keyword_1_label = ttk.Label(self, text="Primeira Chave:")
        self.keyword_1_label.grid(column=0, row=1, sticky=tk.W, **options)

        self.keyword_1 = ttk.Entry(self, textvariable=self.first_keyword)
        self.keyword_1.grid(column=1, row=1, sticky=tk.E, **options)

        # -----------------
        # Segunda chave
        # -----------------
        self.second_keyword = tk.StringVar()
        self.keyword_2_label = ttk.Label(self, text="Segunda Chave:")
        self.keyword_2_label.grid(column=0, row=2, sticky=tk.W, **options)

        self.keyword_2 = ttk.Entry(self, textvariable=self.second_keyword)
        self.keyword_2.grid(column=1, row=2, sticky=tk.E, **options)
        self.keyword_2["state"] = "readonly"

        # ---------------------------------------------------
        # Grid das letras de autenticação
        # ---------------------------------------------------

        # -----------------
        # primeira letra
        # -----------------
        self.first_au = tk.StringVar()
        self.first_au_pos = tk.StringVar()
        self.first_autentication_label = ttk.Label(self, text="Primeira Letra:")
        self.first_autentication_label.grid(column=2, row=0, sticky=tk.W, **options)

        self.first_autentication = ttk.Entry(
            self, textvariable=self.first_au, justify="center", width=3
        )
        self.first_autentication.grid(column=3, row=0, sticky=tk.W, **options)

        self.first_au_pos_box = ttk.Combobox(
            self, textvariable=self.first_au_pos, justify="center", width=3
        )
        self.first_au_pos_box["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.first_au_pos_box["state"] = "readonly"
        self.first_au_pos_box.grid(column=4, row=0, columnspan=1, sticky=tk.W, **options)

        # -----------------
        # segunda letra
        # -----------------
        self.second_au = tk.StringVar()
        self.second_au_pos = tk.StringVar()
        self.second_autentication_label = ttk.Label(self, text="Segunda Letra:")
        self.second_autentication_label.grid(column=2, row=1, sticky=tk.W, **options)

        self.second_autentication = ttk.Entry(
            self, textvariable=self.second_au, justify="center", width=3
        )
        self.second_autentication.grid(column=3, row=1, sticky=tk.W, **options)

        self.second_au_pos_box = ttk.Combobox(
            self, textvariable=self.second_au_pos, justify="center", width=3
        )
        self.second_au_pos_box["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.second_au_pos_box["state"] = "readonly"
        self.second_au_pos_box.grid(column=4, row=1, columnspan=1, sticky=tk.W, **options)

        # ----------------------------------------------------
        # Mensagens de entrada e saida
        # ----------------------------------------------------

        self.message_input_label = ttk.Label(self, text="Mensagem:")
        self.message_input_label.grid(column=0, row=5, sticky=tk.W, padx=5)
        self.message_input = tk.Text(self, width=40, height=10, relief="solid")
        self.message_input.grid(column=0, row=6, columnspan=2, sticky=tk.W, padx=5)

        self.message_output_label = ttk.Label(self, text="Saida:")
        self.message_output_label.grid(column=2, row=5, sticky=tk.W, padx=5)
        self.message_output = tk.Text(self, width=40, height=10, relief="solid")
        self.message_output.grid(column=2, row=6, columnspan=18, sticky=tk.W, padx=5)

        # ----------------------------------------------------
        # Botão de execução
        # ----------------------------------------------------

        self.execute = ttk.Button(self, text="Executar", command=self.execute_cypher)
        self.execute.grid(column=0, row=7, columnspan=2, sticky=tk.W, **options)

        # ----------------------------------------------------
        # Gatilhos de Eventos
        # ----------------------------------------------------

        ## Desabilita/Habilita campo da segunda chave
        self.criptography_type.bind("<<ComboboxSelected>>", self.cript_type_changed)

        # Controla estado das letras de autenticação
        self.first_au.trace("w", lambda *args: self.character_formatting(self.first_au))
        self.second_au.trace("w", lambda *args: self.character_formatting(self.second_au))

        # ----------------------------------------------------
        # Execução da Grid
        # ----------------------------------------------------
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    # ----------------------------------------------------
    # Eventos e Validações (Metodos)
    # ----------------------------------------------------

    def cript_type_changed(self, event):
        """Evento de mudanças do tipo de criptografia"""

        cript_choice = self.cript_type.get()

        if cript_choice == "Chave Dupla":
            self.keyword_2["state"] = "normal"
        elif cript_choice == "Chave Simples":
            self.keyword_2.delete(0, tk.END)
            self.keyword_2["state"] = "readonly"

    def character_formatting(self, entry_text):
        """Realiza a formatação de caracter unico

        Parameters
        ----------
        entry_text : StringVar()
            Realizado a formatação da StringVar() como caractere unico
        """
        entry_text.set(entry_text.get().upper())
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[-1])

    def validate_params(self) -> dict:
        """Realiza a validação dos parametros selecionados

        Returns
        -------
        dict : 'status': bool, 'values': tuple(str | str, str, str)
            Retorna tupla com a mensagem de erro ou os dados completos
        """
        # --------------------------
        # Validações
        # --------------------------
        if len(self.message_input.get("1.0", "end").strip()) <= 0:
            return {"status": False, "values": ("Mensagem Invalida")}
        if len(self.keyword_1.get()) <= 0:
            return {"status": False, "values": ("Chave Invalida")}

        if self.cript_type.get() == "Chave Dupla" and len(self.keyword_2.get()) <= 0:
            return {"status": False, "values": ("Chave Dupla Invalida")}

        if (
            len(self.first_au.get()) <= 0
            or len(self.second_au.get()) <= 0
            or len(self.first_au_pos.get()) <= 0
            or len(self.second_au_pos.get()) <= 0
        ):
            return {"status": False, "values": ("Autenticação Invalida")}

        # --------------------------
        # Transformações
        # --------------------------
        message = self.message_input.get("1.0", "end").strip()
        message = re.sub(r"(\n[ \t]*)+", "\n", message)

        if self.cript_type.get() == "Chave Dupla":
            keywords = (self.keyword_1.get(), self.keyword_2.get())
        else:
            keywords = self.keyword_1.get()

        auth_1 = self.first_au.get()
        auth_1_pos = self.first_au_pos.get()
        auth_2 = self.second_au.get()
        auth_2_pos = self.second_au_pos.get()

        char_au = {
            "char_a1": (auth_1, int(auth_1_pos)),
            "char_a2": (auth_2, int(auth_2_pos)),
        }

        return {"status": True, "values": (message, keywords, char_au)}

    # ----------------------------------------------------
    # Execuções exceto eventos
    # ----------------------------------------------------

    def execute_cypher(self):
        """Evento de execução do botão self.execute"""

        option = self.operation_selection.get()
        cypher_type = self.criptography_type.get()

        if option == "Criptografar":
            if cypher_type == "Chave Simples":

                validations = self.validate_params()
                if validations["status"] is False:
                    print(validations["values"])
                    return

                message, keyword, char_au = validations["values"]

                cypher = SimpleCypher(char_au, message, keyword)

                encrypted_message, _ = cypher.encrypt()
                self.message_output.delete("1.0", "end")
                self.message_output.insert("1.0", encrypted_message)

            elif cypher_type == "Chave Dupla":

                validations = self.validate_params()
                if validations["status"] is False:
                    print(validations["values"])

                message, keywords, char_au = validations["values"]

                cypher = PairCypher(char_au, message, keywords[0], keywords[1])

                encrypted_message = cypher.encrypt()
                self.message_output.delete("1.0", "end")
                self.message_output.insert("1.0", encrypted_message["message"])

        elif option == "Descriptografar":
            if cypher_type == "Chave Simples":

                validations = self.validate_params()
                if validations["status"] is False:
                    print(validations["values"])
                    return

                message, keyword, char_au = validations["values"]

                cypher = SimpleCypher(char_au, message, keyword)

                decrypted_message = cypher.decrypt()
                self.message_output.delete("1.0", "end")
                self.message_output.insert("1.0", decrypted_message["message"])

            elif cypher_type == "Chave Dupla":
                validations = self.validate_params()
                if validations["status"] is False:
                    print(validations["values"])

                message, keywords, char_au = validations["values"]

                cypher = PairCypher(char_au, message, keywords[0], keywords[1])

                decrypted_message = cypher.decrypt()
                self.message_output.delete("1.0", "end")
                self.message_output.insert("1.0", decrypted_message["message"])
        else:
            pass


class App(tk.Tk):
    """Metodo principal de execução da interface

    Parameters
    ----------
    tk : Tk()
        Modulo do tkinter
    """

    def __init__(self):
        super().__init__()

        self.title("Criptografia")
        self.geometry("700x600")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)


if __name__ == "__main__":
    app = App()
    KeywordsFrame(app)

    app.mainloop()
