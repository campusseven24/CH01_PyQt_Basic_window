# PyQt6에서 위젯 관련 기능을 담당하는 QtWidgets 모듈에서 클래스 import
# - QtWidgets: 위젯(UI 구성 요소) 관련 클래스를 전담하는 모듈
# - QApplication: 애플리케이션 실행 및 이벤트 루프 관리 클래스
# - QWidget: 모든 위젯의 기본이 되는 베이스 클래스
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])    #  애플리케이션당 하나의 QApplication 인스턴스 생성 
#window = QWidget()        # 윈도우가 될 Qt 위젯 QWidget 객체 생성, 
                           # 창(Window) 역할을 할 기본 위젯(QWidget)을 생성하는 코드
window = QPushButton("Hello World - Click me")  # 창(Window) 역할을 할 위젯 QPushButton 객체 생성
window.resize(400, 200)  # 윈도우 크기 설정
window.setWindowTitle("내 창")  # 윈도우 제목 설정
window.show()
app.exec()  # 애플리케이션 실행 (이벤트 루프 시작)