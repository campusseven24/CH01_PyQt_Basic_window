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
    button.setCheckable(True)

    # 시그널(이벤트), slot에 연결하여 이벤트 발생하면 실행
    button.clicked.connect(self.the_button_click) # 버튼 클릭 시그널을 슬롯(메서드)과 연결
                                                  # 버튼 클릭 시, the_button_click(checked) 자동 호출
    # self.the_button_click(True)   # 프로그래밍적으로 호출함 , 직접 호출
    # self.the_button_click(False) 

    self.setCentralWidget(button) # 윈도우 중앙  

  # 슬롯(메서드) : 버튼에서 클릭된 시그널을 수신하는 메서드
  def the_button_click(self, checked):  # 클릭할 때마다 내부적으로 **체크 상태(True/False)**가 토글되고, 그 상태 값이 시그널을 통해 checked 매개변수로 전달됨
    print("버튼이 클릭되었습니다. !!", checked)
    

app = QApplication([])    # QApplication 객체 생성
window = MainWindow()    # MainWindow 클래스의 인스턴스 생성
window.resize(400, 200)  # 윈도우 크기 설정
window.show()
app.exec()   