import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio07 import Ui_MainWindow 

class main_exercicio_07(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonCalcular.clicked.connect(self.calcularMedia)

    def calcularMedia(self):
        try:
            num1 = int(self.ui.lineEditNum_1.text())
            num2 = int(self.ui.lineEditNum_2.text())
            num3 = int(self.ui.lineEditNum_3.text())
            
            if num1 < 0 or num2 < 0 or num3 < 0:
                self.ui.labelResultado.setText("Por favor, insira apenas números inteiros.")
            else:
                resultado = (num1 + num2 + num3) / 3
                self.ui.labelResultado.setText(f"A média dos números informados é: {resultado:.2f}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira números válidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exercicio_07()
    janela.show()
    sys.exit(app.exec_())