import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio06 import Ui_MainWindow 

class MainExerc06(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.contarVogais)


    def contarVogais(self):
        texto = self.ui.lineEditPalavra.text()
        vogais = "aeiouAEIOU"
        contador = sum(1 for char in texto if char in vogais)
        self.ui.labelResultado.setText(f"A palavra '{texto}' tem {contador} vogal(is).")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainExerc06()
    janela.show()
    sys.exit(app.exec_())