"""
MÉTODO ALTERNATIVO: Crear tablas usando SQLAlchemy ORM
=======================================================

Este archivo muestra cómo crear tablas usando SQLAlchemy, que es más moderno
y fácil de mantener que SQL directo.

SQLAlchemy es un ORM (Object-Relational Mapping) que:
- Traduce automáticamente entre objetos Python y tablas SQL
- Es más seguro contra inyecciones SQL
- Facilita el mantenimiento del código
- Funciona con diferentes bases de datos sin cambiar código
"""

from database import engine, Base
from models.note import NoteDB

def create_tables_with_sqlalchemy():
    """
    Función para crear todas las tablas usando SQLAlchemy ORM
    
    Esta función:
    1. Lee todos los modelos que heredan de Base
    2. Crea automáticamente las tablas correspondientes
    3. Es más segura y fácil de mantener
    """
    
    try:
        print("🔧 Creando tablas usando SQLAlchemy ORM...")
        
        # PASO 1: Crear todas las tablas definidas en los modelos
        # Base.metadata.create_all() busca todas las clases que heredan de Base
        # y crea las tablas correspondientes en la base de datos
        Base.metadata.create_all(bind=engine)
        
        print("✅ Todas las tablas han sido creadas exitosamente!")
        
        # PASO 2: Mostrar información sobre lo que se creó
        print("\n📊 Información de las tablas creadas:")
        
        # Obtener información de todas las tablas
        for table_name, table in Base.metadata.tables.items():
            print(f"\n🔹 Tabla: {table_name}")
            print("   Columnas:")
            for column in table.columns:
                # Mostrar información detallada de cada columna
                nullable_text = "Opcional" if column.nullable else "Obligatorio"
                primary_key_text = " (CLAVE PRIMARIA)" if column.primary_key else ""
                default_text = f" [Por defecto: {column.default.arg if column.default else 'Sin valor por defecto'}]" if column.default else ""
                
                print(f"     - {column.name}: {column.type} - {nullable_text}{primary_key_text}{default_text}")
        
        print("\n🎉 ¡Base de datos configurada exitosamente con SQLAlchemy!")
        print("💡 Las tablas están listas para almacenar tus notas.")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al crear las tablas con SQLAlchemy: {e}")
        print("💡 Verifica que:")
        print("   - La conexión a la base de datos funcione")
        print("   - Los modelos estén correctamente definidos")
        print("   - No haya conflictos de nombres de tablas")
        return False

def drop_all_tables():
    """
    FUNCIÓN DE UTILIDAD: Eliminar todas las tablas
    
    ⚠️  CUIDADO: Esta función borra TODAS las tablas y sus datos
    Solo úsala en desarrollo, nunca en producción
    """
    
    try:
        print("⚠️  ATENCIÓN: Eliminando todas las tablas...")
        
        # Eliminar todas las tablas
        Base.metadata.drop_all(bind=engine)
        
        print("🗑️  Todas las tablas han sido eliminadas.")
        print("💡 Puedes ejecutar create_tables_with_sqlalchemy() para recrearlas.")
        
    except Exception as e:
        print(f"❌ Error al eliminar las tablas: {e}")

def show_table_info():
    """
    FUNCIÓN DE UTILIDAD: Mostrar información sobre las tablas existentes
    """
    
    try:
        print("📋 Información de las tablas en la base de datos:")
        
        # Reflejar la estructura actual de la base de datos
        Base.metadata.reflect(bind=engine)
        
        if not Base.metadata.tables:
            print("❌ No se encontraron tablas en la base de datos.")
            print("💡 Ejecuta create_tables_with_sqlalchemy() para crearlas.")
            return
        
        for table_name, table in Base.metadata.tables.items():
            print(f"\n🔹 Tabla: {table_name}")
            for column in table.columns:
                print(f"   - {column.name}: {column.type}")
                
    except Exception as e:
        print(f"❌ Error al obtener información de las tablas: {e}")

if __name__ == "__main__":
    """
    Cuando ejecutes este archivo directamente, se ejecutará esta sección
    """
    
    print("=" * 60)
    print("🗄️  CREADOR DE TABLAS CON SQLALCHEMY")
    print("=" * 60)
    
    # Crear las tablas
    success = create_tables_with_sqlalchemy()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ PROCESO COMPLETADO EXITOSAMENTE")
        print("=" * 60)
        print("🚀 Tu base de datos está lista para almacenar notas!")
        print("🔧 Puedes ahora ejecutar tu API y empezar a crear notas.")
    else:
        print("\n" + "=" * 60)
        print("❌ PROCESO FALLIDO")
        print("=" * 60)
        print("🔧 Revisa los errores arriba y corrige la configuración.")