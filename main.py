"""Execução principal da aplicação"""

import os
from src.interface.main import App, InitialFrame

if __name__ == "__main__":

    # ------------------------------
    # Executa interface principal
    # ------------------------------

    application = App()

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    application.iconbitmap(f"{ROOT_DIR}\\src\\img\\jaguar.ico")
    InitialFrame(application)
    application.mainloop()
