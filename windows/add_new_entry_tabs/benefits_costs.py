from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton


class BenefitsAndCosts(QWidget):

    def __init__(self, add_new_entry_window):
        super().__init__()  # noqa
        self.add_new_entry_window = add_new_entry_window
        self.benefits_from_me_label = QLabel('Benefits I give to person:')
        self.benefits_from_me_input = QTextEdit()
        self.benefits_to_me_label = QLabel('Benefits person gives to me:')
        self.benefits_to_me_input = QTextEdit()
        self.costs_from_me_label = QLabel('Costs I put on person:')
        self.costs_from_me_input = QTextEdit()
        self.costs_to_me_label = QLabel('Costs person puts on me:')
        self.costs_to_me_input = QTextEdit()

        self.add_entry_button = QPushButton('Add')
        self.back_button = QPushButton('Back')

    def create_tab(self):
        self.add_entry_button.clicked.connect(self.add_new_entry_window.add_button_clicked)  # noqa
        self.back_button.clicked.connect(self.add_new_entry_window.back_button_clicked)  # noqa

        if self.add_new_entry_window.edit_mode:
            try:
                self.benefits_from_me_input.setText(self.add_new_entry_window.person['benefits_from_me'])
                self.benefits_to_me_input.setText(self.add_new_entry_window.person['benefits_to_me'])
                self.costs_from_me_input.setText(self.add_new_entry_window.person['costs_from_me'])
                self.costs_to_me_input.setText(self.add_new_entry_window.person['costs_to_me'])
            except KeyError:
                pass

        layout = QVBoxLayout()
        layout.addWidget(self.benefits_from_me_label)
        layout.addWidget(self.benefits_from_me_input)
        layout.addWidget(self.benefits_to_me_label)
        layout.addWidget(self.benefits_to_me_input)
        layout.addWidget(self.costs_from_me_label)
        layout.addWidget(self.costs_from_me_input)
        layout.addWidget(self.costs_to_me_label)
        layout.addWidget(self.costs_to_me_input)
        layout.addWidget(self.add_entry_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
        self.setWindowTitle('Agelena Consociata')

    def collect_information(self):
        return {
            'benefits_from_me': self.benefits_from_me_input.toPlainText(),
            'benefits_to_me': self.benefits_to_me_input.toPlainText(),
            'costs_from_me': self.costs_from_me_input.toPlainText(),
            'costs_to_me': self.costs_to_me_input.toPlainText()
        }
