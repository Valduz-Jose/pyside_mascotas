import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget
)
from PySide6.QtGui import QAction

from views.home_view import HomeView
from views.form_view import FormView


class MainWindow(QMainWindow):
    """
    Ventana principal con navegación
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🐾 PySide Mascotas")
        self.setMinimumSize(1280, 720)

        # =========================
        # STACK DE VISTAS
        # =========================
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Vistas
        # [MODIFICADO]
        self.home_view = HomeView(on_edit=self.editar_mascota)
        # Antes:

        self.form_view = FormView(on_cancel=self.mostrar_inicio)  # [MODIFICADO]

        self.stack.addWidget(self.home_view)  # index 0
        self.stack.addWidget(self.form_view)  # index 1

        # =========================
        # MENÚ
        # =========================
        self.crear_menu()

    def crear_menu(self):
        """
        Crea menú de navegación
        """
        menu = self.menuBar()

        menu_navegacion = menu.addMenu("Navegación")

        # Acción: Inicio
        accion_inicio = QAction("Inicio", self)
        accion_inicio.triggered.connect(self.mostrar_inicio)

        # Acción: Agregar Mascota
        accion_form = QAction("Agregar Mascota", self)
        accion_form.triggered.connect(self.mostrar_formulario)

        menu_navegacion.addAction(accion_inicio)
        menu_navegacion.addAction(accion_form)

    # =========================
    # NAVEGACIÓN
    # =========================
    # [MODIFICADO]
    def mostrar_inicio(self):
        self.home_view.cargar_datos()  # refresca tabla
        self.stack.setCurrentIndex(0)

    # [MODIFICADO]
    def mostrar_formulario(self):
        self.form_view.mascota_id = None
        self.form_view.input_nombre.clear()
        self.form_view.input_especie.clear()
        self.form_view.input_peso.clear()
        self.form_view.btn_guardar.setText("Guardar")

        self.stack.setCurrentIndex(1)

    # [NUEVO]
    def editar_mascota(self, mascota_id):
        """
        Abre formulario en modo edición
        """
        self.form_view.cargar_mascota(mascota_id)
        self.stack.setCurrentIndex(1)

def main():
    print("🚀 Iniciando aplicación...")

    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QTableWidget {
        border: none;
        gridline-color: #444;
    }
    QHeaderView::section {
        background-color: #333;
        padding: 6px;
        border: none;
    }
    QLineEdit {
        padding: 6px;
        border-radius: 6px;
    }
    QPushButton {
        padding: 6px 12px;
        border-radius: 6px;
    }
    """)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()