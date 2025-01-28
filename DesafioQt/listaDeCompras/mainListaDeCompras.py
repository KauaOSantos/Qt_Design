from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from listaDeCompras import Ui_MainWindow  # Importa a interface gerada

class mainListaDeCompras (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButtonRemover.clicked.connect(self.removeItem)
        self.pushButtonAdicionar.clicked.connect(self.addItem)
        
    def addItem(self):
        produto = self.lineEdit.text()
        if produto:
            item = QListWidgetItem(produto)
            item.setCheckState(0)
            
            self.listWidget.addItem(item)
            self.lineEdit.clear()
            
    def removeItem(self):
        selected_item = self.listWidget.currentRow()
        if selected_item >= 0 :
            self.listWidget.takeItem(selected_item)
            
if __name__ == "__main__":
    app = QApplication([])
    window = mainListaDeCompras()
    window.show()
    app.exec_()