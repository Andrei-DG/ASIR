#Nombres de Productos y su Precio:
precioPan=0.50
precioLeche=1.00
precioPollo=7.00
precioAtun=2.25
precioMonster=1.50

#Precio calculado de los productos con su/s descuentos determinados:
precioCalculadoProducto1=0
precioCalculadoProducto2=0

#Cantidades del primer producto:
cantidadProducto1=0
#Cantidades del segundo producto:
cantidadProducto2=0

#Descuentos en % de productos:
descuentoPan=0
descuentoLeche=0
descuentoPollo=0
descuentoAtun=0
descuentoMonster=0
descuento2x1=50
cantidadpar=0

#Los 2 Productos que puede comprar el cliente:
productoElegido1=0
productoElegido2=0

#Descuento del VIP para todos los productos y todos los días:
descuentoPanVIP=10
descuentoLecheVIP=10
descuentoPolloVIP=10
descuentoAtunVIP=0
descuentoMonsterVIP=0

#Subida de precio para Pufo todos los productos y todos los días:
subidaPufo=50

#Día de los Border Lines los Martes:
subidaBorderLine=20

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
#Pide al cliente indicar el día en el que hace la compra y transformar en mayúsculas:
diaDeLaSemana= input("Indique el día de la semana en el que hace la compra: ").upper()

#Pide al cliente indicar su nombre:
nombreCliente=input("Indique su nombre: ").lower()

#Según el día de la semana en el que se hace la compra:
##########################################################################################################
##########################################################################################################
############################################## L U N E S #################################################
##########################################################################################################
##########################################################################################################

if diaDeLaSemana=="LUNES":
    print("")
    print("¡BIENVENID@", nombreCliente.upper(), "! Hoy es", diaDeLaSemana, "y tenemos para tí las siguientes noticias sobre nuestros productos:")
    print("")
    descuentoPan=20
    descuentoLeche=0
    descuentoPollo=0
    descuentoAtun=0
    descuentoMonster=0
    if nombreCliente=="carlos" or nombreCliente=="ines":
        sumaDescuentosPanVIP=descuentoPan+descuentoPanVIP
        precioFinalPanVIP=precioPan-(precioPan*sumaDescuentosPanVIP/100)
        if descuentoPan > 0 or descuentoPanVIP > 0:
            print("Hay un descuento en Pan del", descuentoPan, "% por ser cliente NORMAL y del", descuentoPanVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPanVIP ,"% de descuento.")
            print("1-Pan:     ", precioFinalPanVIP, "€/Unidad")
        else:
            print("1-Pan:     ", precioPan, "€/Unidad")
        sumaDescuentosLecheVIP=descuentoLeche+descuentoLecheVIP
        precioFinalLecheVIP=precioLeche-(precioLeche*sumaDescuentosLecheVIP/100)
        if descuentoLeche > 0 or descuentoLecheVIP > 0:
            print("Hay un descuento en Leche del", descuentoLeche, "% por ser cliente NORMAL y del", descuentoLecheVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosLecheVIP ,"% de descuento.")
            print("2-Leche:   ", precioFinalLecheVIP, "€/Unidad")
        else:
            print("2-Leche:   ", precioLeche, "€/Unidad")
        sumaDescuentosPolloVIP=descuentoPollo+descuentoPolloVIP
        precioFinalPolloVIP=precioPollo-(precioPollo*sumaDescuentosPolloVIP/100)
        if descuentoPollo > 0 or descuentoPolloVIP > 0:
            print("Hay un descuento en Pollo del", descuentoPollo, "% por ser cliente NORMAL y del", descuentoPolloVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPolloVIP ,"% de descuento.")
            print("3-Pollo:   ", precioFinalPolloVIP, "€/Unidad")
        else:
            print("3-Pollo:    ", precioPollo, "€/Unidad")
        sumaDescuentosAtunVIP=descuentoAtun+descuentoAtunVIP
        precioFinalAtunVIP=precioAtun-(precioAtun*sumaDescuentosAtunVIP/100)
        if descuentoAtun > 0 or descuentoAtunVIP > 0:
            print("Hay un descuento en Atun del", descuentoAtun, "% por ser cliente NORMAL y del", descuentoAtunVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosAtunVIP ,"% de descuento.")
            print("4-Atun: ", precioFinalAtunVIP, "€/Unidad")
        else:
            print("4-Atun:    ", precioAtun, "€/Unidad")
        sumaDescuentosMonsterVIP=descuentoMonster+descuentoMonsterVIP
        precioFinalMonsterVIP=precioMonster-(precioMonster*sumaDescuentosMonsterVIP/100)
        if descuentoMonster > 0 or descuentoMonsterVIP > 0:
            print("Hay un descuento en Monster del", descuentoMonster, "% por ser cliente NORMAL y del", descuentoMonsterVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosMonsterVIP ,"% de descuento.")
            print("5-Monster: ", precioFinalMonsterVIP, "€/Unidad")
        else:
            print("5-Monster: ", precioMonster, "€/Unidad")

        #Pide al cliente VIP indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0

        #Pide al cliente VIP indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente VIP:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")





    elif nombreCliente=="srmuro":
        subidaPufo=0.50
        print("Todos los productos se han encarecido un", subidaPufo, "% más por ser usted un Cliente PUFO.")
        print("El precio de los productos es el siguiente:")
        precioFinalPanPUFO=precioPan+subidaPufo
        print("Pan: ", precioFinalPanPUFO, "€")
        precioFinalLechePUFO=precioLeche+subidaPufo
        print("Leche: ", precioFinalLechePUFO, "€")
        precioFinalPolloPUFO=precioPollo+subidaPufo
        print("Pollo: ", precioFinalPolloPUFO, "€")
        precioFinalAtunPUFO=precioAtun+subidaPufo
        print("Atun: ", precioFinalAtunPUFO, "€")
        precioFinalMonsterPUFO=precioMonster+subidaPufo
        print("Monster: ", precioFinalMonsterPUFO, "€")
        #Pide al cliente PUFO indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLechePUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente PUFO indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        print("")
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLechePUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente PUFO:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")




    #Si el cliente no es carlos, ines y tampoco srmuro:
    elif nombreCliente!="carlos" and nombreCliente!="ines" and nombreCliente!="srmuro":
        precioFinalPanNORMAL=precioPan-(precioPan*descuentoPan/100)
        if descuentoPan > 0:
            print("Hay un descuento del", descuentoPan, "% en pan.")
            print("1-PAN:     ", precioFinalPanNORMAL, "€/Unidad")
        else:
            print("1-PAN:     ", precioPan, "€/Unidad")
        precioFinalLecheNORMAL=precioLeche-(precioLeche*descuentoLeche/100)
        if descuentoLeche > 0:
            print("Hay un descuento del", descuentoLeche, "% en leche.")
            print("2-LECHE:   ", precioFinalLecheNORMAL, "€/Unidad")
        else:
            print("2-LECHE:   ", precioLeche, "€/Unidad")
        precioFinalPolloNORMAL=precioPollo-(precioPollo*descuentoPollo/100)
        if descuentoPollo > 0:
            print("Hay un descuento del", descuentoPollo, "% en pollo.")
            print("3-POLLO:   ", precioFinalPolloNORMAL, "€/Unidad")
        else:
            print("3-POLLO:   ", precioPollo, "€/Unidad")
        precioFinalAtunNORMAL=precioAtun-(precioAtun*descuentoAtun/100)
        if descuentoAtun > 0:
            print("Hay un descuento del", descuentoAtun, "% en atun.")
            print("4-ATUN:    ", precioFinalAtunNORMAL, "€/Unidad")
        else:
            print("4-ATUN:    ", precioAtun, "€/Unidad")
        precioFinalMonsterNORMAL=precioMonster-(precioMonster*descuentoMonster/100)
        if descuentoMonster > 0:
            print("Hay un descuento del", descuentoMonster, "% en monster.")
            print("5-MONSTER: ", precioFinalMonsterNORMAL, "€/Unidad")
        else:
            print("5-MONSTER: ", precioMonster, "€/Unidad")
        print("")
        #Pide al cliente NORMAL indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL: 
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente NORMAL indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma los dos productos elegidos por el cliente NORMAL:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")

