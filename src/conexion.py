import mysql.connector

conexion = mysql.connector.connect(
    user = 'proyecto',
    password = 'P@ssw0rd',
    host = '68.221.253.134',
    database = 'siete_y_medio', 
    port = '3306' # Aquí coloca el nombre de tu base de datos
)

if conexion.is_connected():
    print("Conexión segura exitosa a la base de datos")

# Crear un cursor para ejecutar las consultas
cursor = conexion.cursor()

# Consulta SQL para insertar datos
consulta_insert = """
    INSERT INTO players (nombre, puntos, rango, is_human, created_at)
    VALUES (%s, %s, %s, %s, %s);
"""

# Valores que deseas insertar
valores = ('Juan', 30, 'Atrevido', True, "2025-01-15 14:30:00")

# Ejecutar la consulta con los valores
cursor.execute(consulta_insert, valores)

# Confirmar los cambios en la base de datos (hacer commit)
conexion.commit()

# Verificar cuántas filas se han insertado
print(f"{cursor.rowcount} fila(s) insertada(s).")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()