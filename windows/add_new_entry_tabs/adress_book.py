from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit, QGridLayout, QPushButton


class AddressBook(QWidget):
    def __init__(self, add_new_entry_window):
        super().__init__()  # noqa
        self.add_new_entry_window = add_new_entry_window
        self.first_name_label = QLabel('First Name:')
        self.first_name_input = QLineEdit()
        self.middle_name_label = QLabel('Middle Name:')
        self.middle_name_input = QLineEdit()
        self.last_name_label = QLabel('Last Name:')
        self.last_name_input = QLineEdit()
        self.birthday_label = QLabel('Birthday:')
        self.birthday_input = QLineEdit()
        self.gender_label = QLabel('Gender:')
        self.gender_input = QLineEdit()
        self.mobile_phone_label = QLabel('Mobile:')
        self.mobile_phone_input = QLineEdit()
        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        self.street_and_number_label = QLabel('Street and number:')
        self.street_and_number_input = QLineEdit()
        self.postcode_label = QLabel('Postcode:')
        self.postcode_input = QLineEdit()
        self.city_label = QLabel('City:')
        self.city_input = QLineEdit()
        self.country_label = QLabel('Country:')
        self.country_input = QLineEdit()
        self.first_contact_label = QLabel('First contact:')
        self.first_contact_input = QTextEdit()
        self.history_summary_label = QLabel('Summary of history:')
        self.history_summary_input = QTextEdit()

        self.add_entry_button = QPushButton('Add')
        self.back_button = QPushButton('Back')

    def create_tab(self):
        if self.add_new_entry_window.edit_mode:
            try:
                self.first_name_input.setText(self.add_new_entry_window.person['first_name'])
                self.middle_name_input.setText(self.add_new_entry_window.person['middle_name'])
                self.last_name_input.setText(self.add_new_entry_window.person['last_name'])
                self.birthday_input.setText(self.add_new_entry_window.person['birthday'])
                self.gender_input.setText(self.add_new_entry_window.person['gender'])
                self.mobile_phone_input.setText(self.add_new_entry_window.person['mobile_phone'])
                self.email_input.setText(self.add_new_entry_window.person['email'])
                self.street_and_number_input.setText(self.add_new_entry_window.person['street_and_number'])
                self.postcode_input.setText(self.add_new_entry_window.person['postcode'])
                self.city_input.setText(self.add_new_entry_window.person['city'])
                self.country_input.setText(self.add_new_entry_window.person['country'])
                self.first_contact_input.setText(self.add_new_entry_window.person['first_contact'])
                self.history_summary_input.setText(self.add_new_entry_window.person['history'])
            except KeyError:
                pass

        self.add_entry_button.clicked.connect(self.add_new_entry_window.add_button_clicked)  # noqa
        self.add_entry_button.setMinimumWidth(130)
        self.back_button.clicked.connect(self.add_new_entry_window.back_button_clicked)  # noqa
        layout = QGridLayout()
        layout.addWidget(self.first_name_label, 0, 0, 1, 1)
        layout.addWidget(self.first_name_input, 0, 1, 1, 1)
        layout.addWidget(self.middle_name_label, 1, 0, 1, 1)
        layout.addWidget(self.middle_name_input, 1, 1, 1, 1)
        layout.addWidget(self.last_name_label, 2, 0, 1, 1)
        layout.addWidget(self.last_name_input, 2, 1, 1, 1)
        layout.addWidget(self.birthday_label, 3, 0, 1, 1)
        layout.addWidget(self.birthday_input, 3, 1, 1, 1)
        layout.addWidget(self.gender_label, 4, 0, 1, 1)
        layout.addWidget(self.gender_input, 4, 1, 1, 1)
        layout.addWidget(self.mobile_phone_label, 5, 0, 1, 1)
        layout.addWidget(self.mobile_phone_input, 5, 1, 1, 1)
        layout.addWidget(self.email_label, 6, 0, 1, 1)
        layout.addWidget(self.email_input, 6, 1, 1, 1)
        layout.addWidget(self.street_and_number_label, 7, 0, 1, 1)
        layout.addWidget(self.street_and_number_input, 7, 1, 1, 1)
        layout.addWidget(self.postcode_label, 8, 0, 1, 1)
        layout.addWidget(self.postcode_input, 8, 1, 1, 1)
        layout.addWidget(self.city_label, 9, 0, 1, 1)
        layout.addWidget(self.city_input, 9, 1, 1, 1)
        layout.addWidget(self.country_label, 10, 0, 1, 1)
        layout.addWidget(self.country_input, 10, 1, 1, 1)
        layout.addWidget(self.first_contact_label, 11, 0, 1, 1)
        layout.addWidget(self.first_contact_input, 11, 1, 1, 1)
        layout.addWidget(self.history_summary_label, 12, 0, 1, 1)
        layout.addWidget(self.history_summary_input, 12, 1, 1, 1)
        layout.addWidget(self.add_entry_button, 0, 3, 1, 1)
        layout.addWidget(self.back_button, 1, 3, 1, 1)
        self.setLayout(layout)

        self.setWindowTitle('Agelena Consociata')

    def collect_information(self):
        return {
            'first_name': self.first_name_input.text(),
            'middle_name': self.middle_name_input.text(),
            'last_name': self.last_name_input.text(),
            'birthday': self.birthday_input.text(),
            'gender': self.gender_input.text(),
            'mobile_phone': self.mobile_phone_input.text(),
            'email': self.email_input.text(),
            'street_and_number': self.street_and_number_input.text(),
            'postcode': self.postcode_input.text(),
            'city': self.city_input.text(),
            'country': self.country_input.text(),
            'first_contact': self.first_contact_input.toPlainText(),
            'history': self.history_summary_input.toPlainText()
        }