##########################################################################################################
##########################################################################################################
#############################################   M A R T E S ##############################################
##########################################################################################################
##########################################################################################################

elif diaDeLaSemana=="MARTES":
    print("")
    print("¡BIENVENID@", nombreCliente.upper(), "! Hoy es", diaDeLaSemana, "y tenemos para tí las siguientes noticias sobre nuestros productos:")
    print("")
    descuentoPan=0
    descuentoLeche=0
    descuentoPollo=0
    descuentoAtun=0
    descuentoMonster=0
    if nombreCliente=="carlos" or nombreCliente=="ines":
        sumaDescuentosPanVIP=descuentoPan+descuentoPanVIP-subidaBorderLine
        precioFinalPanVIP=precioPan-(precioPan*sumaDescuentosPanVIP/100)
        if descuentoPan > 0 or descuentoPanVIP > 0:
            print("Hay un descuento en Pan del", descuentoPan, "% por ser cliente NORMAL y del", descuentoPanVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPanVIP ,"% de descuento.")
            print("1-Pan:     ", precioFinalPanVIP, "€/Unidad")
        else:
            print("1-Pan:     ", precioPan, "€/Unidad")
        sumaDescuentosLecheVIP=descuentoLeche+descuentoLecheVIP
        precioFinalLecheVIP=precioLeche-(precioLeche*sumaDescuentosLecheVIP/100)
        if descuentoLeche > 0 or descuentoLecheVIP > 0:
            print("Hay un descuento en Leche del", descuentoLeche, "% por ser cliente NORMAL y del", descuentoLecheVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosLecheVIP ,"% de descuento.")
            print("2-Leche:   ", precioFinalLecheVIP, "€/Unidad")
        else:
            print("2-Leche:   ", precioLeche, "€/Unidad")
        sumaDescuentosPolloVIP=descuentoPollo+descuentoPolloVIP
        precioFinalPolloVIP=precioPollo-(precioPollo*sumaDescuentosPolloVIP/100)
        if descuentoPollo > 0 or descuentoPolloVIP > 0:
            print("Hay un descuento en Pollo del", descuentoPollo, "% por ser cliente NORMAL y del", descuentoPolloVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPolloVIP ,"% de descuento.")
            print("3-Pollo:   ", precioFinalPolloVIP, "€/Unidad")
        else:
            print("3-Pollo:    ", precioPollo, "€/Unidad")
        sumaDescuentosAtunVIP=descuentoAtun+descuentoAtunVIP
        precioFinalAtunVIP=precioAtun-(precioAtun*sumaDescuentosAtunVIP/100)
        if descuentoAtun > 0 or descuentoAtunVIP > 0:
            print("Hay un descuento en Atun del", descuentoAtun, "% por ser cliente NORMAL y del", descuentoAtunVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosAtunVIP ,"% de descuento.")
            print("4-Atun: ", precioFinalAtunVIP, "€/Unidad")
        else:
            print("4-Atun:    ", precioAtun, "€/Unidad")
        sumaDescuentosMonsterVIP=descuentoMonster+descuentoMonsterVIP
        precioFinalMonsterVIP=precioMonster-(precioMonster*sumaDescuentosMonsterVIP/100)
        if descuentoMonster > 0 or descuentoMonsterVIP > 0:
            print("Hay un descuento en Monster del", descuentoMonster, "% por ser cliente NORMAL y del", descuentoMonsterVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosMonsterVIP ,"% de descuento.")
            print("5-Monster: ", precioFinalMonsterVIP, "€/Unidad")
        else:
            print("5-Monster: ", precioMonster, "€/Unidad")

        #Pide al cliente VIP indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0

        #Pide al cliente VIP indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
            cantidadProducto2=0
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente VIP:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")





    elif nombreCliente=="srmuro":
        subidaPufo=(subidaPufo/100)
        print("Todos los productos se han encarecido un", subidaPufo, "% más por ser usted un Cliente PUFO.")
        print("El precio de los productos es el siguiente:")
        precioFinalPanPUFO=precioPan+subidaPufo-subidaBorderLine
        print("Pan: ", precioFinalPanPUFO, "€")
        precioFinalLechePUFO=precioLeche+subidaPufo
        print("Leche: ", precioFinalLechePUFO, "€")
        precioFinalPolloPUFO=precioPollo+subidaPufo
        print("Pollo: ", precioFinalPolloPUFO, "€")
        precioFinalAtunPUFO=precioAtun+subidaPufo
        print("Atun: ", precioFinalAtunPUFO, "€")
        precioFinalMonsterPUFO=precioMonster+subidaPufo
        print("Monster: ", precioFinalMonsterPUFO, "€")
        #Pide al cliente PUFO indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLechePUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente PUFO indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        print("")
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLechePUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente PUFO:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")




    #Si el cliente no es carlos, ines y tampoco srmuro:
    elif nombreCliente!="carlos" and nombreCliente!="ines" and nombreCliente!="srmuro":
        precioFinalPanNORMAL=precioPan-(precioPan*(descuentoPan-subidaBorderLine)/100)
        if descuentoPan > 0:
            print("Hay un descuento del", descuentoPan, "% en pan.")
            print("1-PAN:     ", precioFinalPanNORMAL, "€/Unidad")
        else:
            print("1-PAN:     ", precioPan, "€/Unidad")
        precioFinalLecheNORMAL=precioLeche-(precioLeche*descuentoLeche/100)
        if descuentoLeche > 0:
            print("Hay un descuento del", descuentoLeche, "% en leche.")
            print("2-LECHE:   ", precioFinalLecheNORMAL, "€/Unidad")
        else:
            print("2-LECHE:   ", precioLeche, "€/Unidad")
        precioFinalPolloNORMAL=precioPollo-(precioPollo*descuentoPollo/100)
        if descuentoPollo > 0:
            print("Hay un descuento del", descuentoPollo, "% en pollo.")
            print("3-POLLO:   ", precioFinalPolloNORMAL, "€/Unidad")
        else:
            print("3-POLLO:   ", precioPollo, "€/Unidad")
        precioFinalAtunNORMAL=precioAtun-(precioAtun*descuentoAtun/100)
        if descuentoAtun > 0:
            print("Hay un descuento del", descuentoAtun, "% en atun.")
            print("4-ATUN:    ", precioFinalAtunNORMAL, "€/Unidad")
        else:
            print("4-ATUN:    ", precioAtun, "€/Unidad")
        precioFinalMonsterNORMAL=precioMonster-(precioMonster*descuentoMonster/100)
        if descuentoMonster > 0:
            print("Hay un descuento del", descuentoMonster, "% en monster.")
            print("5-MONSTER: ", precioFinalMonsterNORMAL, "€/Unidad")
        else:
            print("5-MONSTER: ", precioMonster, "€/Unidad")
        print("")
        #Pide al cliente NORMAL indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL: 
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente NORMAL indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma los dos productos elegidos por el cliente NORMAL:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")

