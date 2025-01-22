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
#cursor = conexion.cursor()

