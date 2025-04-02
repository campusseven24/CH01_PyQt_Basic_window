from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
'''
PyQt6.QtWidgets: GUI 구성 요소 (위젯)들이 포함
QApplication: 애플리케이션을 생성하고 관리
QMainWindow: 애플리케이션의 메인 창 역할을 하는 클래스
QPushButton: 클릭 가능한 버튼을 생성하는 클래스
MainWindow : class MainWindow(QMainWindow):는 PyQt에서 창(Window)을
정의하는 사용자 정의 클래스로 메인 윈도우의 구조와 동작을 정의하는 역할
'''

class MainWindow(QMainWindow):
  def __init__(self): #클래스의 생성자 메서드로 객체가 생성될 때 호출됨
    super().__init__()  #부모 클래스인 QMainWindow의 생성자를 호출하여 초기화

    self.setWindowTitle("My App")
    button = QPushButton("Hello World2 - Press me !") # 버튼생성

    self.setCentralWidget(button) # 윈도우 중앙  

app = QApplication([])    # QApplication 객체 생성
window = MainWindow()    # MainWindow 클래스의 인스턴스 생성
window.resize(400, 200)  # 윈도우 크기 설정
window.show()
app.exec()   