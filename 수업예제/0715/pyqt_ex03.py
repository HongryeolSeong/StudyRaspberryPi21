## QT5 사용자 윈도우 구성 예제
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My QT5 Window') # 제목표시줄
        self.setGeometry(80, 80, 600, 300) # x, y, width, height
        self.setWindowIcon(QIcon('./0715/image/chart.png'))

        #label add
        self.label = QLabel('메시지: ', self)
        self.label.move(10, 10)
        #self.label.setGeometry(10, 10, 300, 20)
        self.label.setFixedWidth(300)

        #button add
        self.btn = QPushButton('Click', self)
        self.btn.move(10, 50)

        #signal add
        self.btn.clicked.connect(self.btn_clicked)

    # 버튼 클릭 시그널(이벤트)
    def btn_clicked(self):
        self.label.clear()
        self.label.setText('메시지: 버튼클릭~!')

app = QApplication(sys.argv)

win = MyWindow()
win.show()
app.exec_()