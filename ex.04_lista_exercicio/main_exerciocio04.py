import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from exercicio04 import Ui_MainWindow

class MainExerc04(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonCalcular.clicked.connect(self.calcular_fibonacci)

    def calcular_fibonacci(self):
        try:
            n = int(self.ui.lineEditNum.text())
            if n <= 0:
                self.ui.labelResultado.setText("Digite um número maior que 0!")
                return
            fibonacci = []
            a, b = 0, 1
            for _ in range(n):
                fibonacci.append(a)
                a, b = b, a + b
            self.ui.labelResultado.setText(f"Sequência: {', '.join(map(str, fibonacci))}")
        except ValueError:
            self.ui.labelResultado.setText("Por favor, insira um número válido!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainExerc04()
    janela.show()
    sys.exit(app.exec_())
