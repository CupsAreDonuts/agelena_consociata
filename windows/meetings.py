import datetime
from PyQt5.QtWidgets import QWidget


class Meetings(QWidget):
    def __init__(self, startup_window):
        super().__init__()  # noqa
        self.startup_window = startup_window

    def create_window(self):
        pass
