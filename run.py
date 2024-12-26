import sys
import os
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from windows.startup import StartUp


def run():
    QDir().setCurrent(os.path.dirname(os.path.abspath(__file__)))
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icons/global_spider.png'))
    startup_window = StartUp()
    startup_window.create_window()
    startup_window.show()
    app.exec()


if __name__ == '__main__':
    run()
