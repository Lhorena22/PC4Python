def crear_tabla_multiplicar(numero):
  with open(f"tabla-{numero}.txt", "w") as archivo:
    for i in range(1, 11):
      archivo.write(f"{numero} x {i} = {numero * i}\n")

def leer_tabla_multiplicar(numero):
  try:
    with open(f"tabla-{numero}.txt", "r") as archivo:
      lineas = archivo.readlines()
      for linea in lineas:
        print(linea.strip())
  except FileNotFoundError:
    print(f"El archivo tabla-{numero}.txt no existe.")

def leer_linea_tabla_multiplicar(numero, linea):
  try:
    with open(f"tabla-{numero}.txt", "r") as archivo:
      lineas = archivo.readlines()
      print(lineas[linea - 1].strip())
  except FileNotFoundError:
    print(f"El archivo tabla-{numero}.txt no existe.")

def main():
  while True:
    print("Opciones:")
    print("1. Crear tabla de multiplicar")
    print("2. Leer tabla de multiplicar")
    print("3. Leer línea de tabla de multiplicar")
    print("4. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
      numero = int(input("Ingrese un número entre 1 y 10: "))
      crear_tabla_multiplicar(numero)
      print(f"La tabla de multiplicar del {numero} se ha creado correctamente.")
    elif opcion == 2:
      numero = int(input("Ingrese un número entre 1 y 10: "))
      leer_tabla_multiplicar(numero)
    elif opcion == 3:
      numero = int(input("Ingrese un número entre 1 y 10: "))
      linea = int(input("Ingrese la línea a leer: "))
      leer_linea_tabla_multiplicar(numero, linea)
    elif opcion == 4:
      break
    else:
      print("Opción no válida.")

if __name__ == "__main__":
  main()

