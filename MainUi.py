# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QProgressBar, QLabel, QHBoxLayout, QVBoxLayout, QTextBrowser, QPushButton
from PyQt5 import QtCore, QtGui
import documentTools


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'test'
        self.left = 20
        self.top = 20
        self.width = 940
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setupUI()

        # self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()

        self.show()


    def setupUI(self):
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(80, 180, 400, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(80, 210, 60, 16))
        self.label_3.setObjectName("label_3")
        self.startButton = QPushButton(self)
        self.startButton.setText("开始")
        self.startButton.setGeometry(QtCore.QRect(self.width/2 - 40, self.height - 80, 80, 40));
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.startTranslate)

        self.widget = QWidget(self)
        self.widget.setGeometry(QtCore.QRect(60, 40, 831, 101))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.textBrowser_2 = QTextBrowser(self.widget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # actions
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.openFileNameDialog)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton.clicked.connect(self.saveFileDialog)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "源文件"))
        self.label_2.setText(_translate("Dialog", "保存为"))
        self.pushButton_2.setText(_translate("Dialog", "打开"))
        self.pushButton.setText(_translate("Dialog", "打开"))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.sourceFileName = fileName
            self.textBrowser.setText(self.sourceFileName)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.targetFileName = fileName
            self.textBrowser_2.setText(self.targetFileName)

    def updateProgress(self, currentValue='', currentText=''):
        self.progressBar.setProperty('value', currentValue)
        self.label_3.setText(currentText)

    def startTranslate(self):
        documentTools.beginTranslate(self, self.sourceFileName, self.targetFileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

