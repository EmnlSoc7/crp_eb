"""Execução principal da aplicação"""

from src.interface.main import App, KeywordsFrame

if __name__ == "__main__":

    # ------------------------------
    # Executa interface principal
    # ------------------------------

    application = App()

    KeywordsFrame(application)
    application.mainloop()
