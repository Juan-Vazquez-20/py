
#juego de adivinar el nuemero
#ingresa nombre y el nuemro
import random

nombre = input("ingresa tu nombre: ")
numero_secreto = random.randint(1, 100)
intentos = 8

print(f'Hola {nombre}, tienes {intentos} intentos para adivinar el número entre 1 y 100')

while intentos > 0:
    numero = int(input("Ingresa un número: "))
    intentos -= 1

    if numero == numero_secreto:
        print(f'¡Felicitaciones {nombre}! Has adivinado el número {numero_secreto}')
        break
    elif numero > numero_secreto:
        print(f'El número es menor. Te quedan {intentos} intentos')
    else:
        print(f'El número es mayor. Te quedan {intentos} intentos')

if intentos == 0 and numero != numero_secreto:
    print(f'Lo siento {nombre}, se acabaron los intentos. El número era {numero_secreto}')
