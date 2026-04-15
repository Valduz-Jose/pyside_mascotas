from sqlalchemy import Column, Integer, String, Float
from database import Base


class Mascota(Base):
    """
    Modelo ORM que representa la tabla 'mascotas'
    """

    __tablename__ = "mascotas"

    # =========================
    # CAMPOS DE LA TABLA
    # =========================

    id = Column(Integer, primary_key=True, autoincrement=True)

    nombre = Column(String(100), nullable=False)

    especie = Column(String(50), nullable=False)

    peso = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Mascota(nombre={self.nombre}, especie={self.especie}, peso={self.peso})>"