"""Modulo de interface da criptografia"""

import re
import tkinter as tk
from tkinter import ttk

# Modulos locais
from src.modules.simple_cypher import SimpleCypher
from src.modules.pair_cypher import PairCypher


class InitialFrame(ttk.Frame):
    """Interface de Criptografia

    Parameters
    ----------
    ttk : Frame()
        root de acesso da interface do tkinter
    """

    OPTIONS = {"padx": 5, "pady": 5}

    def __init__(self, container):
        super().__init__(container)

        # ----------------------------------------------------
        # Seleção do tipo de chave criptografica e de modo
        # ----------------------------------------------------

        self.operation = tk.StringVar()
        self.operation.set("Criptografar")
        self.operation_combobox = self.operation_combobox_field()

        self.cript_type = tk.StringVar(value="Chave Simples")
        self.cript_label = self.keyword_type_label()
        self.criptography_type = self.keyword_type_combobox()

        # ---------------------------------------------------
        # Grid para as chaves criptograficas
        # ---------------------------------------------------

        # -----------------
        # Primeira chave
        # -----------------
        self.first_keyword = tk.StringVar()
        self.key_1_label = self.keyword_1_label()
        self.keyword_1 = self.keyword_1_entry()

        # -----------------
        # Segunda chave
        # -----------------
        self.second_keyword = tk.StringVar()
        self.key_2_label = self.keyword_1_label()
        self.keyword_2 = self.keyword_2_entry()

        # ---------------------------------------------------
        # Grid das letras de autenticação
        # ---------------------------------------------------

        # -----------------
        # Primeira letra
        # -----------------
        self.first_au = tk.StringVar()
        self.first_au_pos = tk.StringVar()
        self.first_autentication_label = self.first_auth_label()
        self.first_autentication = self.first_auth_entry()
        self.first_au_pos_box = self.first_auth_combobox()

        # -----------------
        # Segunda letra
        # -----------------
        self.second_au = tk.StringVar()
        self.second_au_pos = tk.StringVar()
        self.second_autentication_label = self.second_auth_label()
        self.second_autentication = self.second_auth_entry()
        self.second_au_pos_box = self.second_auth_combobox()

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
        self.message_output.grid(column=2, row=6, columnspan=12, sticky=tk.W, padx=5)

        # ----------------------------------------------------
        # Botão de execução
        # ----------------------------------------------------

        self.execute = ttk.Button(self, text="Executar", command=self.execute_cypher)
        self.execute.grid(column=0, row=7, sticky=tk.EW, **self.OPTIONS)

        self.clear = ttk.Button(self, text="Limpar", command=self.clear_interface)
        self.clear.grid(column=1, row=7, sticky=tk.W, **self.OPTIONS)

        self.status = ttk.Label(self, text="", foreground="red", font=("bold", 11))
        self.status.grid(column=2, row=7, sticky=tk.E, columnspan=12, **self.OPTIONS)

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

    def operation_combobox_field(self):
        """Combobox para ação de criptografia ou descriptografia"""

        operation_selection = ttk.Combobox(self, textvariable=self.operation)
        operation_selection["values"] = ("Criptografar", "Descriptografar")
        operation_selection["state"] = "readonly"
        operation_selection.grid(column=0, row=4, columnspan=2, sticky=tk.EW, **self.OPTIONS)

        return operation_selection

    # ----------------------------------------------------
    #  Interface da Chave Criptografica
    # ----------------------------------------------------

    def keyword_type_label(self):
        """Label para o tipo de chave criptografica"""

        label = ttk.Label(self, text="Tipo de Chave:")
        label.grid(column=0, row=0, sticky=tk.W, **self.OPTIONS)
        return label

    def keyword_type_combobox(self):
        """Combobox para o tipo de chave criptografica"""

        criptography_type = ttk.Combobox(self, textvariable=self.cript_type)
        criptography_type["values"] = ("Chave Simples", "Chave Dupla")
        criptography_type["state"] = "readonly"
        criptography_type.grid(column=1, row=0, sticky=tk.E, **self.OPTIONS)
        return criptography_type

    def keyword_1_label(self):
        """Label da primeira chave criptografica"""

        keyword_1_label = ttk.Label(self, text="Primeira Chave:")
        keyword_1_label.grid(column=0, row=1, sticky=tk.W, **self.OPTIONS)
        return keyword_1_label

    def keyword_1_entry(self):
        """Entry da primeira chave criptografica"""

        keyword_1 = ttk.Entry(self, textvariable=self.first_keyword)
        keyword_1.grid(column=1, row=1, sticky=tk.E, **self.OPTIONS)
        return keyword_1

    def keyword_2_label(self):
        """Label da segunda chave criptografica"""

        keyword_2_label = ttk.Label(self, text="Segunda Chave:")
        keyword_2_label.grid(column=0, row=2, sticky=tk.W, **self.OPTIONS)
        return keyword_2_label

    def keyword_2_entry(self):
        """Entry da segunda chave criptografica"""

        keyword_2 = ttk.Entry(self, textvariable=self.second_keyword)
        keyword_2.grid(column=1, row=2, sticky=tk.E, **self.OPTIONS)
        keyword_2["state"] = "readonly"
        return keyword_2

    # ----------------------------------------------------
    #  Interfaces de Autenticação
    # ----------------------------------------------------

    # -----------------------
    #  Segunda Auth
    # -----------------------

    def first_auth_label(self):
        """Label da primeira letra de autenticação"""

        label = ttk.Label(self, text="Primeira Letra:")
        label.grid(column=2, row=0, sticky=tk.W, **self.OPTIONS)
        return label

    def first_auth_entry(self):
        """Entry da primeira letra de autenticação"""

        first_auth_entry = ttk.Entry(self, textvariable=self.first_au, justify="center", width=3)
        first_auth_entry.grid(column=3, row=0, sticky=tk.E, **self.OPTIONS)
        return first_auth_entry

    def first_auth_combobox(self):
        """Combobox da segunda letra de autenticação"""

        first_au_box = ttk.Combobox(self, textvariable=self.first_au_pos, justify="center", width=3)
        first_au_box["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        first_au_box["state"] = "readonly"
        first_au_box.grid(column=4, row=0, columnspan=1, sticky=tk.W, **self.OPTIONS)
        return first_au_box

    # -----------------------
    #  Segunda Auth
    # -----------------------

    def second_auth_label(self):
        """Label da segunda letra de autenticação"""

        label = ttk.Label(self, text="Segunda Letra:")
        label.grid(column=2, row=1, sticky=tk.W, **self.OPTIONS)
        return label

    def second_auth_entry(self):
        """Entry da segunda letra de autenticação"""

        entry = ttk.Entry(self, textvariable=self.second_au, justify="center", width=3)
        entry.grid(column=3, row=1, sticky=tk.E, **self.OPTIONS)
        return entry

    def second_auth_combobox(self):
        """Combobox da segunda letra de autenticação"""

        combobox = ttk.Combobox(self, textvariable=self.second_au_pos, justify="center", width=3)
        combobox["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        combobox["state"] = "readonly"
        combobox.grid(column=4, row=1, columnspan=1, sticky=tk.W, **self.OPTIONS)
        return combobox

    # ----------------------------------------------------
    # Eventos e Validações (Metodos)
    # ----------------------------------------------------

    def cript_type_changed(self, event):
        """Evento de mudanças do tipo de criptografia"""
        print(event)
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

    def change_status(self, message, color="green"):
        """Altera o status do retorno

        Parameters
        ----------
        message : str
            Mensagem de status desejada
        """
        self.status.config(text=message, foreground=color)

    def execute_cypher(self):
        """Evento de execução do botão self.execute"""

        option = self.operation.get()
        cypher_type = self.criptography_type.get()

        if option == "Criptografar":
            if cypher_type == "Chave Simples":

                validations = self.validate_params()
                if validations["status"] is False:
                    self.change_status(validations["values"], "red")
                    return
                message, keyword, char_au = validations["values"]

                cypher = SimpleCypher(char_au, message, keyword)
                encrypted_message, status = cypher.encrypt()

                self.message_output.delete("1.0", "end")
                if status is True:
                    self.change_status("Criptografado com sucesso!", "green")
                    self.message_output.insert("1.0", encrypted_message)
                else:
                    self.change_status(encrypted_message, "red")

            elif cypher_type == "Chave Dupla":

                validations = self.validate_params()
                if validations["status"] is False:
                    print(validations["values"])

                message, keywords, char_au = validations["values"]

                cypher = PairCypher(char_au, message, keywords[0], keywords[1])

                encrypted_message = cypher.encrypt()

                self.message_output.delete("1.0", "end")
                if encrypted_message["status"] == "success":
                    self.change_status("Criptografado com sucesso!", "green")
                    self.message_output.insert("1.0", encrypted_message["message"])
                else:
                    self.change_status(encrypted_message["message"], "red")

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
                if decrypted_message["status"] == "success":
                    self.change_status("Descriptografado com sucesso!", "green")
                    self.message_output.insert("1.0", decrypted_message["message"])
                else:
                    self.change_status(decrypted_message["message"], "red")

            elif cypher_type == "Chave Dupla":
                validations = self.validate_params()
                if validations["status"] is False:
                    print(validations["values"])

                message, keywords, char_au = validations["values"]

                cypher = PairCypher(char_au, message, keywords[0], keywords[1])

                decrypted_message = cypher.decrypt()

                self.message_output.delete("1.0", "end")
                if decrypted_message["status"] == "success":
                    self.change_status("Descriptografado com sucesso!", "green")
                    self.message_output.insert("1.0", decrypted_message["message"])
                else:
                    self.change_status(decrypted_message["message"], "red")
        else:
            pass

    def clear_interface(self):
        """Reseta todos os campos preenchidos"""

        self.cript_type.set("Chave Simples")
        self.cript_type_changed(None)
        self.operation.set("Criptografar")
        self.first_autentication.delete(0, tk.END)
        self.second_autentication.delete(0, tk.END)
        self.first_au_pos_box.set("")
        self.second_au_pos_box.set("")
        self.keyword_1.delete(0, tk.END)
        self.keyword_2.delete(0, tk.END)
        self.message_input.delete("1.0", "end")
        self.message_output.delete("1.0", "end")
        self.change_status("", "green")


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
        self.geometry("690x380")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.iconbitmap("src/img/comandos.ico")


if __name__ == "__main__":
    pass
