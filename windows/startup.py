from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QShortcut
from PyQt5.QtGui import QKeySequence, QIcon
from windows.entries import Entries


class StartUp(QWidget):
    def __init__(self):
        super().__init__()  # noqa
        self.view_entries = QPushButton('View Entries')
        self.entries = None


    def create_window(self):
        view_entries_shortcut = QShortcut(QKeySequence('E'), self)
        view_entries_shortcut.activated.connect(self.view_entries_clicked)  # noqa
        self.view_entries.clicked.connect(self.view_entries_clicked)  # noqa
        layout = QGridLayout()
        layout.addWidget(self.view_entries, 0, 0, 1, 1)
        self.setLayout(layout)

        self.setWindowTitle('Welcome to Agelena Consociata')
        self.setGeometry(300, 300, 300, 300)


    def view_entries_clicked(self):
        self.entries = Entries(startup_window=self)
        self.entries.show()
        self.entries.create_window()
        self.close()
