from PyQt5.QtWidgets import QDialog, QVBoxLayout, QComboBox, QPushButton, QLabel, QFileDialog,QMessageBox
from src.ui.util import *
import os

class ModelSwitchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        default_model = config_read("config", 4)
        directory = config_read("config", 5)

        self.default_module = default_model
        self.directory = directory
        # print(self.default_module,self.directory)

        self.setWindowTitle("模型切换")
        layout = QVBoxLayout(self)

        self.label = QLabel(f"当前模型: {self.default_module}")
        layout.addWidget(self.label)

        self.file_combo = QComboBox()
        self.file_combo.addItem(self.default_module)
        layout.addWidget(self.file_combo)

        self.load_model()

        self.switch_button = QPushButton("保存切换的模型")
        self.switch_button.clicked.connect(self.switch_module)
        layout.addWidget(self.switch_button)
        self.setFixedSize(300, 100)

    def load_model(self):
        # 获取指定目录下的所有文件
        files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f)) and f.endswith('.h5')]
        # print(files)
        # 添加到下拉列表中
        self.file_combo.addItems(files)

    def switch_module(self):
        # 获取用户选择的文件
        selected_file = self.file_combo.currentText()
        self.label.setText(f"当前模型: {selected_file}")
        self.default_module = selected_file
        config_write("config", 4, fr"default_module = {selected_file}")
        QMessageBox.information(self, "处理完成", "模型切换成功")

        self.reject()  # 关闭对话框

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    dialog = ModelSwitchDialog()
    dialog.exec_()
