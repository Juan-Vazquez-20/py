#explicacion de loop for

# Ejemplo 1: Iteración sobre una lista
numeros = [1, 2, 3, 4, 5]
print("Iterando sobre una lista:")
for numero in numeros:
    print(f"Número actual: {numero}")

# Ejemplo 2: Usando range()
print("\nUsando range(5):")
for i in range(5):
    print(f"Iteración {i}")

# Ejemplo 3: Iterando sobre una cadena
texto = "Python"
print("\nIterando sobre una cadena:")
for letra in texto:
    print(f"Letra: {letra}")

# Ejemplo 4: Usando break y continue
print("\nUsando break y continue:")
for i in range(10):
    if i == 3:
        continue  # Salta esta iteración
    if i == 7:
        break  # Termina el bucle
    print(f"Valor de i: {i}")
