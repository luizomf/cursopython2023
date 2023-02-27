import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 150px;')
    window.v_layout.addWidget(label1)
    window.adjustFixedSize()

    window.show()
    app.exec()
