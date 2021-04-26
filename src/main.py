#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
import GUIController

app = QApplication(sys.argv)
calculator = GUIController.App()
sys.exit(app.exec_())