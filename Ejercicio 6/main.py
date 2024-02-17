def contar_lineas_codigo(ruta_archivo):

  try:
    with open(ruta_archivo, "r") as archivo:
      lineas = archivo.readlines()
      contador_lineas = 0
      for linea in lineas:
        if not linea.strip() or linea.startswith("#"):
          continue
        contador_lineas += 1
      return contador_lineas
  except FileNotFoundError:
    print(f"El archivo '{ruta_archivo}' no existe.")
    return None

def main():
  ruta_archivo = input("Ingrese la ruta del archivo Python: ")
  lineas_codigo = contar_lineas_codigo(ruta_archivo)
  if lineas_codigo is not None:
    print(f"El archivo '{ruta_archivo}' tiene {lineas_codigo} líneas de código.")

if __name__ == "__main__":
  main()
