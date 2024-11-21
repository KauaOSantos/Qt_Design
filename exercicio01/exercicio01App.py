import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio01 import Ui_MainWindow #importa a interface convertida


class Exercicio01App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    #conectando o botão com a função 
        self.pushButtonEnviar.clicked.connect(self.exibir_nome_idade)
        
    def exibir_nome_idade(self):
        nome = self.lineEditNome.text()
        idade = self.lineEditIdade.text()
        self.labelResultado.setText(f"Nome: {nome}, Idade: {idade}")
        
        
app = QApplication(sys.argv)
janela = Exercicio01App()
janela.show()
sys.exit(app.exec_())