import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio14 import Ui_MainWindow  

class main_exercicio_14(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.verificarNumero)

    def verificarNumero(self):
        try:
            numero = int(self.ui.lineEditNum.text())

            if numero >= 1 :
                self.ui.labelResultado.setText(f"O número {numero} é positivo.")
            elif numero == 0:
                self.ui.labelResultado.setText(f"O número é {numero}.")
            else:
                self.ui.labelResultado.setText(f"O número {numero} é negativo.")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exercicio_14()
    janela.show()
    sys.exit(app.exec_())
