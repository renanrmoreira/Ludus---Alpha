from PyQt6.QtCore import Qt
from database import *
from editar_matricula2 import *


class Ui_Edit_1_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 750)
        MainWindow.setStyleSheet("background-color: rgb(243, 230, 213);\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        """
        self.confirm_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(676, 40, 136, 71))
        self.confirm_button.setStyleSheet("background-color: rgb(203, 132, 0);\n"
                                          "border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: black;\n"
                                          "font:bold 20px \"Inter Black\" ;\n"
                                          "min-width: 5em;\n"
                                          "padding: 6px;\n"
                                          "color: rgb(243, 230, 213);\n"
                                          "")
        self.confirm_button.setObjectName("confirm_button")
        """
        self.cancel_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.voltar_menu())
        self.cancel_button.setGeometry(QtCore.QRect(530, 40, 136, 71))
        self.cancel_button.setStyleSheet("background-color: rgb(243, 230, 213);\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: black;\n"
                                         "font:bold 20px \"Inter Black\" ;\n"
                                         "min-width: 5em;\n"
                                         "padding: 6px;\n"
                                         "color: rgb(203, 132, 0)")
        self.cancel_button.setObjectName("cancel_button")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(160, 30, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Trend Slab Four")
        font.setPointSize(48)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(203, 132, 0)")
        self.title_label.setObjectName("title_label")
        self.refresh_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.atualizar_lista())
        self.refresh_button.setGeometry(QtCore.QRect(560, 150, 136, 41))
        self.refresh_button.setStyleSheet("background-color: rgb(203, 132, 0);\n"
                                          "border-style: outset;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 10px;\n"
                                          "border-color: black;\n"
                                          "font:bold 20px \"Inter Black\" ;\n"
                                          "min-width: 5em;\n"
                                          "padding: 6px;\n"
                                          "color: rgb(243, 230, 213);\n"
                                          "")
        self.refresh_button.setObjectName("refresh_button")
        self.turma_selection = QtWidgets.QComboBox(parent=self.centralwidget)
        self.turma_selection.setGeometry(QtCore.QRect(290, 150, 261, 41))
        self.turma_selection.setStyleSheet("background-color:rgb(243, 230, 213);\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-radius: 10px;\n"
                                           "border-color: black;\n"
                                           "font:bold 20px  \"Inter Black\" ;\n"
                                           "padding: 6px;\n"
                                           "color: rgb(203, 132, 0);\n"
                                           "alternate-background-color:rgb(243, 230, 213);")
        self.turma_selection.setEditable(True)
        self.turma_selection.setObjectName("turma_selection")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.turma_selection.addItem("")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(130, 210, 721, 451))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 719, 449))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lista_alunos = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.lista_alunos.setStyleSheet("color: rgb(203, 132, 0);\n"
                                        "font: 900 18pt \"Inter \";")
        self.lista_alunos.setObjectName("lista_alunos")
        item = QtWidgets.QListWidgetItem()
        item.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.lista_alunos.addItem(item)
        self.horizontalLayout.addWidget(self.lista_alunos)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.delete_button = QtWidgets.QPushButton(parent=self.centralwidget,clicked=lambda: (self.excluir_aluno()))  # EXCLUIR
        self.delete_button.setGeometry(QtCore.QRect(560, 670, 131, 61))
        self.delete_button.setStyleSheet("background-color: rgb(243, 230, 213);\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: black;\n"
                                            "font:bold 20px \"Inter Black\" ;\n"
                                            "padding: 6px;\n"
                                            "color: rgb(203, 132, 0)")
        self.delete_button.setObjectName("delete_button")

        self.edit_button = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.editar_aluno())  # EDITAR
        self.edit_button.setGeometry(QtCore.QRect(710, 670, 136, 61))
        self.edit_button.setStyleSheet("background-color: rgb(203, 132, 0);\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 10px;\n"
                                            "border-color: black;\n"
                                            "font:bold 20px \"Inter Black\" ;\n"
                                            "min-width: 5em;\n"
                                            "padding: 6px;\n"
                                            "color: rgb(243, 230, 213);\n"
                                            "")
        self.edit_button.setObjectName("edit_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.confirm_button.setText(_translate("MainWindow", "Confirmar"))
        self.cancel_button.setText(_translate("MainWindow", "Cancelar"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p>alunos</p></body></html>"))
        self.refresh_button.setText(_translate("MainWindow", "Atualizar"))
        self.turma_selection.setItemText(0, _translate("MainWindow", "01. Berçário I"))
        self.turma_selection.setItemText(1, _translate("MainWindow", "02. Berçário II"))
        self.turma_selection.setItemText(2, _translate("MainWindow", "03. Maternal I"))
        self.turma_selection.setItemText(3, _translate("MainWindow", "04. Maternal II"))
        self.turma_selection.setItemText(4, _translate("MainWindow", "05. Jardim I"))
        self.turma_selection.setItemText(5, _translate("MainWindow", "06. Jardim II"))
        self.turma_selection.setItemText(6, _translate("MainWindow", "07. Ciclo I - 1° Ano"))
        self.turma_selection.setItemText(7, _translate("MainWindow", "08. Ciclo I - 2° Ano"))
        self.turma_selection.setItemText(8, _translate("MainWindow", "09. Ciclo I - 3° Ano"))
        self.turma_selection.setItemText(9, _translate("MainWindow", "10. Ciclo II - 1° Ano"))
        self.turma_selection.setItemText(10, _translate("MainWindow", "11. Ciclo II - 2° Ano"))
        self.turma_selection.setItemText(11, _translate("MainWindow", "12. Ciclo III - 1° Ano"))
        self.turma_selection.setItemText(12, _translate("MainWindow", "13. Ciclo III - 2° Ano"))
        self.turma_selection.setItemText(13, _translate("MainWindow", "14. Ciclo IV - 1° Ano"))
        self.turma_selection.setItemText(14, _translate("MainWindow", "15. Ciclo IV - 2° Ano"))
        self.turma_selection.setItemText(15, _translate("MainWindow", "16. 1ª Totalidade"))
        self.turma_selection.setItemText(16, _translate("MainWindow", "17.  2ª Totalidade"))
        self.turma_selection.setItemText(17, _translate("MainWindow", "18.  3ª Etapa"))
        self.turma_selection.setItemText(18, _translate("MainWindow", "19.  4ª Etapa"))
        self.turma_selection.setItemText(19, _translate("MainWindow", "20. 1° Ano"))
        self.turma_selection.setItemText(20, _translate("MainWindow", "21. 2° Ano"))
        self.turma_selection.setItemText(21, _translate("MainWindow", "22. 3° Ano"))
        self.turma_selection.setItemText(22, _translate("MainWindow", "23. 4° Ano"))
        __sortingEnabled = self.lista_alunos.isSortingEnabled()
        self.lista_alunos.setSortingEnabled(False)
        self.lista_alunos.setSortingEnabled(__sortingEnabled)
        self.delete_button.setToolTip(_translate("MainWindow", "Excluir perfis selecionados"))
        self.delete_button.setText(_translate("MainWindow", "Excluir"))
        self.edit_button.setToolTip(_translate("MainWindow", "Editar perfil selecionado (Max 1)"))
        self.edit_button.setText(_translate("MainWindow", "Editar"))


    def executar_query(self, query, params):
        conn = connect_db()
        try:
            cur = conn.cursor()

            cur.execute(query, params)

        except Exception as e:
            print(f"Erro ao executar query: {e}")
            conn.rollback()
            return []
        finally:
            cur.close()
            conn.close()
            print("apagado")

    def voltar_menu(self):
        from home_screen import Ui_MainWindow
        self.tela_principal = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.tela_principal)
        self.tela_principal.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def atualizar_lista(self):
        alunos = self.listar_alunos()
        self.listaRefresh(alunos)

    def listar_alunos(self):
        turma = self.turma_selection.currentText()

        resultado = listar_alunos_por_turma(turma)
        return resultado

    def listaRefresh(self, alunos):
        self.lista_alunos.clear()
        for aluno in alunos:
            nome_aluno, matricula = aluno
            item = QtWidgets.QListWidgetItem()
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            item.setText(f"{matricula} - {nome_aluno}")
            self.lista_alunos.addItem(item)

    def abrir_tela_editar_2(self):
        self.tela_alunos = QtWidgets.QMainWindow()
        self.ui = Ui_Edit_2_Window()
        self.ui.setupUi(self.tela_alunos)
        self.tela_alunos.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def armazenar_dados_matricula(self, id):
        conn = connect_db()
        try:
            cur = conn.cursor()

            query_ia = """
                SELECT * FROM identificacao_aluno
                WHERE id_aluno = %s
            """
            cur.execute(query_ia, [id])
            tabela_ia = cur.fetchone()

            id_aluno = tabela_ia[0]

            with open('dados_editar.pkl', 'wb') as arquivo:
                pickle.dump(id_aluno, arquivo)

        except Exception as e:
            print(f"Erro ao executar query: {e}")
            conn.rollback()
            return []
        finally:
            cur.close()
            conn.close()

    def editar_aluno(self):
        for index in range(self.lista_alunos.count()):
            item = self.lista_alunos.item(index)

            if item.checkState() == Qt.CheckState.Checked:

                matricula, nome_aluno = item.text().split(' - ')
                id_aluno = obter_id_aluno_por_matricula(matricula)
                if id_aluno:
                    self.armazenar_dados_matricula(id_aluno)
                    self.abrir_tela_editar_2()
                else:
                    print(f"Não foi possível encontrar o ID para a matrícula {matricula}")

            else:

                print(f"Nenhum item selecionado")

    def excluir_aluno(self):
        for index in range(self.lista_alunos.count()):
            item = self.lista_alunos.item(index)

            if item.checkState() == Qt.CheckState.Checked:

                matricula, nome_aluno = item.text().split(' - ')
                id_aluno = obter_id_aluno_por_matricula(matricula)

                if id_aluno:

                    executar_query("DELETE FROM certidao WHERE id_aluno = %s",[id_aluno])
                    executar_query("DELETE FROM dados_pais_responsavel WHERE id_aluno = %s", [id_aluno])
                    executar_query("DELETE FROM endereco WHERE id_aluno = %s", [id_aluno])
                    executar_query("DELETE FROM informacoes_matricula WHERE id_aluno = %s", [id_aluno])
                    executar_query("DELETE FROM saude WHERE id_aluno = %s", [id_aluno])
                    executar_query("DELETE FROM identificacao_aluno WHERE id_aluno = %s", [id_aluno])

                else:
                    print(f"Não foi possível encontrar o ID para a matrícula {matricula}")

            else:

                print(f"Nenhum item selecionado")

            self.atualizar_lista()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Edit_1_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
