import sys
from kiwoom.kiwoom import *
from PyQt5.QtWidgets import QApplication

class Main():
    def __init__(self):
        print("키움 클래스입니다.")

        self.app = QApplication(sys.argv) # QApplication 객체 생성.
        self.kiwoom = Kiwoom()
        self.app.exec_() # 이벤트 루프 실행.

if __name__ == "__main__":
    Main()