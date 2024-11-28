# falta redimencionar o tamanho das imagens, principalmente da bom.jpg  
import sys
from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from interface import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonVerificar.clicked.connect(self.processar_nota)

    def processar_nota(self):
        try:
            nota = float(self.ui.lineEditNum.text())

            if nota < 0 or nota > 100:
                raise ValueError("Nota fora do intervalo válido (0 a 100).")

            if nota >= 90:
                imagem = "excelente.jpg"
                texto = "Excelente"
            elif 70 <= nota < 90:
                imagem = "bom.jpg"
                texto = "Bom"
            elif 50 <= nota < 70:
                imagem = "regular.jpg"
                texto = "Regular"
            else:
                imagem = "insuficiente.jpg"
                texto = "Insuficiente"

            self.ui.labelResultado.setText(texto)

            img = Image.open(imagem)
            img_blurred = img.filter(ImageFilter.GaussianBlur(4))
            blurred_path = "blurred_temp.jpg"
            img_blurred.save(blurred_path)

            self.ui.centralwidget.setStyleSheet(
                f"background-image: url({blurred_path}); background-repeat: no-repeat; background-position: center;"
            )

        except ValueError as e:
            QMessageBox.critical(self, "Erro", f"Entrada inválida: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
