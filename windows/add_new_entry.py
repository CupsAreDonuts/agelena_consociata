import datetime
from PyQt5.QtWidgets import QTabWidget
from data.mongo import add_person_in_people

from windows.add_new_entry_tabs.adress_book import AddressBook
from windows.add_new_entry_tabs.inside import InsideAttributes
from windows.add_new_entry_tabs.outside import OutsideAttributes
from windows.add_new_entry_tabs.relations import RelationalAttributes


class NewEntryWindow(QTabWidget):
    def __init__(self, entries_window):
        super().__init__()
        self.entries_window = entries_window

        self.address_book = AddressBook(self)
        self.inside_personal_attributes = InsideAttributes(self)
        self.outside_personal_attributes = OutsideAttributes(self)
        self.related_people_attributes = RelationalAttributes(self)

        self.addTab(self.address_book, 'Address book')
        self.addTab(self.inside_personal_attributes, 'Inside')
        self.addTab(self.outside_personal_attributes, 'Outside')
        self.addTab(self.related_people_attributes, 'Relations')
        self.setTabPosition(QTabWidget.North)

        self.setWindowTitle('Agelena Consociata')
        self.setGeometry(400, 400, 2000, 1200)

    def add_button_clicked(self):
        today = datetime.datetime.today().strftime('%d.%m.%Y')
        address_book = self.address_book.collect_information()
        address_book['last_changed'] = today

        add_person_in_people(address_book)
        self.entries_window.refresh()
        self.entries_window.setVisible(True)
        self.destroy()
