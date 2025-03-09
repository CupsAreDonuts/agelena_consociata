import pandas as pd
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QCalendarWidget, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QShortcut)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QKeySequence
from data.mongodb.social_database import get_people


class Birthdays(QWidget):
    def __init__(self, startup_window):
        super().__init__()  # noqa
        self.startup_window = startup_window
        self.people_collection = get_people()
        self.people_dataframe = pd.DataFrame(self.people_collection.find())
        self.people_dataframe_filtered = None

        self.birthdays_from_label = QLabel('From:')
        self.birthdays_from = QCalendarWidget() # noqa

        self.birthdays_until_label = QLabel('Until:')
        self.birthdays_until = QCalendarWidget() # noqa
        self.birthdays_until.setSelectedDate(QDate.currentDate().addDays(30)) # noqa

        self.people_found = QListWidget() # noqa
        self.back_button = QPushButton('Back (B)')

    def create_window(self):
        self.birthdays_from_label.setAlignment(Qt.AlignTop)
        self.birthdays_until_label.setAlignment(Qt.AlignTop)
        self.setup_people_found()

        self.back_button.clicked.connect(self.back_button_clicked)  # noqa
        back_button_shortcut = QShortcut(QKeySequence('B'), self)
        back_button_shortcut.activated.connect(self.back_button_clicked)  # noqa

        self.birthdays_from.selectionChanged.connect(self.setup_people_found)  # noqa
        self.birthdays_until.selectionChanged.connect(self.setup_people_found)  # noqa

        selection_and_buttons = QVBoxLayout()
        selection_and_buttons.addWidget(self.birthdays_from_label)
        selection_and_buttons.addWidget(self.birthdays_from)
        selection_and_buttons.addWidget(self.birthdays_until_label)
        selection_and_buttons.addWidget(self.birthdays_until)
        selection_and_buttons.addWidget(self.back_button)

        layout = QHBoxLayout()
        layout.addWidget(self.people_found)
        layout.addLayout(selection_and_buttons)
        self.setLayout(layout)

        self.setGeometry(200, 200, 700, 556)

    def setup_people_found(self):
        self.people_found.clear()

        self.filter_birthdays_by_dates()

        for index, row in self.people_dataframe_filtered.iterrows():
            birthday_of_row = row['birthday_filtered'].strftime('%d.%m.%Y')
            self.people_found.addItem(f'{birthday_of_row[:6]} {row['first_name']} {row['last_name']}')
        return

    def filter_birthdays_by_dates(self):
        date_from = self.birthdays_from.selectedDate().toString('yyyy-MM-dd')
        date_until = self.birthdays_until.selectedDate().toString('yyyy-MM-dd')
        date_from = pd.Timestamp(date_from)
        date_until = pd.Timestamp(date_until)

        self.people_dataframe_filtered = self.people_dataframe

        self.people_dataframe_filtered['birthday_filtered'] = (
            self.people_dataframe_filtered['birthday'].map(adjust_birthday))

        self.people_dataframe_filtered['birthday_filtered'] = (
            self.people_dataframe_filtered['birthday_filtered'].map(
                lambda birthday: pd.to_datetime(birthday, dayfirst=True)))

        self.people_dataframe_filtered = (self.people_dataframe_filtered[
            (self.people_dataframe_filtered['birthday_filtered'].dt.day_of_year >= date_from.day_of_year) &
            (self.people_dataframe_filtered['birthday_filtered'].dt.day_of_year <= date_until.day_of_year)]
                                          .reset_index())

        self.people_dataframe_filtered['day_of_year'] = (
            self.people_dataframe_filtered['birthday_filtered'].dt.day_of_year)
        self.people_dataframe_filtered.sort_values(by='day_of_year', ascending=True, inplace=True)
        self.people_dataframe_filtered = self.people_dataframe_filtered.reset_index(drop=True)

    def back_button_clicked(self):
        self.startup_window.show()
        self.close()


def adjust_birthday(birthday: str):
    if 'X' in birthday:
        return birthday[:6] + '2000'
    else:
        return birthday
