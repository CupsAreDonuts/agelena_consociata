import sys
import qdarkstyle
import qdarktheme
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)
    #qdarktheme.setup_theme()
    window = MainWindow()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    app.exec()

if __name__ == '__main__':
    main()
