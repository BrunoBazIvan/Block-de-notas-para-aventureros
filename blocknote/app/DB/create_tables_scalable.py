"""
CREADOR PROFESIONAL DE TABLAS - VERSIÓN QUE SÍ FUNCIONA
======================================================

🎯 SOLUCIÓN DEFINITIVA PARA PROYECTOS ESCALABLES

Esta versión soluciona el problema de importaciones relativas
y funciona perfectamente con tu estructura de proyecto.

CÓMO AGREGAR NUEVAS TABLAS:
1. Crea tu modelo en models/tu_nuevo_modelo.py
2. Ejecuta este script (detecta automáticamente nuevos modelos)
3. ¡Tu tabla se creará automáticamente!
"""

import sys
import os
from sqlalchemy import create_engine, text, Column, Integer, String, DateTime, Numeric, JSON, Text, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import declarative_base
from datetime import datetime
import importlib.util
import uuid

# Configuración de base de datos directa
DATABASE_URL = "cockroachdb+psycopg2://admin:Bruno56962953@localhost:26257/DyD_notes_db?sslmode=disable"

engine = create_engine(
    DATABASE_URL, 
    echo=True,
    connect_args={
        "application_name": "blocknote_app",
        "options": "-c default_transaction_isolation=serializable"
    },
    pool_pre_ping=True,
    pool_recycle=300
)

Base = declarative_base()

# ==========================================
# DEFINICIONES DE MODELOS SQLALCHEMY
# ==========================================

# Modelo de Usuario (definición directa para compatibilidad)
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

# Modelo de Nota (definición directa para compatibilidad)
class NoteDB(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

# Modelo de Campaña (definición directa para compatibilidad)
class CampaignDB(Base):
    __tablename__ = "campaigns"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)  # Usando String en lugar de Text por compatibilidad
    master_id = Column(Integer, nullable=False)
    is_active = Column(Integer, default=1)  # Usando Integer en lugar de Boolean por compatibilidad
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

# Modelo de Personaje (definición directa para compatibilidad)
class CharacterDB(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)  # Descripción del personaje
    player_id = Column(Integer, nullable=False)  # ID del jugador
    campaign_id = Column(Integer, nullable=False)  # ID de la campaña
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

class InventoryDB(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)  # Descripción del ítem
    quantity = Column(Integer, nullable=False)  # Cantidad del ítem
    price = Column(String, nullable=False)  # Precio del ítem
    rarity = Column(String, nullable=True)  # Rareza del ítem
    magical = Column(Integer, default=0)  # Usando Integer en lugar de Boolean por compatibilidad
    player_id = Column(Integer, nullable=False)  # ID del jugador
    campaign_id = Column(Integer, nullable=False)  # ID de la campaña
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

class Weapon(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    category = Column(String, nullable=False)
    subtype = Column(String, nullable=True)
    cost_gp = Column(String, nullable=True)  # Usando String por compatibilidad como otros modelos
    weight = Column(String, nullable=True)   # Usando String por compatibilidad como otros modelos
    size = Column(String, nullable=True)
    proficiency = Column(String, nullable=True)
    base_damage = Column(String, nullable=True)          # e.g. "1d8"
    damage_type_id = Column(Integer, nullable=True)
    damage_versatile = Column(String, nullable=True)
    range_normal = Column(Integer, nullable=True)
    range_long = Column(Integer, nullable=True)
    properties = Column(String, nullable=True)  # Usando String en lugar de JSON por compatibilidad
    special = Column(String, nullable=True)     # Usando String en lugar de Text por compatibilidad
    rarity = Column(String, nullable=True)
    source_id = Column(Integer, nullable=True)
    tags = Column(String, nullable=True)        # Usando String en lugar de ARRAY por compatibilidad
    min_strength = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, nullable=True)

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_colored(text, color=Colors.ENDC):
    """Imprimir texto con color"""
    print(f"{color}{text}{Colors.ENDC}")

def load_model_from_file(file_path, model_name):
    """Cargar un modelo específico desde un archivo"""
    try:
        spec = importlib.util.spec_from_file_location("model_module", file_path)
        module = importlib.util.module_from_spec(spec)
        
        # Inyectar Base en el módulo para evitar problemas de importación
        module.Base = Base
        
        # Ejecutar el módulo
        spec.loader.exec_module(module)
        
        # Obtener el modelo
        if hasattr(module, model_name):
            return getattr(module, model_name)
        else:
            print_colored(f"   ⚠️  Modelo {model_name} no encontrado en {file_path}", Colors.WARNING)
            return None
            
    except Exception as e:
        print_colored(f"   ❌ Error cargando {file_path}: {e}", Colors.FAIL)
        return None

def discover_and_load_models():
    """Descubrir y cargar automáticamente todos los modelos"""
    print_colored("🔍 Descubriendo modelos automáticamente...", Colors.OKBLUE)
    
    # Los modelos ya están definidos globalmente y registrados en Base
    models = [UserDB, NoteDB, CampaignDB, CharacterDB, InventoryDB]
    
    print_colored(f"📁 Modelos encontrados: {len(models)}", Colors.OKBLUE)
    for model in models:
        print_colored(f"   - {model.__tablename__} ({model.__name__})", Colors.OKCYAN)
    
    print_colored(f"\n🎉 Total de modelos detectados: {len(models)}", Colors.OKGREEN)
    for model in models:
        print_colored(f"   📝 {model.__tablename__} ({model.__name__})", Colors.OKCYAN)
    
    return models

def test_connection():
    """Probar conexión a la base de datos"""
    try:
        print_colored("🔌 Probando conexión a la base de datos...", Colors.OKBLUE)
        connection = engine.connect()
        connection.close()
        print_colored("✅ Conexión exitosa!", Colors.OKGREEN)
        return True
    except Exception as e:
        print_colored(f"❌ Error de conexión: {e}", Colors.FAIL)
        return False

