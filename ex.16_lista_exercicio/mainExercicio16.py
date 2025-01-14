import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio16 import Ui_MainWindow 

class MainExercicio16(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonVerificar.clicked.connect(self.soma)
        
    def soma(self):
        contador = 0
        
        for num in range (1,101):
            if num % 2 == 0:
                contador += 1
        
        self.ui.labelResultado.setText(f"A soma dos números pares que existem de 1 a 100 é: {contador}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainExercicio16()
    janela.show()
    sys.exit(app.exec_())