# juego del ahorcado
import random

# Lista de palabras
palabras = ["gato", "perro", "casa", "luna", "tren", "sol", "leche"]

# Agregamos un while para que sea un bucle mas grande que contenga el juego
jugar = True

while jugar: 

    # palabra al azar
    palabra_secreta = random.choice(palabras)

    # Crear palabra oculta
    oculto = ["_"] * len(palabra_secreta)

    # vidas
    vidas = 6

    print("\nPalabra:", " ".join(oculto))
    # bucle principal del juego, verifica si el jugador tiene vidas y si aun hay letras por adivinar
    while vidas > 0 and "_" in oculto:

        letra = input("Adivina una letra: ")
# Verificar si la letra está en la palabra secreta
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    oculto[i] = letra
            print("¡Correcto!")
        else:
            vidas -= 1
            print("Letra incorrecta.")
            print("Vidas restantes:", vidas)

        print("Palabra:", " ".join(oculto))

    # verificar si el jugador ganó o perdió
    if "_" not in oculto:
        print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
    else:
        print("¡Has perdido! La palabra secreta era:", palabra_secreta)

    # opcion de jugar nuevamente
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() == "s":
        print("¡Genial! Reiniciando el juego...")
    else: 
        print("¡Gracias por jugar! ¡Hasta la próxima!")
        jugar = False 
       
