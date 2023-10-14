'Proyecto de calculadora'
import math
PI=3.1416
def menu():
    print("**Menu de calculadora**")
    print("1. Sumar")
    print("2. Restar")                     #Imprimi las opciones que va a arrojar el menu
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Promedio")
    print("6. Raiz_cuadrada")
    print("7. Formula general")
    print("8. Areas")
    print("9. Salir")
def suma(lista):
    suma=0
    for numero in lista:
        suma= suma+numero
    return suma
def resta(x,y):
    return x-y                            #PRIMERAMENTE DEFINI CON LA OPCIÓN "def" LAS OPERACIONES QUE VA A TENER MI MENU
def multiplicacion(lista):                  #OBVIAMENTE VOY A IR INCLUYENDO MAS OPCIONES, AHORITA PUSE LO PRINCIPAL
    multiplicacion=1
    for numero in lista:
        multiplicacion= multiplicacion*numero
    return multiplicacion
def division(x,y):
    return x/y
def promedio (lista):
    suma=0
    for numero in lista:                  #para el promedio ya inclui listas pidiendo los datos despues
        suma= suma+numero
    return suma/len(lista)
def raiz(x):
    return x**.5
def formula_general(a,b,c):
    return (-b+math.sqrt(b**2-(4*a*c)))/(2*a)  #para usar la formula general defini dos variables
def formula_general2(a,b,c):                    #para que una se use la resta y otra la suma
    return (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
def menu_areas():
    print("**Menu de areas**")
    print("8.1 Area de cuadrado")
    print("8.2 Area de triangulo")
    print("8.3 Area de circulo")
    print("8.4 Area de rombo")
    print("8.5 Area de trapecio")
    print("8.6 Volver al menu principal")
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
    menu()
    opc=input("Ingrese una opción\n")  #para esta parte, tuve que investigar en opciones externas#y encontre la opción "opc" para que pudiera dar opciones
    if opc=="1":
        lista=[]
        while (True):
            limite=int(input("Ingrese numero de digitos que usara:"))
            for i in range(limite):   
                numero=float(input("Ingresar numeros a sumar:")) 
                lista.append(numero)      
            print(f"La suma es {suma(lista)}")
            break 
    elif opc=="2":
        x=float(input("Da el número al que se va a restar: \n"))
        y=float(input("Da el número que se le va a restar al primero: \n"))
        print(f"La resta de {x} menos {y} es: {resta(x,y)}")   #en esta parte ya inclui los condicionales para cada opción
    elif opc=="3":                            #y según la opción que daba, ponia una función ya definida
        lista=[]
        while (True):
            limite=int(input("Ingrese numero de digitos que usara:"))
            for i in range(limite):   
                numero=float(input("Ingresar numeros a sumar:")) 
                lista.append(numero)      
            print(f"La multiplicacion es {multiplicacion(lista)}")
            break 
    elif opc=="4":
        x=float(input("Da el número al que se le va a divir: \n"))
        y=float(input("Da el número por el que se va a dividr: \n"))
        if y==0:                                #hice lo que recomendo y puse que no se pudiera dividir entre 0
            print("No es posible\n")
        else:
            print(f"La división entre {x} y {y} da: {division(x,y)}")
    elif opc=="5":
        lista=[]
        while (True):
            limite=int(input("Ingrese numero de digitos que usara:"))
            for i in range(limite):    #use un for para que el usuario ponga el numero de digitos que quiere usar
                numero=float(input("Ingresar numeros a promediar:")) 
                lista.append(numero)      #para promediar use un ciclo while para que el usuario ponga los numeros que quiera y para eso tambien use un append para añdir numeros a la lista
            print(f"El promedio es {promedio(lista)}")
            break
    elif opc=="6":
        x=float(input("Dame el valor al que se le sacara raiz: \n"))
        if x<0:
            print("No es posible")
        else:
            print(f"La raiz de {x} es: {raiz(x)}")
    elif opc=="7":
        a=float(input("Dame el coeficiente de la variable cuadratica: \n"))
        b=float(input("Dame el coeficiente de la variable lineal: \n"))
        c=float(input("Dame el termino independientes: \n"))
        if ((b**2)-4*a*c) < 0:                                   #use un "if" para que cuando de negativo dentro de la raiz no se haga
            print("No existe porque no hay raices negativas\n")
        else:
            print(f"La formula general da como x1= {formula_general(a,b,c)} y x2= {formula_general2(a,b,c)}")
    elif opc=="8":
        while True:                 #inclui un segundo menu para que me diera las opciones de areas
            menu_areas()
            opc=input("Ingrese una opción de area\n")
            if opc=="7.1":
                x=float(input("Dame la base del cuadrado: \n"))
                y=float(input("Dame la altura del cuadrado: \n"))
                print(f"El area del cuadrado es: {area_cuadrado(x,y)}")
            elif opc=="7.2":
                x=float(input("Dame la base del triangulo: \n"))
                y=float(input("Dame la altura del triangulo: \n"))
                print(f"El area del triangulo es: {area_triangulo(x,y)}")
            elif opc=="7.3":                                                #puse todo lo que se haria en este menu
                x=float(input("Dame el radio del circulo: \n"))
                print(f"El area del circulo es: {area_circulo(x)}")
            elif opc=="7.4":
                x=float(input("Dame el diametro mayor del rombo: \n"))
                y=float(input("Dame el diametro menor del rombo: \n"))
                print(f"El area del rombo es: {area_rombo(x,y)}")
            elif opc=="7.5":
                x=float(input("Dame la base mayor del trapecio: \n"))
                y=float(input("Dame la base menor del trapecio: \n"))
                z=float(input("Dame la altura del trapecio: \n"))
                print(f"El area del trapecio es: {area_trapecio(x,y,z)}")
            elif opc=="7.6":                                       #use un "break" para poder voler al menu principal
                break      
    elif opc=="9":                   #inclui la opción de salir para que fuera más fácil de usar
        exit()                  #inclui las opciones más básicas, pero ire poniendo opciones mas complejas
