# QT Designer 연동 소스
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./0715/ui/naverSearch.ui', self)

        #ui에 있는 위젯과 시그널처리(= 컨트롤 이벤트 처리)
        self.btnSearch.clicked.connect(self.btnSearch_Clicked)

    def btnSearch_Clicked(self):
        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.txtSearchWord.text()
        display = 100

        # naver api search
        jsonResult = api.getNaverSearchResult(sNode, search_word, 1, display)
        print(jsonResult)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())