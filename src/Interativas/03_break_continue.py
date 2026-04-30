# 'break' sirve para salir de un bucle de golpe.
# 'continue' sirve para saltarse solo una vuelta y seguir con la siguiente.

# 1. Ejemplo de break: parar cuando encontramos algo
for numero in range(1, 11):
    if numero == 5:
        print("¡Encontré el 5! Me salgo del bucle.")
        break
    print(f"Número: {numero}")

# 2. Ejemplo de continue: saltar los números pares
print("Solo números impares:")
for numero in range(1, 11):
    if numero % 2 == 0:
        continue # Si es par, se salta el print y va a la siguiente vuelta
    print(numero)

# 3. Filtrar temperaturas negativas
temperaturas = [22, -5, 28, 31, -15, 19]
print("Temperaturas buenas (positivas):")
for temp in temperaturas:
    if temp <= 0:
        continue # No mostramos las bajo cero
    print(f"{temp} grados")

# 4. Validar una lista de datos y saltar errores
datos = ["10", "hola", "20", "mundo", "30"]
suma = 0
for d in datos:
    if not d.isdigit():
        print(f"Cuidado: '{d}' no es un número, lo ignoro.")
        continue
    suma += int(d)
print(f"La suma total es: {suma}")

# 5. Salir de bucles anidados usando una variable (bandera)
encontrado = False
for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Encontré un resultado mayor a 10: {i} * {j} = {i*j}")
            encontrado = True
            break # Sale del bucle de adentro
    if encontrado:
        break # Sale del bucle de afuera