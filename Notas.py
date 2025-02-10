#Recordar
# lista, tupla, set = se les conoce como colecciones
# tomar en cuenta que La lista es mutable, la tupla es inmutable (pero permiten valores repetidos).
# La lista usa corchetes [] para su inicialización, y las tuplas usan paréntesis ().
# si quiero una coleeccion que no me admita valores repetidos utilizo set se define con los {} y este no posee indice.. si se imprime recorriendolo el orden esta en desorden ya que no posee uno

"""
recorrer palabra validando si posee una letra...
palabra = 'banana'
intento = 'a'
indice = 0
for letra in palabra:
    if intento == letra:
        print(f"Encontre la letra '{letra}' en la posicion {indice}")

    indice= indice + 1
"""

""" ---------------------------------------------------------------------------------------------------------------------------"""
# compresion de lista de numeros pares e impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
numPar = [n for n in numeros if n % 2 == 0]
print(f'\nPares {numPar}')

numImpar = [x for x in numeros if x % 2 != 0]
print(f'\nImpares {numImpar} \n')
""" ---------------------------------------------------------------------------------------------------------------------------"""

#asi creo un archivo
archivo = open('ejemplo.txt', 'w')
print(archivo)

# asi cierro un archivo (siempre es buena practica)
archivo.close()

# asi abro un archivo e indico que voy a escribir en el (a = append)
eje = open('ejemplo.txt', 'a')
eje.write('\nEsto es una linea\n') # \n es para que de los saltos de linea y asi con todo lo que desee agregar (siempre y cuando asi lo desee)
eje.close()

# asi lo abro solo para leer el archivo
test = open('ejemplo.txt', 'r')
print(test.read())
test.close()
""" ---------------------------------------------------------------------------------------------------------------------------"""