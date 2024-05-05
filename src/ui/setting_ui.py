import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog

from src.ui.util import config_read,config_write



class OutputPathSettingWindow(QDialog):
    def __init__(self):
        super().__init__()
        download_path = config_read("config", 1)
        self.output_path = download_path  # 初始输出路径
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置下载路径")

        # 创建标签和输入框
        output_path_label = QLabel("下载路径:")

        self.output_path_entry = QLineEdit(self.output_path)  # 设置初始输出路径
        browse_button = QPushButton("浏览")
        browse_button.clicked.connect(self.browse_output_path)

        # 创建保存按钮
        save_button = QPushButton("保存")
        save_button.clicked.connect(self.save_output_path)

        # 布局
        hbox = QHBoxLayout()
        hbox.addWidget(output_path_label)
        hbox.addWidget(self.output_path_entry)
        hbox.addWidget(browse_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(save_button)

        self.setLayout(vbox)

    def browse_output_path(self):
        output_path = QFileDialog.getExistingDirectory(self, "选择下载路径", self.output_path)
        if output_path:
            self.output_path = output_path  # 更新初始输出路径
            self.output_path_entry.setText(output_path)

    def save_output_path(self):
        output_path = "OUTPUT_PATH = " + self.output_path_entry.text()
        # 在这里执行保存操作，可以将路径保存到配置文件或数据库中
        # print(output_path)
        # self.accept()  # 关闭窗口
        config_write("config",1,output_path)
        # return output_path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OutputPathSettingWindow()
    window.show()
    sys.exit(app.exec_())
