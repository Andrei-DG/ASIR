
#Hay anotaciones en el código para que sea más fácil de entender y recordar qué hace cada cosa

#### Se importan las clases de los paquetes domain.modelo y domain.servicios
from domain.modelo.baraja import Baraja #Se importa la clase Baraja del paquete domain.modelo
from domain.modelo.Jugador import Jugador #Se importa la clase Jugador del paquete domain.modelo
from domain.servicios.servicios_cartas import ServiciosCartas #Se importa la clase ServiciosCartas del paquete domain.servicios

sabeLasReglas = False

#### Se pide al usuario si conoce las reglas del juego, si no, se le muestran. Si las sabe, se inicia el juego (se repiten las cartas y se muestran los resultados)
while sabeLasReglas == False: #Bucle while para que se repita hasta que el usuario introduzca si o no
    print ("------------------------------------------------")
    respuesta = input("--> IMPORTANTE: ¿Conoces las reglas del juego? (si/no): ")
    if respuesta == "si":
        print ("")
        print ("############## EL JUEGO COMIENZA ###############")
        sabeLasReglas = True
    elif respuesta == "no":
        print ("")
        print ("RECOMIENDO probar con 8 jugadores llamados a,b,c,d,e,f,g,h para que sea más fácil de observar resultados y empates.")
        print ("El juego consiste en que cada jugador recibe una carta y se compara por cada turno con las de los demás jugadores. El jugador que tenga la carta más alta se lleva un punto.") 
        print ("El juego se repite hasta que se acaben las cartas, que dependerá de la cantidad de jugadores elegidos. Sólo se pueden elegir los divisores de 40 = 2,4,5,8,10,20")
        print ("Al finalizar el juego se mostrará el/los ganador/es y los puntos que ha obtenido cada jugador hasta el último turno.")
        print ("")
        print ("############## EL JUEGO COMIENZA ###############")
        sabeLasReglas = True
    else:
        print ("")
        print ("Por favor, introduce si o no")

