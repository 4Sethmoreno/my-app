# mainwindow.py
# Church Projector
# Copyright (C) 2025 Seth Moreno
# Licensed under the MIT License.

from PySide6.QtWidgets import QMainWindow, QTabWidget, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Church Projector")
        self.setMinimumSize(800, 600)

        # Create tabs
        tabs = QTabWidget()
        tabs.addTab(QWidget(), "Hymns")
        tabs.addTab(QWidget(), "Bible")
        tabs.addTab(QWidget(), "Videos")
        tabs.addTab(QWidget(), "Announcements")
        tabs.addTab(QWidget(), "Slideshows")

        # Preview area
        self.preview = QTextEdit("Preview content here")
        self.preview.setReadOnly(True)

        # Go Live button
        button = QPushButton("Go Live")
        button.clicked.connect(self.go_live)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        layout.addWidget(self.preview)
        layout.addWidget(button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def go_live(self):
        self.preview.setText("Go Live clicked!")