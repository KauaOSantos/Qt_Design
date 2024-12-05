import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio12 import Ui_MainWindow 

class main_exercicio_12(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.verificarMaior)
        
    def verificarMaior(self):
        try:
            num1 = int(self.ui.lineEditNum_1.text())
            num2 = int(self.ui.lineEditNum_2.text())
            num3 = int(self.ui.lineEditNum_3.text())

            maior = max(num1, num2, num3)

            self.ui.labelResultado.setText(f"O maior número é: {maior}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira números válidos.")
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exercicio_12()
    janela.show()
    sys.exit(app.exec_())
