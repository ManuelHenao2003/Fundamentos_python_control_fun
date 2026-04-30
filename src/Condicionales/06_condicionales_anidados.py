# Los condicionales anidados son 'if' que están adentro de otros 'if'.
# Se usan cuando una decisión depende de otra que tomamos antes.

# Ejemplo 1: Edad y estado civil
edad = 30
estado_civil = 'soltero'
if edad >= 18:
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    print('Eres menor de edad.')

# Ejemplo 2: Licencia de conducir con muchos niveles
edad = 16
permiso_padres = True
if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
else:
    if edad >= 16:
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        print('Eres demasiado joven para conducir.')

# Ejemplo 3: Solo pedir contraseña si el usuario es correcto
usuario = 'admin'
contrasena = '1234'
if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')

# Ejemplo 4: Buscar el número más grande de tres
a = 5
b = 10
c = 15
if a > b:
    if a > c:
        print('a es el mayor.')
    else:
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')

# Una forma más fácil de hacer lo de arriba
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print(f'El número mayor es {mayor}.')