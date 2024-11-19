from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from windows.entries import Entries


class StartUp(QWidget):
    def __init__(self):
        super().__init__()  # noqa
        self.view_entries = QPushButton('View Entries')
        self.entries = None

        layout = QGridLayout()
        layout.addWidget(self.view_entries, 0, 0, 1, 1)
        self.setLayout(layout)

        self.view_entries.clicked.connect(self.view_entries_clicked)  # noqa

        self.setWindowTitle('Welcome to Agelena Consociata')
        self.setGeometry(300, 300, 300, 300)

    def view_entries_clicked(self):
        self.entries = Entries(startup_window=self)
        self.entries.show()
        self.close()