##########################################################################################################
##########################################################################################################
########################################### M I É R C O L E S ############################################
##########################################################################################################
##########################################################################################################

elif diaDeLaSemana=="MIERCOLES" or diaDeLaSemana=="MIÉRCOLES":
    print("")
    print("¡BIENVENID@", nombreCliente.upper(), "! Hoy es", diaDeLaSemana, "y tenemos para tí nuevos tipos de ofertas, aquí las siguientes noticias sobre nuestros productos:")
    print("")
    descuentoPan=0
    descuentoLeche=0
    descuentoPollo=0
    descuentoAtun=0
    descuentoMonster=0
    descuento2x1=50
    cantidadpar=0
    if nombreCliente=="carlos" or nombreCliente=="ines":
        sumaDescuentosPanVIP=descuentoPan+descuentoPanVIP
        precioFinalPanVIP=precioPan-(precioPan*sumaDescuentosPanVIP/100)
        if descuentoPan > 0 or descuentoPanVIP > 0:
            print("Hay un descuento en Pan del", descuentoPan, "% por ser cliente NORMAL y del", descuentoPanVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPanVIP ,"% de descuento.")
            print("1-Pan:     ", precioFinalPanVIP, "€/Unidad")
        else:
            print("1-Pan:     ", precioPan, "€/Unidad")
        sumaDescuentosLecheVIP=descuentoLeche+descuentoLecheVIP
        precioFinalLecheVIP=precioLeche-(precioLeche*sumaDescuentosLecheVIP/100)
        if descuentoLeche > 0 or descuentoLecheVIP > 0:
            print("Hay un descuento en Leche del", descuentoLeche, "% por ser cliente NORMAL y del", descuentoLecheVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosLecheVIP ,"% de descuento.")
            print("2-Leche:   ", precioFinalLecheVIP, "€/Unidad")
        else:
            print("2-Leche:   ", precioLeche, "€/Unidad")
        sumaDescuentosPolloVIP=descuentoPollo+descuentoPolloVIP
        precioFinalPolloVIP=precioPollo-(precioPollo*sumaDescuentosPolloVIP/100)
        if descuentoPollo > 0 or descuentoPolloVIP > 0:
            print("Hay un descuento en Pollo del", descuentoPollo, "% por ser cliente NORMAL y del", descuentoPolloVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPolloVIP ,"% de descuento.")
            print("3-Pollo:   ", precioFinalPolloVIP, "€/Unidad")
            if descuento2x1==50:
                 print("Aparte, se le suma también un descuento en Pollo del", descuento2x1, "% por la promoción 2x1:")
                 print("3-Pollo:   ", precioFinalPolloVIP*(descuento2x1/100), "€/Unidad por cada 2 unidades")
        else:
            print("3-Pollo:    ", precioPollo, "€/Unidad")
        sumaDescuentosAtunVIP=descuentoAtun+descuentoAtunVIP
        precioFinalAtunVIP=precioAtun-(precioAtun*sumaDescuentosAtunVIP/100)
        if descuentoAtun > 0 or descuentoAtunVIP > 0:
            print("Hay un descuento en Atun del", descuentoAtun, "% por ser cliente NORMAL y del", descuentoAtunVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosAtunVIP ,"% de descuento.")
            print("4-Atun: ", precioFinalAtunVIP, "€/Unidad")
        else:
            print("4-Atun:    ", precioAtun, "€/Unidad")
        sumaDescuentosMonsterVIP=descuentoMonster+descuentoMonsterVIP
        precioFinalMonsterVIP=precioMonster-(precioMonster*sumaDescuentosMonsterVIP/100)
        if descuentoMonster > 0 or descuentoMonsterVIP > 0:
            print("Hay un descuento en Monster del", descuentoMonster, "% por ser cliente NORMAL y del", descuentoMonsterVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosMonsterVIP ,"% de descuento.")
            print("5-Monster: ", precioFinalMonsterVIP, "€/Unidad")
        else:
            print("5-Monster: ", precioMonster, "€/Unidad")

        #Pide al cliente VIP indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloVIP*cantidadProducto1
            if cantidadProducto1==2 or cantidadProducto1==4 or cantidadProducto1==6 or cantidadProducto1==8 or cantidadProducto1==10 or cantidadProducto1==12 or cantidadProducto1==14 or cantidadProducto1==16 or cantidadProducto1==18 or cantidadProducto1==20 or cantidadProducto1==22 or cantidadProducto1==24 or cantidadProducto1==26 or cantidadProducto1==28 or cantidadProducto1==30 or cantidadProducto1==32 or cantidadProducto1==34 or cantidadProducto1==36 or cantidadProducto1==38 or cantidadProducto1==40 or cantidadProducto1==42 or cantidadProducto1==44 or cantidadProducto1==46 or cantidadProducto1==48 or cantidadProducto1==50:
               precioCalculadoProducto1=precioFinalPolloVIP*cantidadProducto1*(descuento2x1/100)
               print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€, con el descuento del 2x1 aplicado")
            if cantidadProducto1==1 or cantidadProducto1==3 or cantidadProducto1==5 or cantidadProducto1==7 or cantidadProducto1==9 or cantidadProducto1==11 or cantidadProducto1==13 or cantidadProducto1==15 or cantidadProducto1==17 or cantidadProducto1==19 or cantidadProducto1==21 or cantidadProducto1==23 or cantidadProducto1==25 or cantidadProducto1==27 or cantidadProducto1==29 or cantidadProducto1==31 or cantidadProducto1==33 or cantidadProducto1==35 or cantidadProducto1==37 or cantidadProducto1==39 or cantidadProducto1==41 or cantidadProducto1==43 or cantidadProducto1==45 or cantidadProducto1==47 or cantidadProducto1==49:
                cantidadpar=cantidadProducto1-(cantidadProducto1-1)
                precioCalculadoProducto1=precioFinalPolloVIP*cantidadProducto1*(descuento2x1/100)+(precioFinalPolloVIP-cantidadpar)
                print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€, con el descuento del 2x1 aplicado en los pares")
            else:
               print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
            descuento2x1=0

        #Pide al cliente VIP indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido1==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloVIP*cantidadProducto2
            if cantidadProducto2==2 or cantidadProducto2==4 or cantidadProducto2==6 or cantidadProducto2==8 or cantidadProducto2==10 or cantidadProducto2==12 or cantidadProducto2==14 or cantidadProducto2==16 or cantidadProducto2==18 or cantidadProducto2==20 or cantidadProducto2==22 or cantidadProducto2==24 or cantidadProducto2==26 or cantidadProducto2==28 or cantidadProducto2==30 or cantidadProducto2==32 or cantidadProducto2==34 or cantidadProducto2==36 or cantidadProducto2==38 or cantidadProducto2==40 or cantidadProducto2==42 or cantidadProducto2==44 or cantidadProducto2==46 or cantidadProducto2==48 or cantidadProducto2==50:
               precioCalculadoProducto2=precioFinalPolloVIP*cantidadProducto2*(descuento2x1/100)
               print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€, con el descuento del 2x1 aplicado")
            if cantidadProducto2==1 or cantidadProducto2==3 or cantidadProducto2==5 or cantidadProducto2==7 or cantidadProducto2==9 or cantidadProducto2==11 or cantidadProducto2==13 or cantidadProducto2==15 or cantidadProducto2==17 or cantidadProducto2==19 or cantidadProducto2==21 or cantidadProducto2==23 or cantidadProducto2==25 or cantidadProducto2==27 or cantidadProducto2==29 or cantidadProducto2==31 or cantidadProducto2==33 or cantidadProducto2==35 or cantidadProducto2==37 or cantidadProducto2==39 or cantidadProducto2==41 or cantidadProducto2==43 or cantidadProducto2==45 or cantidadProducto2==47 or cantidadProducto2==49:
                cantidadpar=cantidadProducto2-(cantidadProducto2-1)
                precioCalculadoProducto2=precioFinalPolloVIP*cantidadProducto2*(descuento2x1/100)+(precioFinalPolloVIP-cantidadpar)
                print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€, con el descuento del 2x1 aplicado en los pares")
            else:
               print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
            cantidadProducto2=0
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente VIP:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")





    elif nombreCliente=="srmuro":
        subidaPufo=(subidaPufo/100)
        print("Todos los productos se han encarecido un", subidaPufo, "% más por ser usted un Cliente PUFO.")
        print("El precio de los productos es el siguiente:")
        precioFinalPanPUFO=precioPan+subidaPufo
        print("Pan: ", precioFinalPanPUFO, "€")
        precioFinalLechePUFO=precioLeche+subidaPufo
        print("Leche: ", precioFinalLechePUFO, "€")
        precioFinalPolloPUFO=precioPollo+subidaPufo
        print("Pollo: ", precioFinalPolloPUFO, "€")
        precioFinalAtunPUFO=precioAtun+subidaPufo
        print("Atun: ", precioFinalAtunPUFO, "€")
        precioFinalMonsterPUFO=precioMonster+subidaPufo
        print("Monster: ", precioFinalMonsterPUFO, "€")
        #Pide al cliente PUFO indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLechePUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente PUFO indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        print("")
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLechePUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente PUFO:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")




    #Si el cliente no es carlos, ines y tampoco srmuro:
    elif nombreCliente!="carlos" and nombreCliente!="ines" and nombreCliente!="srmuro":
        precioFinalPanNORMAL=precioPan-(precioPan*descuentoPan/100)
        if descuentoPan > 0:
            print("Hay un descuento del", descuentoPan, "% en pan.")
            print("1-PAN:     ", precioFinalPanNORMAL, "€/Unidad")
        else:
            print("1-PAN:     ", precioPan, "€/Unidad")
        precioFinalLecheNORMAL=precioLeche-(precioLeche*descuentoLeche/100)
        if descuentoLeche > 0:
            print("Hay un descuento del", descuentoLeche, "% en leche.")
            print("2-LECHE:   ", precioFinalLecheNORMAL, "€/Unidad")
        else:
            print("2-LECHE:   ", precioLeche, "€/Unidad")
        precioFinalPolloNORMAL=precioPollo-(precioPollo*descuentoPollo/100)
        if descuentoPollo > 0:
            print("Hay un descuento del", descuentoPollo, "% en pollo.")
            print("3-POLLO:   ", precioFinalPolloNORMAL, "€/Unidad")
        else:
            print("3-POLLO:   ", precioPollo, "€/Unidad")
        precioFinalAtunNORMAL=precioAtun-(precioAtun*descuentoAtun/100)
        if descuentoAtun > 0:
            print("Hay un descuento del", descuentoAtun, "% en atun.")
            print("4-ATUN:    ", precioFinalAtunNORMAL, "€/Unidad")
        else:
            print("4-ATUN:    ", precioAtun, "€/Unidad")
        precioFinalMonsterNORMAL=precioMonster-(precioMonster*descuentoMonster/100)
        if descuentoMonster > 0:
            print("Hay un descuento del", descuentoMonster, "% en monster.")
            print("5-MONSTER: ", precioFinalMonsterNORMAL, "€/Unidad")
        else:
            print("5-MONSTER: ", precioMonster, "€/Unidad")
        print("")
        #Pide al cliente NORMAL indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL: 
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloNORMAL*cantidadProducto1
            if cantidadProducto1==2 or cantidadProducto1==4 or cantidadProducto1==6 or cantidadProducto1==8 or cantidadProducto1==10 or cantidadProducto1==12 or cantidadProducto1==14 or cantidadProducto1==16 or cantidadProducto1==18 or cantidadProducto1==20 or cantidadProducto1==22 or cantidadProducto1==24 or cantidadProducto1==26 or cantidadProducto1==28 or cantidadProducto1==30 or cantidadProducto1==32 or cantidadProducto1==34 or cantidadProducto1==36 or cantidadProducto1==38 or cantidadProducto1==40 or cantidadProducto1==42 or cantidadProducto1==44 or cantidadProducto1==46 or cantidadProducto1==48 or cantidadProducto1==50:
                precioCalculadoProducto1=precioFinalPolloNORMAL*cantidadProducto1*(descuento2x1/100)
                print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€, con el descuento del 2x1 aplicado.")
            if cantidadProducto1==1 or cantidadProducto1==3 or cantidadProducto1==5 or cantidadProducto1==7 or cantidadProducto1==9 or cantidadProducto1==11 or cantidadProducto1==13 or cantidadProducto1==15 or cantidadProducto1==17 or cantidadProducto1==19 or cantidadProducto1==21 or cantidadProducto1==23 or cantidadProducto1==25 or cantidadProducto1==27 or cantidadProducto1==29 or cantidadProducto1==31 or cantidadProducto1==33 or cantidadProducto1==35 or cantidadProducto1==37 or cantidadProducto1==39 or cantidadProducto1==41 or cantidadProducto1==43 or cantidadProducto1==45 or cantidadProducto1==47 or cantidadProducto1==49:
                cantidadpar=cantidadProducto1-(cantidadProducto1-1)
                precioCalculadoProducto1=precioFinalPolloNORMAL*cantidadProducto1*(descuento2x1/100)+(precioFinalPolloNORMAL-cantidadpar)
                print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€, con el descuento del 2x1 aplicado en los pares")
            else:
                print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente NORMAL indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloNORMAL*cantidadProducto2
            if cantidadProducto2==2 or cantidadProducto2==4 or cantidadProducto2==6 or cantidadProducto2==8 or cantidadProducto2==10 or cantidadProducto2==12 or cantidadProducto2==14 or cantidadProducto2==16 or cantidadProducto2==18 or cantidadProducto2==20 or cantidadProducto2==22 or cantidadProducto2==24 or cantidadProducto2==26 or cantidadProducto2==28 or cantidadProducto2==30 or cantidadProducto2==32 or cantidadProducto2==34 or cantidadProducto2==36 or cantidadProducto2==38 or cantidadProducto2==40 or cantidadProducto2==42 or cantidadProducto2==44 or cantidadProducto2==46 or cantidadProducto2==48 or cantidadProducto2==50:
               precioCalculadoProducto2=precioFinalPolloNORMAL*cantidadProducto2*(descuento2x1/100)
               print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€, con el descuento del 2x1 aplicado")
            if cantidadProducto2==1 or cantidadProducto2==3 or cantidadProducto2==5 or cantidadProducto2==7 or cantidadProducto2==9 or cantidadProducto2==11 or cantidadProducto2==13 or cantidadProducto2==15 or cantidadProducto2==17 or cantidadProducto2==19 or cantidadProducto2==21 or cantidadProducto2==23 or cantidadProducto2==25 or cantidadProducto2==27 or cantidadProducto2==29 or cantidadProducto2==31 or cantidadProducto2==33 or cantidadProducto2==35 or cantidadProducto2==37 or cantidadProducto2==39 or cantidadProducto2==41 or cantidadProducto2==43 or cantidadProducto2==45 or cantidadProducto2==47 or cantidadProducto2==49:
                cantidadpar=cantidadProducto2-(cantidadProducto2-1)
                precioCalculadoProducto2=precioFinalPolloNORMAL*cantidadProducto2*(descuento2x1/100)+(precioFinalPolloNORMAL-cantidadpar)
                print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€, con el descuento del 2x1 aplicado en los pares")
            else:
               print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma los dos productos elegidos por el cliente NORMAL:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")

