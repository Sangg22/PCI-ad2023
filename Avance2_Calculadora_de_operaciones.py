'Proyecto de calculadora'
def Suma(x,y):
    return x+y
def Resta(x,y):
    return x-y                            #PRIMERAMENTE DEFINI CON LA OPCIÓN "def" LAS OPERACIONES QUE VA A TENER MI MENU
def Multiplicacion(x,y):                  #OBVIAMENTE VOY A IR INCLUYENDO MAS OPCIONES, AHORITA PUSE LO PRINCIPAL
    return x*y
def Division(x,y):
    return x/y
def Raiz(x):
    return x**.5
while True:  #inserte while para que se creara un ciclo y poder volver al menu y poder tener otra opción
    print("**Menu de calculadora**")
    print("1. Sumar")
    print("2. Restar")                     #Imprimi las opciones que va a arrojar el menu
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raiz_cuadrada")
    print("6. Salir")
    opc=input("Ingrese una opción\n")  #para esta parte, tuve que investigar en opciones externas#y encontre la opción "opc" para que pudiera dar opciones
    if opc=="1":
        x=float(input("Da el primer número a sumar: \n"))
        y=float(input("Da el segundo número a sumar: \n"))
        print(f"La suma es: {Suma(x,y)}")
    elif opc=="2":
        x=float(input("Da el número al que se va a restar: \n"))
        y=float(input("Da el número que se le va a restar al primero: \n"))
        print(f"La resta es: {Resta(x,y)}")   #en esta parte ya inclui los condicionales para cada opción
    elif opc=="3":                            #y según la opción que daba, ponia una función ya definida
        x=float(input("Da el primer número a multiplicar: \n"))
        y=float(input("Da el segundo número a multiplicar: \n"))
        print(f"La multiplicación es: {Multiplicacion(x,y)}")
    elif opc=="4":
        x=float(input("Da el número al que se le va a divir: \n"))
        y=float(input("Da el número por el que se va a dividr: \n"))
        print(f"La división da: {Division(x,y)}")
    elif opc=="5":
        x=float(input("Dame el valor al que se le sacara raiz: \n"))
        print(f"La raiz es: {Raiz(x)}")
    elif opc=="6":                   #inclui la opción de salir para que fuera más fácil de usar
        exit()                  #inclui las opciones más básicas, pero ire poniendo opciones mas complejas