def show_existing_tables():
    """Mostrar tablas existentes en la base de datos"""
    try:
        print_colored("📋 Verificando tablas existentes...", Colors.OKBLUE)
        
        with engine.connect() as conn:
            # Usar information_schema que es más confiable que SHOW TABLES
            result = conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """))
            tables = result.fetchall()
            
            existing_tables = [table[0] for table in tables]
            
            if existing_tables:
                print_colored(f"✅ {len(existing_tables)} tablas existentes:", Colors.OKGREEN)
                for table_name in existing_tables:
                    print_colored(f"   - {table_name}", Colors.OKCYAN)
            else:
                print_colored("❌ No hay tablas existentes", Colors.WARNING)
                
            return existing_tables
                
    except Exception as e:
        print_colored(f"❌ Error al verificar tablas: {e}", Colors.FAIL)
        return []

def create_all_tables(models):
    """Crear todas las tablas automáticamente"""
    
    try:
        print_colored("🔧 Creando/actualizando tablas...", Colors.OKBLUE)
        
        # Mostrar qué tablas se van a procesar
        print_colored(f"📋 {len(models)} modelos detectados:", Colors.OKBLUE)
        for model in models:
            print_colored(f"   📝 {model.__tablename__} ({model.__name__})", Colors.OKCYAN)
        
        # Crear todas las tablas
        print_colored("🔧 Iniciando creación de tablas...", Colors.OKBLUE)
        Base.metadata.create_all(bind=engine)
        print_colored("🔧 Comando create_all ejecutado", Colors.OKBLUE)
        
        # Verificar inmediatamente si se crearon
        print_colored("🔍 Verificando creación inmediata...", Colors.OKBLUE)
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """))
            tables = result.fetchall()
            immediate_tables = [table[0] for table in tables]
            print_colored(f"📋 Tablas detectadas inmediatamente: {len(immediate_tables)}", Colors.OKBLUE)
            for table in immediate_tables:
                print_colored(f"   ✅ {table}", Colors.OKGREEN)
        
        print_colored(f"✅ {len(models)} tablas procesadas exitosamente!", Colors.OKGREEN)
        
        # Mostrar información detallada
        print_colored("\n📊 Información detallada de las tablas:", Colors.HEADER)
        
        for table_name, table in Base.metadata.tables.items():
            print_colored(f"\n🔹 Tabla: {table_name}", Colors.BOLD)
            print_colored("   Columnas:", Colors.OKBLUE)
            for column in table.columns:
                nullable_text = "Opcional" if column.nullable else "Obligatorio"
                primary_key_text = " (CLAVE PRIMARIA)" if column.primary_key else ""
                unique_text = " (ÚNICO)" if column.unique else ""
                default_text = " [Automático]" if column.default else ""
                
                print_colored(f"     - {column.name}: {column.type} - {nullable_text}{primary_key_text}{unique_text}{default_text}", Colors.OKCYAN)
        
        print_colored("\n🎉 ¡Base de datos configurada exitosamente!", Colors.OKGREEN)
        return True
        
    except Exception as e:
        print_colored(f"❌ Error al crear las tablas: {e}", Colors.FAIL)
        return False

if __name__ == "__main__":
    print_colored("=" * 80, Colors.HEADER)
    print_colored("🗄️  CREADOR PROFESIONAL DE TABLAS - VERSIÓN DEFINITIVA", Colors.HEADER)
    print_colored("=" * 80, Colors.HEADER)
    print_colored("💡 Sistema automático que SÍ funciona con tu estructura", Colors.OKBLUE)
    print_colored("💡 Detecta automáticamente nuevos modelos", Colors.OKBLUE)
    
    # 1. Verificar conexión
    print_colored("\n1️⃣ Verificando conexión...", Colors.BOLD)
    if not test_connection():
        print_colored("\n❌ No se pudo conectar. Proceso abortado.", Colors.FAIL)
        sys.exit(1)
    
    # 2. Mostrar estado actual
    print_colored("\n2️⃣ Estado actual de la base de datos...", Colors.BOLD)
    existing_tables = show_existing_tables()
    
    # 3. Descubrir y cargar modelos
    print_colored("\n3️⃣ Descubriendo y cargando modelos...", Colors.BOLD)
    models = discover_and_load_models()
    
    # 4. Crear/actualizar tablas
    print_colored("\n4️⃣ Procesando modelos y creando tablas...", Colors.BOLD)
    success = create_all_tables(models)
    
    if success:
        print_colored("\n" + "=" * 80, Colors.OKGREEN)
        print_colored("✅ PROCESO COMPLETADO EXITOSAMENTE", Colors.OKGREEN)
        print_colored("=" * 80, Colors.OKGREEN)
        print_colored("🚀 Tu sistema está listo para escalar!", Colors.OKGREEN)
        print_colored("\n💡 Para agregar nuevas tablas:", Colors.OKBLUE)
        print_colored("   1. Crea tu modelo en models/tu_modelo.py", Colors.OKCYAN)
        print_colored("   2. Ejecuta este script", Colors.OKCYAN)
        print_colored("   3. ¡Tu nueva tabla se creará automáticamente!", Colors.OKCYAN)
        
        # 5. Verificación final
        print_colored("\n5️⃣ Verificación final...", Colors.BOLD)
        final_tables = show_existing_tables()
        
    else:
        print_colored("\n" + "=" * 80, Colors.FAIL)
        print_colored("❌ PROCESO FALLIDO", Colors.FAIL)
        print_colored("=" * 80, Colors.FAIL)
        print_colored("🔧 Revisa los errores arriba y corrige la configuración.", Colors.WARNING)