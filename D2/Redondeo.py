#rendodeo
import math

numero = 3.14159

print(f"Número original: {numero}")
print(f"Redondeo con round(): {round(numero, 2)}")
print(f"Redondeo hacia abajo con floor(): {math.floor(numero)}")
print(f"Redondeo hacia arriba con ceil(): {math.ceil(numero)}")
print(f"Redondeo con format: {format(numero, '.2f')}")

# Más ejemplos
numero2 = 2.5
numero3 = 3.5
print(f"\nRedondeo de {numero2}: {round(numero2)}")  # redondea a 2
print(f"Redondeo de {numero3}: {round(numero3)}")  # redondea a 4
