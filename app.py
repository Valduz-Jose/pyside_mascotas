import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🐾 PySide Mascotas")
        self.setMinimumSize(1280, 720)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        central_widget.setLayout(layout)

        titulo = QLabel("🐾 Sistema de Adopción de Mascotas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 20pt; font-weight: bold; color: white;")

        subtitulo = QLabel("Gestión de mascotas disponibles para adopción")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setStyleSheet("color: #cccccc;")

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)


def main():
    print("🚀 Iniciando aplicación...")

    app = QApplication(sys.argv)

    # 🔥 DARK MODE NATIVO (SIN QDarkStyle)
    app.setStyle("Fusion")
    app.setStyleSheet("""
        QMainWindow {
            background-color: #121212;
        }
        QLabel {
            color: white;
        }
    """)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()