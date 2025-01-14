from PyQt5.QtWidgets import QApplication, QMainWindow
from listaDeMetas import Ui_MainWindow  # Importa a interface gerada

class mainListaDeMetas (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.add_meta)
        self.pushButton_2.clicked.connect(self.remove_meta)
        
    def add_meta(self):
        meta = self.lineEdit.text()
        if meta:
            self.listWidget.addItem(meta)
            self.lineEdit.clear()
            
    def remove_meta(self):
        selected_item = self.listWidget.currentRow()
        if selected_item >= 0 :
            self.listWidget.takeItem(selected_item)
            
if __name__ == "__main__":
    app = QApplication([])
    window = mainListaDeMetas()
    window.show()
    app.exec_()
