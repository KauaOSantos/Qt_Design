import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from botaoPlay import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.player = QMediaPlayer(self)
        self.isPaused = False
        
        self.ui.pushButtonPlay.clicked.connect(self.tocarMusica)
        self.ui.pushButtonStop.clicked.connect(self.pararMusica)
        self.ui.pushButtonPause.clicked.connect(self.pausarMusica)
        
    def tocarMusica(self):
        caminhoMusica = os.path.abspath("musica/soltoInstrumental.mp3")
        print("Local da música", caminhoMusica)
        
        url = QUrl.fromLocalFile(caminhoMusica)
       
        if url.isValid():
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            print("Tocando música...")
            
        else:
            print("Erro: Caminho do arquivo inválido.")
            
            
    def pararMusica(self):
        self.player.stop()
        self.isPaused = False
        print("A música parou")
        
        
    def pausarMusica(self):
        self.player.pause()
        self.isPaused = True
        print("A música pausou")
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec_())