##########################################################################################################
##########################################################################################################
############################################## J U E V E S ###############################################
##########################################################################################################
##########################################################################################################

if diaDeLaSemana=="JUEVES":
    print("")
    print("¡BIENVENID@", nombreCliente.upper(), "! Hoy es", diaDeLaSemana, "y tenemos para tí las siguientes noticias sobre nuestros productos:")
    print("")
    descuentoPan=0
    descuentoLeche=0
    descuentoPollo=0
    descuentoAtun=0
    descuentoMonster=0
    if nombreCliente=="carlos" or nombreCliente=="ines":
        sumaDescuentosPanVIP=descuentoPan+descuentoPanVIP
        precioFinalPanVIP=precioPan-(precioPan*sumaDescuentosPanVIP/100)
        if descuentoPan > 0 or descuentoPanVIP > 0:
            print("Hay un descuento en Pan del", descuentoPan, "% por ser cliente NORMAL y del", descuentoPanVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPanVIP ,"% de descuento.")
            print("1-Pan:     ", precioFinalPanVIP, "€/Unidad")
        else:
            print("1-Pan:     ", precioPan, "€/Unidad")
        sumaDescuentosLecheVIP=descuentoLeche+descuentoLecheVIP
        precioFinalLecheVIP=precioLeche-(precioLeche*sumaDescuentosLecheVIP/100)
        if descuentoLeche > 0 or descuentoLecheVIP > 0:
            print("Hay un descuento en Leche del", descuentoLeche, "% por ser cliente NORMAL y del", descuentoLecheVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosLecheVIP ,"% de descuento.")
            print("2-Leche:   ", precioFinalLecheVIP, "€/Unidad")
        else:
            print("2-Leche:   ", precioLeche, "€/Unidad")
        sumaDescuentosPolloVIP=descuentoPollo+descuentoPolloVIP
        precioFinalPolloVIP=precioPollo-(precioPollo*sumaDescuentosPolloVIP/100)
        if descuentoPollo > 0 or descuentoPolloVIP > 0:
            print("Hay un descuento en Pollo del", descuentoPollo, "% por ser cliente NORMAL y del", descuentoPolloVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPolloVIP ,"% de descuento.")
            print("3-Pollo:   ", precioFinalPolloVIP, "€/Unidad")
        else:
            print("3-Pollo:    ", precioPollo, "€/Unidad")
        sumaDescuentosAtunVIP=descuentoAtun+descuentoAtunVIP
        precioFinalAtunVIP=precioAtun-(precioAtun*sumaDescuentosAtunVIP/100)
        if descuentoAtun > 0 or descuentoAtunVIP > 0:
            print("Hay un descuento en Atun del", descuentoAtun, "% por ser cliente NORMAL y del", descuentoAtunVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosAtunVIP ,"% de descuento.")
            print("4-Atun: ", precioFinalAtunVIP, "€/Unidad")
        else:
            print("4-Atun:    ", precioAtun, "€/Unidad")
        sumaDescuentosMonsterVIP=descuentoMonster+descuentoMonsterVIP
        precioFinalMonsterVIP=precioMonster-(precioMonster*sumaDescuentosMonsterVIP/100)
        if descuentoMonster > 0 or descuentoMonsterVIP > 0:
            print("Hay un descuento en Monster del", descuentoMonster, "% por ser cliente NORMAL y del", descuentoMonsterVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosMonsterVIP ,"% de descuento.")
            print("5-Monster: ", precioFinalMonsterVIP, "€/Unidad")
        else:
            print("5-Monster: ", precioMonster, "€/Unidad")

        #Pide al cliente VIP indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0

        #Pide al cliente VIP indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente VIP:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")





    elif nombreCliente=="srmuro":
        subidaPufo=0.50
        print("Todos los productos se han encarecido un", subidaPufo, "% más por ser usted un Cliente PUFO.")
        print("El precio de los productos es el siguiente:")
        precioFinalPanPUFO=precioPan+subidaPufo
        print("Pan: ", precioFinalPanPUFO, "€")
        precioFinalLechePUFO=precioLeche+subidaPufo
        print("Leche: ", precioFinalLechePUFO, "€")
        precioFinalPolloPUFO=precioPollo+subidaPufo
        print("Pollo: ", precioFinalPolloPUFO, "€")
        precioFinalAtunPUFO=precioAtun+subidaPufo
        print("Atun: ", precioFinalAtunPUFO, "€")
        precioFinalMonsterPUFO=precioMonster+subidaPufo
        print("Monster: ", precioFinalMonsterPUFO, "€")
        #Pide al cliente PUFO indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLechePUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente PUFO indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        print("")
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLechePUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente PUFO:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")




    #Si el cliente no es carlos, ines y tampoco srmuro:
    elif nombreCliente!="carlos" and nombreCliente!="ines" and nombreCliente!="srmuro":
        precioFinalPanNORMAL=precioPan-(precioPan*descuentoPan/100)
        if descuentoPan > 0:
            print("Hay un descuento del", descuentoPan, "% en pan.")
            print("1-PAN:     ", precioFinalPanNORMAL, "€/Unidad")
        else:
            print("1-PAN:     ", precioPan, "€/Unidad")
        precioFinalLecheNORMAL=precioLeche-(precioLeche*descuentoLeche/100)
        if descuentoLeche > 0:
            print("Hay un descuento del", descuentoLeche, "% en leche.")
            print("2-LECHE:   ", precioFinalLecheNORMAL, "€/Unidad")
        else:
            print("2-LECHE:   ", precioLeche, "€/Unidad")
        precioFinalPolloNORMAL=precioPollo-(precioPollo*descuentoPollo/100)
        if descuentoPollo > 0:
            print("Hay un descuento del", descuentoPollo, "% en pollo.")
            print("3-POLLO:   ", precioFinalPolloNORMAL, "€/Unidad")
        else:
            print("3-POLLO:   ", precioPollo, "€/Unidad")
        precioFinalAtunNORMAL=precioAtun-(precioAtun*descuentoAtun/100)
        if descuentoAtun > 0:
            print("Hay un descuento del", descuentoAtun, "% en atun.")
            print("4-ATUN:    ", precioFinalAtunNORMAL, "€/Unidad")
        else:
            print("4-ATUN:    ", precioAtun, "€/Unidad")
        precioFinalMonsterNORMAL=precioMonster-(precioMonster*descuentoMonster/100)
        if descuentoMonster > 0:
            print("Hay un descuento del", descuentoMonster, "% en monster.")
            print("5-MONSTER: ", precioFinalMonsterNORMAL, "€/Unidad")
        else:
            print("5-MONSTER: ", precioMonster, "€/Unidad")
        print("")
        #Pide al cliente NORMAL indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL: 
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente NORMAL indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma los dos productos elegidos por el cliente NORMAL:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")

