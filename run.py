#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This example shows three labels on a window
using absolute positioning.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.lbl1 = QtGui.QTextEdit('ZetCode', self)
        self.lbl1.setFixedWidth(250)
        self.lbl1.move(15, 10)

        self.lbl2 = QtGui.QTextEdit('ZetCode', self)
        self.lbl2.setFixedWidth(250)
        self.lbl2.move(315, 10)

        self.lbl3 = QtGui.QLineEdit('ZetCode', self)
        self.lbl3.setFixedWidth(250)
        self.lbl3.move(15, 300)

        self.btn = QtGui.QPushButton('Run', self)
        self.btn.move(315, 300)
        self.btn.clicked.connect(self.run_btn)

        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('EagleEye')
        self.show()

    def run_btn(self):
        url=self.lbl1.toPlainText()
        QMessageBox.information(self,url,url)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
