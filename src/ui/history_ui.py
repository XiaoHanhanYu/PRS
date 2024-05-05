import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTextBrowser, QVBoxLayout
from PyQt5.QtGui import QFont

class HistoryViewer(QDialog):
    def __init__(self, file_path):
        super().__init__()
        self.setWindowTitle("历史记录查看器")
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()
        self.load_history(file_path)

    def init_ui(self):
        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建只读文本浏览器
        self.text_browser = QTextBrowser()

        # 设置字体为宋体
        font = QFont("SimSun", 10)  # 使用宋体字体，大小为12
        self.text_browser.setFont(font)

        layout.addWidget(self.text_browser)

        self.setLayout(layout)

    def load_history(self, file_path):
        try:
            with open(file_path, 'r') as file:
                history_text = file.read()
            self.text_browser.setPlainText(history_text)
        except FileNotFoundError:
            self.text_browser.setPlainText(r"历史记录未找到，请检查assets\moz\record\record.txt文件是否存在")

if __name__ == '__main__':
    # 指定要显示的文本文件路径
    file_path = r"E:\Pattern_Recognition\assets\moz\record\record.txt"  # 替换为你的文件路径

    app = QApplication(sys.argv)
    viewer = HistoryViewer(file_path)
    viewer.exec_()
