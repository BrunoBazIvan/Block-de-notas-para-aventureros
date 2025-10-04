"""
🗒️ GUÍA COMPLETA: CÓMO CREAR TABLAS EN BASE DE DATOS
===================================================

Esta guía te explica paso a paso cómo crear y gestionar tablas en una base de datos
para tu aplicación de notas, desde lo más básico hasta conceptos avanzados.

📚 CONCEPTOS FUNDAMENTALES
=========================

1. ¿QUÉ ES UNA TABLA?
   - Es como una hoja de cálculo que organiza información
   - Tiene columnas (campos) y filas (registros)
   - Cada fila es un elemento único (una nota)

2. ¿QUÉ ES UNA CLAVE PRIMARIA?
   - Es un identificador único para cada fila
   - En tu caso, cada nota tiene un 'id' único
   - Nunca se repite, siempre es diferente

3. TIPOS DE DATOS COMUNES:
   - INTEGER: Números enteros (1, 2, 3...)
   - STRING/TEXT: Texto ("Mi nota", "Contenido...")
   - TIMESTAMP: Fechas y horas
   - BOOLEAN: Verdadero o falso

🔧 PASOS PARA CREAR UNA TABLA
============================

PASO 1: PLANIFICACIÓN
---------------------
Antes de crear código, piensa:
- ¿Qué información necesito guardar?
- ¿Qué tipo de datos es cada campo?
- ¿Cuáles campos son obligatorios?
- ¿Necesito fechas automáticas?

Para notas, decidiste:
- id: Identificador único (número)
- title: Título (texto obligatorio)
- content: Contenido (texto obligatorio)
- created_at: Fecha de creación (automática)
- updated_at: Fecha de actualización (opcional)

PASO 2: DEFINIR EL MODELO
-------------------------
En archivo models/note.py ya tienes:

```python
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from blocknote.app.database import Base

class NoteDB(Base):
    __tablename__ = "notes"  # Nombre de la tabla en la BD
    
    # Cada Column define una columna de la tabla
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)      # obligatorio
    content = Column(String, nullable=False)    # obligatorio
    created_at = Column(DateTime, default=datetime.now)  # fecha automática
    updated_at = Column(DateTime, nullable=True) # opcional
```

EXPLICACIÓN DE PARÁMETROS:
- primary_key=True: Esta es la clave primaria
- index=True: Crea un índice para búsquedas rápidas
- nullable=False: El campo es obligatorio
- nullable=True: El campo es opcional
- default=datetime.now: Pone la fecha actual automáticamente

PASO 3: CREAR LA TABLA FÍSICAMENTE
----------------------------------
Tienes dos métodos:

MÉTODO A - SQL Directo (create_db_manual.py):
```python
# Comando SQL que crea la tabla
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,           -- Clave primaria autoincrementable
    title STRING NOT NULL,           -- Título obligatorio
    content STRING NOT NULL,         -- Contenido obligatorio
    created_at TIMESTAMP DEFAULT NOW(), -- Fecha automática
    updated_at TIMESTAMP             -- Fecha opcional
);
```

MÉTODO B - SQLAlchemy (create_db_sqlalchemy.py):
```python
# Crea automáticamente basándose en los modelos
Base.metadata.create_all(bind=engine)
```

📋 COMANDOS PARA EJECUTAR
========================

1. USANDO SQL DIRECTO:
   cd /home/brunobaz/Escritorio/proyectos\ /BackEnd/Block_de_notas_aventurero/blocknote
   python app/create_db_manual.py

2. USANDO SQLALCHEMY (RECOMENDADO):
   cd /home/brunobaz/Escritorio/proyectos\ /BackEnd/Block_de_notas_aventurero/blocknote
   python app/create_db_sqlalchemy.py

🔍 VERIFICAR QUE FUNCIONA
=========================

Después de crear la tabla, puedes verificar:

1. CONECTARTE A LA BASE DE DATOS:
   cockroach sql --insecure --host=localhost:26257 --database=DyD_notes_db

2. VER LAS TABLAS:
   SHOW TABLES;

3. VER ESTRUCTURA DE LA TABLA:
   DESCRIBE notes;

4. INSERTAR UNA NOTA DE PRUEBA:
   INSERT INTO notes (title, content) VALUES ('Mi primera nota', 'Contenido de prueba');

5. VER LAS NOTAS:
   SELECT * FROM notes;

⚠️ PROBLEMAS COMUNES Y SOLUCIONES
=================================

ERROR: "relation does not exist"
SOLUCIÓN: La tabla no existe, ejecuta el script de creación

ERROR: "connection refused"
SOLUCIÓN: CockroachDB no está ejecutándose, inicia el servicio

ERROR: "permission denied"
SOLUCIÓN: El usuario no tiene permisos, verifica credenciales

ERROR: "duplicate key value"
SOLUCIÓN: Intentas insertar un ID que ya existe

🚀 CÓMO EJECUTAR EL SCRIPT PARA CREAR TABLAS
============================================

UBICACIÓN ACTUALIZADA: El script está en app/DB/

OPCIÓN 1: Script independiente (RECOMENDADO)
-------------------------------------------
Ejecuta desde el directorio del proyecto:

```bash
cd "blocknote/app/DB"
python create_tables_standalone.py
```

Este script:
✅ Funciona sin problemas de importaciones
✅ Incluye prueba de conexión
✅ Muestra información detallada de las tablas creadas

OPCIÓN 2: Script original (requiere ajustes)
-------------------------------------------
Si quieres usar el script original, ejecuta desde el directorio app:

```bash
cd "blocknote/app"
python -m DB.create_db_sqlalchemy
```

⚠️ NOTAS IMPORTANTES:
- Asegúrate de que CockroachDB esté ejecutándose
- Verifica que la base de datos 'DyD_notes_db' exista
- El script mostrará información detallada de las tablas creadas

🎉 RESULTADO EXITOSO:
Verás el mensaje "✅ PROCESO COMPLETADO EXITOSAMENTE"
y la información de la tabla 'notes' con sus columnas.

🚀 PRÓXIMOS PASOS
================

1. ✅ Crear la tabla (¡Ya completado!)
2. Probar insertar datos manualmente
3. Desarrollar la API para CRUD operations:
   - CREATE: Crear nuevas notas
   - READ: Leer notas existentes
   - UPDATE: Actualizar notas
   - DELETE: Eliminar notas

💡 CONSEJOS IMPORTANTES
======================

1. SIEMPRE HACER RESPALDOS antes de cambios importantes
2. USAR MIGRACIONES para cambios en producción
3. VALIDAR DATOS antes de insertarlos
4. USAR ÍNDICES para búsquedas frecuentes
5. DOCUMENTAR cambios en la estructura

🔄 MIGRACIONES (CONCEPTO AVANZADO)
=================================

Cuando tu aplicación esté en producción con datos reales,
NO puedes simplemente borrar y recrear tablas.

Usas MIGRACIONES para:
- Agregar nuevas columnas
- Modificar tipos de datos
- Crear nuevas tablas
- Mantener datos existentes

Tu proyecto incluye Alembic para esto, pero es tema avanzado.

================================================================================
¡Con esta guía tienes todo lo necesario para crear y gestionar tu tabla de notas!
================================================================================
"""