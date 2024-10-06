from frontend.WhatsApp import WhatsAppMessenger
from PyQt5.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.whatsapp = WhatsAppMessenger()

        self.button = QPushButton('Send Whatsapp message')
        self.button.clicked.connect(self.open_whatsapp)
        self.setCentralWidget(self.button)


    def open_whatsapp(self):
        if not self.whatsapp.isVisible():
            self.whatsapp.show()
