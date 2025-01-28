from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from listaDeChamada import Ui_MainWindow  # Importa a interface gerada

class mainListaDeChamada(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.desabilitarCheckbox(self.checkBox_5)
        self.desabilitarCheckbox(self.checkBox_7)
        self.desabilitarCheckbox(self.checkBox_3)
        self.desabilitarCheckbox(self.checkBox_4)
        self.desabilitarCheckbox(self.checkBox_9)
        self.desabilitarCheckbox(self.checkBox_8)
        self.desabilitarCheckbox(self.checkBox_6)
        self.desabilitarCheckbox(self.checkBox_10)
        self.desabilitarCheckbox(self.checkBox_2)
        self.desabilitarCheckbox(self.checkBox)

    def desabilitarCheckbox(self, checkbox):
        checkbox.setStyleSheet("color: #ececec;")  

if __name__ == "__main__":
    app = QApplication([])
    window = mainListaDeChamada()
    window.show()
    app.exec_()