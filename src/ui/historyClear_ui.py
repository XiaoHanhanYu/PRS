import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtCore import Qt
import os
from src.ui.util import config_write

class ClearHistoryDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("清空历史记录")
        self.setModal(True)  # 设置为模态对话框
        self.setGeometry(100, 100, 300, 100)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 提示文本
        label = QLabel("确定要删除历史记录吗？")
        label.setAlignment(Qt.AlignCenter)  # 将文本居中显示
        label.setStyleSheet("font-size: 12pt; font-family: Microsoft YaHei;")  # 设置字号为12号并使用宋体字体

        # 按钮布局
        button_layout = QHBoxLayout()

        # 确定按钮
        ok_button = QPushButton("确定")
        ok_button.setFixedSize(100, 30)  # 设置按钮的固定大小为宽100，高30
        ok_button.clicked.connect(self.okClear)  # 点击确定按钮后，调用accept()方法

        # 取消按钮
        cancel_button = QPushButton("取消")
        cancel_button.setFixedSize(100, 30)
        cancel_button.clicked.connect(self.cancelClear)  # 点击取消按钮后，调用reject()方法

        # 添加按钮到按钮布局
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        # 将控件添加到布局中
        layout.addWidget(label)
        layout.addLayout(button_layout)  # 将按钮布局添加到主布局中

        self.setLayout(layout)

    def cancelClear(self):
        self.reject()  # 关闭对话框

    def okClear(self):
        # 删除指定目录下的内容
        try:
            directory = "assets/moz/picture"  # 替换为你要删除文件的目录路径
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                if os.path.isfile(filepath):
                    os.remove(filepath)

            directory2 = "assets/moz/record/record.txt"  # 替换为你要处理的txt文件所在的目录路径
            with open(directory2, 'r') as f:
                lines = f.readlines()
            with open(directory2, 'w') as f:
                f.write(lines[0])  # 只写入第一行内容

            config_write("config", 3, fr"MOZ_COUNT = 1")
            QMessageBox.information(self, "处理完成", "历史记录已成功清空！")

            self.reject()  # 关闭对话框

        except Exception as e:
            QMessageBox.critical(self, "删除失败", "发生错误：" + str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ClearHistoryDialog()
    viewer.exec_()
