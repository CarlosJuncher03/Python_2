# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(566, 286)
        Form.setStyleSheet("background-color: rgb(145, 145, 145);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 571, 301))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(4, 4, 4);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bd_ip = QtWidgets.QLineEdit(self.frame)
        self.bd_ip.setGeometry(QtCore.QRect(90, 20, 141, 20))
        self.bd_ip.setStyleSheet("border-color: rgb(7, 7, 7);")
        self.bd_ip.setObjectName("bd_ip")
        self.bd_porta = QtWidgets.QLineEdit(self.frame)
        self.bd_porta.setGeometry(QtCore.QRect(290, 20, 61, 21))
        self.bd_porta.setObjectName("bd_porta")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setStyleSheet("font: 8pt \"Impact\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 41, 21))
        self.label_2.setStyleSheet("font: 8pt \"Impact\";")
        self.label_2.setObjectName("label_2")
        self.bd_banco = QtWidgets.QLineEdit(self.frame)
        self.bd_banco.setGeometry(QtCore.QRect(410, 20, 121, 20))
        self.bd_banco.setObjectName("bd_banco")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(360, 20, 41, 21))
        self.label_3.setStyleSheet("font: 8pt \"Impact\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 171, 16))
        self.label_4.setStyleSheet("font: 8pt \"Impact\";")
        self.label_4.setObjectName("label_4")
        self.bd_local_salvar = QtWidgets.QLineEdit(self.frame)
        self.bd_local_salvar.setGeometry(QtCore.QRect(170, 50, 251, 20))
        self.bd_local_salvar.setObjectName("bd_local_salvar")
        self.but_backup = QtWidgets.QPushButton(self.frame)
        self.but_backup.setGeometry(QtCore.QRect(240, 110, 75, 23))
        self.but_backup.setObjectName("but_backup")
        self.but_local = QtWidgets.QPushButton(self.frame)
        self.but_local.setGeometry(QtCore.QRect(430, 50, 75, 21))
        self.but_local.setObjectName("but_local")
        self.bd_ususario = QtWidgets.QLineEdit(self.frame)
        self.bd_ususario.setGeometry(QtCore.QRect(62, 79, 121, 21))
        self.bd_ususario.setObjectName("bd_ususario")
        self.bd_senha = QtWidgets.QLineEdit(self.frame)
        self.bd_senha.setGeometry(QtCore.QRect(250, 80, 81, 21))
        self.bd_senha.setObjectName("bd_senha")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.label_5.setStyleSheet("font: 8pt \"Impact\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(200, 80, 47, 20))
        self.label_6.setStyleSheet("font: 8pt \"Impact\";")
        self.label_6.setObjectName("label_6")
        self.but_cancelar = QtWidgets.QPushButton(self.frame)
        self.but_cancelar.setGeometry(QtCore.QRect(240, 220, 75, 23))
        self.but_cancelar.setObjectName("but_cancelar")
        self.bd_andamento = QtWidgets.QTextEdit(self.frame)
        self.bd_andamento.setGeometry(QtCore.QRect(20, 140, 501, 71))
        self.bd_andamento.setObjectName("bd_andamento")
        self.test_conexao = QtWidgets.QPushButton(self.frame)
        self.test_conexao.setGeometry(QtCore.QRect(350, 80, 91, 23))
        self.test_conexao.setObjectName("test_conexao")
        self.but_voltar = QtWidgets.QPushButton(self.frame)
        self.but_voltar.setGeometry(QtCore.QRect(240, 250, 75, 23))
        self.but_voltar.setObjectName("but_voltar")
        self.but_backup.raise_()
        self.bd_ip.raise_()
        self.bd_porta.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.bd_banco.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.bd_local_salvar.raise_()
        self.but_local.raise_()
        self.bd_ususario.raise_()
        self.bd_senha.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.but_cancelar.raise_()
        self.bd_andamento.raise_()
        self.test_conexao.raise_()
        self.but_voltar.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "IP DO BANCO:"))
        self.label_2.setText(_translate("Form", "PORTA:"))
        self.label_3.setText(_translate("Form", "BANCO:"))
        self.label_4.setText(_translate("Form", "LOCAL PARA SALVAR O BACKUP:"))
        self.but_backup.setText(_translate("Form", "INICIAR"))
        self.but_local.setText(_translate("Form", "LOCAL"))
        self.label_5.setText(_translate("Form", "USUARIO:"))
        self.label_6.setText(_translate("Form", "SENHA:"))
        self.but_cancelar.setText(_translate("Form", "CANCELAR"))
        self.test_conexao.setText(_translate("Form", "Testar conexao"))
        self.but_voltar.setText(_translate("Form", "VOLTAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
