from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit, QGridLayout, QPushButton


class OutsideAttributes(QWidget):
    def __init__(self, add_new_entry_window):
        super().__init__()  # noqa
        self.add_new_entry_window = add_new_entry_window

        self.body_language_label = QLabel('Typical bodylanguage:')
        self.body_language_input = QTextEdit()
        self.clothes_style_label = QLabel('Typical clothes style:')
        self.clothes_style_input = QTextEdit()
        self.hygiene_label = QLabel('Typical hygiene:')
        self.hygiene_input = QLineEdit()
        self.sexual_orientation_label = QLabel('Sexual orientation:')
        self.sexual_orientation_input = QLineEdit()
        self.studying_behaviour_label = QLabel('Studying behaviour:')
        self.studying_behaviour_input = QTextEdit()
        self.loyalty_label = QLabel('Typical loyalty behaviour:')
        self.loyalty_input = QTextEdit()
        self.current_job_label = QLabel('Current job:')
        self.current_job_input = QLineEdit()
        self.job_history_label = QLabel('Job history:')
        self.job_history_input = QTextEdit()
        self.political_strategies_label = QLabel('Political strategies employed:')
        self.political_strategies_input = QTextEdit()
        self.projects_undertaken_label = QLabel('Projects undertaken:')
        self.projects_undertaken_input = QTextEdit()
        self.successful_projects_label = QLabel('Successful projects:')
        self.successful_projects_input = QTextEdit()
        self.failed_projects_label = QLabel('Failed projects')
        self.failed_projects_input = QTextEdit()
        self.social_style_label = QLabel('Typical social style:')
        self.social_style_input = QTextEdit()
        self.base_trust_label = QLabel('Base trust in the world:')
        self.base_trust_input = QLineEdit()
        self.phone_usage_label = QLabel('Phone usage behaviour:')
        self.phone_usage_input = QLineEdit()
        self.social_media_usage_label = QLabel('Social media usage behaviour:')
        self.social_media_usage_input = QTextEdit()
        self.add_entry_button = QPushButton('Add')
        self.back_button = QPushButton('Back')

    def create_tab(self):
        if self.add_new_entry_window.edit_mode:
            self.body_language_input.setText(self.add_new_entry_window.person['body_language'])
            self.clothes_style_input.setText(self.add_new_entry_window.person['clothes_style'])
            self.hygiene_input.setText(self.add_new_entry_window.person['hygiene'])
            self.sexual_orientation_input.setText(self.add_new_entry_window.person['sexual_orientation'])
            self.studying_behaviour_input.setText(self.add_new_entry_window.person['studying_behaviour'])
            self.loyalty_input.setText(self.add_new_entry_window.person['loyalty'])
            self.current_job_input.setText(self.add_new_entry_window.person['current_job'])
            self.job_history_input.setText(self.add_new_entry_window.person['job_history'])
            self.political_strategies_input.setText(self.add_new_entry_window.person['political_strategies'])
            self.projects_undertaken_input.setText(self.add_new_entry_window.person['previous_projects'])
            self.successful_projects_input.setText(self.add_new_entry_window.person['successful_projects'])
            self.failed_projects_input.setText(self.add_new_entry_window.person['failed_projects'])
            self.social_style_input.setText(self.add_new_entry_window.person['social_style'])
            self.base_trust_input.setText(self.add_new_entry_window.person['base_trust'])
            self.phone_usage_input.setText(self.add_new_entry_window.person['phone_usage'])
            self.social_media_usage_input.setText(self.add_new_entry_window.person['social_media_usage'])

        self.add_entry_button.setMinimumWidth(130)
        self.add_entry_button.clicked.connect(self.add_new_entry_window.add_button_clicked)  # noqa
        self.back_button.clicked.connect(self.add_new_entry_window.back_button_clicked)  # noqa

        layout = QGridLayout()
        layout.addWidget(self.body_language_label, 0, 0, 1, 1)
        layout.addWidget(self.body_language_input, 0, 1, 1, 1)
        layout.addWidget(self.clothes_style_label, 1, 0, 1, 1)
        layout.addWidget(self.clothes_style_input, 1, 1, 1, 1)
        layout.addWidget(self.hygiene_label, 2, 0, 1, 1)
        layout.addWidget(self.hygiene_input, 2, 1, 1, 1)
        layout.addWidget(self.sexual_orientation_label, 3, 0, 1, 1)
        layout.addWidget(self.sexual_orientation_input, 3, 1, 1, 1)
        layout.addWidget(self.studying_behaviour_label, 4, 0, 1, 1)
        layout.addWidget(self.studying_behaviour_input, 4, 1, 1, 1)
        layout.addWidget(self.loyalty_label, 5, 0, 1, 1)
        layout.addWidget(self.loyalty_input, 5, 1, 1, 1)
        layout.addWidget(self.current_job_label, 6, 0, 1, 1)
        layout.addWidget(self.current_job_input, 6, 1, 1, 1)
        layout.addWidget(self.job_history_label, 7, 0, 1, 1)
        layout.addWidget(self.job_history_input, 7, 1, 1, 1)
        layout.addWidget(self.political_strategies_label, 8, 0, 1, 1)
        layout.addWidget(self.political_strategies_input, 8, 1, 1, 1)
        layout.addWidget(self.projects_undertaken_label, 9, 0, 1, 1)
        layout.addWidget(self.projects_undertaken_input, 9, 1, 1, 1)
        layout.addWidget(self.successful_projects_label, 10, 0, 1, 1)
        layout.addWidget(self.successful_projects_input, 10, 1, 1, 1)
        layout.addWidget(self.failed_projects_label, 11, 0, 1, 1)
        layout.addWidget(self.failed_projects_input, 11, 1, 1, 1)
        layout.addWidget(self.social_style_label, 12, 0, 1, 1)
        layout.addWidget(self.social_style_input, 12, 1, 1, 1)
        layout.addWidget(self.base_trust_label, 13, 0, 1, 1)
        layout.addWidget(self.base_trust_input, 13, 1, 1, 1)
        layout.addWidget(self.phone_usage_label, 14, 0, 1, 1)
        layout.addWidget(self.phone_usage_input, 14, 1, 1, 1)
        layout.addWidget(self.social_media_usage_label, 15, 0, 1, 1)
        layout.addWidget(self.social_media_usage_input, 15, 1, 1, 1)
        layout.addWidget(self.add_entry_button, 0, 2, 1, 1)
        layout.addWidget(self.back_button, 1, 2, 1, 1)
        self.setLayout(layout)

    def collect_information(self):
        information = {
            'body_language': self.body_language_input.toPlainText(),
            'clothes_style': self.clothes_style_input.toPlainText(),
            'hygiene': self.hygiene_input.text(),
            'sexual_orientation': self.sexual_orientation_input.text(),
            'studying_behaviour': self.studying_behaviour_input.toPlainText(),
            'loyalty': self.loyalty_input.toPlainText(),
            'current_job': self.current_job_input.text(),
            'job_history': self.job_history_input.toPlainText(),
            'political_strategies': self.political_strategies_input.toPlainText(),
            'previous_projects': self.projects_undertaken_input.toPlainText(),
            'successful_projects': self.successful_projects_input.toPlainText(),
            'failed_projects': self.failed_projects_input.toPlainText(),
            'social_style': self.social_style_input.toPlainText(),
            'base_trust': self.base_trust_input.text(),
            'phone_usage': self.phone_usage_input.text(),
            'social_media_usage': self.social_media_usage_input.toPlainText()}
        return information
