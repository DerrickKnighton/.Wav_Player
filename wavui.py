# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wavUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import _pickle
import wave
import contextlib
import winsound


class Ui_Dialog(object):
    
    file_Path = ""
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 737)
        Dialog.setMaximumSize(QtCore.QSize(750, 1000))
        self.debugTextBrowser = QtWidgets.QTextBrowser(Dialog)
        self.debugTextBrowser.setGeometry(QtCore.QRect(50, 360, 631, 291))
        self.debugTextBrowser.setMaximumSize(QtCore.QSize(750, 1000))
        self.debugTextBrowser.setBaseSize(QtCore.QSize(750, 1000))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(14)
        self.debugTextBrowser.setFont(font)
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(280, 30, 358, 52))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(630, 40, 93, 28))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("Browse")
        self.pushButton.clicked.connect(self.handleButton)
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 120, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.playSong)
        
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 120, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.stopSong)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 220, 101, 31))
        self.lineEdit_2.setBaseSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(14)
        
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 220, 101, 31))
        self.lineEdit_3.setBaseSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.debugTextBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS PGothic\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">Hello and welcome to my application made using Pyqt and python to play .wav files using the winsound library. To get started click on the browse button and look for the wav file you wish to play.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:18pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "My wav Player"))
        self.label_2.setText(_translate("Dialog", "FileName"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Play"))
        self.pushButton_3.setText(_translate("Dialog", "Pause"))
    
    
    def stopSong(self):
        #stops song completely doesnt pause
        winsound.PlaySound(None, winsound.SND_PURGE)
        
    
    def playSong(self):
        winsound.PlaySound(ui.file_Path, winsound.SND_ASYNC)
        
    
    
    def current_Song_Time():
        print("this function doesnt work yet")
    
    def determine_Song_Length(self,data_path):
        with contextlib.closing(wave.open(data_path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            hours, seconds = divmod(duration * 60, 3600)  # split to hours and seconds
            minutes, seconds = divmod(seconds, 60)  # split the seconds to minutes and seconds
            result = "{:02.0f}:{:02.0f}:{:02.0f}".format(hours, minutes, seconds)
            return result
    
    def handleButton(self):
        #data path arg determines location to open file on your computer to browse 
        #second arg is type of file which is .wav because this plays wav files
        data_path, _ =QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', r"Documents/personalproj", '*.wav')
        with open('data_path.pickle', 'wb') as handle:
            _pickle.dump(data_path,handle)
        self.lineEdit.setText(data_path)
        ui.file_Path = data_path
        self.lineEdit_2.setText("00:00:00")
        self.lineEdit_3.setText(self.determine_Song_Length(ui.file_Path))
        

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

