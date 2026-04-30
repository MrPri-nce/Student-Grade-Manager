"""Main module that starts the app"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from gui import GradeManagerWindow

def main() -> None:
    """start the app"""
    app = QApplication(sys.argv)
    window = GradeManagerWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()