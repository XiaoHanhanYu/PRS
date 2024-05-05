# 模型位置参数
MODEL_CK = "./models/cnn3_best_weights_ck.h5"
MODEL_JAFFE = "../models/cnn3_best_weights_jaffe.h5"
MODEL_FER = "../models/cnn3_best_weights_fer.h5"
MODEL_PATH = "models"
# 日志等级参数
import os
"""
0：显示所有日志（默认级别）
1：显示警告和错误日志
2：只显示错误日志
3：只显示错误和致命日志
"""
LOG_LEVEL = os.environ.get("TF_CPP_MIN_LOG_LEVEL", "2")
# 版本
__VERSION__ = "1.0"
RESULT_COUNT = {
    "count": 0,
    "index": 1,
    'emotion': [],
    'possibility': []
}
TEMP = "assets/moz/temp_directory/temp-"
RECORD = "assets/moz/record/record.txt"
TEMP_PATH = 'assets/moz/temp_directory'
MAT = {
    'bar': '柱状图',
    'line': '直线图',
    'pie': '饼图'
}
EXPRESSION = {
        '发怒': 0,
        '厌恶': 0,
        '恐惧': 0,
        '开心': 0,
        '伤心': 0,
        '惊讶': 0,
        '中性': 0,
        '蔑视': 0

    }
Eemotions = {
        '发怒': 'anger',
        '厌恶': 'disgust',
        '恐惧': 'fear',
        '开心': 'happy',
        '伤心': 'sad',
        '惊讶': 'surprised',
        '中性': 'neutral',
        '蔑视': 'contempt'

    }
GRAPHICS_VIEW = []