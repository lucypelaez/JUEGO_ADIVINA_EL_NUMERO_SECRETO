import random  # importamos la biblioteca random para que posteriormente el programa pueda generar un número aleatorio

# 1. Generamos el número secreto
numero_secreto = random.randint(1, 100)     # numero_secreto es la variable y random.randint es el método
intentos = 0                                # establecemos un contador de intentos para que empiece a contar a partir de cero
adivinado = False                           # variable booleana, significa que mientras adivinado no coincida con el número random sigue dando intentos al usuario

print("¡Bienvenido al juego de adivinar!")                          # Mostramos un mensaje de Bienvenida para iniciar el juego
print("He pensado un número entre 1 y 100. ¿Puedes adivinarlo?")    # Mostramos un mensaje que indique al jugador cual es el objetivo

# 2. Creamos un bucle que se repita hasta que el usuario acierte
while not adivinado:
    intento_usuario = int(input("Introduce tu número: "))           # le decimos al programa que pida al usuario que ingrese un numero
    intentos += 1                                                   # cada intento fallido sumara un dígito al contador

    if intento_usuario < numero_secreto:                            # establecemos pistas con condicionales  `[if, elif, else25]`
        print("Demasiado bajo. ¡Intenta otra vez!")
    elif intento_usuario > numero_secreto:
        print("Demasiado alto. ¡Prueba de nuevo!")
    else:
        adivinado = True
        print(f"¡Felicidades! Lo lograste en {intentos} intentos.")