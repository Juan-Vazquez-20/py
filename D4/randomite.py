from random import *

aleatorio = randint(1,10)
print(aleatorio)

color=['azul','rojo','verde']
aleatorio = choice(color)
print(aleatorio)

numero= list(range(1,101,5))
shuffle(numero)
print(numero)