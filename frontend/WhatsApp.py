from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QHBoxLayout

class WhatsAppMessenger(QWidget):

    def __init__(self):
        super().__init__()

        self.send = QPushButton('Send message!')
        self.phone_number = QLineEdit()
        self.send.clicked.connect(self.send_whatsapp_message)

        layout = QHBoxLayout()
        layout.addWidget(self.phone_number)
        layout.addWidget(self.send)
        self.setLayout(layout)


    def send_whatsapp_message(self):
        print(self.phone_number.text())