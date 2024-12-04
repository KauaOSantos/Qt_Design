import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio02 import Ui_MainWindow


class main_exercicio_02(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.verificaIdade)

    def verificaIdade(self):  # Agora está dentro da classe
        try:
            idade = int(self.ui.lineEditIdade.text())

            if idade < 0:
                self.ui.labelResultado.setText("A idade não pode ser negativa.")
            elif 0 <= idade < 18:
                self.ui.labelResultado.setText("Menor de idade.")
            else:
                self.ui.labelResultado.setText("Maior de idade.")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira apenas números inteiros.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exercicio_02()
    janela.show()
    sys.exit(app.exec_())
