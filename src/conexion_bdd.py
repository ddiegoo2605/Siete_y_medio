import mysql.connector

def get_connection():
    """Establece una conexión con la base de datos MySQL."""
    return mysql.connector.connect(
        host='68.221.253.134',  # Cambia a la IP de tu servidor
        user='proyecto',        # Usuario configurado en Azure
        password='P@ssw0rd',    # Contraseña del usuario
        database='siete_y_medio',  # Nombre de la base de datos
        port=3306,              # Puerto de MySQL
        ssl_ca='/ruta/al/certificado/ca-certificate.crt'  # Ruta al certificado SSL
    )
