import pandas as pd
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QListWidget, QLabel, QPushButton, QGridLayout, QShortcut
from PyQt5.QtGui import QKeySequence
from data.mongodb.social_database import get_meetings, find_meeting_in_meetings

from windows.add_meeting import AddMeeting


class Meetings(QWidget):
    def __init__(self, startup_window):
        super().__init__()  # noqa
        self.startup_window = startup_window
        self.add_meeting_window = None
        self.meetings = get_meetings()
        self.meetings_as_table = None
        self.meetings_list = QListWidget()   # noqa
        self.meetings_headline = QLabel()  # noqa
        self.add_meeting_button = QPushButton('Add Meeting')
        self.edit_meeting_button = QPushButton('Edit Meeting')
        self.delete_meeting_button = QPushButton('Delete Meeting')
        self.back_button = QPushButton('Back (B)')
        self.back_button_shortcut = QShortcut(QKeySequence('B'), self)
        self.has_layout = None

    def create_window(self):
        self.meetings_headline.setMaximumHeight(30)
        if list(self.meetings.find()):
            if self.has_layout:
                self.meetings_list.clear()
            self.meetings_as_table = pd.DataFrame(list(self.meetings.find()))
            self.fill_meetings_list()

        if not self.has_layout:
            self.add_meeting_button.clicked.connect(self.add_meeting_button_clicked)  # noqa
            self.edit_meeting_button.clicked.connect(self.edit_meeting_button_clicked)  # noqa
            self.back_button.clicked.connect(self.back_button_clicked)  # noqa
            self.back_button_shortcut.activated.connect(self.back_button_clicked)  # noqa

            layout = QGridLayout()
            layout.addWidget(self.meetings_headline, 0, 0, 1, 1)
            layout.addWidget(self.meetings_list, 1, 0, 10, 1)
            layout.addWidget(self.add_meeting_button, 1, 1, 1, 1)
            layout.addWidget(self.edit_meeting_button, 2, 1, 1, 1)
            layout.addWidget(self.delete_meeting_button, 3, 1, 1, 1)
            layout.addWidget(self.back_button, 10, 1, 1, 1)

            self.setLayout(layout)
            self.setWindowTitle('Agelena Consociata')
            self.setGeometry(200, 200, 900, 556)
            self.has_layout = True
        pass

    def fill_meetings_list(self):
        self.meetings_as_table['date'] = self.meetings_as_table['date'].map(
            lambda date: datetime.strptime(date, '%d.%m.%Y'))
        self.meetings_as_table.sort_values(by='date', inplace=True)
        for meeting in self.meetings_as_table.itertuples():
            self.meetings_list.addItem(str(meeting.date.strftime('%d.%m.%Y')) + ' ' + str(meeting.participants))

    def add_meeting_button_clicked(self):
        self.setVisible(False)
        self.add_meeting_window = AddMeeting(self)
        self.add_meeting_window.create_window()
        self.add_meeting_window.show()
        pass

    def edit_meeting_button_clicked(self):
        if self.meetings_list.currentItem():
            date = self.meetings_list.currentItem().text()[:10]
            participants = self.meetings_list.currentItem().text()[11:]
            matching_meetings = find_meeting_in_meetings({'date': date, 'participants': participants})
            for meeting in matching_meetings:
                print(meeting)
                self.add_meeting_window = AddMeeting(self, meeting)
                self.add_meeting_window.show()


        pass

    def back_button_clicked(self):
        self.startup_window.setVisible(True)
        self.destroy()
