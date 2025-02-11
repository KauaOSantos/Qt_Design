import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pag1 import Ui_MainWindow as Ui_Pag1
from pag2 import Ui_MainWindow as Ui_Pag2

class main(QMainWindow):
    def __init__(self):
       super().__init__()
       self.ui = Ui_Pag1()
       self.ui.setupUi(self)
       self.ui.pushButton.clicked.connect(self.abrirSegundaTela)
       
    def abrirSegundaTela(self):
        self.segunda_tela = SegundaTela(self)
        self.segunda_tela.show()
        self.close()
        
class SegundaTela(QMainWindow):
    def __init__(self, main_window):
       super().__init__()
       self.ui = Ui_Pag2()
       self.ui.setupUi(self)
       self.main_window = main_window
       self.ui.pushButton.clicked.connect
       (self.voltarParaPrimeiraTela)
       
    def voltarParaPrimeiraTela(self):
        self.main_window.show()
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = main()
    main_window.show()
    sys.exit(app.exec_())