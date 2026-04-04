from services.suma import suma_
from services.resta import resta_
from services.division import division_
from services.multiplicacion import multiplicacion_

bandera = 1
while bandera:
    num_1 = int(input("ingresa el primer numero: "))
    num_2 = int(input("ingresa el segundo numero: "))

    print("selecciona la operacion a realizar: ")
    print("1.  suma")
    print("2.  resta")
    print("3.  multiplicacion")
    print("4.  division")

    operation = int(input())

    print("este es el resultado de tu operacion")
    if operation == 1:
        print(suma_(num_1,num_2))
    elif operation == 2:
        print(resta_(num_1,num_2))
    elif operation == 3:
        print(multiplicacion_(num_1,num_2))
    elif operation == 4:
        print(division_(num_1,num_2))
    
    bandera=int(input("quieres salir? 0 si 1 no"))







