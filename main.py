import sys

from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget,\
    QTableWidgetItem, QDialog, QVBoxLayout, QLineEdit, QPushButton, QComboBox, \
    QAbstractItemView, QToolBar, QStatusBar, QLabel, QMessageBox,  \
    QStyle, QGridLayout, QWidget, QTextEdit, QSizePolicy
from backend import ChatBot
import threading



class ChatBotWindow(QMainWindow):
    responseReceived = pyqtSignal(str)  # Define a new signal

    def __init__(self):
        super().__init__()

        self.chatbot = ChatBot()
        self.responseReceived.connect(self.append_response)

        self.setWindowTitle("BPM's ChatBot")
        self.setGeometry(200, 200, 500, 500)
        self.setFixedSize(self.size())
        self.setStyleSheet("background-color: #2f3136; color: white;")

        self.chat_area = QTextEdit(self)
        self.chat_area.setReadOnly(True)

        # Add input field widget:
        self.input_field = TextEdit(self)
        self.input_field.setStyleSheet("background-color: #808080; color: white;")
        # Change dimensions of the input field:
        font_metrics = self.input_field.fontMetrics()
        line_height = font_metrics.lineSpacing()
        self.input_field.setFixedHeight(4 * line_height)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the "Submit query to ChatBot" button:
        self.button = QPushButton("Submit query to ChatBot", self)
        self.button.setStyleSheet("background-color: #808080; color: black;")
        self.button.clicked.connect(self.send_message)


        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        self.show()

    def send_message(self):
        try:
                user_input = self.input_field.toPlainText().strip()
                if not user_input:
                    return "Please enter a query."
                else:
                    self.chat_area.append(f"Your query: {user_input}")
                    self.input_field.clear()

                    thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
                    thread.start()
        except Exception as e:
            print(f"An error occured: {e}")
            QMessageBox.warning(self, "Error", str(e))
            return "An error occured while getting the response."
    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input, tokens=1000)
        self.responseReceived.emit(response)

    def append_response(self, response):
       self.chat_area.append(f"<p style='color:  #FFC300'>gpt-3.5-turbo: {response}</p>")

class TextEdit(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent=parent)

    returnPressed = pyqtSignal()

    def keyPressEvent(self, qKeyEvent):
        super().keyPressEvent(qKeyEvent)
        try:
            if qKeyEvent.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
                # ChatBot.connect(self.send_message)
                self.returnPressed.emit()

        except Exception as e:
            print(f"An error occured: {e}")
            QMessageBox.warning(self, "Error", str(e))
            return "An error occured while getting the response."

app = QApplication(sys.argv)
window = ChatBotWindow()
window.show()
print(type(Qt.Key.Key_Enter))
print(type(Qt.Key.Key_Return))
sys.exit(app.exec())