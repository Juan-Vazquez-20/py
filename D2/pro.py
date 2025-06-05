#calcular comision
#nombre
#cuanto an vendido
#comision del 15%


nombre = input("Ingresa tu nombre: ")
print(nombre)
venta = input("cuantos an vendido")
print(venta)
venta = float(venta)
comision = venta * 0.13
comision2 = round(venta * 13/100,2)
print(comision)

print(f"tu nombre es {nombre}, tu tola de ventas es {venta}y tu comision es {comision} y tu comision es {comision2}")

