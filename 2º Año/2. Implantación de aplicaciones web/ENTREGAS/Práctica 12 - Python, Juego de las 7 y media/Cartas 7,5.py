import random
print ("--------------------------------------------------------------------------------------------------------------------")
print ("NOTA: Según las reglas que leo por internet, dicen: Si la Banca excede el puntaje estipulado ganan los apostadores") 
print ("que no hayan superado el puntaje ideal, por tanto no modifiqué que gane sólo el de más puntuación.")
print ("--------------------------------------------------------------------------------------------------------------------")

class Carta:
    def __init__(self, valor, nombre):
        self.nombre = nombre
        self.valor = valor

class Jugador:
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

def crear_baraja():
    baraja = []
    valores = [1, 2, 3, 4, 5, 6, 7, 0.5, 0.5, 0.5]
    nombres = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']

    for i in range (4):#4 cartas de cada valor
        for j in range(len(valores)):#10 valores
            carta = Carta(valores[j], nombres[j])
            baraja.append(carta)
    random.shuffle(baraja)
    return baraja


def pedir_cantidad_jugadores():
    cantidad_jugadores = int(input("(>) Ingresa la cantidad de jugadores: "))
    while 40 % cantidad_jugadores != 0:
        print("No es divisor de 40,")
        cantidad_jugadores = int(input("(>) Ingresa la cantidad de jugadores: "))

    return cantidad_jugadores


def crear_jugadores(cantidad_jugadores):
    jugadores = []
    puntuacion = 0
    for i in range(cantidad_jugadores):
        nombre = input(f"(>) Ingresa el nombre del jugador {i+1}: ")
        jugador = Jugador(nombre, puntuacion)

        jugadores.append(jugador)
    
    ##Banca
    banca = Jugador("BANCA", 0)
    jugadores.append(banca)
    return jugadores


def imprimir_jugadores(jugadores):
    print(f"-------------------------")
    print(f"Jugadores de la partida:")
    for jugador in jugadores:
        print(f"[{jugador.nombre}]")

#aprieta enter para continuar
    input("(>) Presiona enter para continuar")
    print(f"----------------------------------")


def jugar(jugadores, baraja):
    for jugador in jugadores:
        puntuacion = 0
        cartas = []
        carta = baraja.pop()
        puntuacion += carta.valor
        cartas.append(carta)

        print(f"[{jugador.nombre}], tu primera carta es {carta.valor}")

        while puntuacion < 7.5:
            quiere_carta = input(f"[{jugador.nombre}], quieres otra carta? (s/n)")
            if(quiere_carta == 's'):
                carta = baraja.pop()
                puntuacion += carta.valor
                cartas.append(carta)
                print(f"has sacado la carta {carta.nombre}, tu puntuacion es {puntuacion}")
            else:
                print("----------------------------------")
                break
        
        if puntuacion == 7.5:
            print(f"[{jugador.nombre}], tienes la puntuación de ganador ya: {puntuacion} puntos")
            print("----------------------------------")


        ##esto es para comparar con la banca
        jugador.puntuacion = puntuacion

#Elegí si hay empate que gane la banca
def resultados(jugadores):

    banca = jugadores.pop()
    for jugador in jugadores:


        if jugador.puntuacion > banca.puntuacion and jugador.puntuacion <= 7.5 and banca.puntuacion <= 7.5:
            print(f"[{jugador.nombre}] GANASTE con {jugador.puntuacion} puntos")
        elif banca.puntuacion > jugador.puntuacion and banca.puntuacion <= 7.5 and jugador.puntuacion <= 7.5:
            print(f"[{banca.nombre}] GANASTE con {banca.puntuacion} puntos")
            break



###Esto da mal
#        if banca.puntuacion > 7.5:
#            print(f"{banca.nombre}. PERDISTE con {banca.puntuacion} puntos")
#            banca.puntuacion = 0
#        elif jugador.puntuacion <= 7.5 and banca.puntuacion <= 7.5:
#            print(f"{jugador.nombre}. GANASTE con {jugador.puntuacion} puntos")
#        elif jugador.puntuacion <= 7.5 and jugador.puntuacion <= banca.puntuacion:
#            print(f"{banca.nombre}. GANASTE con {banca.puntuacion} puntos a {jugador.nombre}")
#        elif jugador.puntuacion > 7.5:
#            print(f"{jugador.nombre}. PERDISTE con {jugador.puntuacion} puntos")
#        elif jugador.puntuacion > banca.puntuacion:
#            print(f"{jugador.nombre}. GANASTE con {jugador.puntuacion} puntos")
             
if __name__ == "__main__":
    cantidad_jugadores = pedir_cantidad_jugadores()
    jugadores = crear_jugadores(cantidad_jugadores)
    imprimir_jugadores(jugadores)
    baraja = crear_baraja()
    jugar(jugadores, baraja)
    resultados(jugadores)