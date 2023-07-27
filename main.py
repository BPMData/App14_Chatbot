import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget,\
    QTableWidgetItem, QDialog, QVBoxLayout, QLineEdit, QPushButton, QComboBox, \
    QAbstractItemView, QToolBar, QStatusBar, QLabel, QMessageBox,  \
    QStyle, QGridLayout, QWidget, QTextEdit, QSizePolicy

class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BPM's ChatBot")
        self.setGeometry(200, 200, 500, 500)
        self.setFixedSize(self.size())
        self.setStyleSheet("background-color: #2f3136;")

        self.chat_area = QTextEdit(self)

        # Add input field widget:
        self.input_field = QTextEdit(self)
        self.input_field.setStyleSheet("background-color: #808080; color: white;")
        # Change dimensions of the input field:
        # self.input_field.setFixedHeight(50)
        font_metrics = self.input_field.fontMetrics()
        line_height = font_metrics.lineSpacing()
        self.input_field.setFixedHeight(4 * line_height)

        # Add the "Submit query to ChatBot" button:
        self.button = QPushButton("Submit query to ChatBot", self)
        self.button.setStyleSheet("background-color: #808080; color: black;")

        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        self.show()

class ChatBot:
    pass

app = QApplication(sys.argv)
window = ChatBotWindow()
window.show()
sys.exit(app.exec())