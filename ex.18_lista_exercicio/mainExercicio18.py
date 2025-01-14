import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio18 import Ui_MainWindow  # Importa a interface gerada

class mainExercicio18(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonEnviar.clicked.connect(self.verificaMaior)
    
    def verificaMaior(self):
        try:
            numeros = [
                int(self.ui.lineEditNum1.text()),
                int(self.ui.lineEditNum2.text()),
                int(self.ui.lineEditNum3.text()),
                int(self.ui.lineEditNum4.text()),
                int(self.ui.lineEditNum5.text()),
                int(self.ui.lineEditNum6.text()),
                int(self.ui.lineEditNum7.text()),
                int(self.ui.lineEditNum8.text()),
                int(self.ui.lineEditNum9.text()),
                int(self.ui.lineEditNum10.text())
            ]
                    
            maior = max(numeros)
            
            self.ui.labelResultado.setText(f"Resultado: O maior número é {maior}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira números válidos!")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = mainExercicio18()
    janela.show()
    sys.exit(app.exec_())
