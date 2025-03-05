import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt  # Qt 플래그를 사용하기 위해 추가

from ui.mainwindow_ui import Ui_MainWindow  # Designer에서 uic로 생성된 UI 클래스

# 아래 import는 나중에 구현될 페이지들을 위한 것입니다
# from robot_gui_pkg.src.home_page import HomePage
# from robot_gui_pkg.src.jog_page import JogPage
# from robot_gui_pkg.src.setting_page import SettingPage
# from robot_gui_pkg.src.help_page import HelpPage

# 아이콘 리소스 파일
#import _icons_rc
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import logging
from PySide6.QtCore import QThread, QTimer

# SerialManager 클래스는 나중에 구현될 예정입니다
# from robot_gui_pkg.src.serial_manager import SerialManager


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 로거 설정
        self.logger = logging.getLogger(__name__)
        
        # 프레임리스 윈도우 설정
        #self.setWindowFlags(Qt.FramelessWindowHint)
        # 윈도우 배경을 투명하게 설정
        #self.setAttribute(Qt.WA_TranslucentBackground)
        
        # UI 클래스 인스턴스를 생성하고 현재 윈도우에 설정합니다.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 시리얼 매니저 설정 (나중에 구현)
        # self.serial_manager = SerialManager.get_instance()
        # self.serial_manager.set_main_window(self)  # MainWindow 참조 설정
        
        # UI 요소 초기화 및 이벤트 연결
        self.init_ui()
        
    def init_ui(self):
        """UI 요소 초기화 및 이벤트 연결"""
        """
        # 메뉴 버튼 클릭 이벤트 연결
        self.ui.menuButton.clicked.connect(self.toggle_menu)
        
        # 페이지 버튼 클릭 이벤트 연결
        self.ui.homeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.jogButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.settingButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.helpButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        
        # 최소화, 최대화, 닫기 버튼 이벤트 연결
        self.ui.minimizeButton.clicked.connect(self.showMinimized)
        self.ui.maximizeButton.clicked.connect(self.toggle_maximize)
        self.ui.closeButton.clicked.connect(self.close)
        """
        # 페이지 초기화 (나중에 구현)
        # self.init_pages()
        
        # 상태 표시줄 초기화
        self.init_status_bar()
        
    def toggle_menu(self):
        """좌측 메뉴 토글"""
        current_width = self.ui.leftMenuSubContainer.width()
        target_width = 50 if current_width > 50 else 200
        
        # 메뉴 너비 변경
        self.ui.leftMenuSubContainer.setMaximumWidth(target_width)
        self.ui.leftMenuSubContainer.setMinimumWidth(target_width)
        
    def toggle_maximize(self):
        """윈도우 최대화/복원 토글"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def init_status_bar(self):
        """상태 표시줄 초기화"""
        # 상태 업데이트 타이머 설정
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self.update_status)
        self.status_timer.start(1000)  # 1초마다 상태 업데이트
    
    def update_status(self):
        """상태 정보 업데이트"""
        # 시리얼 연결 상태 등 업데이트 (나중에 구현)
        pass
    
    # 마우스 이벤트 처리 (프레임리스 윈도우 드래그 이동 기능)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main() 