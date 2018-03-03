#-*- coding:utf-8 -*-

import json
import sys
#PyQt must be installed.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

longNative = open('data/long.json', encoding = 'utf-8').read()
print(type(longNative))
longJson = json.loads(longNative)

formClass = uic.loadUiType('ui.ui')[0]

with open('data/long.txt', mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    if len(lines) != 0:
        lines[0] = lines[0].replace(u"\ufeff", '')
longdata = [s.strip('\n') for s in lines]

Culture = True
Manner = True

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wordInput.textChanged.connect(self.wordSearch)

    def wordSearch(self):
        self.setCulture()
        self.setManner()
        searchTarget = self.wordInput.text()
        self.listWidget.clear()
        if not searchTarget == '':
            for i in range(len(longdata)):
                if searchTarget[0] == longdata[i][0]:
                    self.listWidget.addItem(longdata[i])
    
    def setCulture(self):
        if self.CheckBoxCulture.isChecked():
            Culture = True
        else:
            Culture = False

    def setManner(self):
        if self.CheckBoxMannerEnable.isChecked():
            Manner = True
        else:
            Manner = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()