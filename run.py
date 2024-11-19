import sys
from PyQt5.QtWidgets import QApplication

from windows.startup import StartUp


def run():
    app = QApplication(sys.argv)
    startup_window = StartUp()
    startup_window.show()
    app.exec()


if __name__ == '__main__':
    run()
