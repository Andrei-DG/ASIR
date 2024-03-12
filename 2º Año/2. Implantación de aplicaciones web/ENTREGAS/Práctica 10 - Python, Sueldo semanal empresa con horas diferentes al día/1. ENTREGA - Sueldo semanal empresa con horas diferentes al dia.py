
#Una empresa paga a sus empleados con base en las horas trabajadas en la semana.
#Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo
#para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la
#empresa por los N empleados.

print("")
print("")
print("")
print("")
print("")
print("")
print("")
sueldoTotal = 0
sueldoHora = float(input("Introduce el sueldo por hora: "))
sueldoEmpleado = 0

while True:

    for i in range(7):
        if i == 0:
            horas = int(input("Ingrese las horas trabajadas el Lunes: "))
        elif i == 1:
            horas = int(input("Ingrese las horas trabajadas el Martes: "))
        elif i == 2:
            horas = int(input("Ingrese las horas trabajadas el Miércoles: "))
        elif i == 3:
            horas = int(input("Ingrese las horas trabajadas el Jueves: "))
        elif i == 4:
            horas = int(input("Ingrese las horas trabajadas el Viernes: "))
        elif i == 5:
            horas = int(input("Ingrese las horas trabajadas el Sábado: "))
        elif i == 6:
            horas = int(input("Ingrese las horas trabajadas el Domingo: "))
            
        sueldoEmpleado += horas * sueldoHora
    print("El sueldo del empleado es: ", sueldoEmpleado)
    sueldoTotal += sueldoEmpleado
    sueldoEmpleado = 0
    otroEmpleado = input("¿Desea añadir otro empleado?: ").lower()
    if otroEmpleado != "si" and otroEmpleado != "no":
        while otroEmpleado != "si" and otroEmpleado != "no":
            otroEmpleado = input("Introduce un valor válido: ").lower()
    if otroEmpleado == "si":
        continue
    if otroEmpleado == "no":
        break
print("El sueldo total de la empresa es: ", sueldoTotal)