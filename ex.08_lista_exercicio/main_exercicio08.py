import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio08 import Ui_MainWindow 

class MainExerc08(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.verificarQuadrado)

    def verificarQuadrado(self):
        try:
            num = int(self.ui.lineEditNum_1.text())
            quadrado = num ** 2
            
            self.ui.labelResultado.setText(f"O quadrado de {num} é: {quadrado}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    janela = MainExerc08()
    janela.show()
    sys.exit(app.exec_())