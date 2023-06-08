
# run qt script

import sys
from PyQt6.QtWidgets import QApplication

from parent_package.main_window import MainWindowApplication
from splash.splash_widget import SplashScreenWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreenWidget()
    window.show()
    sys.exit(app.exec())