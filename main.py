import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QDesktopWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from assets import assets


# 是为了引入assets文件夹中的资源文件，看似是灰色的没有用，但实际不能删掉
# 只是为了让pyinstaller打包时能打包到exe文件中。
# 需要进入assets文件夹后在命令行输入指令 `pyrcc5 image.rcc -o assets.py` 来更新assets.py文件


class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("我要干啥来着")
        # 设置窗口大小
        self.setWindowIcon(QIcon(":/favicon.ico"))
        self._move_window_to_center()
        # 将背景设置为透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.FramelessWindowHint  # 无边框
            | Qt.WindowStaysOnTopHint  # 始终置顶
            # | Qt.SplashScreen  # 只显示在通知栏
        )

        # 创建一个多行文本输入框
        text_edit = QTextEdit(self)
        text_edit.setPlaceholderText("我打算……")
        text_edit.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0.1); color: white;"
            "border: none"
        )
        # 创建一个透明的QLabel来实现拖拽效果
        drag_label = QLabel(self)
        drag_label.setFixedHeight(40)
        drag_label.setStyleSheet(
            "background-color: rgba(166, 226, 46, 0.5);"
        )
        drag_label.setCursor(Qt.OpenHandCursor)
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(drag_label)
        layout.addWidget(text_edit)
        layout.setSpacing(0)  # 设置控件之间的间距为0
        layout.setContentsMargins(0, 0, 0, 0)  # 设置布局的边距为0
        self.setLayout(layout)
        # 显示窗口
        self.show()

    def _move_window_to_center(self):
        # 获取屏幕可用空间（macOS上会有titlebar占据一部分空间）
        screen_geometry = QDesktopWidget().availableGeometry()

        new_width = 300
        new_height = 300

        # 计算窗口应该移动到的新位置
        new_left = (screen_geometry.width() - new_width) / 2
        new_top = (screen_geometry.height() - new_height) / 2 + screen_geometry.top()

        # 移动窗口到新位置
        self.setGeometry(int(new_left), int(new_top), int(new_width), int(new_height))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()


def main():
    app = QApplication(sys.argv)
    ex = TransparentWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
