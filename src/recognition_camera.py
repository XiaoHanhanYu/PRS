import argparse
import cv2
import numpy as np
from src.model import CNN2, CNN3
from src.utils import index2emotion, cv2_img_add_text
from src.blazeface import blaze_detect
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from src.config import *
from src.ui.util import *

LOG_LEVEL = "2"

class Camera(object):
    def __init__(self, model):
        self.model = model
        parser = argparse.ArgumentParser()
        parser.add_argument("--source", type=int, default=0, help="data source, 0 for camera 1 for video")
        parser.add_argument("--video_path", type=str, default=None)
        opt = parser.parse_args()

        if opt.source == 1 and opt.video_path is not None:
            self.filename = opt.video_path
        else:
            self.filename = None

    def generate_faces(self, face_img, img_size=48):
        """
        将探测到的人脸进行增广
        :param face_img: 灰度化的单个人脸图
        :param img_size: 目标图片大小
        :return:
        """

        face_img = face_img / 255.
        face_img = cv2.resize(face_img, (img_size, img_size), interpolation=cv2.INTER_LINEAR)
        resized_images = list()
        resized_images.append(face_img)
        resized_images.append(face_img[2:45, :])
        resized_images.append(face_img[1:47, :])
        resized_images.append(cv2.flip(face_img[:, :], 1))

        for i in range(len(resized_images)):
            resized_images[i] = cv2.resize(resized_images[i], (img_size, img_size))
            resized_images[i] = np.expand_dims(resized_images[i], axis=-1)
        resized_images = np.array(resized_images)
        return resized_images


    def predict_expression(self):
        """
        实时预测
        :return:
        """
        # 参数设置
        model = self.model

        border_color = (0, 0, 0)  # 黑框框
        font_color = (255, 255, 255)  # 白字字
        capture = cv2.VideoCapture(0)  # 指定0号摄像头
        if self.filename:
            capture = cv2.VideoCapture(self.filename)

        while True:
            _, frame = capture.read()  # 读取一帧视频，返回是否到达视频结尾的布尔值和这一帧的图像
            frame = cv2.cvtColor(cv2.resize(frame, (1200, 800)), cv2.COLOR_BGR2RGB)
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 灰度化
            cascade = cv2.CascadeClassifier('.\dataset\params\haarcascade_frontalface_alt.xml')  # 检测人脸
            # 利用分类器识别出哪个区域为人脸
            faces = cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(120, 120))
            faces = blaze_detect(frame)
            # print(len(faces))
            # 如果检测到人脸
            # possibilitys = []
            if faces is not None and len(faces) > 0:
                for (x, y, w, h) in faces:
                    face = frame_gray[y: y + h, x: x + w]  # 脸部图片
                    faces = self.generate_faces(face)
                    results = model.predict(faces)
                    result_sum = np.sum(results, axis=0).reshape(-1) #possibilitys
                    label_index = np.argmax(result_sum, axis=0)
                    emotion = index2emotion(label_index)
                    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), border_color, thickness=2)
                    frame = cv2_img_add_text(frame, emotion, x+30, y+30, font_color, 20)
                    EXPRESSION[emotion] += 1
                    # puttext中文显示问题
                    # cv2.putText(frame, emotion, (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

                    # possibilitys.append(result_sum)

            cv2.imshow("recognition_camera", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))  # 利用人眼假象

            key = cv2.waitKey(30)  # 等待30ms，返回ASCII码

            # 如果输入esc则退出循环
            if key == 27:
                break
            if cv2.getWindowProperty('recognition_camera', 0) == -1:  # 当窗口关闭时为-1，显示时为0
                break
        capture.release()  # 释放摄像头
        cv2.destroyAllWindows()  # 销毁窗口

