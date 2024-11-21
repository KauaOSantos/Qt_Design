import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio05 import Ui_MainWindow 

class MainExerc05(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.verificarNumero)

    def verificarNumero(self):
        try:
            n = int(self.ui.lineEditNum.text())
            if n < 2:
                self.ui.labelResultado.setText(f"{n} não é um número primo!")
            elif all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
                self.ui.labelResultado.setText(f"{n} é um número primo!")
            else:
                self.ui.labelResultado.setText(f"{n} não é um número primo!")
        except ValueError:
            self.ui.labelResultado.setText("Insira um número válido!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainExerc05()
    janela.show()
    sys.exit(app.exec_())