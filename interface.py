"""Interface de usuário"""

import tkinter as tk
from tkinter import ttk


class KeywordsFrame(ttk.Frame):
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

        # criptography_type.bind("<<ComboboxSelected>>", self.cript_defined)

        self.operation = tk.StringVar()
        self.operation.set("Criptografar")
        self.operation_selection = ttk.Combobox(self, textvariable=self.operation)
        self.operation_selection["values"] = ("Criptografar", "Descriptografar")
        self.operation_selection["state"] = "readonly"
        self.operation_selection.grid(
            column=0, row=4, columnspan=2, sticky=tk.EW, **options
        )

        # ---------------------------------------------------
        # Grid para as chaves criptograficas
        # ---------------------------------------------------

        # primeira chave
        self.first_keyword = tk.StringVar()
        self.keyword_1_label = ttk.Label(self, text="Primeira Chave:")
        self.keyword_1_label.grid(column=0, row=1, sticky=tk.W, **options)

        self.keyword_1 = ttk.Entry(self, textvariable=self.first_keyword)
        self.keyword_1.grid(column=1, row=1, sticky=tk.E, **options)

        # segunda chave
        self.second_keyword = tk.StringVar()
        self.keyword_2_label = ttk.Label(self, text="Segunda Chave:")
        self.keyword_2_label.grid(column=0, row=2, sticky=tk.W, **options)

        self.keyword_2 = ttk.Entry(self, textvariable=self.second_keyword)
        self.keyword_2.grid(column=1, row=2, sticky=tk.E, **options)
        self.keyword_2["state"] = "readonly"

        # ---------------------------------------------------
        # Grid para as chaves criptograficas
        # ---------------------------------------------------

        # primeira chave
        self.first_keyword = tk.StringVar()
        self.keyword_1_label = ttk.Label(self, text="Primeira Chave:")
        self.keyword_1_label.grid(column=0, row=1, sticky=tk.W, **options)

        self.keyword_1 = ttk.Entry(self, textvariable=self.first_keyword)
        self.keyword_1.grid(column=1, row=1, sticky=tk.E, **options)

        # segunda chave
        self.second_keyword = tk.StringVar()
        self.keyword_2_label = ttk.Label(self, text="Segunda Chave:")
        self.keyword_2_label.grid(column=0, row=2, sticky=tk.W, **options)

        self.keyword_2 = ttk.Entry(self, textvariable=self.second_keyword)
        self.keyword_2.grid(column=1, row=2, sticky=tk.E, **options)
        self.keyword_2["state"] = "readonly"

        # ---------------------------------------------------
        # Grid das letras de autenticação
        # ---------------------------------------------------

        # primeira letra
        self.first_au = tk.StringVar()
        self.first_au_pos = tk.StringVar()
        self.first_autentication_label = ttk.Label(self, text="Primeira Letra:")
        self.first_autentication_label.grid(column=2, row=0, sticky=tk.W, **options)

        self.first_autentication = ttk.Entry(self, textvariable=self.first_au, width=3)
        self.first_autentication.grid(column=3, row=0, sticky=tk.W, **options)

        self.first_au_pos_box = ttk.Combobox(self, textvariable=self.first_au_pos)
        self.first_au_pos_box["values"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.first_au_pos_box["state"] = "readonly"
        self.first_au_pos_box.grid(
            column=4, row=0, columnspan=1, sticky=tk.W, **options
        )

        # segunda letra
        self.second_au = tk.StringVar()
        self.second_autentication_label = ttk.Label(self, text="Segunda Chave:")
        self.second_autentication_label.grid(column=2, row=1, sticky=tk.W, **options)

        self.second_autentication = ttk.Entry(
            self, textvariable=self.second_au, width=3
        )
        self.second_autentication.grid(column=3, row=1, sticky=tk.W, **options)
        self.second_autentication["state"] = "readonly"

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
        # Eventos
        # ----------------------------------------------------

        ## Desabilita/Habilita campo da segunda chave
        self.criptography_type.bind("<<ComboboxSelected>>", self.cript_type_changed)

        # ----------------------------------------------------
        # Execução da Grid
        # ----------------------------------------------------
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def cript_type_changed(self, event):
        """Recebe o evento de alteração do tipo de criptografia"""

        cript_choice = self.cript_type.get()

        if cript_choice == "Chave Dupla":
            self.keyword_2["state"] = "normal"
        elif cript_choice == "Chave Simples":
            self.keyword_2.delete(0, tk.END)
            self.keyword_2["state"] = "readonly"

    def execute_cypher(self):
        pass


class App(tk.Tk):
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
