import random
from pyfiglet import Figlet

def main():
  figlet = Figlet()
  fuente_aleatoria = random.choice(figlet.getFonts())
  fuente = input("Ingrese el nombre de la fuente (dejar en blanco para aleatoria): ") or fuente_aleatoria
  texto = input("Ingrese el texto a imprimir: ")
  figlet.setFont(font=fuente)
  print(figlet.renderText(texto))

if __name__ == "__main__":
  main()