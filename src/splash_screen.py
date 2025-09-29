import sys
from pathlib import Path

from PyQt5.QtGui.QIcon import pixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class WelcomeOSScreen:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(True)

        PROJECT_ROOT = Path(__file__).parent.parent
        splash_image_path = PROJECT_ROOT / 'assets' / 'images' / 'splash' / 'welcomeMessageOS.jpg'

        if not splash_image_path.exists():
            print(f'The welcome image file is not found: {splash_image_path}')
            self.splash = QSplashScreen()
        else:
            pixmap = QPixmap(str(splash_image_path))
            self.splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

            self.splash.showMessage('Initialisation HellKernel...', Qt.AlignBottom | Qt.AlignCenter, Qt.white)

    def show(self, duration=3000):
        self.splash.show()

        self.app.processEvents()

        QTimer.singleShot(duration, self.close_splash)

        return self.app.exec_()

    def close_splash(self):
        self.splash.close()

        from core.os_simulator import OSSimulator
        self.main_window = OSSimulator()
        self.main_window.show()

if __name__ == '__main__':
    print('Testing splash screen...')
    splash = WelcomeOSScreen()
    splash.show(duration=2000)