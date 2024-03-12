# Ejercicio 14 Dado un número de dos cifras, diseñe un algoritmo
# que permita obtener el número invertido. 
# Ejemplo, si se introduce 23 que muestre 32. 

num = int(input("Introduce un número de dos cifras:"))
decenas = num // 10
unidades = num % 10
print("Primera cifra (decenas):", decenas)
print("Segunda cifra (unidades):", unidades)
