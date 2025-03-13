import sys
import json
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from telaHome import Ui_MainWindow as Ui_Pag1
from cadastroDeUsuario import Ui_MainWindow as Ui_Pag2

class main(QMainWindow):
    def __init__(self):
       super().__init__()
       self.ui = Ui_Pag1()
       self.ui.setupUi(self)
       self.ui.pushButton.clicked.connect(self.abrirSegundaTela)
       
    def abrirSegundaTela(self):
        self.segunda_tela = SegundaTela(self)
        self.segunda_tela.show()
        self.close()
        
class SegundaTela(QMainWindow):
    def __init__(self, main_window):
       super().__init__()
       self.ui = Ui_Pag2() 
       self.ui.setupUi(self)
       self.main_window = main_window
       self.ui.pushButtonVoltar.clicked.connect(self.voltarParaPrimeiraTela) 
       self.ui.pushButtonEnviar.clicked.connect(self.enviarFormulario) 
        
    def voltarParaPrimeiraTela(self):
        self.main_window.show() 
        self.close()
        
    def enviarFormulario(self):
        '''Nome, Idade, Sexo, Peso, Altura e poderá selecionar quantos checkbox quiser, tendo o total de 3  sobre o objetivo dele, abaixo vou deixar o nome de onde estão sendo armazenados no QtDesign: lineEditNome, lineEditIdade, lineEditSexo, lineEditPeso, lineEditAltura, checkbox1, checkbox2, checkbox3'''
        dados = {
            "nome": self.ui.lineEditNome.text(),
            "idade": self.ui.lineEditIdade.text(),
            "sexo": self.ui.lineEditSexo.text(),
            "peso": self.ui.lineEditPeso.text(),
            "altura": self.ui.lineEditNome.text(),
            "checkbox1": self.ui.checkBox1.isChecked(),
            "checkbox2": self.ui.checkBox2.isChecked(),
            "checkbox3": self.ui.checkBox3.isChecked(),
        }
        
        users_folder = os.path.join(os.getcwd(), 'users')
        os.makedirs(users_folder, exist_ok=True)

        nome_arquivo = self.ui.lineEditNome.text().strip()
        if not nome_arquivo:
            QMessageBox.warning(self, "Erro", "O nome não pode estar vazio!")
            return

        # caminho da pasta users
        file_path = os.path.join(users_folder, f"{nome_arquivo}.json")

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(dados, file, ensure_ascii=False, indent=4)

            QMessageBox.information(self, "Sucesso", "Cadastro salvo com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar: {e}")
        
        QMessageBox.information(self, "Sucesso", "Formulário enviado com sucesso", QMessageBox.Ok)
        self.main_window.show()  
        self.close() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = main()
    main_window.show()
    sys.exit(app.exec_())