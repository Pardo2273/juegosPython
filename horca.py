import random

def jugar():
    imprime_presentacion()
    palabra_secreta = cargar_palabra()
    letras_acertadas = inicializar_lista(palabra_secreta)
    print(letras_acertadas)

    # Mientras la persona no se ahorque o acierte la palabra el juego continua
    ahorco = False
    acerto = False
    errores = 0

    while (not ahorco and not acerto):
        intento = pide_intento()
        if intento in palabra_secreta:
            marca_intento_correcto(intento, letras_acertadas, palabra_secreta)
        else:
            errores += 1
            dibuja_horca(errores)
            print(f'La palabra no contiene la letra {intento}, te quedan {7 - errores} intentos')
        ahorco = errores == 7
        acerto = "_" not in letras_acertadas
        print(letras_acertadas)

        if ahorco:
            imprime_mensaje_perdedor(palabra_secreta)
        elif acerto:
            imprime_mensaje_vencedor(palabra_secreta)

    print('Fin del juego')
    
def imprime_presentacion():
    print('*************************************************')
    print('***********      La Horca              **********')
    print('*************************************************\n')
    print("Bienvenido al juego del ahorcado")

def cargar_palabra():
    archivo = open('palabras.txt', 'r')
    palabras = [linea.strip() for linea in archivo]
    archivo.close()

    i = random.randrange(0 ,len(palabras))
    palabra_secreta = palabras[i].strip().upper() # strip = quitamos espacios y upper = mayusculas
    return palabra_secreta

def inicializar_lista(palabra):
    return ['_' for letra in palabra] # compresion de lista, quiero que ponga un '_' por cada letra que haya en la palabra

def pide_intento():
    intento = input('\nDigita una letra: ')
    intento = intento.strip().upper()
    return intento

def marca_intento_correcto(intento, letras_acertadas, palabra_secreta):
    indice = 0

    for letra in palabra_secreta:
        if intento.upper()  == letra.upper():
            letras_acertadas[indice] = letra.upper() # si lo encuentra queda almacenadoen el indice en el que esta
            print(f"Encontre la letra '{letra}' en la posicion {indice}")
        indice += 1

def dibuja_horca(errores):
    print("  _______     ")
    print(" |/      |    ")

    if(errores == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errores == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errores == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errores == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errores == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errores == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errores == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")

def imprime_mensaje_perdedor(palabra_secreta):
    print("💀  GAME OVER  💀")
    print(f"La palabra era: {palabra_secreta}")
    print("")
    print("    +--------+    ")
    print("    |        |    ")
    print("    |        O    ")
    print("    |       /|\\  ")
    print("    |       / \\  ")
    print("    |             ")
    print("  =======         ")
    print("  ||    ||        ")
    print("  ||    ||        ")
    print("  ||    ||        ")
    print(" /  \\  /  \\      ")
    print("")

def imprime_mensaje_vencedor(palabra_secreta):
    print("🎉 ¡FELICIDADES, HAS GANADO! 🎉")
    print(f"La palabra era {palabra_secreta}")
    print("      ___________        ")
    print("     '._==_==_=_.'       ")
    print("     .-\\:      /-.      ")
    print("    | (|:.     |) |      ")
    print("     '-|:.     |-'       ")
    print("       \\::.    /        ")
    print("        '::. .'          ")
    print("          ) (            ")
    print("        _.' '._          ")
    print("       '-------'         ")
    print("        /     \\          ")
    print("       |       |         ")
    print("     (_____)_____)       ")
    print("        🏆 VICTORIA 🏆   ")
    print("        🎉 🎊 🎉 🎊      ")

if __name__ == "__main__":
    jugar()