import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from exercicio15 import Ui_MainWindow 

class MainExercicio15(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonVerificar.clicked.connect(self.iniciar_contagem)

        self.contador = 10
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_contagem)

    def iniciar_contagem(self):
        self.contador = 10 
        self.ui.labelResultado.setText(str(self.contador))
        self.timer.start(1000)

    def atualizar_contagem(self):
        self.contador -= 1
        if self.contador >= 0:
            self.ui.labelResultado.setText(str(self.contador))
        else:
            self.timer.stop()  
            self.ui.labelResultado.setText("Fim da sequência")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainExercicio15()
    janela.show()
    sys.exit(app.exec_())