##########################################################################################################
##########################################################################################################
############################################ V I E R N E S ###############################################
##########################################################################################################
##########################################################################################################

if diaDeLaSemana=="VIERNES":
    print("")
    print("¡BIENVENID@", nombreCliente.upper(), "! Hoy es", diaDeLaSemana, "y tenemos para tí muy grandiosas ofertas, he aquí las siguientes noticias sobre nuestros productos:")
    print("")
    descuentoPan=70
    descuentoLeche=70
    descuentoPollo=70
    descuentoAtun=70
    descuentoMonster=70
    if nombreCliente=="carlos" or nombreCliente=="ines":
        sumaDescuentosPanVIP=descuentoPan+descuentoPanVIP
        precioFinalPanVIP=precioPan-(precioPan*sumaDescuentosPanVIP/100)
        if descuentoPan > 0 or descuentoPanVIP > 0:
            print("Hay un descuento en Pan del", descuentoPan, "% por ser cliente NORMAL y del", descuentoPanVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPanVIP ,"% de descuento.")
            print("1-Pan:     ", precioFinalPanVIP, "€/Unidad")
        else:
            print("1-Pan:     ", precioPan, "€/Unidad")
        sumaDescuentosLecheVIP=descuentoLeche+descuentoLecheVIP
        precioFinalLecheVIP=precioLeche-(precioLeche*sumaDescuentosLecheVIP/100)
        if descuentoLeche > 0 or descuentoLecheVIP > 0:
            print("Hay un descuento en Leche del", descuentoLeche, "% por ser cliente NORMAL y del", descuentoLecheVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosLecheVIP ,"% de descuento.")
            print("2-Leche:   ", precioFinalLecheVIP, "€/Unidad")
        else:
            print("2-Leche:   ", precioLeche, "€/Unidad")
        sumaDescuentosPolloVIP=descuentoPollo+descuentoPolloVIP
        precioFinalPolloVIP=precioPollo-(precioPollo*sumaDescuentosPolloVIP/100)
        if descuentoPollo > 0 or descuentoPolloVIP > 0:
            print("Hay un descuento en Pollo del", descuentoPollo, "% por ser cliente NORMAL y del", descuentoPolloVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPolloVIP ,"% de descuento.")
            print("3-Pollo:   ", precioFinalPolloVIP, "€/Unidad")
        else:
            print("3-Pollo:    ", precioPollo, "€/Unidad")
        sumaDescuentosAtunVIP=descuentoAtun+descuentoAtunVIP
        precioFinalAtunVIP=precioAtun-(precioAtun*sumaDescuentosAtunVIP/100)
        if descuentoAtun > 0 or descuentoAtunVIP > 0:
            print("Hay un descuento en Atun del", descuentoAtun, "% por ser cliente NORMAL y del", descuentoAtunVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosAtunVIP ,"% de descuento.")
            print("4-Atun: ", precioFinalAtunVIP, "€/Unidad")
        else:
            print("4-Atun:    ", precioAtun, "€/Unidad")
        sumaDescuentosMonsterVIP=descuentoMonster+descuentoMonsterVIP
        precioFinalMonsterVIP=precioMonster-(precioMonster*sumaDescuentosMonsterVIP/100)
        if descuentoMonster > 0 or descuentoMonsterVIP > 0:
            print("Hay un descuento en Monster del", descuentoMonster, "% por ser cliente NORMAL y del", descuentoMonsterVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosMonsterVIP ,"% de descuento.")
            print("5-Monster: ", precioFinalMonsterVIP, "€/Unidad")
        else:
            print("5-Monster: ", precioMonster, "€/Unidad")

        #Pide al cliente VIP indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0

        #Pide al cliente VIP indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente VIP:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")





    elif nombreCliente=="srmuro":
        subidaPufo=0.50
        print("Todos los productos se han encarecido un", subidaPufo, "% más por ser usted un Cliente PUFO.")
        print("El precio de los productos es el siguiente:")
        precioFinalPanPUFO=precioPan+subidaPufo
        print("Pan: ", precioFinalPanPUFO, "€")
        precioFinalLechePUFO=precioLeche+subidaPufo
        print("Leche: ", precioFinalLechePUFO, "€")
        precioFinalPolloPUFO=precioPollo+subidaPufo
        print("Pollo: ", precioFinalPolloPUFO, "€")
        precioFinalAtunPUFO=precioAtun+subidaPufo
        print("Atun: ", precioFinalAtunPUFO, "€")
        precioFinalMonsterPUFO=precioMonster+subidaPufo
        print("Monster: ", precioFinalMonsterPUFO, "€")
        #Pide al cliente PUFO indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLechePUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente PUFO indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        print("")
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLechePUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente PUFO:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")




    #Si el cliente no es carlos, ines y tampoco srmuro:
    elif nombreCliente!="carlos" and nombreCliente!="ines" and nombreCliente!="srmuro":
        precioFinalPanNORMAL=precioPan-(precioPan*descuentoPan/100)
        if descuentoPan > 0:
            print("Hay un descuento del", descuentoPan, "% en pan.")
            print("1-PAN:     ", precioFinalPanNORMAL, "€/Unidad")
        else:
            print("1-PAN:     ", precioPan, "€/Unidad")
        precioFinalLecheNORMAL=precioLeche-(precioLeche*descuentoLeche/100)
        if descuentoLeche > 0:
            print("Hay un descuento del", descuentoLeche, "% en leche.")
            print("2-LECHE:   ", precioFinalLecheNORMAL, "€/Unidad")
        else:
            print("2-LECHE:   ", precioLeche, "€/Unidad")
        precioFinalPolloNORMAL=precioPollo-(precioPollo*descuentoPollo/100)
        if descuentoPollo > 0:
            print("Hay un descuento del", descuentoPollo, "% en pollo.")
            print("3-POLLO:   ", precioFinalPolloNORMAL, "€/Unidad")
        else:
            print("3-POLLO:   ", precioPollo, "€/Unidad")
        precioFinalAtunNORMAL=precioAtun-(precioAtun*descuentoAtun/100)
        if descuentoAtun > 0:
            print("Hay un descuento del", descuentoAtun, "% en atun.")
            print("4-ATUN:    ", precioFinalAtunNORMAL, "€/Unidad")
        else:
            print("4-ATUN:    ", precioAtun, "€/Unidad")
        precioFinalMonsterNORMAL=precioMonster-(precioMonster*descuentoMonster/100)
        if descuentoMonster > 0:
            print("Hay un descuento del", descuentoMonster, "% en monster.")
            print("5-MONSTER: ", precioFinalMonsterNORMAL, "€/Unidad")
        else:
            print("5-MONSTER: ", precioMonster, "€/Unidad")
        print("")
        #Pide al cliente NORMAL indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL: 
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente NORMAL indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma los dos productos elegidos por el cliente NORMAL:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")

