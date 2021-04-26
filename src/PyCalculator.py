from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import CalculatorGUI

#import mathlib


class App(QMainWindow, CalculatorGUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_zero.clicked.connect(lambda: self.button_click("0"))
        self.pushButton_doublezero.clicked.connect(lambda: self.button_click("00"))
        self.pushButton_one.clicked.connect(lambda: self.button_click("1"))
        self.pushButton_two.clicked.connect(lambda: self.button_click("2"))
        self.pushButton_three.clicked.connect(lambda: self.button_click("3"))
        self.pushButton_four.clicked.connect(lambda: self.button_click("4"))
        self.pushButton_five.clicked.connect(lambda: self.button_click("5"))
        self.pushButton_six.clicked.connect(lambda: self.button_click("6"))
        self.pushButton_seven.clicked.connect(lambda: self.button_click("7"))
        self.pushButton_eight.clicked.connect(lambda: self.button_click("8"))
        self.pushButton_nine.clicked.connect(lambda: self.button_click("9"))
        self.pushButton_point.clicked.connect(lambda: self.button_click("."))
        self.pushButton_ABS.clicked.connect(lambda: self.button_click("abs"))
        self.pushButton_mul.clicked.connect(lambda: self.button_click("*"))
        self.pushButton_plus.clicked.connect(lambda: self.button_click("+"))
        self.pushButton_minus.clicked.connect(lambda: self.button_click("-"))
        self.pushButton_div.clicked.connect(lambda: self.button_click("/"))
        self.pushButton_squareroot.clicked.connect(lambda: self.button_click("√"))
        self.pushButton_fact.clicked.connect(lambda: self.button_click("fac"))
        self.pushButton_power.clicked.connect(lambda: self.button_click("^"))
        self.pushButton_AC.clicked.connect(lambda: self.button_click("AC"))
        self.pushButton_DEL.clicked.connect(lambda: self.button_click("DEL"))
        self.pushButton_equal.clicked.connect(lambda: self.button_click("="))

    def button_click(self, text):
        if text == "AC":
            self.clear_display()
        elif text == "DEL":
            if len(self.display_text()) > 0:
                self.remove_one()
        elif text == "=":
            self.clear_display()
        else:
            self.set_display_text(text)

    def set_display_text(self, text):
        temp = self.display_text() + text
        self.lineEdit.setText(temp)

    def clear_display(self):
        self.lineEdit.setText("")

    def display_text(self):
        return self.lineEdit.text()

    def remove_one(self):
        text = self.display_text()
        text_len = len(text)
        if text[text_len - 1] == "s" or text[text_len - 1] == "c":
            new_text = text[:-3]
        else:
            new_text = text[:-1]
        self.clear_display()
        self.set_display_text(new_text)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            self.button_click("0")
        elif event.key() == Qt.Key_1:
            self.button_click("1")
        elif event.key() == Qt.Key_2:
            self.button_click("2")
        elif event.key() == Qt.Key_3:
            self.button_click("3")
        elif event.key() == Qt.Key_4:
            self.button_click("4")
        elif event.key() == Qt.Key_5:
            self.button_click("5")
        elif event.key() == Qt.Key_6:
            self.button_click("6")
        elif event.key() == Qt.Key_7:
            self.button_click("7")
        elif event.key() == Qt.Key_8:
            self.button_click("8")
        elif event.key() == Qt.Key_9:
            self.button_click("9")
        elif event.key() == Qt.Key_Period:
            self.button_click(".")
        elif event.key() == Qt.Key_Plus:
            self.button_click("+")
        elif event.key() == Qt.Key_Minus:
            self.button_click("-")
        elif event.key() == Qt.Key_Asterisk:
            self.button_click("*")
        elif event.key() == Qt.Key_Slash:
            self.button_click("/")
        elif event.key() == Qt.Key_9:
            self.button_click("9")
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.button_click("=")
        elif event.key() == Qt.Key_Backspace:
            self.button_click("DEL")
        print(event.text())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    calculator = App()
    # Form = QWidget()
    # ui = CalculatorGUI.Ui_Form()
    # ui.setupUi(Form)
    # Form.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     myapp = QtWidgets.QMainWindow()
#     myapp.show()
#     sys.exit(app.exec_())


        ##self.pushButton_six.clicked(print("sest\n"))

# class CaclDisplay(QtWidgets.QMainWindow):
#     def set_display_text(self, text):
#         self.lineEdit.setText(text)
#         self.lineEdit.setFocus()
#
#     def display_text(self):
#         return self.lineEdit.text()
#
#     def clear_display(self):
#         self.set_display_text("")



