import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_tables_manually():
    """
    Función para crear las tablas manualmente usando SQL directo
    
    Esta función se conecta directamente a la base de datos CockroachDB
    y ejecuta comandos SQL para crear la tabla 'notes'
    """
    
    # PASO 1: Establecer conexión con la base de datos
    # Aquí defines los parámetros de conexión a tu base de datos
    conn = psycopg2.connect(
        host='localhost',        # Dirección del servidor (local en este caso)
        port='26257',           # Puerto de CockroachDB (por defecto es 26257)
        user='admin',           # Usuario de la base de datos
        password='Bruno56962953', # Contraseña del usuario
        database='DyD_notes_db', # Nombre de la base de datos
        sslmode='disable'       # Configuración SSL (deshabilitada para desarrollo local)
    )
    
    # PASO 2: Configurar el cursor para ejecutar comandos SQL
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # Hace que los cambios se guarden automáticamente
    cursor = conn.cursor()  # Cursor para ejecutar comandos SQL
    
    try:
        # PASO 3: Definir el SQL para crear la tabla
        # Este es el comando SQL que crea la estructura de tu tabla
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS notes (
            -- COLUMNA ID: Clave primaria que se autoincrementa
            -- SERIAL significa que CockroachDB asignará automáticamente números únicos (1, 2, 3...)
            id SERIAL PRIMARY KEY,
            
            -- COLUMNA TITLE: Para almacenar el título de la nota
            -- STRING es texto variable, NOT NULL significa que es obligatorio
            title STRING NOT NULL,
            
            -- COLUMNA CONTENT: Para almacenar el contenido de la nota
            -- También es obligatorio (NOT NULL)
            content STRING NOT NULL,
            
            -- COLUMNA CREATED_AT: Fecha y hora de creación
            -- DEFAULT NOW() significa que se pondrá automáticamente la fecha actual
            created_at TIMESTAMP DEFAULT NOW(),
            
            -- COLUMNA UPDATED_AT: Fecha y hora de última actualización
            -- Esta columna puede estar vacía (sin NOT NULL) hasta que se actualice la nota
            updated_at TIMESTAMP
        );
        """
        
        # PASO 4: Ejecutar el comando SQL para crear la tabla
        print("🔧 Creando tabla 'notes' en la base de datos...")
        cursor.execute(create_table_sql)  # Aquí se ejecuta el SQL
        print("✅ Tabla 'notes' creada exitosamente!")
        
        # PASO 5: Verificar que la tabla se creó correctamente
        # Hacemos una consulta simple para confirmar que funciona
        cursor.execute("SELECT COUNT(*) FROM notes;")
        result = cursor.fetchone()  # Obtener el resultado
        print(f"✅ Verificación: La tabla está funcionando correctamente. Registros actuales: {result[0]}")
        
        # PASO 6: Mostrar información adicional sobre la tabla
        print("\n📊 Información de la tabla creada:")
        print("- Nombre: notes")
        print("- Columnas: id, title, content, created_at, updated_at")
        print("- Tipo de base de datos: CockroachDB")
        
        print("\n🎉 ¡Base de datos configurada exitosamente!")
        print("💡 Ahora puedes usar tu API para crear, leer, actualizar y eliminar notas.")
        
    except Exception as e:
        print(f"❌ Error al crear las tablas: {e}")
        print("💡 Verifica que:")
        print("   - CockroachDB esté ejecutándose")
        print("   - Los datos de conexión sean correctos")
        print("   - Tengas permisos para crear tablas")
    finally:
        # PASO 7: Cerrar conexiones (importante para liberar recursos)
        cursor.close()  # Cerrar el cursor
        conn.close()    # Cerrar la conexión
        print("🔌 Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    create_tables_manually()