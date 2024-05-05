import sys
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from PyQt5 import QtWidgets

sys.path.append(os.path.dirname(__file__) + '/ui')
from src.ui.ui import UI
from src.config import *
from src.model import CNN3
from src.ui.util import *

def load_cnn_model(model):
    """
    载入CNN模型
    :return:
    """
    # 引入模块
    MODEL = os.path.join(MODEL_PATH,config_read("config", 4))

    model.load_weights(MODEL)
    return model


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    model = CNN3()
    model = load_cnn_model(model)
    ui = UI(form, model)
    form.show()
    sys.exit(app.exec_())
