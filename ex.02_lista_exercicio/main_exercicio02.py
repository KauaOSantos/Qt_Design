import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from exercicio02 import Ui_MainWindow

class main_exercicio02(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #conectar o botão a função que realiza a verificação 
        self.ui.pushButtonVerificar.clicked.connect(self.verificar_numero)
        
    def verificar_numero(self):
        try:
            num = int(self.ui.lineEditNum.text())
            if num % 2 == 0:
                resultado = "par"
            else:
                resultado = "ímpar"
            self.ui.labelResultado.setText(f"O seu número é: {resultado}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira números válidos!")
            
if __name__ == "__main__":
    app=QApplication(sys.argv)
    janela = main_exercicio02()
    janela.show()
    sys.exit(app.exec_())