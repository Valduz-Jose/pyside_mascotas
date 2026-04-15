from PySide6.QtWidgets import QMessageBox  # [NUEVO]
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QSizePolicy
)
from PySide6.QtCore import Qt

from services.mascota_service import MascotaService


class HomeView(QWidget):
    """
    Vista principal que muestra el listado de mascotas
    """

    def __init__(self, on_edit=None):
        super().__init__()

        self.on_edit = on_edit  # callback hacia app

        # =========================
        # LAYOUT PRINCIPAL
        # =========================
        layout = QVBoxLayout()
        self.setLayout(layout)

        # =========================
        # ENCABEZADO
        # =========================
        titulo = QLabel("🐾 Sistema de Adopción de Mascotas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 20pt; font-weight: bold;")

        subtitulo = QLabel("Gestión de mascotas disponibles para adopción")
        subtitulo.setAlignment(Qt.AlignCenter)

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        # =========================
        # TABLA
        # =========================
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Especie", "Peso"])
        self.tabla.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)  # [NUEVO]
        self.tabla.cellDoubleClicked.connect(self.on_double_click)  # [NUEVO]
        layout.addWidget(self.tabla)

        # Control de espacios (dashboard)
        layout.setStretch(0, 0)
        layout.setStretch(1, 0)
        layout.setStretch(2, 1)

        # =========================
        # CARGAR DATOS
        # =========================
        self.cargar_datos()

    def cargar_datos(self):
        """
        Carga las mascotas desde la base de datos
        """
        servicio = MascotaService()
        mascotas = servicio.obtener_todos()

        self.tabla.setRowCount(len(mascotas))

        for fila, mascota in enumerate(mascotas):
            self.tabla.setItem(fila, 0, QTableWidgetItem(str(mascota.id)))
            self.tabla.setItem(fila, 1, QTableWidgetItem(mascota.nombre))
            self.tabla.setItem(fila, 2, QTableWidgetItem(mascota.especie))
            self.tabla.setItem(fila, 3, QTableWidgetItem(str(mascota.peso)))

    # [MODIFICADO]
    def on_double_click(self, row, column):
        item_id = self.tabla.item(row, 0)

        if item_id:
            mascota_id = int(item_id.text())

            if self.on_edit:
                self.on_edit(mascota_id)