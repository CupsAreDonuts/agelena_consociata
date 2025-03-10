from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit, QGridLayout, QPushButton


class InsideAttributes(QWidget):
    def __init__(self, add_new_entry_window):
        super().__init__()  # noqa
        self.add_new_entry_window = add_new_entry_window

        self.likes_label = QLabel('Likes:')
        self.likes_input = QTextEdit()
        self.dislikes_label = QLabel('Dislikes:')
        self.dislikes_input = QTextEdit()
        self.wants_label = QLabel('Wants or wishes:')
        self.wants_input = QTextEdit()
        self.fears_label = QLabel('Fears and concerns:')
        self.fears_input = QTextEdit()
        self.confidence_label = QLabel('How confident is the person in general?')
        self.confidence_input = QLineEdit()
        self.openness_label = QLabel('How open to new experiences and how curious is the person?')
        self.openness_input = QLineEdit()
        self.conscientiousness_label = QLabel('How disciplined, organised and conscientious is the person?')
        self.conscientiousness_input = QLineEdit()
        self.extraversion_label = QLabel('How extraverted or intraverted is the person?')
        self.extraversion_input = QLineEdit()
        self.agreeableness_label = QLabel('How agreeable, kind and cooperative is the person?')
        self.agreeableness_input = QLineEdit()
        self.neuroticism_label = QLabel('How neurotic, anxious and fearful is the person?')
        self.neuroticism_input = QLineEdit()
        self.ambitiousness_label = QLabel('How ambitious is the person?')
        self.ambitiousness_input = QLineEdit()
        self.education_label = QLabel('Education:')
        self.education_input = QLineEdit()
        self.subject_of_study_label = QLabel('Subject of study:')
        self.subject_of_study_input = QLineEdit()
        self.bad_mental_health_indicators_label = QLabel('What indicates bad mental health in the person?')
        self.bad_mental_health_indicators_input = QTextEdit()
        self.risk_tolerance_label = QLabel('How risk tolerant is the person?')
        self.risk_tolerance_input = QLineEdit()
        self.risk_seeking_label = QLabel('How risk seeking is the person?')
        self.risk_seeking_input = QLineEdit()
        self.goals_label = QLabel('Goals:')
        self.goals_input = QTextEdit()
        self.hobbies_label = QLabel('Hobbies:')
        self.hobbies_input = QTextEdit()

        self.add_entry_button = QPushButton('Add')
        self.back_button = QPushButton('Back')

    def create_tab(self):
        if self.add_new_entry_window.edit_mode:
            try:
                self.likes_input.setText(self.add_new_entry_window.person['likes'])
                self.dislikes_input.setText(self.add_new_entry_window.person['dislikes'])
                self.wants_input.setText(self.add_new_entry_window.person['wants'])
                self.fears_input.setText(self.add_new_entry_window.person['fears'])
                self.confidence_input.setText(self.add_new_entry_window.person['confidence'])
                self.openness_input.setText(self.add_new_entry_window.person['openness'])
                self.conscientiousness_input.setText(self.add_new_entry_window.person['conscientiousness'])
                self.extraversion_input.setText(self.add_new_entry_window.person['extraversion'])
                self.agreeableness_input.setText(self.add_new_entry_window.person['agreeableness'])
                self.neuroticism_input.setText(self.add_new_entry_window.person['neuroticism'])
                self.ambitiousness_input.setText(self.add_new_entry_window.person['ambitiousness'])
                self.education_input.setText(self.add_new_entry_window.person['education'])
                self.subject_of_study_input.setText(self.add_new_entry_window.person['subject_of_study'])
                self.bad_mental_health_indicators_input.setText(
                    self.add_new_entry_window.person['bad_mental_health_indicators'])
                self.risk_tolerance_input.setText(self.add_new_entry_window.person['risk_tolerance'])
                self.risk_seeking_input.setText(self.add_new_entry_window.person['risk_seeking'])
                self.goals_input.setText(self.add_new_entry_window.person['goals'])
                self.hobbies_input.setText(self.add_new_entry_window.person['hobbies'])
            except KeyError:
                pass

        self.add_entry_button.setMinimumWidth(130)
        self.add_entry_button.clicked.connect(self.add_new_entry_window.add_button_clicked)  # noqa
        self.back_button.clicked.connect(self.add_new_entry_window.back_button_clicked)  # noqa

        layout = QGridLayout()
        layout.addWidget(self.likes_label, 0, 0, 1, 1)
        layout.addWidget(self.likes_input, 0, 1, 1, 1)
        layout.addWidget(self.dislikes_label, 1, 0, 1, 1)
        layout.addWidget(self.dislikes_input, 1, 1, 1, 1)
        layout.addWidget(self.wants_label, 2, 0, 1, 1)
        layout.addWidget(self.wants_input, 2, 1, 1, 1)
        layout.addWidget(self.fears_label, 3, 0, 1, 1)
        layout.addWidget(self.fears_input, 3, 1, 1, 1)
        layout.addWidget(self.confidence_label, 4, 0, 1, 1)
        layout.addWidget(self.confidence_input, 4, 1, 1, 1)
        layout.addWidget(self.openness_label, 5, 0, 1, 1)
        layout.addWidget(self.openness_input, 5, 1, 1, 1)
        layout.addWidget(self.conscientiousness_label, 6, 0, 1, 1)
        layout.addWidget(self.conscientiousness_input, 6, 1, 1, 1)
        layout.addWidget(self.extraversion_label, 7, 0, 1, 1)
        layout.addWidget(self.extraversion_input, 7, 1, 1, 1)
        layout.addWidget(self.agreeableness_label, 8, 0, 1, 1)
        layout.addWidget(self.agreeableness_input, 8, 1, 1, 1)
        layout.addWidget(self.neuroticism_label, 9, 0, 1, 1)
        layout.addWidget(self.neuroticism_input, 9, 1, 1, 1)
        layout.addWidget(self.ambitiousness_label, 10, 0, 1, 1)
        layout.addWidget(self.ambitiousness_input, 10, 1, 1, 1)
        layout.addWidget(self.education_label, 11, 0, 1, 1)
        layout.addWidget(self.education_input, 11, 1, 1, 1)
        layout.addWidget(self.subject_of_study_label, 12, 0, 1, 1)
        layout.addWidget(self.subject_of_study_input, 12, 1, 1, 1)
        layout.addWidget(self.bad_mental_health_indicators_label, 13, 0, 1, 1)
        layout.addWidget(self.bad_mental_health_indicators_input, 13, 1, 1, 1)
        layout.addWidget(self.risk_tolerance_label, 14, 0, 1, 1)
        layout.addWidget(self.risk_tolerance_input, 14, 1, 1, 1)
        layout.addWidget(self.risk_seeking_label, 15, 0, 1, 1)
        layout.addWidget(self.risk_seeking_input, 15, 1, 1, 1)
        layout.addWidget(self.goals_label, 16, 0, 1, 1)
        layout.addWidget(self.goals_input, 16, 1, 1, 1)
        layout.addWidget(self.hobbies_label, 17, 0, 1, 1)
        layout.addWidget(self.hobbies_input, 17, 1, 1, 1)
        layout.addWidget(self.add_entry_button, 0, 2, 1, 1)
        layout.addWidget(self.back_button, 1, 2, 1, 1)
        self.setLayout(layout)
        self.setWindowTitle('Agelena Consociata')

    def collect_information(self):
        return {
            'likes': self.likes_input.toPlainText(),
            'dislikes': self.dislikes_input.toPlainText(),
            'wants': self.wants_input.toPlainText(),
            'fears': self.fears_input.toPlainText(),
            'confidence': self.confidence_input.text(),
            'openness': self.openness_input.text(),
            'conscientiousness': self.conscientiousness_input.text(),
            'extraversion': self.extraversion_input.text(),
            'agreeableness': self.agreeableness_input.text(),
            'neuroticism': self.neuroticism_input.text(),
            'ambitiousness': self.ambitiousness_input.text(),
            'education': self.education_input.text(),
            'subject_of_study': self.subject_of_study_input.text(),
            'bad_mental_health_indicators': self.bad_mental_health_indicators_input.toPlainText(),
            'risk_tolerance': self.risk_tolerance_input.text(),
            'risk_seeking': self.risk_seeking_input.text(),
            'goals': self.goals_input.toPlainText(),
            'hobbies': self.hobbies_input.toPlainText()
        }
