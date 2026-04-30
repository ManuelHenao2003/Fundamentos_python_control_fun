# Los parámetros son los "huecos" que dejamos en la función.
# Los argumentos son los valores reales que metemos en esos huecos.

# 1. Parámetros normales (por posición)
def calcular_precio(base, impuesto):
    return base + (base * impuesto)

print(f"Total: {calcular_precio(100, 0.21)}")

# 2. Valores por defecto (si no pones nada, usa el que ya está)
def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Juan") # Usa el mensaje de siempre
saludar("María", "¿Qué tal todo?") # Usa el mensaje nuevo

# 3. Llamar a la función usando los nombres (sin importar el orden)
def dividir(dividendo, divisor):
    return dividendo / divisor

print(f"División: {dividir(divisor=2, dividendo=10)}")

# 4. Mezclar varios tipos de parámetros
def calcular_pago(horas, tarifa=15, moneda="EUR"):
    return f"{horas * tarifa} {moneda}"

print(calcular_pago(40)) # Solo horas
print(calcular_pago(30, moneda="USD")) # Horas y moneda

# 5. Argumentos variables (*args): Cuando no sabes cuántos números te van a dar
def sumar_muchos(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(f"Suma de muchos: {sumar_muchos(1, 2, 3, 4, 5)}")

# 6. Argumentos con nombre variables (**kwargs): Para pasar datos como en un diccionario
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Python", version=3.12)