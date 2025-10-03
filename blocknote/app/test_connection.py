#!/usr/bin/env python3
"""
Script de prueba para verificar la conexión con CockroachDB
"""

from database import engine, Base, SessionLocal
from sqlalchemy import text

def test_connection():
    """Prueba la conexión a la base de datos"""
    try:
        # Crear una sesión
        session = SessionLocal()
        
        # Ejecutar una consulta simple para verificar la conexión
        result = session.execute(text("SELECT version()"))
        version = result.fetchone()[0]
        print(f"✅ Conexión exitosa!")
        print(f"📊 Versión de la base de datos: {version}")
        
        # Verificar que podemos obtener información de la base de datos
        result = session.execute(text("SELECT current_database()"))
        database = result.fetchone()[0]
        print(f"🏛️ Base de datos actual: {database}")
        
        session.close()
        return True
        
    except Exception as e:
        print(f"❌ Error al conectar con la base de datos: {e}")
        return False

def test_engine():
    """Prueba el engine directamente"""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1 as test"))
            test_value = result.fetchone()[0]
            print(f"✅ Engine funcionando correctamente: {test_value}")
            return True
    except Exception as e:
        print(f"❌ Error con el engine: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Probando conexión con CockroachDB...")
    print("=" * 50)
    
    # Probar el engine
    engine_ok = test_engine()
    
    # Probar la sesión
    session_ok = test_connection()
    
    if engine_ok and session_ok:
        print("\n🎉 ¡Todas las pruebas pasaron correctamente!")
    else:
        print("\n⚠️ Algunas pruebas fallaron. Revisa la configuración.")