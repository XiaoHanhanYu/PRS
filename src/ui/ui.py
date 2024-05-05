from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QAction,QMainWindow,QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")

from src.recognition_camera import Camera
from src.recognition_video import Video

from src.ui.setting_ui import OutputPathSettingWindow
from src.ui.history_ui import HistoryViewer
from src.ui.historyClear_ui import ClearHistoryDialog
from src.ui.modelSwitch_ui import ModelSwitchDialog
from src.recognition import *
from src.config import *



class UI(object):
    def __init__(self, form, model):
        super().__init__()
        self.setup_ui(form)
        self.model = model

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(1250, 800)
        icon = QIcon("assets/logo/logo.png")  # 替换为你的图标文件路径
        form.setWindowIcon(icon)
        # 原图无图时显示的label
        self.label_raw_pic = QtWidgets.QLabel(form)
        self.label_raw_pic.setGeometry(QtCore.QRect(10, 30, 320, 240))
        self.label_raw_pic.setStyleSheet("background-color:#bbbbbb;")
        self.label_raw_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_raw_pic.setObjectName("label_raw_pic")
        # 原图右方垂直分割线
        self.line1 = QtWidgets.QFrame(form)
        self.line1.setGeometry(QtCore.QRect(340, 30, 20, 670))
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        # 原图下方水平分割线
        self.line3 = QtWidgets.QFrame(form)
        self.line3.setGeometry(QtCore.QRect(10, 320, 320, 20))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        # 作者说明label
        self.label_designer = QtWidgets.QLabel(form)
        self.label_designer.setGeometry(QtCore.QRect(20, 700, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_designer.setFont(font)
        self.label_designer.setObjectName("label_designer")

        # 结果布局设置
        self.layout_widget = QtWidgets.QWidget(form)
        self.layout_widget.setGeometry(QtCore.QRect(10, 310, 320, 240))
        self.layout_widget.setObjectName("layoutWidget")

        self.vertical_layout = QtWidgets.QVBoxLayout(self.layout_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("verticalLayout")
        # 右侧水平线
        self.line2 = QtWidgets.QFrame(self.layout_widget)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.vertical_layout.addWidget(self.line2)

        # 图片选择按钮
        self.pushButton_select_img = QtWidgets.QPushButton(form)
        self.pushButton_select_img.setGeometry(QtCore.QRect(10, 380, 320, 30))
        self.pushButton_select_img.setObjectName("pushButton_2")
        # 摄像头选择按钮
        self.pushButton_select_camera = QtWidgets.QPushButton(form)
        self.pushButton_select_camera.setGeometry(QtCore.QRect(10, 420, 320, 30))
        self.pushButton_select_camera.setObjectName("pushButton_3")
        # 视频选择按钮
        self.pushButton_select_video = QtWidgets.QPushButton(form)
        self.pushButton_select_video.setGeometry(QtCore.QRect(10, 460, 320, 30))
        self.pushButton_select_video.setObjectName("pushButton_3")
        # 下载图片按钮
        self.pushButton_download = QtWidgets.QPushButton(form)
        self.pushButton_download.setGeometry(QtCore.QRect(300, 280, 30, 30))
        self.pushButton_download.setObjectName("download_button")
        self.pushButton_download.setStyleSheet(
            '''
            QPushButton {
                border: 2px solid transparent;
                border-radius: 10px; /* 调整圆角大小 */
                background-color: rgba(255, 255, 255, 0); /* 使背景透明 */
                background-image: url("button_image.png");
                background-position: center;
                background-repeat: no-repeat;
                border-image: url("assets/logo/download2.png");
            }
            '''
        )

        # 创建下拉按钮
        self.comboBox = QtWidgets.QComboBox(form)
        self.comboBox.setGeometry(QtCore.QRect(1180, 100, 40, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.hide()  # 隐藏
        self.comboBox.currentIndexChanged.connect(self.selected_index_changed)
        # mat选择按钮
        self.comboBoxMat = QtWidgets.QComboBox(form)
        self.comboBoxMat.setGeometry(QtCore.QRect(1170, 250, 70, 30))
        self.comboBoxMat.setObjectName("comboBoxMat")
        default = config_read('config', 6)
        self.comboBoxMat.addItem(MAT[default])
        for k in MAT.keys():
            if k != default:
                self.comboBoxMat.addItem(MAT[k])

        self.comboBoxMat.hide()
        self.comboBoxMat.currentIndexChanged.connect(self.selected_index_mat)  # 连接信号到处理方法


        # 其他布局
        self.graphicsView = QtWidgets.QGraphicsView(form)
        self.graphicsView.setGeometry(QtCore.QRect(360, 210, 800, 500))
        self.graphicsView.setObjectName("graphicsView")
        # GRAPHICS_VIEW = self.graphicsView
        # print(type(GRAPHICS_VIEW))
        self.label_result = QtWidgets.QLabel(form)
        self.label_result.setGeometry(QtCore.QRect(361, 25, 200, 16))
        self.label_result.setObjectName("label_result")
        self.label_emotion = QtWidgets.QLabel(form)
        self.label_emotion.setGeometry(QtCore.QRect(715, 25, 71, 16))
        self.label_emotion.setObjectName("label_emotion")
        self.label_emotion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bar = QtWidgets.QLabel(form)
        self.label_bar.setGeometry(QtCore.QRect(720, 170, 80, 180))
        self.label_bar.setObjectName("label_bar")
        self.line = QtWidgets.QFrame(form)
        self.line.setGeometry(QtCore.QRect(361, 150, 800, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_rst = QtWidgets.QLabel(form)
        self.label_rst.setGeometry(QtCore.QRect(700, 50, 100, 100))
        self.label_rst.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rst.setObjectName("label_rst")

        # 信号槽
        self.pushButton_select_img.clicked.connect(self.open_file_browser)
        self.pushButton_select_camera.clicked.connect(self.open_camera)
        self.pushButton_select_video.clicked.connect(self.open_video)
        self.pushButton_download.clicked.connect(self.download)

        self.retranslate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

        # 初始状态下禁用下载按钮
        self.pushButton_download.setEnabled(False)

        # 创建设置输出路径按钮
        set_output_path_action = QAction(QIcon('assets/logo/setting.png'), '下载路径', form)
        set_output_path_action.triggered.connect(self.open_output_path_setting_window)

        # 创建历史记录查看按钮
        history_button = QAction(QIcon('assets/logo/history.png'), "历史记录查看", form)
        history_button.triggered.connect(self.open_history_window)

        # 创建历史记录查看按钮
        historyClear_button = QAction(QIcon('assets/logo/historyClear.png'), "清空历史记录", form)
        historyClear_button.triggered.connect(self.open_historyClear_window)

        # 创建模型切换按钮
        modelSwitch_button = QAction(QIcon('assets/logo/modelSwitch.png'), "模型切换", form)
        modelSwitch_button.triggered.connect(self.open_modelSwitch_window)

        # 添加设置输出路径动作到菜单栏
        menubar = form.menuBar()

        file_menu = menubar.addMenu('设置')
        file_menu.addAction(set_output_path_action)
        file_menu.addAction(history_button)
        file_menu.addAction(historyClear_button)
        file_menu.addAction(modelSwitch_button)


    def open_modelSwitch_window(self):
        modelSwitchUI = ModelSwitchDialog()
        modelSwitchUI.exec_()

    def open_historyClear_window(self):

        historyUI = ClearHistoryDialog()
        # 获取主窗口的中心坐标
        # center_point = self.label_raw_pic.rect().center()
        # 将历史记录查看窗口移动到主窗口的中心
        # historyUI.move(form.mapToGlobal(center_point) - QtCore.QPoint(-250, -150))
        historyUI.move(769, 385)
        historyUI.exec_()

    # 导入输出目录ui
    def open_output_path_setting_window(self):
        dialog = OutputPathSettingWindow()
        dialog.exec_()  # 显示为模态对话框

    # 导入历史记录查看ui
    def open_history_window(self):
        file_path = r"assets\moz\record\record.txt"
        historyUI = HistoryViewer(file_path=file_path)
        historyUI.exec_()


    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "PRS"))
        self.label_raw_pic.setText(_translate("Form", "O(∩_∩)O"))
        # self.label_designer.setAlignment(Qt.AlignCenter)
        self.label_designer.setText(_translate("Form", "Pattern Recognition System"))
        self.pushButton_select_img.setText(_translate("Form", "选择图片"))
        self.pushButton_select_camera.setText(_translate("Form", "选择摄像头"))
        self.pushButton_select_video.setText(_translate("Form", "选择视频"))
        self.label_result.setText(_translate("Form", "等待操作..."))
        self.label_emotion.setText(_translate("Form", "null"))
        mat = config_read('config' , 6)
        self.label_bar.setText(_translate("Form", f"概率{MAT[mat]}"))
        self.label_rst.setText(_translate("Form", "Result"))

    def download(self):
        result = read_last_line(r"assets/moz/record/record.txt")
        result = "_".join(result.split("\t")[0:2]) + ".png"
        # print("r:",result)
        down_load = config_read("config", 1)
        # print(fr"{result}", down_load)
        copy_file(fr"assets/moz/picture/{result}", down_load+"/")

        download_successful = check_file(down_load,result)

        if download_successful == 1:
            # 下载成功，显示消息框
            QtWidgets.QMessageBox.information(None, "下载成功", fr"图片成功下载到{down_load+'/'}")
        elif download_successful == 2:
            # 下载失败，显示错误消息框
            QtWidgets.QMessageBox.critical(None, "Error", "图片下载失败，下载图片路径出错，请重试！")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "图片下载失败，下载目录路径出错，请重试！")



    def open_camera(self):
        # print("camera")
        Camera(model=self.model).predict_expression()
        max_expression = max(EXPRESSION, key=EXPRESSION.get)
        # max_value = EXPRESSION[max_expression]
        Eemotion = Eemotions[max_expression]
        # print(max_expression, max_value)


    def open_video(self):
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(caption="选取视频", directory="./",
                                                                     filter="All Files (*);;Text Files (*.txt)")
        if file_name is not None and file_name != "":
            Video(filename=file_name, model=self.model).predict_expression()

    def open_file_browser(self):
        self.pushButton_download.setEnabled(True)
        # 加载模型
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(caption="选取图片", directory="./",
                                                                     filter="All Files (*);;Text Files (*.txt)")
        # 显示原图
        if file_name is not None and file_name != "":

            emotion, possibility = predict_expression(file_name, self.model)
            # print(emotion,possibility)
            RESULT_COUNT['emotion'] = emotion
            RESULT_COUNT["possibility"] = possibility
            self.show_raw_img(fr'{TEMP}1.png')
            self.show_results(emotion[0], possibility[0])


        self.pushButton_download.setStyleSheet(
            """
            QPushButton {
                    border: 2px solid transparent;
                    border-radius: 10px; /* 调整圆角大小 */
                    background-color: rgba(255, 255, 255, 0); /* 使背景透明 */
                    background-image: url("button_image.png");
                    background-position: center;
                    background-repeat: no-repeat;
                    border-image: url("assets/logo/download.png");
                }
            """
        )

        result_count = RESULT_COUNT['count']
        self.comboBox.blockSignals(True)  # 禁用信号
        self.comboBox.clear()  # 清除选项
        self.comboBox.blockSignals(False)  # 启用信号
        if result_count >= 1:
            for i in range(1, result_count+1):
                self.comboBox.addItem(f"{i}")

            self.comboBox.show()
            self.comboBoxMat.show()
            self.label_result.setText(f"识别到{result_count}处人脸，当前显示第{RESULT_COUNT['index']}种结果")
        else:
            self.label_result.setText("请重试，没有识别到脸部表情")

    def selected_index_mat(self, index):
        selected_mat = self.comboBoxMat.currentText()
        # print(selected_mat)
        self.label_bar.setText(f"概率{selected_mat}")
        if selected_mat == '柱状图':
            config_write('config', 6, 'mat = bar')
        elif selected_mat == '直线图':
            config_write('config', 6, 'mat = line')
        elif selected_mat == '饼图':
            config_write('config', 6, 'mat = pie')
        mat = config_read('config', 6)
        self.show_Canva(list(RESULT_COUNT['possibility'][int(RESULT_COUNT['index'])-1]), mat)


    def selected_index_changed(self, index):
        # 获取选择的数字 1-n
        selected_number = self.comboBox.currentText()
        RESULT_COUNT['index'] = selected_number
        result_count = RESULT_COUNT['count']
        self.label_result.setText(f"识别到{result_count}处人脸，当前显示第{RESULT_COUNT['index']}种结果")
        self.show_results(RESULT_COUNT['emotion'][int(selected_number)-1], RESULT_COUNT["possibility"][int(selected_number)-1])
        self.show_raw_img(fr'{TEMP}{selected_number}.png')

    def show_raw_img(self, filename):
        img = cv2.imread(filename)
        height, width, channels = img.shape
        if width > height:
            height = int(320*height/width)
            width = 320
        elif width < height:
            width = int(240*width/height)
            height = 240
        else:
            width = 320
            height = 240
        frame = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (width, height))
        self.label_raw_pic.setPixmap(QtGui.QPixmap.fromImage(
                    QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], 3 * frame.shape[1],
                                 QtGui.QImage.Format_RGB888)))

    def show_results(self, emotion, possibility, select='picture'):
        # 显示表情名
        self.label_emotion.setText(QtCore.QCoreApplication.translate("Form", emotion))
        # 显示emoji
        if emotion != 'no':
            print(1)
            img = cv2.imread('./assets/icons/' + str(emotion) + '.png')
            frame = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (100, 100))
            self.label_rst.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], 3 * frame.shape[1],
                             QtGui.QImage.Format_RGB888)))
        else:
            self.label_rst.setText(QtCore.QCoreApplication.translate("Form", "no result"))

        if select == 'picture':
            # 显示matplotlib
            mat = config_read("config", 6)
            self.show_Canva(list(possibility), mat)

    def show_Canva(self, possbility, mat):
        dr = MyFigureCanvas()
        if mat == 'bar':
            dr.draw_bar_chart(possbility)
        elif mat == 'line':
            dr.draw_line_chart(possbility)
        elif mat == 'pie':
            dr.draw_pie_chart(possbility)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()

    def get_faces_from_image(self, img_path):
        """
        获取图片中的人脸
        :param img_path:
        :return:
        """
        img, img_gray, faces = face_detect(img_path, 'blazeface')
        if len(faces) == 0:
            return None
        # 遍历每一个脸
        faces_gray = []
        for (x, y, w, h) in faces:
            face_img_gray = img_gray[y:y + h + 10, x:x + w + 10]
            face_img_gray = cv2.resize(face_img_gray, (48, 48))
            faces_gray.append(face_img_gray)
        return faces_gray


class MyFigureCanvas(FigureCanvas):

    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = fig.add_subplot(111)

    def draw_bar_chart(self, possibility):
        x = ['anger', 'disgust', 'fear', 'happy', 'sad', 'surprised', 'neutral', 'contempt']
        self.axes.bar(x, possibility, align='center')

    def draw_line_chart(self, possibility):
        x = ['anger', 'disgust', 'fear', 'happy', 'sad', 'surprised', 'neutral', 'contempt']
        self.axes.plot(x, possibility, color='red', linestyle='-', marker='o')


    def draw_pie_chart(self, possibility):
        labels = ['anger', 'disgust', 'fear', 'happy', 'sad', 'surprised', 'neutral', 'contempt']
        self.axes.pie(possibility, labels=labels, autopct='%1.1f%%', startangle=140, labeldistance=1.2)
