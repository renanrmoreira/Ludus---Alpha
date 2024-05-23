from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QCoreApplication, QSettings
from register_screen import *
from database import realiza_login,busca_nome_usuario
from home_screen import Ui_MainWindow

QCoreApplication.setOrganizationName("LUDUS")
QCoreApplication.setApplicationName("LUDUS-App")
settings = QSettings()

class Ui_Login_Win(object):
    def setupUi(self, Login_Win):
        Login_Win.setObjectName("Login_Win")
        Login_Win.resize(640, 480)
        Login_Win.setStyleSheet("background-color: rgb(243, 230, 213);")
        self.centralwidget = QtWidgets.QWidget(parent=Login_Win)
        self.centralwidget.setObjectName("centralwidget")
        Login_Win.setWindowIcon(QIcon('imagens\\7.png'))
        Login_Win.setStyleSheet("background-color: rgb(243, 230, 213);")
        
        self.cadastrar_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.openCadastro())
        self.cadastrar_button.setGeometry(QtCore.QRect(200, 320, 106, 31))
        self.cadastrar_button.setStyleSheet("background-color:  rgb(45, 84, 60);\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 90px;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.cadastrar_button.setObjectName("cadastrar_button")
        
        self.login_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked = lambda: self.logar())
        self.login_button.setGeometry(QtCore.QRect(320, 320, 106, 31))
        self.login_button.setStyleSheet("background-color: rgb(131, 3, 2);;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 90px;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.login_button.setObjectName("login_button")
        
        self.LUDUS_logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.LUDUS_logo.setGeometry(QtCore.QRect(120, 110, 405, 120))
        
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        
        self.LUDUS_logo.setFont(font)
        self.LUDUS_logo.setStyleSheet("color: rgb(130, 3, 0);")
        self.LUDUS_logo.setObjectName("LUDUS_logo")
        
        self.senha = QtWidgets.QLineEdit(self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(170, 282, 281, 31))
        self.senha.setStyleSheet("background-color: rgb(131, 3, 2);;\n"
                                 "border-width: 2px;\n"
                                 "border-radius: 10px;\n"
                                 "font:bold 14px \"Inter Black\" ;\n"
                                 "min-width: 90px;\n"
                                 "padding: 6px;\n"
                                 "color: rgb(243, 230, 213);\n"
                                 "")
        self.senha.setObjectName("senha")
        self.senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username.setGeometry(QtCore.QRect(170, 246, 281, 31))
        self.username.setStyleSheet("background-color: rgb(243, 230, 213);\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"border-style:outset;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 90px;\n"
"padding: 6px;\n"
"color: rgb(131, 3, 2);\n"
"")
        self.username.setObjectName("username")
        
        Login_Win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_Win)
        QtCore.QMetaObject.connectSlotsByName(Login_Win)

    def openCadastro(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_RegisterUserWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def retranslateUi(self, Login_Win):
        _translate = QtCore.QCoreApplication.translate
        Login_Win.setWindowTitle(_translate("Login_Win", "LUDUS - Login"))
        self.cadastrar_button.setText(_translate("Login_Win", "Cadastrar"))
        self.login_button.setText(_translate("Login_Win", "Login"))
        self.LUDUS_logo.setText(_translate("Login_Win", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">LUDUS</span></p></body></html>"))
        self.senha.setPlaceholderText(_translate("Login_Win", "Senha"))
        self.username.setPlaceholderText(_translate("Login_Win", "Username"))

    def logar(self):
        login = self.username.text()
        senha = self.senha.text()

        if realiza_login(login, senha):
            self.exibir_mensagem_sucesso()
            nome_usuario = busca_nome_usuario(login)
            settings.setValue("username", nome_usuario)
            self.abrir_tela_principal(nome_usuario)
        else:
            self.exibir_mensagem_erro()

    def get_nome_prof(self):
        login = self.username.text()
        nome_usuario = busca_nome_usuario(login)
        return nome_usuario


    def exibir_mensagem_sucesso(self):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText(f"Login realizado com sucesso! Bem ao LUDUS vindo: {self.username.text()}")
        mensagem.setWindowTitle("Confirmação de Login")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()
    
    def exibir_mensagem_erro(self):
        mensagem = QMessageBox()
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setText("Login não foi realizado, usuário ou senha incorretos! Tente novamente")
        mensagem.setWindowTitle("Confirmação de Login ERRO")
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()

    def abrir_tela_principal(self, nome_usuario):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window, username=nome_usuario)
        self.window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Win = QtWidgets.QMainWindow()
    ui = Ui_Login_Win()
    ui.setupUi(Login_Win)
    Login_Win.show()
    sys.exit(app.exec())