#### Ejecución de cosas
def main():
    servicios_cartas: ServiciosCartas = ServiciosCartas() #Con una variable se inicia la clase ServiciosCartas para poder usar sus métodos y atributos (baraja) en el main (que es el programa principal)
    baraja: Baraja = servicios_cartas.crear_baraja() #Se crea una variable baraja que es un objeto de la clase Baraja, que se crea con el método crear_baraja de la clase ServiciosCartas (que es la que tiene el atributo baraja)
    servicios_cartas.mezclar_baraja(baraja) #Se llama al método mezclar_baraja de la clase ServiciosCartas, que recibe como parámetro la variable baraja (que es un objeto de la clase Baraja) y mezcla las cartas de la baraja
    
    #### Pedir cuántos jugadores van a haber. Sólo podrán haber los divisores de 40 = 2,4,5,8,10,20 (ya que depende de las cartas que se repartan y por tanto de los jugadores que hayan)
    cantidadJugadores = 0
    while (cantidadJugadores != 2 and cantidadJugadores != 4 and cantidadJugadores != 5 and cantidadJugadores != 8 and cantidadJugadores != 10 and cantidadJugadores != 20):
        cantidadJugadores = int(input("Introduce el número de jugadores: "))


    #### Combat cartas
    listaJugadores: list[Jugador] = [] #Lista vacía de objetos Jugador para guardar los nombres y puntos de los jugadores
    for i in range(0, cantidadJugadores): #Bucle for para crear tantos jugadores como se haya indicado en cantidadJugadores
        nombre = input("Introduce el nombre del jugador " + str(i + 1) + ": ") #Pide el nombre del jugador y se guarda en la variable nombre
        ####puntos no se pone en main porque ya está inicializado en 0

        jugador: Jugador = Jugador(nombre)  #Crea un objeto Jugador con el nombre que se ha introducido en la variable nombre y se guarda en la variable jugador
        listaJugadores.append(jugador) #Añade el objeto Jugador a la lista de objetos Jugador (listaJugadores) que se creó al principio del main
    

    #### Sacar una carta para cada jugador
    contadorTurno=1 #Variable para contar los turnos (para mostrarlo por pantalla) y se inicializa a 1 (porque el primer turno es el 1)
    for i in range (0,40,cantidadJugadores):  #Bucle for para sacar una carta para cada jugador en cada turno (se repite 40 veces, que es la cantidad de cartas que hay en la baraja)
        print ("")
        print ("--> TURNO", contadorTurno)
        contadorTurno+=1 #Se suma 1 al contador de turnos
        cartaMasAlta=0 #Variable para guardar la carta más alta de cada turno
        for j in range (0,cantidadJugadores): #Bucle para sacar carta para cada jugador
            listaJugadores[j].carta = baraja.cartas[i+j] #Se guarda la carta que se saca en la variable carta del objeto Jugador
            print ("(i)", listaJugadores[j].nombre, "obtiene la carta:", listaJugadores[j].carta) #Se muestra por pantalla el nombre del jugador y la carta que ha sacado
            if (listaJugadores[j].carta.valor.value > cartaMasAlta): #Se compara la carta que se ha sacado con la carta más alta del turno
                cartaMasAlta=listaJugadores[j].carta.valor.value #Si la carta que se ha sacado es más alta que la carta más alta del turno, se guarda el valor de la carta que se ha sacado en la variable cartaMasAlta


    #### Un punto al jugador que la tenga más grande
        for j in range (0,cantidadJugadores): #Bucle for para comparar la carta más alta del turno con las cartas que han sacado los jugadores
            if (listaJugadores[j].carta.valor.value == cartaMasAlta): #Se compara la carta más alta del turno con la carta que ha sacado cada jugador
                listaJugadores[j].puntos+=1 #Si la carta que ha sacado el jugador es la carta más alta del turno, se le suma un punto a la variable puntos del objeto Jugador
                print ("(↑) De los  ",cantidadJugadores,"  jugadores:  ",listaJugadores[j].nombre," ha sacado la carta más alta del turno, sumando un total de: ",listaJugadores[j].puntos,"puntos") #Se muestra por pantalla el nombre del jugador que ha sacado la carta más alta del turno y los puntos que tiene
                print ("")


    #### Mostrar los puntos de cada jugador por cada turno y guardar el máximo en una variable
        puntosMaximosJugador=0 #Variable para guardar los puntos máximos de cada turno y se inicializa a 0
        for j in range (0,cantidadJugadores): #Bucle for para mostrar los puntos de cada jugador
            if (listaJugadores[j].puntos > puntosMaximosJugador): #Compara los puntos de cada jugador con los puntos máximos del turno
                puntosMaximosJugador=listaJugadores[j].puntos #Si los puntos de un jugador son más altos que los puntos máximos del turno, se guarda el valor de los puntos de ese jugador en la variable puntosMaximosJugador
            print ("(@) Puntos de ",listaJugadores[j].nombre,": ",listaJugadores[j].puntos) #Se muestra por pantalla el nombre del jugador y los puntos que tiene
            print ("-------------------------------------------------------------------------------------------------------")


    print ("(F) GANADOR/ES:") 
    for i in range (0,cantidadJugadores): #Bucle for para mostrar los jugadores que han sacado la carta más alta del turno
        if (listaJugadores[i].puntos == puntosMaximosJugador): #Compara los puntos de cada jugador con los puntos máximos del turno
            print ("   ",listaJugadores[i].nombre,"con",listaJugadores[i].puntos,"puntos") #Muestra por pantalla el nombre del jugador y los puntos que tiene


    #### Al final preguntar si volver a empezar la partida. Si aprieta Enter, se le pregunta otravez. Si aprieta si, se vuelve a ejecutar el main. Si aprieta no, se acaba el programa
    respuesta = "" 
    while (respuesta != "si" and respuesta != "no"): #Bucle while para que se le pregunte al usuario si quiere jugar otra partida
        respuesta = input("¿Quieres jugar otra partida? (si/no): ")
        if (respuesta == "si"): #Si la respuesta es si, se vuelve a ejecutar el main
            main()
        elif (respuesta == "no"): #Si la respuesta es no, se acaba el programa
            print ("")
            print ("Hasta la próxima!")
        else: #Si la respuesta no es si o no, se pregunta de nuevo
            print ("")
            print ("Por favor, introduce si o no")