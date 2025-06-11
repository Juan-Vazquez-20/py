#ingresar un texto
from itertools import count

texto=input("Ingresa un texto: ")

#ingresar 3 letras
letras=list(input("Ingresa 3 letras sin espacios: "))
print(texto)
print(letras)
# 5 analisis
#cunatas veces aparece las letras que el usuario ingreso en el texto.
print("\nCantidad de veces que aparece cada letra:")
for letra in letras:
    print(f"La letra '{letra}' aparece {texto.lower().count(letra.lower())} veces")

# cuantas palabras hay en el texto
palabras = len(texto.split())
print(f"\nNúmero de palabras en el texto: {palabras}")

# cual es la primera y ultima letra de texto
print(f"\nPrimera letra: {texto[0]}")
print(f"Última letra: {texto[-1]}")

# mostrara el texto invertido
print(f"\nTexto invertido: {texto[::-1]}")

# mostrara si la palabra "python" se encuentra en el texto
esta_python = "python" in texto.lower()
print(f"\n¿La palabra 'python' está en el texto?: {'Sí' if esta_python else 'No'}")
