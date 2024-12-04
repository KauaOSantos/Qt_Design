import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio03 import Ui_MainWindow 


class Calculo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonVerificar.clicked.connect(self.calcular_imc)

    def calcular_imc(self):
        try:
            peso = float(self.ui.lineEditPeso.text())
            
            altura = float(self.ui.lineEditAltura.text())

            imc = peso / (altura ** 2)
            
            if imc < 18.5:
                texto = "Abaixo do peso"
                imagem = "cachorro_abaixo_do_peso.jpg"
            elif 18.5 <= imc < 24.9:
                texto = "Peso normal"
                imagem = "cachorro_com_peso_normal.jpg"
            elif 25 <= imc < 29.9:
                texto = "Sobrepeso"
                imagem = "cachorro-acima-do-peso.jpg"
            else:
                texto = "Obesidade"
                imagem = "cachorro-obeso.jpg"
                
            self.ui.labelResultado.setText(texto)
            
            blurred_path = imagem
            
            self.ui.centralwidget.setStyleSheet(
            f"background-image: url({blurred_path}); background-repeat: no-repeat; background-position: center;"
        )

            self.ui.labelResultado.setText(f"IMC: {imc:.2f}\nCategoria: {texto}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira valores válidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Calculo()
    janela.show()
    sys.exit(app.exec_())