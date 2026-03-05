import random

def pedir_numero():

    while True:
        try:
            num = int(input("Introduce un número del 1 al 100: "))
            return num
        except ValueError:
            print("Esa no es una cifra válida. Prueba otra vez.")

def jugar_partida():

    numero_secreto = random.randint (1, 100)
    intentos = 0
    print ("He pensado un número del 1 al 100. Adivínalo   ")

    while True:
        intento_usuario = pedir_numero()
        intentos +=1

        if intento_usuario > numero_secreto:
            print ("demasiado alto, prueba con otro número")
        elif intento_usuario < numero_secreto:
            print ("demasiado bajo, inténtalo de nuevo")
        else:
            print ("Has acertado!, ¡Enhorabuena!")
            print (f"Lo has conseguido en {intentos} intentos ")
            return intentos    
       
def main():
    mejor_puntuacion = None

    while True:
        nuevo_intento = jugar_partida()

        if mejor_puntuacion is None or nuevo_intento < mejor_puntuacion:
            mejor_puntuacion = nuevo_intento 
            print(f"¡Nuevo récord! {mejor_puntuacion}")
        else:
            print(f"No superado. Récord: {mejor_puntuacion}")
            return nuevo_intento
            
        continuar_jugando = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if continuar_jugando != "s":
            print("Gracias por jugar")
            break

    

main()


    

            
        

        
            
    
        
















 









