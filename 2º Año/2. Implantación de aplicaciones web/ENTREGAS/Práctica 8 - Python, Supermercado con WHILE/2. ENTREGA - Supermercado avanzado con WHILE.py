#Lista de 5 productos
productos = ["Monster", "Galletas", "Helado", "Pizza", "Pan"]

#Lista de precios
precio = [1.50, 1, 1.25, 2.50, 0.50]

#Guardar total de la compra
total = 0

#Pedir nombre del cliente
print("######################################################################################")
print(" ___                                                                         _        ")
print("(  _`\  Bienvenido al                                                       ( )       ") 
print("| (_(_) _   _  _ _      __   _ __   ___ ___     __   _ __    ___    _ _    _| |   _   ") 
print("`\__ \ ( ) ( )( '_`\  /'__`\( '__)/' _ ` _ `\ /'__`\( '__) /'___) /'_` ) /'_` | /'_`\ ") 
print("( )_) || (_) || (_) )(  ___/| |   | ( ) ( ) |(  ___/| |   ( (___ ( (_| |( (_| |( (_) )") 
print("`\____)`\___/'| ,__/'`\____)(_)   (_) (_) (_)`\____)(_)   `\____)`\__,_)`\__,_)`\___/'") 
print("              | |  de Andrei                                                          ") 
print("              (_)                                                                     ") 
print("")
print("")
print("")
nombre = input("--> ¿Cuál es tu nombre? ").lower()
#Pedir día de la semana
dia = input("--> ¿Qué día es hoy? ").lower()
#Pedir al cliente que introduzca los productos que quiere
print("      PRODUCTOS             -DESCUENTOS/+SUBIDAS                DESCUENTOS VIP                    PUFO")
#Mostrar la lista de productos y su precio
print(" __________________      ___________________________      __________________________       _________________")
print("| ",productos[0],":", precio[0],"€ |    |  LUNES: -20% en MONSTER   |    |  -10% adicional en       |     |  +50% en TODO   |")
print("| ",productos[1],":", precio[1],"€  |    |  MARTES: +20% en TODO     |    |  MONSTER, PIZZA, HELADO  |     |  SIN DESCUENTOS |")
print("| ",productos[2],":", precio[2],"€ |    |  MIERCOLES: 2x1 en PIZZA  |")
print("| ",productos[3],":", precio[3],"€   |    |  VIERNES: -70% en TODO    |")
print("| ",productos[4],":", precio[4],"€     |")

#CÁLCULOS SEGÚN EL DÍA----------------------------------------------------------------
if dia == "lunes" or dia == "1": # 20% de descuento en MONSTER
    precio[0] = precio[0] * 0.8
elif dia == "martes" or dia == "2": # 20% subida en TODO
        precio[0] = precio[0] * 1.2
        precio[1] = precio[1] * 1.2
        precio[2] = precio[2] * 1.2
        precio[3] = precio[3] * 1.2
        precio[4] = precio[4] * 1.2
elif dia == "miercoles" or dia == "3": #2x1 en HELADO, hecho en las cantidades más abajo
    precio[2] = precio[2]
elif dia == "jueves" or dia == "4": # Mismos precios en TODO
    precio[0] = precio[0] * 1
    precio[1] = precio[1] * 1
    precio[2] = precio[2] * 1
    precio[3] = precio[3] * 1
    precio[4] = precio[4] * 1
elif dia == "viernes" or dia == "5": #70% descuento en TODO
    precio[0] = precio[0] * 0.3 
    precio[1] = precio[1] * 0.3
    precio[2] = precio[2] * 0.3
    precio[3] = precio[3] * 0.3
    precio[4] = precio[4] * 0.3
elif dia == "sabado" or dia == "6": # Mismos precios en TODO
    precio[0] = precio[0]
    precio[1] = precio[1]
    precio[2] = precio[2]
    precio[3] = precio[3]
    precio[4] = precio[4]
elif dia == "domingo" or dia == "7":
    print("---- El supermercado está cerrado ----")
    exit()
else:
    print("No has introducido un día correcto")
    exit()
#CÁLCULOS DE PRECIOS DE LOS PRODUCTOS SEGÚN EL CLIENTE--------------------------------
if nombre == "carlos" or nombre == "ines": # 10% descuento adiciona en MONSTER, PIZZA, HELADO
    precio[0] = precio[0] * 0.9
    precio[1] = precio[1] * 0.9
    precio[2] = precio[2] * 0.9
elif nombre == "sr.muro": # 50% de subida en TODO
    precio[0] = precio[0] * 1.5
    precio[1] = precio[1] * 1.5
    precio[2] = precio[2] * 1.5
    precio[3] = precio[3] * 1.5
    precio[4] = precio[4] * 1.5
else:
    precio[0] = precio[0]
    precio[1] = precio[1]
    precio[2] = precio[2]
    precio[3] = precio[3]
    precio[4] = precio[4]

