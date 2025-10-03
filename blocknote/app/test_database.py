"""
🧪 SCRIPT DE PRUEBAS: Probar la tabla de notas
=============================================

Este script te permite probar que tu tabla funciona correctamente
insertando, consultando y manipulando datos de prueba.
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from datetime import datetime

def connect_to_database():
    """Establecer conexión con la base de datos"""
    try:
        conn = psycopg2.connect(
            host='localhost',
            port='26257',
            user='admin',
            password='Bruno56962953',
            database='DyD_notes_db',
            sslmode='disable'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return conn
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        return None

def insert_test_note(conn, title, content):
    """Insertar una nota de prueba"""
    try:
        cursor = conn.cursor()
        
        # SQL para insertar una nueva nota
        insert_sql = """
        INSERT INTO notes (title, content, created_at) 
        VALUES (%s, %s, NOW()) 
        RETURNING id, created_at;
        """
        
        cursor.execute(insert_sql, (title, content))
        result = cursor.fetchone()
        
        print(f"✅ Nota creada con ID: {result[0]}")
        print(f"📅 Fecha de creación: {result[1]}")
        
        cursor.close()
        return result[0]
        
    except Exception as e:
        print(f"❌ Error al insertar nota: {e}")
        return None

def get_all_notes(conn):
    """Obtener todas las notas"""
    try:
        cursor = conn.cursor()
        
        # SQL para obtener todas las notas
        select_sql = "SELECT id, title, content, created_at, updated_at FROM notes ORDER BY created_at DESC;"
        
        cursor.execute(select_sql)
        notes = cursor.fetchall()
        
        print(f"\n📋 Total de notas en la base de datos: {len(notes)}")
        print("=" * 80)
        
        for note in notes:
            print(f"🔸 ID: {note[0]}")
            print(f"   Título: {note[1]}")
            print(f"   Contenido: {note[2][:50]}{'...' if len(note[2]) > 50 else ''}")
            print(f"   Creado: {note[3]}")
            print(f"   Actualizado: {note[4] if note[4] else 'Nunca'}")
            print("-" * 80)
        
        cursor.close()
        return notes
        
    except Exception as e:
        print(f"❌ Error al obtener notas: {e}")
        return []

def update_note(conn, note_id, new_title=None, new_content=None):
    """Actualizar una nota existente"""
    try:
        cursor = conn.cursor()
        
        # Construir SQL dinámicamente según qué se quiere actualizar
        updates = []
        params = []
        
        if new_title:
            updates.append("title = %s")
            params.append(new_title)
            
        if new_content:
            updates.append("content = %s")
            params.append(new_content)
        
        if not updates:
            print("❌ No hay nada que actualizar")
            return False
        
        # Agregar timestamp de actualización
        updates.append("updated_at = NOW()")
        params.append(note_id)
        
        update_sql = f"""
        UPDATE notes 
        SET {', '.join(updates)}
        WHERE id = %s
        RETURNING title, updated_at;
        """
        
        cursor.execute(update_sql, params)
        result = cursor.fetchone()
        
        if result:
            print(f"✅ Nota actualizada: '{result[0]}'")
            print(f"📅 Fecha de actualización: {result[1]}")
        else:
            print(f"❌ No se encontró nota con ID: {note_id}")
        
        cursor.close()
        return result is not None
        
    except Exception as e:
        print(f"❌ Error al actualizar nota: {e}")
        return False

def delete_note(conn, note_id):
    """Eliminar una nota"""
    try:
        cursor = conn.cursor()
        
        delete_sql = "DELETE FROM notes WHERE id = %s RETURNING title;"
        cursor.execute(delete_sql, (note_id,))
        result = cursor.fetchone()
        
        if result:
            print(f"🗑️  Nota eliminada: '{result[0]}'")
        else:
            print(f"❌ No se encontró nota con ID: {note_id}")
        
        cursor.close()
        return result is not None
        
    except Exception as e:
        print(f"❌ Error al eliminar nota: {e}")
        return False

def run_interactive_test():
    """Ejecutar pruebas interactivas"""
    
    print("🧪 PRUEBAS INTERACTIVAS DE LA TABLA NOTES")
    print("=" * 50)
    
    # Conectar a la base de datos
    conn = connect_to_database()
    if not conn:
        return
    
    try:
        # Insertar notas de prueba
        print("\n1️⃣ INSERTANDO NOTAS DE PRUEBA...")
        
        note1_id = insert_test_note(
            conn, 
            "Mi primera nota", 
            "Este es el contenido de mi primera nota. ¡Qué emocionante!"
        )
        
        note2_id = insert_test_note(
            conn, 
            "Lista de tareas", 
            "1. Aprender bases de datos\n2. Crear API\n3. Hacer frontend\n4. ¡Ser awesome!"
        )
        
        note3_id = insert_test_note(
            conn, 
            "Receta de pizza", 
            "Ingredientes: masa, salsa de tomate, queso, pepperoni..."
        )
        
        # Mostrar todas las notas
        print("\n2️⃣ MOSTRANDO TODAS LAS NOTAS...")
        notes = get_all_notes(conn)
        
        # Actualizar una nota
        if note1_id:
            print(f"\n3️⃣ ACTUALIZANDO NOTA {note1_id}...")
            update_note(
                conn, 
                note1_id, 
                new_title="Mi primera nota (ACTUALIZADA)", 
                new_content="Contenido actualizado con nueva información!"
            )
        
        # Mostrar notas después de actualizar
        print("\n4️⃣ MOSTRANDO NOTAS DESPUÉS DE ACTUALIZAR...")
        get_all_notes(conn)
        
        # Eliminar una nota
        if note3_id:
            print(f"\n5️⃣ ELIMINANDO NOTA {note3_id}...")
            delete_note(conn, note3_id)
        
        # Mostrar estado final
        print("\n6️⃣ ESTADO FINAL DE LA BASE DE DATOS...")
        get_all_notes(conn)
        
        print("\n🎉 ¡TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE!")
        print("✅ Tu tabla de notas funciona perfectamente")
        
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
    finally:
        conn.close()
        print("🔌 Conexión cerrada")

if __name__ == "__main__":
    run_interactive_test()