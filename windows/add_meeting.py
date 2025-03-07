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
from PyQt5.QtCore import QDate

from data.mongodb.social_database import add_meeting_in_meetings, edit_meeting_in_meetings


class AddMeeting(QWidget):
    def __init__(self, meetings_window, previous: None | dict = None):
        super().__init__()  # noqa
        self.meetings_window = meetings_window
        self.date_label = QLabel('Date')
        self.date_input = QCalendarWidget()  # noqa
        self.time_label = QLabel('Time')
        self.time_input = QLineEdit()
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

        self.previous = previous

    def create_window(self):
        self.time_input.setText('hh:mm')
        self.add_button.clicked.connect(self.add_button_clicked)  # noqa
        self.back_button_shortcut.activated.connect(self.back_button_clicked)  # noqa
        self.back_button.clicked.connect(self.back_button_clicked)  # noqa

        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.time_label)
        layout.addWidget(self.time_input)
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

        if self.previous:
            previous_date = QDate.fromString(self.previous['date'], 'dd.MM.yyyy')
            self.date_input.setSelectedDate(previous_date)
            self.time_input.setText(self.previous['time'])
            self.location_input.setText(self.previous['location'])
            self.reason.setText(self.previous['reason'])
            self.type.setText(self.previous['type'])
            self.participants.setText(self.previous['participants'])
            self.notes.setText(self.previous['notes'])
            if self.previous['finalised'] == 'yes':
                self.finalised.setChecked(True)

    def add_button_clicked(self):
        if (self.participants.toPlainText() and self.time_input.text() and self.location_input.toPlainText()
                and self.type.text()):
            meeting = {'date': self.date_input.selectedDate().toString('dd.MM.yyyy'),
                       'time': self.time_input.text(),
                       'location': self.location_input.toPlainText(),
                       'reason': self.reason.toPlainText(),
                       'type': self.type.text(),
                       'participants': self.participants.toPlainText(),
                       'notes': self.notes.toPlainText(),
                       'finalised': 'yes' if self.finalised.checkState() else 'no'}
            if self.previous:
                edit_meeting_in_meetings(self.previous, meeting)
            else:
                add_meeting_in_meetings(meeting)

            self.show_added_to_database(meeting)

            if not self.previous:
                self.clear_input()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Please provide a date, time, location, participants and a type.')
            msg.exec()

    def show_added_to_database(self, meeting):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if self.previous:
            msg.setText('Meeting has been edited.')

        else:
            msg.setText(f'Meeting: \n \n'
                        f'When: {meeting['date']} at {meeting['time']}\n'
                        f'Where: {meeting['location']} \n'
                        f'With: {meeting['participants']}\n \n'
                        f'added to database.')
        msg.exec()

    def clear_input(self):
        self.time_input.setText('hh:mm')
        self.location_input.setText('')
        self.reason.setText('')
        self.type.setText('')
        self.participants.setText('')
        self.notes.setText('')
        self.finalised.setChecked(False)

    def back_button_clicked(self):
        self.meetings_window.create_window()
        self.meetings_window.setVisible(True)
        self.destroy()
