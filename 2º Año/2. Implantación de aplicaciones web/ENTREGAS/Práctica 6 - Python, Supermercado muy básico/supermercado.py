#Supermercado virtual

#Listar variables de productos y su precio:
from datetime import datetime


pPan = 0.50
pLeche = 1.50
pMonster = 1.42
pChocolate = 1.25
pGalletas = 2.00

print("------------------------------------")
print("Bienvenido al supermercado virtual")
print()
cPan = int(input("¿Cuántos panes desea comprar? "))
cLeche = int(input("¿Cuántas leches desea comprar? "))
cMonster = int(input("¿Cuántos monsters desea comprar? "))
cChocolate = int(input("¿Cuántos chocolates desea comprar? "))
cGalletas = int(input("¿Cuántas galletas desea comprar? "))
total = (cPan * pPan) + (cLeche * pLeche) + (cMonster * pMonster) + (cChocolate * pChocolate) + (cGalletas * pGalletas) 
print()
print("El total a pagar es: ", round(total, 2)) #Redondear porque da muchos decimales el Python (no debería)
print("------------------------------------")
print("Muchas gracias por su compra")
print("------------------------------------")