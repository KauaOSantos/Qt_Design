import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio17 import Ui_MainWindow 

class MainExercicio17(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonVerificar.clicked.connect(self.soma)
        
    def soma(self):
        soma_impares = 0
        num = 1

        while num <= 50:
            if num % 2 != 0:
                soma_impares += num
            num += 1 

        self.ui.labelResultado.setText(f"A soma dos números ímpares de 1 a 50 é: {soma_impares}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainExercicio17()
    janela.show()
    sys.exit(app.exec_())