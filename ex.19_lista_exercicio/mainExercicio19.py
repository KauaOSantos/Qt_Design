import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from exercicio19 import Ui_MainWindow 

class MainExercicio19(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Configurações iniciais
        self.ui.lineEditQuantidade.setValidator(QIntValidator(1, 100))  # Apenas inteiros positivos
        self.ui.pushButtonCalcular.clicked.connect(self.calculaMedia)
    
    def calculaMedia(self):
        try:
            quantidade = int(self.ui.lineEditQuantidade.text())
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")
            
            numeros = []
            for i in range(quantidade):
                valor, ok = self.getNumero(f"Digite o número {i + 1}:")
                if not ok:
                    raise ValueError("Operação cancelada pelo usuário.")
                numeros.append(valor)
            
            media = sum(numeros) / quantidade
            
            self.ui.labelResultado.setText(f"A média dos números é: {media:.2f}")
        except ValueError as e:
            self.ui.labelResultado.setText(str(e))
        except Exception as e:
            self.ui.labelResultado.setText("Ocorreu um erro inesperado.")
    
    def getNumero(self, mensagem):
        valor, ok = QInputDialog.getInt(
            self, 
            "Entrada de Número", 
            mensagem, 
            0, 
            -100000, 
            100000,
            1 
        )
        return valor, ok

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainExercicio19()
    janela.show()
    sys.exit(app.exec_())
