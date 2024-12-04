import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio09 import Ui_MainWindow 

class main_exercicio_09(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.calcularTabuada)

    def calcularTabuada(self):
        try:
            num = int(self.ui.lineEditNum.text())

            tabuada = [f"{num} x {i} = {num * i}" for i in range(1, 11)]

            resultado = "\n".join(tabuada)
            self.ui.labelResultado.setText(resultado)
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exercicio_09()
    janela.show()
    sys.exit(app.exec_())       