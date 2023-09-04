'Proyecto de calculadora'
import math
PI=3.1416
def suma(x,y):
    return x+y
def resta(x,y):
    return x-y                            #PRIMERAMENTE DEFINI CON LA OPCIÓN "def" LAS OPERACIONES QUE VA A TENER MI MENU
def multiplicacion(x,y):                  #OBVIAMENTE VOY A IR INCLUYENDO MAS OPCIONES, AHORITA PUSE LO PRINCIPAL
    return x*y
def division(x,y):
    return x/y
def raiz(x):
    return x**.5
def area_cuadrado(x,y):
    return x*y
def area_triangulo(x,y):
    return (x*y)/2
def area_circulo(x):
    return  PI*(x**2)
def area_rombo(x,y):
    return  (x*y)/2
def area_trapecio(x,y,z):
    return ((x*y)*z)/2
while True:  #inserte while para que se creara un ciclo y poder volver al menu y poder tener otra opción
    print("**Menu de calculadora**")
    print("1. Sumar")
    print("2. Restar")                     #Imprimi las opciones que va a arrojar el menu
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raiz_cuadrada")
    print("6. Areas")
    print("7. Salir")
    opc=input("Ingrese una opción\n")  #para esta parte, tuve que investigar en opciones externas#y encontre la opción "opc" para que pudiera dar opciones
    if opc=="1":
        x=float(input("Da el primer número a sumar: \n"))
        y=float(input("Da el segundo número a sumar: \n"))
        print(f"La suma de {x} y {y} es: {suma(x,y)}")
    elif opc=="2":
        x=float(input("Da el número al que se va a restar: \n"))
        y=float(input("Da el número que se le va a restar al primero: \n"))
        print(f"La resta de {x} menos {y} es: {resta(x,y)}")   #en esta parte ya inclui los condicionales para cada opción
    elif opc=="3":                            #y según la opción que daba, ponia una función ya definida
        x=float(input("Da el primer número a multiplicar: \n"))
        y=float(input("Da el segundo número a multiplicar: \n"))
        print(f"La multiplicación entre {x} y {y} es: {multiplicacion(x,y)}")
    elif opc=="4":
        x=float(input("Da el número al que se le va a divir: \n"))
        y=float(input("Da el número por el que se va a dividr: \n"))
        print(f"La división entre {x} y {y} da: {division(x,y)}")
    elif opc=="5":
        x=float(input("Dame el valor al que se le sacara raiz: \n"))
        if x<0:
            print("No es posible")
        else:
            print(f"La raiz de {x} es: {raiz(x)}")
    elif opc=="6":
        while True:                 #inclui un segundo menu para que me diera las opciones de areas
            print("**Menu de areas**")
            print("6.1 Area de cuadrado")
            print("6.2 Area de triangulo")
            print("6.3 Area de circulo")
            print("6.4 Area de rombo")
            print("6.5 Area de trapecio")
            print("6.6 Volver al menu principal")
            opc=input("Ingrese una opción de area\n")
            if opc=="6.1":
                x=float(input("Dame la base del cuadrado: \n"))
                y=float(input("Dame la altura del cuadrado: \n"))
                print(f"El area del cuadrado es: {area_cuadrado(x,y)}")
            elif opc=="6.2":
                x=float(input("Dame la base del triangulo: \n"))
                y=float(input("Dame la altura del triangulo: \n"))
                print(f"El area del triangulo es: {area_triangulo(x,y)}")
            elif opc=="6.3":                                                #puse todo lo que se haria en este menu
                x=float(input("Dame el radio del circulo: \n"))
                print(f"El area del circulo es: {area_circulo(x)}")
            elif opc=="6.4":
                x=float(input("Dame el diametro mayor del rombo: \n"))
                y=float(input("Dame el diametro menor del rombo: \n"))
                print(f"El area del rombo es: {area_rombo(x,y)}")
            elif opc=="6.5":
                x=float(input("Dame la base mayor del trapecio: \n"))
                y=float(input("Dame la base menor del trapecio: \n"))
                z=float(input("Dame la altura del trapecio: \n"))
                print(f"El area del trapecio es: {area_trapecio(x,y,z)}")
            elif opc=="6.6":                                       #use un "break" para poder voler al menu principal
                break      
    elif opc=="7":                   #inclui la opción de salir para que fuera más fácil de usar
        exit()                  #inclui las opciones más básicas, pero ire poniendo opciones mas complejas
