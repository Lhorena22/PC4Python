import requests
import sqlite3
from datetime import datetime

def obtener_precio_bitcoin():
  url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"
  respuesta = requests.get(url)
  if respuesta.status_code == 200:
    datos = respuesta.json()
    precio_usd = datos["bpi"]["USD"]["rate_float"]
    return precio_usd
  else:
    print(f"Error al obtener el precio de Bitcoin: {respuesta.status_code}")
    return None

def obtener_tipo_cambio(fecha):
  url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={fecha.month}&year={fecha.year}"
  respuesta = requests.get(url)
  if respuesta.status_code == 200:
    datos = respuesta.json()
    for dia in datos:
      if dia["fecha"] == fecha.strftime("%Y-%m-%d"):
        return dia["venta"]
  else:
    print(f"Error al obtener el tipo de cambio: {respuesta.status_code}")
    return None

def agregar_registro_bitcoin(fecha, precio_usd):
  conexion = sqlite3.connect("base.db")
  cursor = conexion.cursor()

  precio_gbp = precio_usd * 0.79
  precio_eur = precio_usd * 0.92
  tipo_cambio = obtener_tipo_cambio(fecha)
  if tipo_cambio is None:
    return

  precio_pen = precio_usd * tipo_cambio

  cursor.execute("""
    INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
    VALUES (?, ?, ?, ?, ?)
  """, (fecha.strftime("%Y-%m-%d"), precio_usd, precio_gbp, precio_eur, precio_pen))

  conexion.commit()
  cursor.close()
  conexion.close()

fecha = datetime.now()
precio_usd = obtener_precio_bitcoin()
tipo_cambio = obtener_tipo_cambio(fecha)

if tipo_cambio is not None:
  agregar_registro_bitcoin(fecha, precio_usd)

conexion = sqlite3.connect("base.db")
cursor = conexion.cursor()
cursor.execute("""
SELECT fecha, precio_pen, precio_eur
FROM bitcoin
ORDER BY fecha DESC
LIMIT 1;
""")

fila = cursor.fetchone()
conexion.close()

if fila is not None:
  print(f"Fecha: {fila[0]}")
  print(f"Precio de compra de 10 bitcoins en PEN: {fila[1] * 10}")
