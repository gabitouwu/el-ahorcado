import time
import random
BIENVENIDA='''

 ▄▄▄▄    ██▓▓█████  ███▄    █ ██▒   █▓▓█████  ███▄    █  ██▓▓█████▄  ▒█████   ▐██▌ 
▓█████▄ ▓██▒▓█   ▀  ██ ▀█   █▓██░   █▒▓█   ▀  ██ ▀█   █ ▓██▒▒██▀ ██▌▒██▒  ██▒ ▐██▌ 
▒██▒ ▄██▒██▒▒███   ▓██  ▀█ ██▒▓██  █▒░▒███   ▓██  ▀█ ██▒▒██▒░██   █▌▒██░  ██▒ ▐██▌ 
▒██░█▀  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒ ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░██░░▓█▄   ▌▒██   ██░ ▓██▒ 
░▓█  ▀█▓░██░░▒████▒▒██░   ▓██░  ▒▀█░  ░▒████▒▒██░   ▓██░░██░░▒████▓ ░ ████▓▒░ ▒▄▄  
░▒▓███▀▒░▓  ░░ ▒░ ░░ ▒░   ▒ ▒   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▓   ▒▒▓  ▒ ░ ▒░▒░▒░  ░▀▀▒ 
▒░▒   ░  ▒ ░ ░ ░  ░░ ░░   ░ ▒░  ░ ░░   ░ ░  ░░ ░░   ░ ▒░ ▒ ░ ░ ▒  ▒   ░ ▒ ▒░  ░  ░ 
 ░    ░  ▒ ░   ░      ░   ░ ░     ░░     ░      ░   ░ ░  ▒ ░ ░ ░  ░ ░ ░ ░ ▒      ░ 
 ░       ░     ░  ░         ░      ░     ░  ░         ░  ░     ░        ░ ░   ░    
      ░                           ░                          ░                     '''
NOMBRE_DEL_JUEGO='''

███████╗██╗          █████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗ 
██╔════╝██║         ██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗
█████╗  ██║         ███████║███████║██║   ██║██████╔╝██║     ███████║██║  ██║██║   ██║
██╔══╝  ██║         ██╔══██║██╔══██║██║   ██║██╔══██╗██║     ██╔══██║██║  ██║██║   ██║
███████╗███████╗    ██║  ██║██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝
╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ '''

IMÁGENES_AHORCADO = ['''

 +---+
  |  | 
  | 
  | 
  | 
  | 
 =========''', '''

 +---+
  |  | 
  |  O 
  | 
  | 
  |  
 =========''', '''

 +---+
  |  | 
  |  O 
  |  | 
  | 
  | 
 =========''', '''

 +---+
  |  | 
  |  O 
  | /| 
  | 
  | 
 =========''', '''

 +---+
  |  | 
  |  O 
  | /|\ 
  | 
  | 
 =========''', '''

 +---+
  |  | 
  |  O 
  | /|\ 
  | / 
  | 
 =========''', '''

 +---+ 
  |  | 
  |  O 
  | /|\ 
  | / \ 
  | 
 =========''','''

+---+ 
  |  | 
  | [O 
  | /|\ 
  | / \ 
  | 
 =========''','''

+---+ 
  |  | 
  | [O] 
  | /|\ 
  | / \ 
  | 
 =========''']

palabras = {'Colores':'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split(),
'Formas':'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentagono hexagono heptagono octogono'.split(),
'Frutas':'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split(),
'Animales':'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

def obtenerPalabraAlAzar(diccionarioDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    # Primero, elige una clave al azar del diccionario:
    claveDePalabras = random.choice(list(diccionarioDePalabras.keys()))
    # Segundo, elige una palabra aleatoria de la lista correspondiente a la clave en el diccionario:
    índiceDePalabra = random.randint(0, len(diccionarioDePalabras[claveDePalabras]) - 1)

    return [diccionarioDePalabras[claveDePalabras][índiceDePalabra], claveDePalabras]

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
        
    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos:
        print(letra, end=' ')
    print()

def obtenerInteno(letrasProbadas):

    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya haz probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento

def jugarDeNuevo():
    print('¿Quiéres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')
        
for i in range(len(BIENVENIDA)):
    print(BIENVENIDA[i], end='')
print('\n')
for i in range(len(NOMBRE_DEL_JUEGO)):
    print(NOMBRE_DEL_JUEGO[i], end='')
print('\n')
letrasIncorrectas=''
letrasCorrectas=''
palabraSecreta, claveSecreta=obtenerPalabraAlAzar(palabras)
juegoTerminado=False

while True:
    print('La palabra secreta pertenece al conjunto: ' + claveSecreta)
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    intento = obtenerInteno(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

        todasLasLetrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                todasLasLetrasEncontradas = False
                break
        if todasLasLetrasEncontradas:
            print('¡Sí! ¡La palabra secrta es "' + palabraSecreta + '"! ¡Has ganado con ' + str(len(letrasIncorrectas)) + ' letras incorrectas!')
            juegoTerminado = True
            
    else:
        letrasIncorrectas = letrasIncorrectas + intento

    if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado=True

    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta, claveSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break


