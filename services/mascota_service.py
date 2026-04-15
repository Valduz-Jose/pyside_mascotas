from database import SessionLocal
from models.mascota import Mascota


class MascotaService:
    """
    Capa de acceso a datos (Service Layer)
    """

    def obtener_todos(self):
        """
        Retorna todas las mascotas registradas
        """
        session = SessionLocal()
        try:
            mascotas = session.query(Mascota).all()
            return mascotas
        finally:
            session.close()

    def crear(self, datos):
        """
        Crea una nueva mascota en la base de datos
        """
        session = SessionLocal()
        try:
            # Validación básica
            if not datos["nombre"] or not datos["especie"] or not datos["peso"]:
                raise ValueError("Todos los campos son obligatorios")

            mascota = Mascota(
                nombre=datos["nombre"],
                especie=datos["especie"],
                peso=float(datos["peso"])
            )

            session.add(mascota)
            session.commit()

            return mascota

        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def obtener_por_id(self, mascota_id):
        """
        Obtiene una mascota por su ID
        """
        session = SessionLocal()
        try:
            mascota = session.query(Mascota).filter(Mascota.id == mascota_id).first()
            return mascota
        finally:
            session.close()

            # [NUEVO]
    def actualizar(self, mascota_id, datos):
        """
        Actualiza una mascota existente
        """
        session = SessionLocal()
        try:
            mascota = session.query(Mascota).filter(Mascota.id == mascota_id).first()

            if not mascota:
                raise ValueError("Mascota no encontrada")

            # Validación básica
            if not datos["nombre"] or not datos["especie"] or not datos["peso"]:
                raise ValueError("Todos los campos son obligatorios")

            mascota.nombre = datos["nombre"]
            mascota.especie = datos["especie"]
            mascota.peso = float(datos["peso"])

            session.commit()

            return mascota

        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def eliminar(self, mascota_id):
        """
        Elimina una mascota por su ID
        """
        session = SessionLocal()
        try:
            mascota = session.query(Mascota).filter(Mascota.id == mascota_id).first()

            if not mascota:
                raise ValueError("Mascota no encontrada")

            session.delete(mascota)
            session.commit()

            return True

        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()