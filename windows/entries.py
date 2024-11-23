import pandas as pd
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QListWidget, QLabel, QMessageBox

from data.mongo import get_people
from windows.add_new_entry import NewEntryWindow


class Entries(QWidget):
    def __init__(self, startup_window):
        super().__init__()  # noqa
        self.startup_window = startup_window
        self.add_new_entry_window = None

        self.people = get_people()
        self.people_as_table = None
        self.people_list = QListWidget()  # noqa

        self.view_entry_button = QPushButton('View')
        self.add_entry_button = QPushButton('Add new entry')
        self.delete_button = QPushButton('Delete')
        self.edit_entry_button = QPushButton('Edit')
        self.people_list_headline = QLabel('People with Entry')


    def create_window(self):
        self.people_list_headline.setMaximumHeight(self.view_entry_button.sizeHint().height())
        if list(self.people.find()):
            self.people_as_table = pd.DataFrame(list(self.people.find()))
            self.fill_people_list()

        self.add_entry_button.clicked.connect(self.add_entry_button_clicked)  # noqa
        self.delete_button.clicked.connect(self.delete_entry_button_clicked)  # noqa

        layout = QGridLayout()
        layout.addWidget(self.people_list_headline, 0, 0, 1, 1)
        layout.addWidget(self.people_list, 1, 0, 10, 1)
        layout.addWidget(self.view_entry_button, 1, 1, 1, 1)
        layout.addWidget(self.add_entry_button, 2, 1, 1, 1)
        layout.addWidget(self.edit_entry_button, 3, 1, 1, 1)
        layout.addWidget(self.delete_button, 4, 1, 1, 1)
        self.setLayout(layout)
        self.setWindowTitle('Agelena Consociata')
        self.setGeometry(400, 400, 900, 556)

    def fill_people_list(self):
        self.people_as_table.sort_values(by='first_name', inplace=True)
        for entry in self.people_as_table.itertuples():
            self.people_list.addItem(str(entry.first_name) + " " + str(entry.last_name))  # noqa

    def add_entry_button_clicked(self):
        self.setVisible(False)
        self.add_new_entry_window = NewEntryWindow(self)
        self.add_new_entry_window.create_window()
        self.add_new_entry_window.show()

    def delete_entry_button_clicked(self):
        if self.people_list.currentItem():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            names = self.people_list.currentItem().text().rsplit(' ')
            msg.setText(f"Are you sure you want to delete {self.people_list.currentItem().text()}?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            reply = msg.exec()
            if reply == QMessageBox.Ok:
                delete_filter = {"first_name": names[0], "last_name": names[1]}
                self.people.delete_one(delete_filter)

            self.refresh()

    def refresh(self):
        self.hide()
        self.__init__(startup_window=self.startup_window)
        self.create_window()
        self.show()
