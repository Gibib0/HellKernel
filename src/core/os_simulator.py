import sys
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette

try:
    from .state_manager import StateManager
except ImportError:
    from state_manager import StateManager

class OSSimulator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.state_manager = StateManager()
        self.state_manager.load_game()

        self.setup_window()

        self.setup_background()

        self.setup_test_label()

        print('HellKernel is launched')
        print(f'The current act: {self.state_manager.current_act}')
        print(f'Keys found: {self.state_manager.keys_found}')

    def setup_window(self):
        self.showFullScreen()
        self.setWindowTitle('HellKernel OS')

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, Qt.black)
        self.setPalette(palette)

    def setup_background(self):
        PROJECT_ROOT = Path(__file__).parent.parent.parent
        background_path = PROJECT_ROOT / 'assets' / 'images' / 'desktop' / 'background.png'

        if background_path.exists():
            background_label = QLabel(self)
            pixmap = QPixmap(str(background_path))

            background_label.setPixmap(pixmap.scaled(
                self.size().width(),
                self.size().height(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            ))

            background_label.setGeometry(0, 0, self.width(), self.height())

            background_label.lower()
            print('The background is loaded')
        else:
            print(f'The background is not found: {background_path}')

    def setup_test_label(self):
        test_label = QLabel('HellKernel OS = desktop', self)
        test_label.setAlignment(Qt.AlignCenter)
        test_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 24px;
                background-color: rgba(0, 0, 0, 150);
                padding: 20px;
                border-radius: 10px;
            }
        """)

        test_label.resize(400, 100)
        test_label.move(
            (self.width() - test_label.width()) // 2,
            (self.height() - test_label.height()) // 2
        )

    def closeEvent(self, event):
        print('Closing HellKernel OS...')
        self.state_manager.save_game()
        event.accept()

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = OSSimulator()
    window.show()
    sys.exit(app.exec_())
