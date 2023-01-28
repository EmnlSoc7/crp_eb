"""Execução principal da aplicação"""

from src.interface.main import App, InitialFrame

if __name__ == "__main__":

    # ------------------------------
    # Executa interface principal
    # ------------------------------

    application = App()

    InitialFrame(application)
    application.mainloop()