#PEDIR AL CLIENTE INTRODUCIR PRODUCTOS Y CANTIDAD QUE QUIERE--------------------------
while True:
    cantidad2x1=0
    print("")
    producto = input("--> ¿Qué producto quieres? ")
    if producto == "monster" or producto == "1":
        cantidad = int(input("--> ¿Cuántos MONSTER quieres? "))
        total = total + (cantidad * precio[0])
    elif producto == "galletas" or producto == "2":
        cantidad = int(input("--> ¿Cuántas GALLETAS quieres? "))
        total = total + (cantidad * precio[1])
    elif producto == "helado" or producto == "3":
        #2x1 en HELADO en pares. Si es 1 cantidad, se le cobra el precio normal. Si es 2 cantidad, se le cobra la mitad. Si tiene más de 2, se le cobra el par con el 2x1 y uno a precio normal.
        cantidad = int(input("--> ¿Cuántos HELADOS quieres? "))
        cantidad2x1 = cantidad # Guardar cantidad de helados por si quiere seguir comprando que no se pierda el número
        if cantidad2x1+cantidad == 1:
            total = total + (cantidad * precio[2])
        elif cantidad2x1+cantidad == 2 or cantidad2x1+cantidad == 4 or cantidad2x1+cantidad == 6 or cantidad2x1+cantidad == 8 or cantidad2x1+cantidad == 10 or cantidad2x1+cantidad == 12 or cantidad2x1+cantidad == 14 or cantidad2x1+cantidad == 16 or cantidad2x1+cantidad == 18 or cantidad2x1+cantidad == 20 or cantidad2x1+cantidad == 22 or cantidad2x1+cantidad == 24 or cantidad2x1+cantidad == 26 or cantidad2x1+cantidad == 28 or cantidad2x1+cantidad == 30 or cantidad2x1+cantidad == 32 or cantidad2x1+cantidad == 34 or cantidad2x1+cantidad == 36 or cantidad2x1+cantidad == 38 or cantidad2x1+cantidad == 40 or cantidad2x1+cantidad == 42 or cantidad2x1+cantidad == 44 or cantidad2x1+cantidad == 46 or cantidad2x1+cantidad == 48 or cantidad2x1+cantidad == 50 or cantidad2x1+cantidad == 52 or cantidad2x1+cantidad == 54 or cantidad2x1+cantidad == 56 or cantidad2x1+cantidad == 58 or cantidad2x1+cantidad == 60 or cantidad2x1+cantidad == 62 or cantidad2x1+cantidad == 64 or cantidad2x1+cantidad == 66 or cantidad2x1+cantidad == 68 or cantidad2x1+cantidad == 70 or cantidad2x1+cantidad == 72 or cantidad2x1+cantidad == 74 or cantidad2x1+cantidad == 76 or cantidad2x1+cantidad == 78 or cantidad2x1+cantidad == 80 or cantidad2x1+cantidad == 82 or cantidad2x1+cantidad == 84 or cantidad2x1+cantidad == 86 or cantidad2x1+cantidad == 88 or cantidad2x1+cantidad == 90 or cantidad2x1+cantidad == 92 or cantidad2x1+cantidad == 94 or cantidad2x1+cantidad == 96 or cantidad2x1+cantidad == 98 or cantidad2x1+cantidad == 100:
            total = total + (cantidad * precio[2])/2
        elif cantidad2x1+cantidad == 3 or cantidad2x1+cantidad == 5 or cantidad2x1+cantidad == 7 or cantidad2x1+cantidad == 9 or cantidad2x1+cantidad == 11 or cantidad2x1+cantidad == 13 or cantidad2x1+cantidad == 15 or cantidad2x1+cantidad == 17 or cantidad2x1+cantidad == 19 or cantidad2x1+cantidad == 21 or cantidad2x1+cantidad == 23 or cantidad2x1+cantidad == 25 or cantidad2x1+cantidad == 27 or cantidad2x1+cantidad == 29 or cantidad2x1+cantidad == 31 or cantidad2x1+cantidad == 33 or cantidad2x1+cantidad == 35 or cantidad2x1+cantidad == 37 or cantidad2x1+cantidad == 39 or cantidad2x1+cantidad == 41 or cantidad2x1+cantidad == 43 or cantidad2x1+cantidad == 45 or cantidad2x1+cantidad == 47 or cantidad2x1+cantidad == 49 or cantidad2x1+cantidad == 51 or cantidad2x1+cantidad == 53 or cantidad2x1+cantidad == 55 or cantidad2x1+cantidad == 57 or cantidad2x1+cantidad == 59 or cantidad2x1+cantidad == 61 or cantidad2x1+cantidad == 63 or cantidad2x1+cantidad == 65 or cantidad2x1+cantidad == 67 or cantidad2x1+cantidad == 69 or cantidad2x1+cantidad == 71 or cantidad2x1+cantidad == 73 or cantidad2x1+cantidad == 75 or cantidad2x1+cantidad == 77 or cantidad2x1+cantidad == 79 or cantidad2x1+cantidad == 81 or cantidad2x1+cantidad == 83 or cantidad2x1+cantidad == 85 or cantidad2x1+cantidad == 87 or cantidad2x1+cantidad == 89 or cantidad2x1+cantidad == 91 or cantidad2x1+cantidad == 93 or cantidad2x1+cantidad == 95 or cantidad2x1+cantidad == 97 or cantidad2x1+cantidad == 99:
            total = total + ((cantidad - 1)/2 * precio[2])
    elif producto == "pizza" or producto == "4":
        cantidad = int(input("--> ¿Cuántas PIZZAS quieres? "))
        total = total + (cantidad * precio[3])
    elif producto == "pan" or producto == "5":
        cantidad = int(input("--> ¿Cuántos PANES quieres?"))
        total = total + (cantidad * precio[4])
    else:
        print("No tenemos ese producto")
    seguirComprando = input("--> ¿Quieres seguir comprando? ").lower()
    cantidad2x1 = cantidad
    if seguirComprando == "no":
        break
print("- - - - - - - - - - - - - - - - - - - -")
print("El total de la compra es", total, "€")
