#explicacion del loop while

# Ejemplo básico de while
print("\nEjemplo 1: Contador básico")
moneda = 5
while moneda > 0:
    print(f"Tienes {moneda} monedas")
    moneda -= 1
    print("perdiste una moneda")
print("Te quedaste sin monedas!")

# Ejemplo con entrada del usuario
print("\nEjemplo 2: Adivina el número")
numero_secreto = 7
intento = 0
while intento != numero_secreto:
    intento = int(input("Adivina el número (1-10): "))
    if intento < numero_secreto:
        print("Muy bajo!")
    elif intento > numero_secreto:
        print("Muy alto!")
print("¡Correcto!")

# Ejemplo con break
print("\nEjemplo 3: Using break")
contador = 0
while True:
    if contador >= 5:
        break
    print(f"Contador: {contador}")
    contador += 1

# Ejemplo con continue
print("\nEjemplo 4: Using continue")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(f"Número: {i}")
