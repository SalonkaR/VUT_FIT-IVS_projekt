#!/usr/bin/env python3

##
# @brief Main spustajuci kalkulacku
import sys
from PyQt5.QtWidgets import QApplication
import GUIController

##
# @file main.py

app = QApplication(sys.argv)
calculator = GUIController.App()
sys.exit(app.exec_())