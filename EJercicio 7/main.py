import requests
import sqlite3

año = 2023
for mes in range(1, 13):
  url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={año}"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    conexion = sqlite3.connect("base.db")
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha TEXT,
        compra REAL,
        venta REAL
    );
    """)

    for dia in datos:
        fecha = dia["fecha"]
        compra = dia["compra"]
        venta = dia["venta"]
        cursor.execute("""
        INSERT INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
        """, (fecha, compra, venta))

    conexion.commit()
    cursor.close()
    conexion.close()

else:
    print(f"Error al obtener el tipo de cambio: {respuesta.status_code}")

conexion = sqlite3.connect("base.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM sunat_info")
for fila in cursor.fetchall():
    print(f"Fecha: {fila[0]} - Compra: {fila[1]} - Venta: {fila[2]}")

conexion.close()