import psycopg2
import pandas as pd

# Conectarse a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="Datos",
    user="postgres",
    password="51+9=60"
)

# Crear una tabla si no existe
create_table_query = """
CREATE TABLE IF NOT EXISTS personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(15)
);
"""
with conn, conn.cursor() as cur:
    cur.execute(create_table_query)

# Insertar datos de ejemplo
insert_data_query = """
INSERT INTO personas (nombre, apellido, telefono)
VALUES
    ('Juan', 'Pérez', '123-456-7890'),
    ('María', 'Gómez', '987-654-3210'),
    ('Carlos', 'López', '555-555-5555');
"""
with conn, conn.cursor() as cur:
    cur.execute(insert_data_query)

# Obtener la lista de personas ordenada por apellido de forma descendente en un DataFrame
query = "SELECT * FROM personas ORDER BY apellido DESC;"
df = pd.read_sql_query(query, conn)

# Mostrar el DataFrame en pantalla
print(df)

# Cerrar la conexión
conn.close()