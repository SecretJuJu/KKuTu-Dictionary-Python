#-*- coding:utf-8 -*-

import json
import sys
#PyQt must be installed.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('ui.ui')[0]

longdata = []


longNative = open('data/long.json', encoding = 'utf-8').read()
longJson = json.loads(longNative)

with open('data/long.txt', mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    if len(lines) != 0:
        lines[0] = lines[0].replace(u"\ufeff", '')
longdata = [s.strip('\n') for s in lines]


class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wordInput.textChanged.connect(self.wordSearch)

    def wordSearch(self):
        culture = self.setCulture()
        manner = self.setManner()
        searchTarget = self.wordInput.text()
        self.listWidget.clear()
        if not searchTarget == '':
            for i in range(len(longdata)):
                if searchTarget[0] == longdata[i][0]:
                    if culture == True and str(manner) == longJson[longdata[i]]['onepunch']:
                        self.listWidget.addItem(longdata[i])
                    elif culture == False and str(manner) == longJson[longdata[i]]['onepunch']:
                        if longJson[longdata[i]]['culture'] == 'False':
                            self.listWidget.addItem(longdata[i])
    
    def setCulture(self):
        if self.CheckBoxCulture.isChecked():
            return True
        else:
            return False

    def setManner(self): #원 펀치 여부 반환
        if self.CheckBoxMannerEnable.isChecked():
            return False
        else:
            return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()