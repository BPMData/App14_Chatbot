import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BPM's ChatBot")
        self.setMinimumSize(700, 500)
        # self.setFixedSize(self.size())
        self.setStyleSheet("background-color: #2f3136;")

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)
        '''The setGeometry() method takes four arguments: the x and y coordinates of the top-left corner of the widget, 
        and the width and height of the widget. In this case, the top-left corner is set to be 10 pixels 
        from the left and 10 pixels from the top of the window'''

        # Add input field widget:
        self.input_field = QTextEdit(self)
        self.input_field.setStyleSheet("background-color: #808080; color: white;")
        self.input_field.setGeometry(10, 330, 480, 50) # 10 pixels from the left, 350 pixels from the top, 480 pixels wide, 50 pixels tall
        # Change dimensions of the input field:
        # self.input_field.setFixedHeight(50)
        # font_metrics = self.input_field.fontMetrics()
        # line_height = font_metrics.lineSpacing()
        # self.input_field.setFixedHeight(4 * line_height)

        # Add the "Submit query to ChatBot" button:
        self.button = QPushButton("Submit query to ChatBot", self)
        self.button.setStyleSheet("background-color: #808080; color: black;")
        self.button.setGeometry(10, 380, 481, 20)

        # layout = QVBoxLayout()
        # layout.addWidget(self.chat_area)
        # layout.addWidget(self.input_field)
        # layout.addWidget(self.button)
        #
        # central_widget = QWidget(self)
        # self.setCentralWidget(central_widget)
        # central_widget.setLayout(layout)

        self.show()


app = QApplication(sys.argv)
window = ChatBotWindow()
window.show()
sys.exit(app.exec())