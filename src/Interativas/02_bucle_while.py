# El bucle 'while' se repite todo el tiempo mientras una condición sea verdad.
# Es muy útil cuando no sabemos cuántas veces vamos a repetir algo.

# 1. Ejemplo básico de contador
contador = 1
while contador <= 5:
    print(f"Cuenta: {contador}")
    contador += 1 # Importante: si no sumamos, el bucle no para nunca

# 2. Pedir algo al usuario hasta que esté bien
# Usamos .isdigit() para saber si es un número
entrada = ""
while not entrada.isdigit():
    entrada = input("Dime un número (solo números): ")
print(f"Gracias, pusiste el {entrada}")

# 3. Un bucle que parece infinito pero se corta con 'break'
while True:
    respuesta = input("¿Quieres que pare? (si/no): ").lower()
    if respuesta == "si":
        print("Vale, me detengo.")
        break
    else:
        print("Sigo funcionando...")

# 4. Un pequeño juego de adivinar
objetivo = 7
intentos = 0
adivinado = False

while not adivinado and intentos < 3:
    intentos += 1
    numero = int(input(f"Intento {intentos}/3 - ¿Qué número del 1 al 10 estoy pensando?: "))
    
    if numero == objetivo:
        print("¡Lo lograste!")
        adivinado = True
    else:
        print("Nop, intenta otra vez.")

# 5. Dibujar un triángulo con asteriscos
altura = 5
fila = 1
while fila <= altura:
    print("*" * fila)
    fila += 1