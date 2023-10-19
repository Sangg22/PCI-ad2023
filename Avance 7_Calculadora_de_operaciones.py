'Proyecto de calculadora'
import math
#Libreria Math (Python). (n.d.). Stack Overflow En Español. 
# https://es.stackoverflow.com/questions/279147/libreria-math-python
PI=3.1416
#defini el menu completo de la calculador
def menu():
    print("**menu de calculadora**")
    print("1. sumar")
    print("2. restar")                  
    print("3. multiplicar")
    print("4. dividir")
    print("5. promedio")
    print("6. raiz_cuadrada")
    print("7. formula general")
    print("8. areas")
    print("9. salir")
def suma(lista):
#defini la suma con una lista para que agregue 
# los numeros que quiera
    suma=0
    for numero in lista:
        suma= suma+numero
    return suma
def resta(num1,num2):
#calcula la resta apartir de num1 y num2
    return num1-num2                         
def multiplicacion(lista):  
#defini la multiplicacion con una lista para que agregue
# los numeros que quiera multiplicar                
    multiplicacion=1
#defini multiplicacion como 1 para que no afecte
    for numero in lista:
        multiplicacion= multiplicacion*numero
    return multiplicacion
def division(num1,num2):
#calcula la division de num1 entre num2
    return num1/num2
def promedio (lista):
#el promedio lo hice igual con lista para que agregue numeros
    suma=0
    for numero in lista:                  
        suma= suma+numero
    return suma/len(lista)
#use len para que contara los datos y dividir
def raiz(num1):
#calcula raiz de num1
    return num1**.5
def formula_general(a,b,c):
#calcula raiz 1 a partir del a,b y c 
    return (-b+math.sqrt(b**2-(4*a*c)))/(2*a) 
def formula_general2(a,b,c):
#calcula raiz 1 a partir del a,b y c                     
    return (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
def menu_areas():
#defini un menu nuevo para separar las opciones de areas
    print("**menu de areas**")
    print("8.1 area de cuadrado")
    print("8.2 area de triangulo")
    print("8.3 area de circulo")
    print("8.4 area de rombo")
    print("8.5 area de trapecio")
    print("8.6 volver al menu principal")
def area_cuadrado(base,altura):
#calcula are_cuadrado con base y altura
    return base*altura
def area_triangulo(base,altura):
#calcula area_triangulo con base y altura
    return (base*altura)/2
def area_circulo(radio):
#calcula are_circulo con su radio
    return  PI*(radio**2)
def area_rombo(diametro_mayor,diametro_menor):
#calcula are_rombo con dimetro_mayor y diametro_menor
    return  ((diametro_mayor)*(diametro_menor))/2
def area_trapecio(base_mayor,base_menor,altura):
#calcula are_trapecio con base_mayor, base_menor y altura
    return ((base_mayor*base_menor)*altura)/2
#inserte while para que se creara un ciclo y 
# poder volver al menu y poder tener otra opción
while True:
    menu()
#para esta parte, tuve que investigar en opciones externasy 
# encontre la opción "opc" para que pudiera dar opciones
    opc=input("ingrese una opción\n")  
    if opc=="1":
        lista=[]
        while (True):
            limite=int(input("ingrese numero de digitos que usara:"))
            for i in range(limite):   
                numero=float(input("ingresar numeros a sumar:")) 
                lista.append(numero)      
            print(f"la suma es {suma(lista)}")
            break 
    elif opc=="2":
#solicitar los numeros para la resta
        num1=float(input("da el número al que se va a restar: \n"))
        num2=float(input
                   ("""da el número que se le va a restar al primero: \n"""))
        print(f"la resta de {num1} menos {num2} es: {resta(num1,num2)}")  
    elif opc=="3":
#crear lista para que pueda multiplicar los numeros que quiera
        lista=[]                            
        while (True):
            limite=int(input("ingrese numero de digitos que usara:"))
            for i in range(limite):   
                numero=float(input("ingresar numeros a multiplicar:")) 
                lista.append(numero)      
            print(f"la multiplicacion es {multiplicacion(lista)}")
            break 
#solicitaar numeros que se usaran en la division
    elif opc=="4":
        num1=float(input("da el número al que se le va a divir: \n"))
        num2=float(input("da el número por el que se va a dividr: \n"))
#hice lo que recomendo y puse que no se pudiera dividir entre 0
        if num2==0:                               
            print("no es posible\n")
        else:
            print(f"""la división entre {num1} y {num2} da: 
                  {division(num1,num2)}""")
    elif opc=="5":
        lista=[]
        while (True):
            limite=int(input("ingrese numero de digitos que usara:"))
 #use un for para que el usuario ponga el numero de digitos que quiere usar
            for i in range(limite):  
                numero=float(input("ingresar numeros a promediar:")) 
#para promediar use un ciclo while para que el usuario ponga los numeros que quiera
#  y para eso tambien use un append para añdir numeros a la lista
                lista.append(numero)      
            print(f"el promedio es {promedio(lista)}")
            break
    elif opc=="6":
#solicitar el numero para raiz
        num1=float(input("dame el valor al que se le sacara raiz: \n"))
#si el numero es menor que 0 imprimir que no es posible
        if num1<0:
            print("no es posible")
        else:
            print(f"la raiz de {num1} es: {raiz(num2)}")
    elif opc=="7":
#solicitar datos que se tienen en la ecuacion
        a=float(input("dame el coeficiente de la variable cuadratica: \n"))
        b=float(input("dame el coeficiente de la variable lineal: \n"))
        c=float(input("dame el termino independientes: \n"))
#use un "if" para que cuando de negativo dentro de la raiz no se haga
        if ((b**2)-4*a*c) < 0:                                   
            print("no existe porque no hay raices negativas\n")
        else:
            print(f"""la formula general da como x1= {formula_general(a,b,c)}
                   y x2= {formula_general2(a,b,c)}""")
    elif opc=="8":
        while True:
#inclui un segundo menu para que me diera las opciones de areas
            menu_areas()
            opc=input("ingrese una opción de area\n")
            if opc=="8.1":
#solicitar base y altura del cuadrado
                base=float(input("dame la base del cuadrado: \n"))
                altura=float(input("dame la altura del cuadrado: \n"))
                print(f"""el area del cuadrado es:
                       {area_cuadrado(base,altura)}""")
            elif opc=="8.2":
#solicitar base y altura del triangulo
                base=float(input("dame la base del triangulo: \n"))
                altura=float(input("dame la altura del triangulo: \n"))
                print(f"""el area del triangulo es: 
                      {area_triangulo(base,altura)}""")
            elif opc=="8.3":
#solicitar radio del circulo                                               
                radio=float(input("dame el radio del circulo: \n"))
                print(f"el area del circulo es: {area_circulo(radio)}")
            elif opc=="8.4":
#solicitar el diametro mayor y menor 
                diametro_mayor=float(input("dame el diametro mayor: \n"))
                diametro_menor=float(input("dame el diametro menor: \n"))
                print(f"""el area del rombo es: 
                      {area_rombo(diametro_mayor,diametro_menor)}""")
            elif opc=="8.5":
#solicitar la base mayor, menor y altura
                base_mayor=float(input("dame la base mayor: \n"))
                base_menor=float(input("dame la base menor: \n"))
                altura=float(input("dame la altura del trapecio: \n"))
                print(f"""el area del trapecio es: 
                      {area_trapecio(base_mayor,base_menor,altura)}""")
            elif opc=="8.6":
#use un "break" para poder voler al menu principal
                break      
#inclui la opción de salir para que fuera más fácil de usar
    elif opc=="9":                   
        exit()
