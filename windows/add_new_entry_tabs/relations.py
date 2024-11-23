from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QLineEdit, QGridLayout, QPushButton


class RelationalAttributes(QWidget):
    def __init__(self, add_new_entry_window):
        super().__init__()  # noqa
        self.add_new_entry_window = add_new_entry_window
        self.family_members_label = QLabel('Family members:')
        self.family_members_input = QTextEdit()
        self.close_people_label = QLabel('Close people:')
        self.close_people_input = QTextEdit()
        self.main_caregiver_as_child_label = QLabel('Main caregiver as child:')
        self.main_caregiver_as_child_input = QTextEdit()
        self.main_caregiver_behaviour_label = QLabel('Main caregiver behaviour:')
        self.main_caregiver_behaviour_input = QTextEdit()
        self.parents_label = QLabel('Parents:')
        self.parents_input = QLineEdit()
        self.parental_care_label = QLabel('How did the parents care for the person?')
        self.parental_care_input = QTextEdit()
        self.siblings_label = QLabel('Siblings:')
        self.siblings_input = QLineEdit()
        self.sibling_care_label = QLabel('How much did siblings care for person?')
        self.sibling_care_input = QTextEdit()
        self.current_romantic_partner_label = QLabel('Current romantic partner:')
        self.current_romantic_partner_input = QLineEdit()
        self.romantic_ex_partners_label = QLabel('Romantic ex partners:')
        self.romantic_ex_partners_input = QTextEdit()
        self.type_of_romantic_relationships_in_past_label = QLabel('Type of romantic relationships in past:')
        self.type_of_romantic_relationships_in_past_input = QTextEdit()
        self.type_of_romantic_relationship_at_present_label = QLabel('Type of romantic relationship at present:')
        self.type_of_romantic_relationship_at_present_input = QLineEdit()
        self.close_friends_label = QLabel('Close friends:')
        self.close_friends_input = QTextEdit()
        self.close_enemies_label = QLabel('Close enemies:')
        self.close_enemies_input = QTextEdit()
        self.likes_these_people_label = QLabel('Likes these people:')
        self.likes_these_people_input = QTextEdit()
        self.dislikes_these_people_label = QLabel('Dislikes these people:')
        self.dislikes_these_people_input = QTextEdit()
        self.social_circles_label = QLabel('Social circles:')
        self.social_circles_input = QTextEdit()
        self.close_friend_groups_label = QLabel('Close friend groups')
        self.close_friend_groups_input = QTextEdit()
        self.relationship_with_family_label = QLabel('Relationship with family:')
        self.relationship_with_family_input = QTextEdit()
        self.frequency_of_visiting_family_label = QLabel('Frequency of visiting family:')
        self.frequency_of_visiting_family_input = QTextEdit()
        self.likes_to_visit_family_label = QLabel('Likes to visit family?')
        self.likes_to_visit_family_input = QLineEdit()
        self.current_crushes_label = QLabel('Current crushes (love):')
        self.current_crushes_input = QTextEdit()
        self.possibly_useful_people_for_person_label = QLabel('Possibly useful people for this person:')
        self.possibly_useful_people_for_person_input = QTextEdit()
        self.person_probably_useful_for_these_people_label = QLabel('Person is or could likely be useful for these:')
        self.person_probably_useful_for_these_people_input = QTextEdit()
        self.useful_people_already_known_to_person_label = QLabel('Useful people already known to person:')
        self.useful_people_already_known_to_person_input = QTextEdit()
        self.reputation_in_each_social_circle_label = QLabel('Reputation in each social circle: ')
        self.reputation_in_each_social_circle_input = QTextEdit()
        self.reputation_with_close_friends_label = QLabel('Reputation with close friends:')
        self.reputation_with_close_friends_input = QTextEdit()
        self.specific_actions_in_past_label = QLabel('tba')
        self.predicted_future_actions_label = QLabel('tba')
        self.past_meetings_label = QLabel('Past Meetings:')
        self.past_meetings_input = QTextEdit()
        self.add_entry_button = QPushButton('Add')
        self.back_button = QPushButton('Back')

    def create_tab(self):
        self.add_entry_button.setMinimumWidth(130)
        self.add_entry_button.clicked.connect(self.add_new_entry_window.add_button_clicked)  # noqa
        self.back_button.clicked.connect(self.add_new_entry_window.back_button_clicked)  # noqa

        layout = QGridLayout()
        layout.addWidget(self.family_members_label, 0, 0, 1, 1)
        layout.addWidget(self.family_members_input, 0, 1, 1, 1)
        layout.addWidget(self.close_people_label, 1, 0, 1, 1)
        layout.addWidget(self.close_people_input, 1, 1, 1, 1)
        layout.addWidget(self.main_caregiver_as_child_label, 2, 0, 1, 1)
        layout.addWidget(self.main_caregiver_as_child_input, 2, 1, 1, 1)
        layout.addWidget(self.main_caregiver_behaviour_label, 3, 0, 1, 1)
        layout.addWidget(self.main_caregiver_behaviour_input, 3, 1, 1, 1)
        layout.addWidget(self.parents_label, 4, 0, 1, 1)
        layout.addWidget(self.parents_input, 4, 1, 1, 1)
        layout.addWidget(self.parental_care_label, 5, 0, 1, 1)
        layout.addWidget(self.parental_care_input, 5, 1, 1, 1)
        layout.addWidget(self.siblings_label, 6, 0, 1, 1)
        layout.addWidget(self.siblings_input, 6, 1, 1, 1)
        layout.addWidget(self.sibling_care_label, 7, 0, 1, 1)
        layout.addWidget(self.sibling_care_input, 7, 1, 1, 1)
        layout.addWidget(self.current_romantic_partner_label, 8, 0, 1, 1)
        layout.addWidget(self.current_romantic_partner_input, 8, 1, 1, 1)
        layout.addWidget(self.romantic_ex_partners_label, 9, 0, 1, 1)
        layout.addWidget(self.romantic_ex_partners_input, 9, 1, 1, 1)
        layout.addWidget(self.type_of_romantic_relationships_in_past_label, 10, 0, 1, 1)
        layout.addWidget(self.type_of_romantic_relationships_in_past_input, 10, 1, 1, 1)
        layout.addWidget(self.type_of_romantic_relationship_at_present_label, 11, 0, 1, 1)
        layout.addWidget(self.type_of_romantic_relationship_at_present_input, 11, 1, 1, 1)
        layout.addWidget(self.close_friends_label, 12, 0, 1, 1)
        layout.addWidget(self.close_friends_input, 12, 1, 1, 1)
        layout.addWidget(self.close_enemies_label, 13, 0, 1, 1)
        layout.addWidget(self.close_enemies_input, 13, 1, 1, 1)
        layout.addWidget(self.likes_these_people_label, 14, 0, 1, 1)
        layout.addWidget(self.likes_these_people_input, 14, 1, 1, 1)
        layout.addWidget(self.dislikes_these_people_label, 15, 0, 1, 1)
        layout.addWidget(self.dislikes_these_people_input, 15, 1, 1, 1)
        layout.addWidget(self.social_circles_label, 0, 2, 1, 1)
        layout.addWidget(self.social_circles_input, 0, 3, 1, 1)
        layout.addWidget(self.close_friend_groups_label, 1, 2, 1, 1)
        layout.addWidget(self.close_friend_groups_input, 1, 3, 1, 1)
        layout.addWidget(self.relationship_with_family_label, 2, 2, 1, 1)
        layout.addWidget(self.relationship_with_family_input, 2, 3, 1, 1)
        layout.addWidget(self.frequency_of_visiting_family_label, 3, 2, 1, 1)
        layout.addWidget(self.frequency_of_visiting_family_input, 3, 3, 1, 1)
        layout.addWidget(self.likes_to_visit_family_label, 4, 2, 1, 1)
        layout.addWidget(self.likes_to_visit_family_input, 4, 3, 1, 1)
        layout.addWidget(self.current_crushes_label, 5, 2, 1, 1)
        layout.addWidget(self.current_crushes_input, 5, 3, 1, 1)
        layout.addWidget(self.possibly_useful_people_for_person_label, 6, 2, 1, 1)
        layout.addWidget(self.possibly_useful_people_for_person_input, 6, 3, 1, 1)
        layout.addWidget(self.person_probably_useful_for_these_people_label, 7, 2, 1, 1)
        layout.addWidget(self.person_probably_useful_for_these_people_input, 7, 3, 1, 1)
        layout.addWidget(self.useful_people_already_known_to_person_label, 8, 2, 1, 1)
        layout.addWidget(self.useful_people_already_known_to_person_input, 8, 3, 1, 1)
        layout.addWidget(self.reputation_in_each_social_circle_label, 9, 2, 1, 1)
        layout.addWidget(self.reputation_in_each_social_circle_input, 9, 3, 1, 1)
        layout.addWidget(self.reputation_with_close_friends_label, 10, 2, 1, 1)
        layout.addWidget(self.reputation_with_close_friends_input, 10, 3, 1, 1)
        layout.addWidget(self.specific_actions_in_past_label, 11, 2, 1, 1)
        layout.addWidget(self.predicted_future_actions_label, 11, 3, 1, 1)
        layout.addWidget(self.past_meetings_label, 12, 2, 1, 1)
        layout.addWidget(self.past_meetings_input, 12, 3, 1, 1)
        layout.addWidget(self.add_entry_button, 0, 4, 1, 1)
        layout.addWidget(self.back_button, 1, 4, 1, 1)

        self.setLayout(layout)
        self.setWindowTitle('Agelena Consociata')

    def collect_information(self):
        return {
            'family_members': self.family_members_input.toPlainText(),
            'close_people': self.close_people_input.toPlainText(),
            'main_caregiver_as_child': self.main_caregiver_as_child_input.toPlainText(),
            'main_caregiver_behaviour': self.main_caregiver_behaviour_input.toPlainText(),
            'parents': self.parents_input.text(),
            'parental_care': self.parental_care_input.toPlainText(),
            'siblings': self.siblings_input.text(),
            'siblings_care': self.sibling_care_input.toPlainText(),
            'current_romantic_partner': self.current_romantic_partner_input.text(),
            'romantic_ex_partners': self.romantic_ex_partners_input.toPlainText(),
            'type_of_romantic_relationships_in_past': self.type_of_romantic_relationships_in_past_input.toPlainText(),
            'type_of_romantic_relationship_at_present': self.type_of_romantic_relationship_at_present_input.text(),
            'close_friends': self.close_friends_input.toPlainText(),
            'close_enemies': self.close_enemies_input.toPlainText(),
            'likes_these_people': self.likes_these_people_input.toPlainText(),
            'dislikes_these_people': self.dislikes_these_people_input.toPlainText(),
            'social_circles': self.social_circles_input.toPlainText(),
            'close_friend_groups': self.close_friend_groups_input.toPlainText(),
            'relationship_with_family': self.relationship_with_family_input.toPlainText(),
            'frequency_of_visiting_family': self.frequency_of_visiting_family_input.toPlainText(),
            'likes_to_visit_family': self.likes_to_visit_family_input.text(),
            'current_crushes': self.current_crushes_input.toPlainText(),
            'possibly_useful_people_for_this_person': self.possibly_useful_people_for_person_input.toPlainText(),
            'person_probably_useful_for_these_people': self.person_probably_useful_for_these_people_input.toPlainText(),
            'useful_people_already_known_to_person': self.useful_people_already_known_to_person_input.toPlainText(),
            'reputation_in_each_social_circle': self.reputation_in_each_social_circle_input.toPlainText(),
            'reputation_with_close_friends': self.reputation_with_close_friends_input.toPlainText(),
            'specific_actions_in_past': '',  # tba
            'predicted_future_actions': '',  # tba
            'past_meetings': self.past_meetings_input.toPlainText()
        }
