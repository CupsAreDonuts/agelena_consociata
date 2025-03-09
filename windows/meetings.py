import pandas as pd
from datetime import datetime
from PyQt5.QtWidgets import (QWidget,
                             QListWidget,
                             QLabel,
                             QPushButton,
                             QGridLayout,
                             QShortcut,
                             QMessageBox,
                             QCheckBox)
from PyQt5.QtGui import QKeySequence
from data.mongodb.social_database import get_meetings, find_meeting_in_meetings, delete_meeting_in_meetings

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
        self.include_finalised_label = QLabel('Include finalised')
        self.include_finalised_checkbox = QCheckBox()
        self.back_button = QPushButton('Back (B)')
        self.back_button_shortcut = QShortcut(QKeySequence('B'), self)
        self.has_layout = None

    def create_window(self):
        self.meetings_headline.setMaximumHeight(30)
        self.include_finalised_label.setMaximumHeight(self.add_meeting_button.sizeHint().height())
        if list(self.meetings.find()):
            if self.has_layout:
                self.meetings_list.clear()
            self.meetings_as_table = pd.DataFrame(list(self.meetings.find()))
            self.fill_meetings_list()

        if not self.has_layout:
            self.add_meeting_button.clicked.connect(self.add_button_clicked)  # noqa
            self.edit_meeting_button.clicked.connect(self.edit_button_clicked)  # noqa
            self.delete_meeting_button.clicked.connect(self.delete_button_clicked)  # noqa
            self.back_button.clicked.connect(self.back_button_clicked)  # noqa
            self.back_button_shortcut.activated.connect(self.back_button_clicked)  # noqa
            self.include_finalised_checkbox.clicked.connect(self.finalised_checkbox_clicked)  # noqa

            layout = QGridLayout()
            layout.addWidget(self.meetings_headline, 0, 0, 1, 1)
            layout.addWidget(self.meetings_list, 1, 0, 10, 1)
            layout.addWidget(self.add_meeting_button, 1, 1, 1, 1)
            layout.addWidget(self.edit_meeting_button, 2, 1, 1, 1)
            layout.addWidget(self.delete_meeting_button, 3, 1, 1, 1)
            layout.addWidget(self.include_finalised_label, 4, 1, 1, 1)
            layout.addWidget(self.include_finalised_checkbox, 5, 1, 1, 1)
            layout.addWidget(self.back_button, 10, 1, 1, 1)

            self.setLayout(layout)
            self.setWindowTitle('Agelena Consociata')
            self.setGeometry(200, 200, 900, 556)
            self.has_layout = True
        pass

    def fill_meetings_list(self):
        self.meetings_as_table['date'] = self.meetings_as_table['date'].map(
            lambda date: datetime.strptime(date, '%d.%m.%Y') if isinstance(date, str) else date)
        self.meetings_as_table.sort_values(by='date', inplace=True)
        for meeting in self.meetings_as_table.itertuples():
            if self.include_finalised_checkbox.checkState() == 2:
                self.meetings_list.addItem(str(meeting.date.strftime('%d.%m.%Y')) + ' at ' + str(meeting.time) +
                                           ' with ' +
                                           str(meeting.participants))
            else:
                if meeting.finalised.endswith('no'):
                    self.meetings_list.addItem(
                        str(meeting.date.strftime('%d.%m.%Y')) + ' at ' + str(meeting.time) + ' with ' +
                        str(meeting.participants))

    def add_button_clicked(self):
        self.setVisible(False)
        self.add_meeting_window = AddMeeting(self)
        self.add_meeting_window.create_window()
        self.add_meeting_window.show()
        pass

    def edit_button_clicked(self):
        if self.meetings_list.currentItem():
            date, time, participants = self.get_search_metrics_of_meeting_from_list()
            meeting = find_meeting_in_meetings({'date': date, 'time': time, 'participants': participants})
            self.add_meeting_window = AddMeeting(self, meeting)
            self.add_meeting_window.create_window()
            self.setVisible(False)
            self.add_meeting_window.show()
            pass

    def get_search_metrics_of_meeting_from_list(self):
        if self.meetings_list.currentItem():
            date = self.meetings_list.currentItem().text()[:10]
            time = self.meetings_list.currentItem().text()[14:19]
            participants = self.meetings_list.currentItem().text()[25:]
            return date, time, participants
        else:
            pass

    def delete_button_clicked(self):
        if self.meetings_list.currentItem():
            date, time, participants = self.get_search_metrics_of_meeting_from_list()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f'Are you sure you want to delete this meeting?')
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            reply = msg.exec()
            if reply == QMessageBox.Ok:
                meeting_to_delete = (
                    find_meeting_in_meetings({'date': date, 'time': time, 'participants': participants}))
                delete_meeting_in_meetings(meeting_to_delete)
                self.confirm_meeting_deleted()
                self.refresh()

    @staticmethod
    def confirm_meeting_deleted():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Meeting has been deleted.')
        msg.exec()

    def finalised_checkbox_clicked(self):
        self.meetings_list.clear()
        self.fill_meetings_list()

    def back_button_clicked(self):
        self.startup_window.setVisible(True)
        self.destroy()

    def refresh(self):
        self.hide()
        self.__init__(startup_window=self.startup_window)
        self.create_window()
        self.show()