##########################################################################################################
##########################################################################################################
############################################## S Á B A D O ###############################################
##########################################################################################################
##########################################################################################################

if diaDeLaSemana=="SABADO" or diaDeLaSemana=="SÁBADO":
    print("")
    print("¡BIENVENID@", nombreCliente.upper(), "! Hoy es", diaDeLaSemana, "y tenemos para tí las siguientes noticias sobre nuestros productos:")
    print("")
    descuentoPan=0
    descuentoLeche=0
    descuentoPollo=0
    descuentoAtun=0
    descuentoMonster=0
    if nombreCliente=="carlos" or nombreCliente=="ines":
        sumaDescuentosPanVIP=descuentoPan+descuentoPanVIP
        precioFinalPanVIP=precioPan-(precioPan*sumaDescuentosPanVIP/100)
        if descuentoPan > 0 or descuentoPanVIP > 0:
            print("Hay un descuento en Pan del", descuentoPan, "% por ser cliente NORMAL y del", descuentoPanVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPanVIP ,"% de descuento.")
            print("1-Pan:     ", precioFinalPanVIP, "€/Unidad")
        else:
            print("1-Pan:     ", precioPan, "€/Unidad")
        sumaDescuentosLecheVIP=descuentoLeche+descuentoLecheVIP
        precioFinalLecheVIP=precioLeche-(precioLeche*sumaDescuentosLecheVIP/100)
        if descuentoLeche > 0 or descuentoLecheVIP > 0:
            print("Hay un descuento en Leche del", descuentoLeche, "% por ser cliente NORMAL y del", descuentoLecheVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosLecheVIP ,"% de descuento.")
            print("2-Leche:   ", precioFinalLecheVIP, "€/Unidad")
        else:
            print("2-Leche:   ", precioLeche, "€/Unidad")
        sumaDescuentosPolloVIP=descuentoPollo+descuentoPolloVIP
        precioFinalPolloVIP=precioPollo-(precioPollo*sumaDescuentosPolloVIP/100)
        if descuentoPollo > 0 or descuentoPolloVIP > 0:
            print("Hay un descuento en Pollo del", descuentoPollo, "% por ser cliente NORMAL y del", descuentoPolloVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosPolloVIP ,"% de descuento.")
            print("3-Pollo:   ", precioFinalPolloVIP, "€/Unidad")
        else:
            print("3-Pollo:    ", precioPollo, "€/Unidad")
        sumaDescuentosAtunVIP=descuentoAtun+descuentoAtunVIP
        precioFinalAtunVIP=precioAtun-(precioAtun*sumaDescuentosAtunVIP/100)
        if descuentoAtun > 0 or descuentoAtunVIP > 0:
            print("Hay un descuento en Atun del", descuentoAtun, "% por ser cliente NORMAL y del", descuentoAtunVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosAtunVIP ,"% de descuento.")
            print("4-Atun: ", precioFinalAtunVIP, "€/Unidad")
        else:
            print("4-Atun:    ", precioAtun, "€/Unidad")
        sumaDescuentosMonsterVIP=descuentoMonster+descuentoMonsterVIP
        precioFinalMonsterVIP=precioMonster-(precioMonster*sumaDescuentosMonsterVIP/100)
        if descuentoMonster > 0 or descuentoMonsterVIP > 0:
            print("Hay un descuento en Monster del", descuentoMonster, "% por ser cliente NORMAL y del", descuentoMonsterVIP, "% por ser VIP lo que da un total de:   ",sumaDescuentosMonsterVIP ,"% de descuento.")
            print("5-Monster: ", precioFinalMonsterVIP, "€/Unidad")
        else:
            print("5-Monster: ", precioMonster, "€/Unidad")

        #Pide al cliente VIP indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterVIP*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0

        #Pide al cliente VIP indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio VIP:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterVIP*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioFinalMonsterVIP=0
            precioFinalAtunVIP=0
            precioFinalPolloVIP=0
            precioFinalLecheVIP=0
            precioFinalPanVIP=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente VIP:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")





    elif nombreCliente=="srmuro":
        subidaPufo=0.50
        print("Todos los productos se han encarecido un", subidaPufo, "% más por ser usted un Cliente PUFO.")
        print("El precio de los productos es el siguiente:")
        precioFinalPanPUFO=precioPan+subidaPufo
        print("Pan: ", precioFinalPanPUFO, "€")
        precioFinalLechePUFO=precioLeche+subidaPufo
        print("Leche: ", precioFinalLechePUFO, "€")
        precioFinalPolloPUFO=precioPollo+subidaPufo
        print("Pollo: ", precioFinalPolloPUFO, "€")
        precioFinalAtunPUFO=precioAtun+subidaPufo
        print("Atun: ", precioFinalAtunPUFO, "€")
        precioFinalMonsterPUFO=precioMonster+subidaPufo
        print("Monster: ", precioFinalMonsterPUFO, "€")
        #Pide al cliente PUFO indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLechePUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterPUFO*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente PUFO indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio PUFO:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        print("")
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLechePUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterPUFO*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterPUFO=0
            precioFinalAtunPUFO=0
            precioFinalPolloPUFO=0
            precioFinalLechePUFO=0
            precioFinalPanPUFO=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma de los dos productos elegidos por el cliente PUFO:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")




    #Si el cliente no es carlos, ines y tampoco srmuro:
    elif nombreCliente!="carlos" and nombreCliente!="ines" and nombreCliente!="srmuro":
        precioFinalPanNORMAL=precioPan-(precioPan*descuentoPan/100)
        if descuentoPan > 0:
            print("Hay un descuento del", descuentoPan, "% en pan.")
            print("1-PAN:     ", precioFinalPanNORMAL, "€/Unidad")
        else:
            print("1-PAN:     ", precioPan, "€/Unidad")
        precioFinalLecheNORMAL=precioLeche-(precioLeche*descuentoLeche/100)
        if descuentoLeche > 0:
            print("Hay un descuento del", descuentoLeche, "% en leche.")
            print("2-LECHE:   ", precioFinalLecheNORMAL, "€/Unidad")
        else:
            print("2-LECHE:   ", precioLeche, "€/Unidad")
        precioFinalPolloNORMAL=precioPollo-(precioPollo*descuentoPollo/100)
        if descuentoPollo > 0:
            print("Hay un descuento del", descuentoPollo, "% en pollo.")
            print("3-POLLO:   ", precioFinalPolloNORMAL, "€/Unidad")
        else:
            print("3-POLLO:   ", precioPollo, "€/Unidad")
        precioFinalAtunNORMAL=precioAtun-(precioAtun*descuentoAtun/100)
        if descuentoAtun > 0:
            print("Hay un descuento del", descuentoAtun, "% en atun.")
            print("4-ATUN:    ", precioFinalAtunNORMAL, "€/Unidad")
        else:
            print("4-ATUN:    ", precioAtun, "€/Unidad")
        precioFinalMonsterNORMAL=precioMonster-(precioMonster*descuentoMonster/100)
        if descuentoMonster > 0:
            print("Hay un descuento del", descuentoMonster, "% en monster.")
            print("5-MONSTER: ", precioFinalMonsterNORMAL, "€/Unidad")
        else:
            print("5-MONSTER: ", precioMonster, "€/Unidad")
        print("")
        #Pide al cliente NORMAL indicar primer producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL: 
        productoElegido1=int(input("Indique el primer producto que quiere comprar: "))
        if productoElegido1==1:
            cantidadProducto1=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPanNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pan es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==2:
            cantidadProducto1=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto1=precioFinalLecheNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Leche es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==3:
            cantidadProducto1=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto1=precioFinalPolloNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Pollo es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==4:
            cantidadProducto1=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto1=precioFinalAtunNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Atun es de:", precioCalculadoProducto1, "€")
        elif productoElegido1==5:
            cantidadProducto1=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto1=precioFinalMonsterNORMAL*cantidadProducto1
            print("El precio de", cantidadProducto1, "unidades de Monster es de:", precioCalculadoProducto1, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido1 , "  Cantidad: ", cantidadProducto1, "  Precio: ", precioCalculadoProducto1*productoElegido1, "€")
            precioCalculadoProducto1
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Pide al cliente NORMAL indicar segundo producto que quiere comprar, pedir cantidad, multiplicar cantidad por precio NORMAL:
        productoElegido2=int(input("Indique el segundo producto que quiere comprar: "))
        if productoElegido2==1:
            cantidadProducto2=int(input("Indique la cantidad de pan que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPanNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pan es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==2:
            cantidadProducto2=int(input("Indique la cantidad de leche que quiere comprar: "))
            precioCalculadoProducto2=precioFinalLecheNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Leche es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==3:
            cantidadProducto2=int(input("Indique la cantidad de pollo que quiere comprar: "))
            precioCalculadoProducto2=precioFinalPolloNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Pollo es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==4:
            cantidadProducto2=int(input("Indique la cantidad de atun que quiere comprar: "))
            precioCalculadoProducto2=precioFinalAtunNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Atun es de:", precioCalculadoProducto2, "€")
        elif productoElegido2==5:
            cantidadProducto2=int(input("Indique la cantidad de monster que quiere comprar: "))
            precioCalculadoProducto2=precioFinalMonsterNORMAL*cantidadProducto2
            print("El precio de", cantidadProducto2, "unidades de Monster es de:", precioCalculadoProducto2, "€")
        else:
            print("El producto que ha indicado no existe.")
            print ("Producto elegido:", productoElegido2 , "  Cantidad: ", cantidadProducto2, "  Precio: ", precioCalculadoProducto2*productoElegido2, "€")
            precioCalculadoProducto2
            precioFinalMonsterNORMAL=0
            precioFinalAtunNORMAL=0
            precioFinalPolloNORMAL=0
            precioFinalLecheNORMAL=0
            precioFinalPanNORMAL=0
            cantidadProducto1=0
            cantidadProducto2=0
            productoElegido1=0
            productoElegido2=0
        #Suma los dos productos elegidos por el cliente NORMAL:
        print("--> Su compra es de:", precioCalculadoProducto1+precioCalculadoProducto2, "€")

##########################################################################################################
##########################################################################################################
############################################# D O M I N G O ##############################################
##########################################################################################################
##########################################################################################################
if diaDeLaSemana=="DOMINGO":
    print("")
    print("¡BIENVENID@", nombreCliente.upper(), "! Hoy es", diaDeLaSemana, "y por tanto estamos cerrados, pero si en realidad eres Óscar te podemos abrir ;)")
    print("")