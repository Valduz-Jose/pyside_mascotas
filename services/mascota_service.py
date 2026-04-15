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