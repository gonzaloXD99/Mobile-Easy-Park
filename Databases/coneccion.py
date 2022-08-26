import mysql.connector

try:
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='easypark'
    )
    if connection.is_connected():
        print("conexion exitosa")
        info_server=connection.get_server_info()
        print(info_server)
        cursor=connection.cursor()
        cursor.execute("SELECT DATABASE()")
        row=cursor.fetchone()
        print("conectado a la base de datos: {}".format(row))
except Exception as ex:
    print(ex)
finally:
    if connection.is_connected():
        connection.close()
        print("conexion finalizada.")
