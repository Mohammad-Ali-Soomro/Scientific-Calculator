import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QPushButton, QWidget, QLineEdit, QTextEdit, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt

class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.initUI()

    def initUI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout(self.centralWidget)
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.layout.addWidget(self.display)

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.history_label = QLabel("History", self)
        self.history_label.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.history_label)

        self.history_display = QTextEdit(self)
        self.history_display.setReadOnly(True)
        self.history_display.setFixedHeight(100)
        self.layout.addWidget(self.history_display)

        self.clear_history_button = QPushButton("Clear History", self)
        self.clear_history_button.setFixedWidth(100)
        self.clear_history_button.setStyleSheet("font-size: 14px; color: white; background-color: #555;")
        self.clear_history_button.clicked.connect(self.clear_history)
        self.layout.addWidget(self.clear_history_button, alignment=Qt.AlignLeft)

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.buttons = [
            '7', '8', '9', '/', 'sin', 'cos', 'tan', 'log',
            '4', '5', '6', '*', '(', ')', '^', '√',
            '1', '2', '3', '-', 'C', 'CE', 'ANS', '=',
            '0', '.', '+', 'π', 'e', 'exp', 'ln', '%'
        ]

        self.gridLayout = QGridLayout()
        self.layout.addLayout(self.gridLayout)

        row, col = 0, 0
        for button in self.buttons:
            btn = QPushButton(button)
            btn.setStyleSheet("font-size: 18px; color: white; background-color: #333;")
            btn.clicked.connect(self.on_button_click)
            self.gridLayout.addWidget(btn, row, col)
            col += 1
            if col > 7:
                col = 0
                row += 1

        self.history = []
        self.ans = 0

    def on_button_click(self):
        button = self.sender().text()

        if button == 'C':
            self.display.clear()
        elif button == 'CE':
            self.display.setText(self.display.text()[:-1])
        elif button == '=':
            try:
                expression = self.display.text()
                expression = expression.replace('^', '**').replace('sqrt', 'math.sqrt').replace('pi', 'math.pi').replace('e', 'math.e').replace('log', 'math.log10').replace('ln', 'math.log').replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan').replace('exp', 'math.exp').replace('mod', '%')
                self.ans = eval(expression)
                self.display.setText(str(self.ans))
                self.add_to_history(expression + " = " + str(self.ans))
            except Exception as e:
                self.display.setText("Error")
        elif button == 'ANS':
            self.display.setText(self.display.text() + str(self.ans))
        else:
            self.display.setText(self.display.text() + button)

    def add_to_history(self, calculation):
        self.history.insert(0, calculation)
        self.update_history_display()

    def update_history_display(self):
        self.history_display.setText("\n".join(self.history))

    def clear_history(self):
        self.history = []
        self.update_history_display()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec())