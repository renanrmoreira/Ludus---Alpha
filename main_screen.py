from PyQt6 import QtCore, QtGui, QtWidgets
from matricula_screen import *
from frequencia_screen import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(108, 50, 423, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.dasboard_button = QtWidgets.QPushButton(parent=self.frame)
        self.dasboard_button.setGeometry(QtCore.QRect(210, 290, 196, 75))
        self.dasboard_button.setMinimumSize(QtCore.QSize(196, 75))
        self.dasboard_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dasboard_button.setStyleSheet("background-color: rgb(44, 46, 89);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 180px;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.dasboard_button.setObjectName("dasboard_button")
        self.nome_professor = QtWidgets.QLabel(parent=self.frame)
        self.nome_professor.setGeometry(QtCore.QRect(9, 156, 405, 28))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.nome_professor.setFont(font)
        self.nome_professor.setStyleSheet("color: rgb(130, 3, 0);")
        self.nome_professor.setObjectName("nome_professor")
        self.ficha_button = QtWidgets.QPushButton(parent=self.frame)
        self.ficha_button.setGeometry(QtCore.QRect(9, 290, 196, 75))
        self.ficha_button.setMinimumSize(QtCore.QSize(196, 75))
        self.ficha_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ficha_button.setStyleSheet("background-color: rgb(229, 149, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 180px;\n"
"padding: 6px;\n"
"color: rgb(22, 22, 29)\n"
"")
        self.ficha_button.setObjectName("ficha_button")
        self.matricula_button = QtWidgets.QPushButton(parent=self.frame, clicked = lambda: self.abrir_tela_cadastro())
        self.matricula_button.setGeometry(QtCore.QRect(210, 210, 196, 75))
        self.matricula_button.setMinimumSize(QtCore.QSize(196, 75))
        self.matricula_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.matricula_button.setStyleSheet("background-color: rgb(45, 84, 60);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 180px;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);")
        self.matricula_button.setCheckable(False)
        self.matricula_button.setObjectName("matricula_button")
        self.welcome_label = QtWidgets.QLabel(parent=self.frame)
        self.welcome_label.setGeometry(QtCore.QRect(9, 122, 405, 28))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: rgb(130, 3, 0);")
        self.welcome_label.setObjectName("welcome_label")
        self.LUDUS_logo = QtWidgets.QLabel(parent=self.frame)
        self.LUDUS_logo.setGeometry(QtCore.QRect(9, -8, 405, 120))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.LUDUS_logo.setFont(font)
        self.LUDUS_logo.setStyleSheet("color: rgb(130, 3, 0);")
        self.LUDUS_logo.setObjectName("LUDUS_logo")
        self.frequencia_button = QtWidgets.QPushButton(parent=self.frame, clicked = lambda: self.abrir_tela_frequencia())
        self.frequencia_button.setGeometry(QtCore.QRect(9, 210, 196, 75))
        self.frequencia_button.setMinimumSize(QtCore.QSize(196, 75))
        self.frequencia_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.frequencia_button.setStyleSheet("background-color: rgb(131, 3, 2);;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font:bold 14px \"Inter Black\" ;\n"
"min-width: 180px;\n"
"padding: 6px;\n"
"color: rgb(243, 230, 213);\n"
"")
        self.frequencia_button.setObjectName("frequencia_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def abrir_tela_cadastro(self):
        self.tela_cadastro = QtWidgets.QMainWindow()
        self.ui = UI_MatriculaWindow()           
        self.ui.setupUi(self.tela_cadastro)           
        self.tela_cadastro.show()                     
        QtWidgets.QApplication.instance().activeWindow().close()
    def abrir_tela_frequencia(self):
        self.tela_frequencia = QtWidgets.QMainWindow()
        self.ui = UI_FrequenciaWindow()           
        self.ui.setupUi(self.tela_frequencia)           
        self.tela_frequencia.show()                     
        QtWidgets.QApplication.instance().activeWindow().close()


    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dasboard_button.setToolTip(_translate("MainWindow", "Informações relevantes sobre as frequências"))
        self.dasboard_button.setText(_translate("MainWindow", "Dashboard"))
        self.nome_professor.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">nome_professor</span></p></body></html>"))
        self.ficha_button.setToolTip(_translate("MainWindow", "Perfis individuais de alunos para exportação"))
        self.ficha_button.setText(_translate("MainWindow", "Fichas"))
        self.matricula_button.setToolTip(_translate("MainWindow", "Cadastro de novos alunos nas turmas"))
        self.matricula_button.setText(_translate("MainWindow", "Matricula"))
        self.welcome_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Bem vindo professor(a)</span></p></body></html>"))
        self.LUDUS_logo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">LUDUS</span></p></body></html>"))
        self.frequencia_button.setToolTip(_translate("MainWindow", "Registros de frequências, justificativas e observações"))
        self.frequencia_button.setText(_translate("MainWindow", "Frequência"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
