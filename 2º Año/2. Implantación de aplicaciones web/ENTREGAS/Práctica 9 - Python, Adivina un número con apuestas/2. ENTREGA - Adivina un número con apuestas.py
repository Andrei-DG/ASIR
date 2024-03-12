#Un usuario al entrar dice el dinero que tiene.
#Apuesta una cantidad de ese dinero en cada partida y tiene diez oportunidades para adivinar un numero aleatorio, 
#No puede apostar mas del dinero que le queda
#Con mensaje diciendo si es mayor o no
#Si lo advina gana lo apostado si falla pierde lo apostado
#Con la posiblidad de volver a jugar otra vez si le queda dinero
import random
print("")
print("")
print("")
print("")
print("")
print("")
print("")
dinero = int(input("--> ¿Cuánto dinero tienes? "))
while True:
    print("Tienes", dinero, "euros")
    repeat = apuesta = int(input("--> ¿Cuánto dinero quieres apostar? "))
    if apuesta > dinero:
        print("No puedes apostar más dinero del que tienes")
        continue
    elif apuesta == dinero:
        print("Has apostado todo tu dinero")
    elif apuesta < dinero:
        print("Has apostado", apuesta, "euros")
    numero = random.randint(1, 10)
    print("El número a adivinar es un número entre 1 y 10")
    for i in range(10):
        print("INTENTO", i+1)
        intento = int(input("--> ¿Cuál es el número? "))
        if intento == numero:
            print("Has acertado")
            dinero = dinero + apuesta
            print("Ahora tienes", dinero, "euros")
            break
        elif intento > numero:
            print("El número es menor")
        elif intento < numero:
            print("El número es mayor")
    else:
        print("Has perdido")
        dinero = dinero - apuesta
        print("Ahora tienes", dinero, "euros")
    if dinero == 0:
        print("No te queda dinero")
        break
    elif dinero > 0:
        print("--> ¿Quieres volver a jugar?")
        respuesta = input("SI o NO? ").lower()
        if respuesta == "si":
            print("")
        elif respuesta == "no":
            print("Has terminado el juego")
            break
        else:
            print("No has introducido una respuesta correcta")
            break


