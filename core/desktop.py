import os
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DesktopWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HellKernell. Welcome")
        self.showFullScreen()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.background_label = QLabel(self.central_widget)
        bg_path = os.path.join(BASE_DIR, "assets", "backgrounds", "background.png")
        if os.path.exists(bg_path):
            pixmap = QPixmap(bg_path)
            scaled_pixmap = pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.background_label.setPixmap(scaled_pixmap)
        else:
            print(f"Background image is not found: {bg_path}")

        layout.addWidget(self.background_label)

        self.icons_widget = QWidget(self.central_widget)
        self.icons_widget.setGeometry(0, 0, self.width(), self.height())

        self.icons = []
        self.create_icon(os.path.join(BASE_DIR, "assets", "icons", "Internet.png"), 50, 50)
        self.create_icon(os.path.join(BASE_DIR, "assets", "icons", "Calculator.png"), 50, 250)
        self.create_icon(os.path.join(BASE_DIR, "assets", "icons", "Translator.png"), 50, 450)
        self.create_icon(os.path.join(BASE_DIR, "assets", "icons", "Trashbag.png"), 800, 700)
        self.create_icon(os.path.join(BASE_DIR, "assets", "icons", "Advicer.png"), 800, 400)
        self.create_icon(os.path.join(BASE_DIR, "assets", "icons", "Text_document.png"), 800, 450, 128)
        self.create_icon(os.path.join(BASE_DIR, "assets", "icons", "Thing", "Thing1.png"), 400, 400, 512)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'background_label') and self.background_label.pixmap():
            pixmap = self.background_label.pixmap()
            scaled_pixmap = pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.background_label.setPixmap(scaled_pixmap)

        if hasattr(self, 'icons_widget'):
            self.icons_widget.setGeometry(0, 0, self.width(), self.height())

    def create_icon(self, image_path, x, y, size=128):
        if not os.path.exists(image_path):
            print(f"The icon image is not found: {image_path}")
            return

        button = QPushButton(self.icons_widget)

        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        button.setIcon(QIcon(scaled_pixmap))
        button.setIconSize(scaled_pixmap.size())
        button.setGeometry(x, y, size, size)

        button.setStyleSheet(f"""
            QPushButton {{
                border: none;
                background: transparent;
            }}
            QPushButton:hover {{
                background: rgba(255, 255, 255, 50);
                border-radius: {size // 8}px;
            }}
            QPushButton:pressed {{
                background: rgba(255, 255, 255, 100);
            }}
        """)
        self.icons.append(button)
        return button
