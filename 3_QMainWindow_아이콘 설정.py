from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon
import os

class MainWindow(QMainWindow):
  def __init__(self): #클래스의 생성자 메서드로 객체가 생성될 때 호출됨
    super().__init__()  #부모 클래스인 QMainWindow의 생성자를 호출하여 초기화

    icon_path = r"FACE02.ICO"
    if os.path.exists(icon_path): # 파일 존재 여부 확인
      icon = QIcon(icon_path) # 아이콘 파일 로드
      self.setWindowIcon(icon) # 윈도우 타이틀 아이콘 변경
    else:
        print(f"경고: 아이콘 파일을 찾을 수 없습니다. ({icon_path})")

    self.setWindowTitle("My App")
    button = QPushButton("Hello World2 - Press me !") # 버튼생성

    self.setCentralWidget(button) # 윈도우 중앙  

app = QApplication([])    # QApplication 객체 생성
window = MainWindow()    # MainWindow 클래스의 인스턴스 생성
window.resize(400, 200)  # 윈도우 크기 설정
window.show()
app.exec()   