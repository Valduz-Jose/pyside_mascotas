import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from views.home_view import HomeView


class MainWindow(QMainWindow):
    """
    Ventana principal que contiene las vistas
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🐾 PySide Mascotas")
        self.setMinimumSize(1280, 720)

        # Cargar vista principal
        self.home_view = HomeView()
        self.setCentralWidget(self.home_view)


def main():
    print("🚀 Iniciando aplicación...")

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()