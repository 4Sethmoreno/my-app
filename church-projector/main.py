# main.py
# Church Projector
# Copyright (C) 2025 Seth Moreno
# Licensed under the MIT License.

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())