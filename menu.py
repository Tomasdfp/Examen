import Funciones as fun
from os import system

trabajadores=[]

op = 0

while op !=5:
    system("cls")
    fun.menu()
    op = fun.validar_op()
    if op==1:
        system("cls")
        fun.generar_sueldos(trabajadores)
        print("Se generaron los sueldo exitosamente")
        system("pause")
    elif op==2:
        system("cls")
        fun.clasificar_empleados(trabajadores)
        system("pause")
    elif op==3:
        system("cls")
        fun.imprimir_estadisticas(trabajadores)
        system("pause")
    elif op==4:
        system("cls")
        fun.report_sueldos(trabajadores)
        system("pause")
    else:
        system("cls")
        fun.salir()

    
    


