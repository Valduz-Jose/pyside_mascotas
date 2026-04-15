import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# =========================
# CARGAR VARIABLES .ENV
# =========================
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# =========================
# URL DE CONEXIÓN MYSQL
# =========================
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# =========================
# ENGINE (CONEXIÓN PRINCIPAL)
# =========================
engine = create_engine(DATABASE_URL, echo=True)

# =========================
# SESSION (TRANSACCIONES)
# =========================
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# =========================
# BASE (MODELOS ORM)
# =========================
Base = declarative_base()

# Permite importar Base desde otros módulos fácilmente
__all__ = ["engine", "SessionLocal", "Base"]
# =========================
# PRUEBA DE CONEXIÓN
# =========================
if __name__ == "__main__":
    try:
        connection = engine.connect()
        print("✅ Conexión exitosa a MySQL")
        print("Conexión:", connection)
        connection.close()
    except Exception as e:
        print("❌ Error de conexión:", e)