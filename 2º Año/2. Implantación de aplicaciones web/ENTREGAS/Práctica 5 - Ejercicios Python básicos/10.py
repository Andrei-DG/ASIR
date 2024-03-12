# Ejercicio 10 Un alumno desea saber cual será su calificación final 
# en la materia de Algoritmos. Dicha calificación se compone de los 
# siguientes #porcentajes: •55% del promedio de sus tres calificaciones 
# parciales. •30% de la calificación del examen final. 
# •15% de la calificación de un trabajo final. 

parcial1 = float(input("Introduce la 1º nota: "))
parcial2 = float(input("Introduce la 2º nota: "))
parcial3 = float(input("Introduce la 3º nota: "))

promedio = (parcial1+parcial2+parcial3) / 3

examen = float(input("Introduce el promedio del examen final:"))
trabajo = float(input("Introduce la nota del trabajo final:"))

notafinal = (promedio * 0.55) + (examen * 0.30) + (trabajo * 0.15)
print("El promedio final de la materia de Algoritmos es:", notafinal)