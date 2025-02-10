import random

# el uso de funciones es debido a que si importo este modulo en otro.. se  ejecutara de una vez todo el codigo..

def jugar():
    print('*************************************************')
    print('*********       Adivina el numero       *********')
    print('*************************************************')
    print("Elije el nivel de dificultad")
    print("(1) Novato (2) Intermedio (3) Avanzado")

    # le decimos al usuario que ingrese el nivel que desea jugar y conforme a su eleccion asi sera la cantidad de intentos
    nivel = int(input("Nivel: "))

    if nivel == 1:
        total_intentos = 20
    elif nivel == 2:
        total_intentos = 10
    else:
        total_intentos = 5

    numero_secreto = random.randint(1, 100)
    # print(numero_secreto)

    # declaramos la cantidad de puntos inicial con la que empieza el juego
    puntos = 1000


    for intento in range(1, total_intentos + 1):
        print(f"Intento {intento} de {total_intentos}")

        # Introducir numero
        entrada = input('Ingrese el numero: ')
        valor = int(entrada)

        if (valor < 1 or valor > 100):
            print('Digita un numero mayor que 0 y menor o igual a 100')
            continue

        acierto = valor == numero_secreto
        mayor = valor > numero_secreto
        menor = valor < numero_secreto

        # validacion
        if (acierto):
            print('Haz adivinado el numero secreto')
            print(f"Tu puntaje es de {puntos}")
            break
        else:
            if (mayor):
                print('El numero secreto es menor')
            elif (menor):
                print('El numero secreto es mayor')
                
            # puntos perdidos = numero secreto - la cantidad que ingreso el usuario en consola..
            puntos_perdidos = abs(numero_secreto - valor)
            puntos = puntos - puntos_perdidos

    print('El juego ha concluido')

# si al momento de llamarlo recibe este valor.. pues ejecuta la funcion jugar
# esto debido a si quiero solo llamar este archivo individualmente (para que se ejecute solo el)
# es muy comun verlo, sin esto no se ejecutaria individualmente
if (__name__ == "__main__"):
    jugar()