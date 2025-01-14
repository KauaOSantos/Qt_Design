import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio03 import Ui_MainWindow  

class main_exerc03(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonCalcular.clicked.connect(self.calcular_fatorial)
    
    def calcular_fatorial(self):
        try:
            num = int(self.ui.lineEditNum.text())
            if num < 0:
                self.ui.labelResultado.setText("Fatorial não é definido para números negativos.")
                return
            
            fatorial = 1
            for i in range(1, num + 1):
                fatorial *= i
            
            self.ui.labelResultado.setText(f"Resultado: {fatorial}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira um número válido!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = main_exerc03()
    janela.show()
    sys.exit(app.exec_())