import numpy as np
import keras


def load_file(filename):
    """

    :param filename:
    :return:
    """
    import pickle
    data_file = open(filename, 'rb')
    data = pickle.load(data_file)
    data_file.close()
    return data.history


def plot_loss(his, ds):
    """
    :param his:
    :return:
    """
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 8))
    plt.plot(np.arange(len(his['loss'])), his['loss'], label='train loss')
    plt.plot(np.arange(len(his['val_loss'])), his['val_loss'], label='valid loss')
    plt.title(ds + ' training loss')
    plt.legend(loc='best')
    plt.savefig(f'../assets/view/his_loss_{ds}.png')



def plot_acc(his, ds):
    """

    :param his:
    :return:
    """
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 8))
    plt.plot(np.arange(len(his['accuracy'])), his['accuracy'], label='train accuracy')
    plt.plot(np.arange(len(his['val_accuracy'])), his['val_accuracy'], label='valid accuracy')
    plt.title(ds + ' training accuracy')
    plt.legend(loc='best')
    plt.savefig(f'../assets/view/his_acc_{ds}.png')


def plot_feature_map():
    from model import CNN3
    model = CNN3()
    model.load_weights('../models/cnn3_best_weights_ck.h5')

    def get_feature_map(model, layer_index, channels, input_img):
        from keras import backend as K
        layer = K.function([model.layers[0].input], [model.layers[layer_index].output])
        feature_map = layer([input_img])[0]
        import matplotlib.pyplot as plt
        plt.figure(figsize=(20, 8))
        for i in range(channels):
            img = feature_map[:, :, :, i]
            plt.subplot(4, 8, i + 1)
            plt.imshow(img[0], cmap='gray')
        plt.savefig('rst.png')
        plt.show()
    import cv2
    img = cv2.cvtColor(cv2.imread('../data/demo.jpg'), cv2.cv2.COLOR_BGR2GRAY)
    img.shape = (1, 48, 48, 1)
    get_feature_map(model, 4, 32, img)


