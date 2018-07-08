import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, \
     QFileDialog, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from PIL import Image


def resize(image, length, width):
    size = image.size
    if length is not None and width is not None:
        size1 = int(length)
        size2 = int(width)
        new_image = image.resize((size1, size2))
        return new_image
    elif length is None and width:
        size2 = int(width)
        size1 = int(size2 * (size[0] / size[1]))
        new_image_1 = image.resize((size1, size2))
        return new_image_1
    elif length and width is None:
        size1 = int(length)
        size2 = int(size1 * (size[1] / size[0]))
        new_image_2 = image.resize((size1, size2))
        return new_image_2
    else:
        pass


class ImageResize(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Decorative', 8))
        button1 = QPushButton('Конвертировать', self)
        button1.move(70, 160)
        button1.resize(150, 30)
        button1.clicked.connect(resize)


        self.setGeometry(800, 300, 300, 220)
        self.setWindowTitle('Изменение изображения')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageResize()
    sys.exit(app.exec_())

