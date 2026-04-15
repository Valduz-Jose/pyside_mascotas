
from services.mascota_service import MascotaService
from PySide6.QtWidgets import QMessageBox
from services.mascota_service import MascotaService
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QHBoxLayout
)
from PySide6.QtCore import Qt


class FormView(QWidget):
    """
    Formulario para registrar nuevas mascotas
    """

    def __init__(self, on_cancel=None):
        super().__init__()
        
        self.mascota_id = None
        self.on_cancel = on_cancel  # Callback para volver

        # =========================
        # LAYOUT PRINCIPAL
        # =========================
        layout = QVBoxLayout()
        self.setLayout(layout)

        # =========================
        # ENCABEZADO
        # =========================
        titulo = QLabel("🐾 Registrar Mascota")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18pt; font-weight: bold;")

        subtitulo = QLabel("Ingrese los datos de la mascota")
        subtitulo.setAlignment(Qt.AlignCenter)

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        # =========================
        # FORMULARIO
        # =========================
        form_layout = QFormLayout()

        self.input_nombre = QLineEdit()
        self.input_especie = QLineEdit()
        self.input_peso = QLineEdit()

        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Especie:", self.input_especie)
        form_layout.addRow("Peso (kg):", self.input_peso)

        layout.addLayout(form_layout)

        # =========================
        # BOTONES
        # =========================
        botones_layout = QHBoxLayout()

        self.btn_guardar = QPushButton("Guardar")
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_eliminar = QPushButton("Eliminar")
        botones_layout.addWidget(self.btn_eliminar)
        self.btn_guardar.setText("Guardar")
        botones_layout.addWidget(self.btn_guardar)
        botones_layout.addWidget(self.btn_cancelar)

        layout.addLayout(botones_layout)

        # =========================
        # EVENTOS
        # =========================
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.btn_guardar.clicked.connect(self.guardar)  
        self.btn_eliminar.clicked.connect(self.eliminar)
    # =========================
    # ACCIONES
    # =========================
    def cancelar(self):
        """
        Acción de cancelar → volver al inicio
        """
        if self.on_cancel:
            self.on_cancel()

    # [MODIFICADO]
    def guardar(self):
        """
        Procesa guardar o actualizar mascota
        """
        datos = {
            "nombre": self.input_nombre.text(),
            "especie": self.input_especie.text(),
            "peso": self.input_peso.text()
        }

        servicio = MascotaService()

        try:
            # 🔥 MODO EDICIÓN
            if self.mascota_id:
                servicio.actualizar(self.mascota_id, datos)
                QMessageBox.information(self, "Éxito", "Mascota actualizada correctamente")

            # 🔥 MODO CREACIÓN
            else:
                servicio.crear(datos)
                QMessageBox.information(self, "Éxito", "Mascota creada correctamente")

            # Limpiar formulario
            self.input_nombre.clear()
            self.input_especie.clear()
            self.input_peso.clear()
            self.mascota_id = None
            self.btn_guardar.setText("Guardar")

            # Volver al inicio
            if self.on_cancel:
                self.on_cancel()

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    
    def cargar_mascota(self, mascota_id):
        """
        Carga y muestra datos en el formulario (modo edición)
        """
        servicio = MascotaService()
        mascota = servicio.obtener_por_id(mascota_id)

        if mascota:
            self.mascota_id = mascota.id

            self.input_nombre.setText(mascota.nombre)
            self.input_especie.setText(mascota.especie)
            self.input_peso.setText(str(mascota.peso))
            self.btn_guardar.setText("Guardar cambios")  

    def eliminar(self):
        """
        Elimina la mascota actual con confirmación
        """
        if not self.mascota_id:
            QMessageBox.warning(self, "Error", "No hay mascota seleccionada")
            return

        confirmacion = QMessageBox.question(
            self,
            "Confirmar",
            "¿Estás seguro de eliminar esta mascota?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmacion == QMessageBox.Yes:
            servicio = MascotaService()

            try:
                servicio.eliminar(self.mascota_id)

                QMessageBox.information(self, "Éxito", "Mascota eliminada correctamente")

                # Limpiar formulario
                self.input_nombre.clear()
                self.input_especie.clear()
                self.input_peso.clear()
                self.mascota_id = None
                self.btn_guardar.setText("Guardar")

                # Volver al inicio
                if self.on_cancel:
                    self.on_cancel()

            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))