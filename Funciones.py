from random import randrange
import csv

def menu():
    print("BIENVENIDO")
    print("************************************")
    print("1 Asignar sueldos aleatorios.")
    print("2 Clasificar sueldos")
    print("3 Ver estadísticas")
    print("4 Reporte de suedos")
    print("5 Salir del programa")

def validar_op():
    while True:
        try:
            op = int(input())
            if op>=1 and op<=4:
                return op
            else:
                raise ValueError
        except:
            print("Selecciona una opcion valida.")

def generar_sueldos(lista):
    empleados = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
    for i in range(len(empleados)):
        
        nom = empleados[i]
        sueldo = randrange(500000,2500000)
        d = {"nombre":nom,"sueldo":sueldo}
        lista.append(d)

def clasificar_empleados(lista):
    bajos = []
    medios = []
    altos = []

    for trabajador in lista:
        if trabajador["sueldo"]<=800000:
            bajos.append(trabajador)
        elif trabajador["sueldo"]<=2000000 and trabajador["sueldo"]>=800000:
            medios.append(trabajador)
        else:
            altos.append(trabajador)
    
    print("Sueldos menores a $800.000")
    print("Total")
    print("")
    for i in range(len(bajos)):
        print(bajos[i]["nombre"])
        print(bajos[i]["sueldo"])
    print("")
    print("Sueldos entre $800.000 y $2.000.000")
    print("Total")
    print("")
    for i in range(len(medios)):
        print(medios[i]["nombre"])
        print(medios[i]["sueldo"])
    print("")
    print("Sueldos mayores a $2.000.000")
    print("Total")
    print("")
    for i in range(len(altos)):
        print(altos[i]["nombre"])
        print(altos[i]["sueldo"])
    
    listar_bajos = [sueldo["sueldo"] for sueldo in bajos]
    listar_altos = [sueldo["sueldo"] for sueldo in altos]
    listar_medios = [sueldo["sueldo"] for sueldo in medios]
    sumat = sum(listar_bajos)+sum(listar_medios)+sum(listar_altos)
    print("el total de los sueldos es ", sumat)

def imprimir_estadisticas(lista):
    bajo = lista[0]
    for empleado in lista:
        if bajo["sueldo"]>empleado["sueldo"]:
            bajo = empleado

    alto = lista[0]
    for empleado in lista:
        if alto["sueldo"]<empleado["sueldo"]:
            alto = empleado

    print(f"Sueldo más bajo: {alto}")
    print(f"Sueldo más alto: {bajo}")
    listar_sueldos = [sueldo["sueldo"] for sueldo in lista]
    suma = sum(listar_sueldos)
    promedio = suma/10
    print(f"Sueldo promedio: {promedio:,.0f}")
    print(f"Media Geometrica: {promedio:,.0f}")

def report_sueldos(lista):
    for trabajador in lista:
        sueldo_bruto = trabajador["sueldo"]
        afp = int(sueldo_bruto * 0.12)
        salud = int(sueldo_bruto * 0.07)
        sueldo_liquido = sueldo_bruto - afp - salud
        a = {"nombre":trabajador["nombre"],"sueldo_bruto":sueldo_bruto,"afp":afp,"salud":salud,"sueldo_liquido":sueldo_liquido}
        print("nombre        Sueldo base        salud         AFP        sueldo liquido       ")   
        print(trabajador["nombre"],"  ",sueldo_bruto,"  ",salud,"   ",afp,"   ",sueldo_liquido,"  ")

        
def salir():


        print("Programa finaliza.....")
        print("Creado por Tomas del fierro")
        print("Rut: 17516572-K")