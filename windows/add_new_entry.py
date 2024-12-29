import datetime
from PyQt5.QtWidgets import QTabWidget, QMessageBox
from data.mongo import add_person_in_people, edit_person_in_people

from windows.add_new_entry_tabs.adress_book import AddressBook
from windows.add_new_entry_tabs.inside import InsideAttributes
from windows.add_new_entry_tabs.outside import OutsideAttributes
from windows.add_new_entry_tabs.relations import RelationalAttributes
from windows.add_new_entry_tabs.benefits_costs import BenefitsAndCosts


class NewEntryWindow(QTabWidget):
    def __init__(self, entries_window, edit_mode=False, person=None):
        super().__init__()  # noqa
        self.entries_window = entries_window
        self.edit_mode = edit_mode
        self.person = person

        self.address_book = AddressBook(self)
        self.inside_personal_attributes = InsideAttributes(self)
        self.outside_personal_attributes = OutsideAttributes(self)
        self.related_people_attributes = RelationalAttributes(self)
        self.benefits_attributes = BenefitsAndCosts(self)

    def create_window(self):
        self.address_book.create_tab()
        self.inside_personal_attributes.create_tab()
        self.outside_personal_attributes.create_tab()
        self.related_people_attributes.create_tab()
        self.benefits_attributes.create_tab()

        self.addTab(self.address_book, 'Address book')
        self.addTab(self.inside_personal_attributes, 'Inside')
        self.addTab(self.outside_personal_attributes, 'Outside')
        self.addTab(self.related_people_attributes, 'Relations')
        self.addTab(self.benefits_attributes, 'Benefits and Costs')
        self.setTabPosition(QTabWidget.North)

        self.setWindowTitle('Agelena Consociata')
        self.setGeometry(400, 400, 2000, 1200)

    def back_button_clicked(self):
        self.entries_window.setVisible(True)
        self.destroy()

    def add_button_clicked(self):
        personal_attributes = self.collect_all_information()
        if self.edit_mode:
            personal_attributes['_id'] = self.person['_id']
            edit_person_in_people(personal_attributes)
        else:
            add_person_in_people(personal_attributes)
        self.show_completed()
        self.entries_window.refresh()
        self.entries_window.setVisible(True)
        self.destroy()

    def collect_all_information(self):
        address_book = self.address_book.collect_information()
        inside = self.inside_personal_attributes.collect_information()
        outside = self.outside_personal_attributes.collect_information()
        relations = self.related_people_attributes.collect_information()
        benefits = self.benefits_attributes.collect_information()
        personal_attributes = {**address_book, **inside, **outside, **relations, **benefits}
        today = datetime.datetime.today().strftime('%d.%m.%Y')
        personal_attributes['last_changed'] = today
        return personal_attributes

    def show_completed(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Database Update')
        msg.setText("Person has been added to the database.")
        msg.setInformativeText('You will now be redirected to the entries page.')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
