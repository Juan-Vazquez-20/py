# Programa para demostrar el uso de zip con dos listas
import numbers

# Crear las listas para combinar
nombres = ["Juan", "María", "Pedro", "Ana", "Luis"]
edades = [25, 30, 22, 28, 35]

# Usar zip para combinar y mostrar las listas
for nombre, edad in zip(nombres, edades):
    print(f"Nombre: {nombre}, Edad: {edad} años")
