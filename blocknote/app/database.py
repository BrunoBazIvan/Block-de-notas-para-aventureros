from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión: usando el dialecto específico de CockroachDB
DATABASE_URL = "cockroachdb+psycopg2://admin:Bruno56962953@localhost:26257/DyD_notes_db?sslmode=disable"

engine = create_engine(
    DATABASE_URL, 
    echo=True,
    connect_args={
        "application_name": "blocknote_app",
        "options": "-c default_transaction_isolation=serializable"
    },
    # Configuraciones adicionales para evitar problemas de versión
    pool_pre_ping=True,
    pool_recycle=300
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()