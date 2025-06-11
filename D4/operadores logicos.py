# Ejemplos con operadores lógicos
es_mayor = True
tiene_permiso = False

# Operador AND
print("AND:", es_mayor and tiene_permiso)

# Operador OR
print("OR:", es_mayor or tiene_permiso)

# Operador NOT
print("NOT:", not es_mayor)

# Combinando operadores
edad = 25
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia
print("Puede conducir:", puede_conducir)

# Operadores con valores
a = 10
b = 5
c = 20
resultado = (a > b) and (c > a)
print("Resultado de comparación:", resultado)
