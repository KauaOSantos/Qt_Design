import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio13 import Ui_MainWindow  

class main_exercicio_13(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.verificarIntervalo)

    def verificarIntervalo(self):
        try:
            numero = int(self.ui.lineEditNum.text())

            if 10 <= numero <= 20:
                self.ui.labelResultado.setText(f"O número {numero} está entre 10 e 20.")
            else:
                self.ui.labelResultado.setText(f"O número {numero} não está entre 10 e 20.")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exercicio_13()
    janela.show()
    sys.exit(app.exec_())
