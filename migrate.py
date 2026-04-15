from alembic.config import Config
from alembic import command
from database import engine
from sqlalchemy import text


def limpiar_version_huerfana():
    """
    Elimina alembic_version si está inconsistente
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
            print("🧹 Tabla alembic_version limpiada (si existía)")
    except Exception as e:
        print("⚠️ No fue necesario limpiar:", e)


def migrar():
    """
    Ejecuta migraciones automáticas
    """
    try:
        limpiar_version_huerfana()

        alembic_cfg = Config("alembic.ini")

        print("🚀 Generando migración automática...")
        command.revision(
            alembic_cfg,
            message="creacion tabla mascotas",
            autogenerate=True
        )

        print("⬆️ Aplicando migraciones...")
        command.upgrade(alembic_cfg, "head")

        print("✅ Migraciones aplicadas correctamente")

    except Exception as e:
        print("❌ Error en migración:", e)


if __name__ == "__main__":
    migrar()