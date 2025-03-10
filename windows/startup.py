from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from windows.entries import Entries
from windows.check_birthdays import Birthdays
from windows.meetings import Meetings


class StartUp(QWidget):
    def __init__(self):
        super().__init__()  # noqa
        self.entries_button = QPushButton('Entries (1)')
        self.birthdays_button = QPushButton('Check Birthdays (2)')
        self.meetings_button = QPushButton('Check Meetings (3)')
        self.entries = None
        self.birthdays = None
        self.meetings = None

    def create_window(self):
        view_entries_shortcut = QShortcut(QKeySequence('1'), self)
        view_entries_shortcut.activated.connect(self.view_entries_clicked)  # noqa
        self.entries_button.clicked.connect(self.view_entries_clicked)  # noqa

        check_birthdays_shortcut = QShortcut(QKeySequence('2'), self)
        check_birthdays_shortcut.activated.connect(self.check_birthdays_clicked)  # noqa
        self.birthdays_button.clicked.connect(self.check_birthdays_clicked)  # noqa

        view_meetings_shortcut = QShortcut(QKeySequence('3'), self)
        view_meetings_shortcut.activated.connect(self.meetings_button_clicked)  # noqa
        self.meetings_button.clicked.connect(self.meetings_button_clicked)  # noqa

        layout = QVBoxLayout()
        layout.addWidget(self.entries_button)
        layout.addWidget(self.birthdays_button)
        layout.addWidget(self.meetings_button)
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        self.setWindowTitle('Welcome to Agelena Consociata')
        self.setGeometry(200, 200, 300, 300)

    def view_entries_clicked(self):
        self.entries = Entries(startup_window=self)
        self.entries.show()
        self.entries.create_window()
        self.close()

    def check_birthdays_clicked(self):
        self.birthdays = Birthdays(startup_window=self)
        self.birthdays.show()
        self.birthdays.create_window()
        self.close()

    def meetings_button_clicked(self):
        self.meetings = Meetings(startup_window=self)
        self.meetings.show()
        self.meetings.create_window()
        self.close()
