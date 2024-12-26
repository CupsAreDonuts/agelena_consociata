from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton


class RelationalAttributes(QWidget):
    def __init__(self, add_new_entry_window):
        super().__init__()  # noqa
        self.add_new_entry_window = add_new_entry_window
        self.family_label = QLabel('Family:')
        self.family_input = QTextEdit()
        self.friendships_label = QLabel('Friendships:')
        self.friendships_input = QTextEdit()
        self.professional_label = QLabel('Professional:')
        self.professional_input = QTextEdit()
        self.romantic_label = QLabel('Romantic')
        self.romantic_input = QTextEdit()
        self.communities_label = QLabel('Communities:')
        self.communities_input = QTextEdit()
        self.add_entry_button = QPushButton('Add')
        self.back_button = QPushButton('Back')

    def create_tab(self):
        if self.add_new_entry_window.edit_mode:
            try:
                self.family_input.setText(self.add_new_entry_window.person['family'])
                self.friendships_input.setText(self.add_new_entry_window.person['friendships'])
                self.professional_input.setText(self.add_new_entry_window.person['professional'])
                self.romantic_input.setText(self.add_new_entry_window.person['romantic'])
                self.communities_input.setText(self.add_new_entry_window.person['communities'])

            except KeyError:
                pass

        self.add_entry_button.setMinimumWidth(130)
        self.add_entry_button.clicked.connect(self.add_new_entry_window.add_button_clicked)  # noqa
        self.back_button.clicked.connect(self.add_new_entry_window.back_button_clicked)  # noqa

        layout = QVBoxLayout()
        layout.addWidget(self.family_label)
        layout.addWidget(self.family_input)
        layout.addWidget(self.friendships_label)
        layout.addWidget(self.friendships_input)
        layout.addWidget(self.professional_label)
        layout.addWidget(self.professional_input)
        layout.addWidget(self.romantic_label)
        layout.addWidget(self.romantic_input)
        layout.addWidget(self.communities_label)
        layout.addWidget(self.communities_input)
        layout.addWidget(self.add_entry_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)
        self.setWindowTitle('Agelena Consociata')

    def collect_information(self):
        return {
            'family': self.family_input.toPlainText(),
            'friendships': self.friendships_input.toPlainText(),
            'professional': self.professional_input.toPlainText(),
            'romantic': self.romantic_input.toPlainText(),
            'communities': self.communities_input.toPlainText()
        }
