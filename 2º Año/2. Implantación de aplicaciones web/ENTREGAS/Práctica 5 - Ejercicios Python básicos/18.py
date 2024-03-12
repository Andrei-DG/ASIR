# Ejercicio 18 Pedir el nombre y los dos apellidos 
# de una persona y mostrar las iniciales. 

nombre = input("Introduce tu nombre:")
apellido1 = input("Introduce tu primer apellido:")
apellido2 = input("Introduce tu segundo apellido:")

inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]

inicial = inicial.upper()
print("Iniciales:",inicial)