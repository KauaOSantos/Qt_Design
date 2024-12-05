import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio11 import Ui_MainWindow 

class main_exercicio_11(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonCalcular.clicked.connect(self.calcularPotencia)
        
    def calcularPotencia(self):
        try:
            base = int(self.ui.lineEditBase.text())
            expoente = int(self.ui.lineEditExpoente.text())

            resultado = base ** expoente

            self.ui.labelResultado.setText(f"Resultado: {resultado}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira números válidos.")
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exercicio_11()
    janela.show()
    sys.exit(app.exec_())