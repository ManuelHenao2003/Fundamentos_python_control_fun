# Los operadores lógicos nos ayudan a juntar varias condiciones en una sola.

# 1. Operador 'and' (Y): Las dos cosas tienen que ser verdad
edad = 25
ingresos = 30000
if edad >= 18 and ingresos >= 20000:
    print("Eres elegible para el crédito.")

# 2. Operador 'or' (O): Con que una de las dos sea verdad, ya funciona
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")

# 3. Operador 'not' (NO): Cambia la verdad por mentira y al revés
llueve = False
if not llueve:
    print("Podemos salir al parque.")

# 4. Mezclando todo
# Es mejor usar paréntesis para no confundirnos
edad = 17
permiso_parental = True
if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")

# 5. El orden importa en Python
# Primero se hace el 'not', luego el 'and' y al final el 'or'
a = True
b = False
c = not b # Esto es True
resultado = a or b and c
print(f"Resultado sin paréntesis: {resultado}")

# Usando paréntesis para cambiar el orden
resultado = (a or b) and c
print(f"Resultado con paréntesis: {resultado}")

# 6. Código más cortito
usuario = "admin"
contrasena = "1234"
# En vez de poner un if dentro de otro, usamos 'and'
if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido.")