import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QKeySequence
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cool Calculator')
        self.setStyleSheet("""
            QWidget {
                background-color: #2C3E50;
                color: white;
            }
            QPushButton {
                background-color: #34495E;
                color: white;
                border: none;
                padding: 15px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QLineEdit {
                background-color: #34495E;
                color: white;
                border: none;
                padding: 10px;
                font-size: 24px;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '←', '±', '^']
        ]

        button_grid = QGridLayout()
        layout.addLayout(button_grid)

        for row, row_buttons in enumerate(buttons):
            for col, button_text in enumerate(row_buttons):
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_click)
                button_grid.addWidget(button, row, col)

        self.setGeometry(300, 300, 300, 400)

    def on_button_click(self):
        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText('Error')
        elif key == 'C':
            self.display.clear()
        elif key == '←':
            self.display.setText(self.display.text()[:-1])
        elif key == '±':
            text = self.display.text()
            if text and text[0] == '-':
                self.display.setText(text[1:])
            else:
                self.display.setText('-' + text)
        elif key == '^':
            self.display.setText(self.display.text() + '**')
        else:
            self.display.setText(self.display.text() + key)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Return or key == Qt.Key_Enter:
            self.on_button_click()  # Simulate clicking the '=' button
        elif key == Qt.Key_Escape:
            self.display.clear()
        elif key == Qt.Key_Backspace:
            self.display.setText(self.display.text()[:-1])
        else:
            super().keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())