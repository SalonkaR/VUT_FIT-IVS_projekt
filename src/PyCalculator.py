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

        self.pushButton_six.clicked.connect(self.printText())  # self.set_display_text(self.display_text()))

    def printText(self):
        print("hah")

    def set_display_text(self, text):
        self.lineEdit.setText(text)
        self.lineEdit.setFocus()

    def display_text(self):
        return self.lineEdit.text()

    def clear_display(self):
        self.set_display_text("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = CalculatorGUI.Ui_Form()
    ui.setupUi(Form)
    Form.show()
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



