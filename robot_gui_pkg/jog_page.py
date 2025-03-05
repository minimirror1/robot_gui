import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, Signal, Slot, QTimer

from ui.jog_page_ui import Ui_JogPage

class JogPage(QWidget):
    """
    로봇 조그 제어를 위한 페이지 클래스
    """
    
    # 시그널 정의
    position_changed = Signal(int)
    velocity_changed = Signal(int)
    current_changed = Signal(float)
    
    def __init__(self, parent=None):
        """
        JogPage 클래스 초기화
        """
        super().__init__(parent)
        
        # UI 설정
        self.ui = Ui_JogPage()
        self.ui.setupUi(self)
        
        # 초기 값 설정
        self.init_values()
        
        # 이벤트 연결
        self.connect_events()
        
        # 상태 업데이트 타이머
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self.update_status)
        self.status_timer.start(100)  # 100ms마다 상태 업데이트
        
        # 조그 모드 플래그
        self.is_jogging = False
        
    def init_values(self):
        """
        UI 요소의 초기값 설정
        """
        # 모션 파라미터 초기값
        self.ui.lineEdit.setText("1000")    # 가속도
        self.ui.lineEdit_2.setText("1000")  # 감속도
        self.ui.lineEdit_3.setText("2000")  # 정지 감속도
        self.ui.lineEdit_4.setText("50")    # 스무딩
        self.ui.lineEdit_5.setText("500")   # 속도
        self.ui.lineEdit_6.setText("0")     # 드웰 타임
        
        # 상태 표시 초기값
        self.ui.lineEdit_7.setText("0")     # 위치
        self.ui.lineEdit_8.setText("0")     # 속도
        self.ui.lineEdit_9.setText("0.0")   # 전류
        self.ui.lineEdit_14.setText("0")    # 위치 (두번째)
        
        # PTP 이동 초기값
        self.ui.lineEdit_10.setText("0")    # 절대 이동 위치 1
        self.ui.lineEdit_11.setText("0")    # 절대 이동 위치 2
        self.ui.lineEdit_12.setText("100")  # 상대 이동 거리
        
        # 체크박스 초기값
        self.ui.checkBox.setChecked(False)  # 반복 이동 (절대)
        self.ui.checkBox_2.setChecked(False)  # 반복 이동 (상대)
        
    def connect_events(self):
        """
        UI 요소의 이벤트 연결
        """
        # PTP 절대 이동 버튼
        self.ui.pushButton.clicked.connect(self.on_absolute_move_1)
        self.ui.pushButton_2.clicked.connect(self.on_absolute_move_2)
        
        # PTP 상대 이동 버튼
        self.ui.pushButton_3.clicked.connect(self.on_relative_move_right)
        self.ui.pushButton_4.clicked.connect(self.on_relative_move_left)
        
        # 조그 버튼
        self.ui.pushButton_5.clicked.connect(self.on_jog_left_pressed)
        self.ui.pushButton_6.clicked.connect(self.on_jog_right_pressed)
        
        # 정지 버튼
        self.ui.pushButton_7.clicked.connect(self.on_stop)
        
    def update_status(self):
        """
        상태 정보 업데이트 (타이머에 의해 주기적으로 호출)
        """
        # 실제 구현에서는 로봇 컨트롤러로부터 상태 정보를 가져와 업데이트
        # 여기서는 예시로 간단히 구현
        pass
        
    @Slot()
    def on_absolute_move_1(self):
        """
        첫 번째 절대 위치로 이동
        """
        try:
            position = int(self.ui.lineEdit_10.text())
            self.move_to_absolute_position(position)
        except ValueError:
            print("유효한 위치 값을 입력하세요.")
            
    @Slot()
    def on_absolute_move_2(self):
        """
        두 번째 절대 위치로 이동
        """
        try:
            position = int(self.ui.lineEdit_11.text())
            self.move_to_absolute_position(position)
        except ValueError:
            print("유효한 위치 값을 입력하세요.")
            
    @Slot()
    def on_relative_move_right(self):
        """
        상대적으로 오른쪽으로 이동
        """
        try:
            distance = int(self.ui.lineEdit_12.text())
            self.move_by_relative_distance(distance)
        except ValueError:
            print("유효한 거리 값을 입력하세요.")
            
    @Slot()
    def on_relative_move_left(self):
        """
        상대적으로 왼쪽으로 이동
        """
        try:
            distance = int(self.ui.lineEdit_12.text())
            self.move_by_relative_distance(-distance)
        except ValueError:
            print("유효한 거리 값을 입력하세요.")
            
    @Slot()
    def on_jog_left_pressed(self):
        """
        왼쪽 조그 버튼 누름
        """
        self.is_jogging = True
        self.start_jogging(-1)  # 음수 방향
        
    @Slot()
    def on_jog_right_pressed(self):
        """
        오른쪽 조그 버튼 누름
        """
        self.is_jogging = True
        self.start_jogging(1)  # 양수 방향
        
    @Slot()
    def on_stop(self):
        """
        정지 버튼 누름
        """
        self.is_jogging = False
        self.stop_motion()
        
    def move_to_absolute_position(self, position):
        """
        지정된 절대 위치로 이동
        
        Args:
            position (int): 이동할 절대 위치 (카운트 단위)
        """
        # 실제 구현에서는 로봇 컨트롤러에 명령 전송
        print(f"절대 위치 {position}으로 이동")
        
        # 반복 이동 모드인 경우
        if self.ui.checkBox.isChecked():
            # 반복 이동 로직 구현
            pass
        
    def move_by_relative_distance(self, distance):
        """
        현재 위치에서 상대적으로 이동
        
        Args:
            distance (int): 이동할 상대적 거리 (카운트 단위)
        """
        # 실제 구현에서는 로봇 컨트롤러에 명령 전송
        print(f"상대적으로 {distance} 만큼 이동")
        
        # 반복 이동 모드인 경우
        if self.ui.checkBox_2.isChecked():
            # 반복 이동 로직 구현
            pass
        
    def start_jogging(self, direction):
        """
        조그 모드 시작
        
        Args:
            direction (int): 이동 방향 (1: 양수 방향, -1: 음수 방향)
        """
        if self.is_jogging:
            # 실제 구현에서는 로봇 컨트롤러에 조그 명령 전송
            speed = int(self.ui.lineEdit_5.text())
            print(f"조그 시작: 방향 {direction}, 속도 {speed}")
        
    def stop_motion(self):
        """
        모든 모션 정지
        """
        # 실제 구현에서는 로봇 컨트롤러에 정지 명령 전송
        print("모션 정지")
        
    def get_motion_parameters(self):
        """
        현재 설정된 모션 파라미터 반환
        
        Returns:
            dict: 모션 파라미터 딕셔너리
        """
        try:
            params = {
                'acceleration': int(self.ui.lineEdit.text()),
                'deceleration': int(self.ui.lineEdit_2.text()),
                'stop_deceleration': int(self.ui.lineEdit_3.text()),
                'smoothing': int(self.ui.lineEdit_4.text()),
                'speed': int(self.ui.lineEdit_5.text()),
                'dwell_time': int(self.ui.lineEdit_6.text())
            }
            return params
        except ValueError:
            print("모션 파라미터에 유효한 값을 입력하세요.")
            return None


# 테스트용 메인 함수
def main():
    app = QApplication(sys.argv)
    window = JogPage()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
