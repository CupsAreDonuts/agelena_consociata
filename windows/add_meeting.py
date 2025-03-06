from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QVBoxLayout,
                             QListWidget,
                             QLabel,
                             QMessageBox,
                             QShortcut,
                             QCalendarWidget,
                             QLineEdit,
                             QTextEdit,
                             QCheckBox)
from PyQt5.QtGui import QKeySequence


class AddMeeting(QWidget):
    def __init__(self, meetings_window):
        self.meetings_window = meetings_window
        self.date_input = QCalendarWidget('Date')
        self.location_label = QLabel('Location')
        self.location = QLineEdit(),
        self.reason_label = QLabel('Reason')
        self.reason = QTextEdit()
        self.type_label = QLabel()
        self.type = QLineEdit()
        self.participants_label = QLabel('Participants')
        self.participants = QTextEdit()
        self.notes_label = QLabel('Notes')
        self.notes = QTextEdit()
        self.finalised = QCheckBox()

        self.add_button = QPushButton('Add Meeting')
        self.back_button = QPushButton('Back (B)')

    def create_window(self):
        layout = QVBoxLayout()
        layout.addWidget(self.date_input)
        layout.addWidget(self.location_label)
        layout.addWidget(self.location)
        layout.addWidget(self.reason_label)
        layout.addWidget(self.reason)
        layout.addWidget(self.type_label)
        layout.addWidget(self.type)
        layout.addWidget(self.participants_label)
        layout.addWidget(self.participants)
        layout.addWidget(self.notes_label)
        layout.addWidget(self.notes)
        layout.addWidget(self.finalised)
        layout.addWidget(self.add_button)
        layout.addWidget(self.back_button)
