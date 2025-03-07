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

from data.mongodb.social_database import add_meeting_in_meetings


class AddMeeting(QWidget):
    def __init__(self, meetings_window):
        super().__init__()  # noqa
        self.meetings_window = meetings_window
        self.date_label = QLabel('Date')
        self.date_input = QCalendarWidget()  # noqa
        self.location_label = QLabel('Location')
        self.location_input = QTextEdit()
        self.reason_label = QLabel('Reason')
        self.reason = QTextEdit()
        self.type_label = QLabel('Type')
        self.type = QLineEdit()
        self.participants_label = QLabel('Participants')
        self.participants = QTextEdit()
        self.notes_label = QLabel('Notes')
        self.notes = QTextEdit()
        self.finalised_label = QLabel('Finalised?')
        self.finalised = QCheckBox()

        self.add_button = QPushButton('Add Meeting')
        self.back_button_shortcut = QShortcut(QKeySequence('B'), self)
        self.back_button = QPushButton('Back (B)')

    def create_window(self):
        self.add_button.clicked.connect(self.add_button_clicked)  # noqa
        self.back_button_shortcut.activated.connect(self.back_button_clicked)  # noqa
        self.back_button.clicked.connect(self.back_button_clicked)  # noqa

        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_input)
        layout.addWidget(self.reason_label)
        layout.addWidget(self.reason)
        layout.addWidget(self.type_label)
        layout.addWidget(self.type)
        layout.addWidget(self.participants_label)
        layout.addWidget(self.participants)
        layout.addWidget(self.notes_label)
        layout.addWidget(self.notes)
        layout.addWidget(self.finalised_label)
        layout.addWidget(self.finalised)
        layout.addWidget(self.add_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.setWindowTitle('Agelena Consociata')
        self.setGeometry(200, 200, 900, 556)

    def add_button_clicked(self):
        if self.participants.toPlainText() and self.location_input.toPlainText() and self.type.text():
            meeting = {'date': self.date_input.selectedDate().toString('dd-MM-yyyy'),
                       'location': self.location_input.toPlainText(),
                       'reason': self.reason.toPlainText(),
                       'type': self.type.text(),
                       'participants': self.participants.toPlainText(),
                       'notes': self.notes.toPlainText(),
                       'finalised': 'yes' if self.finalised.checkState() else 'no'}
            add_meeting_in_meetings(meeting)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f'Meeting: \n \n'
                        f'When: {meeting['date']} \n'
                        f'Where: {meeting['location']} \n'
                        f'With: {meeting['participants']}\n \n'
                        f'added to database.')
            msg.exec()

            self.location_input.setText('')
            self.reason.setText('')
            self.type.setText('')
            self.participants.setText('')
            self.notes.setText('')
            self.finalised.setChecked(False)

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Please provide a date, location, participants and a type.')
            msg.exec()

    def back_button_clicked(self):
        self.meetings_window.setVisible(True)
        self.destroy()
