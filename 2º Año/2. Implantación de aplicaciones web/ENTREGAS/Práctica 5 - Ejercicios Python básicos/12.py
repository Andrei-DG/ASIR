# Ejercicio 12 Pide al usuario dos pares de números 
# x1,y2 y x2,y2, que representen dos puntos en el plano. 
# Calcula y muestra la distancia entre ellos. 

import math
print("Introduce coordenada del punto 1:")
x1 = int(input())
y1 = int(input())
print("Introduce coordenada del punto 2:")
x2 = int(input())
y2 = int(input())
distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print("Distancia:", distancia)