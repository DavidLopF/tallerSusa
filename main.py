# #Define dos variables, nombre y edad, e imprime un mensaje de saludo que las utilice.
name="Valentina"
edad=22

print("Hola mi nombre es "+name+" y tengo "+str(edad)+" años")

print("______________________________________________________________")


# #Calcula y muestra el área de un círculo. Pide al usuario que ingrese el radio.

radio=float(input("Ingrese el radio del circulo: "))
area=3.1416*radio**2
print("El area del circulo es: "+str(area))

print("______________________________________________________________")
#Escribe una función calcular_promedio que tome una lista de números como argumento y devuelva su promedio.

def calcular_promedio(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma/len(lista)
lista=[15, 20, 25, 30, 35, 24, 12, 16]

print("El promedio de la lista es: "+str(calcular_promedio(lista)))

#Crea una lista de números y utiliza un bucle for para mostrar los números mayores que 10.

lista=[15, 20, 25, 30, 35, 24, 12, 16]

for i in lista:
    if i>10:
        print(i)


#Define un diccionario que almacene los precios de tres productos diferentes. Pide al usuario que ingrese el nombre de un producto y muestra su precio.

productos={"arroz": 2000, "frijoles": 3000, "papa": 1000}
productocliente = input("Ingrese el nombre del producto: ")
precio=productos[productocliente]
print("El precio del "+ productocliente+" es: "+str(precio))


#Escribe una función es_primo que determine si un número dado es primo o no.

def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero=int(input("Ingrese un numero: "))
if es_primo(numero):
    print("El numero es primo")
else:
    print("El numero no es primo")

#Crea una lista de nombres y utiliza un bucle while para imprimir cada nombre hasta que encuentres el nombre "Alex".
lista=["Valentina", "Santiago", "Alex", "Juan", "Maria"]

while lista:
    print(lista.pop(0))
    if lista[0]=="Alex":
        print("Se encontro el nombre Alex")
        break


#Escribe una función invertir_cadena que tome una cadena como argumento y devuelva la cadena invertida.
cadena="Hola mundo"
print(cadena[::-1])



#Crea una lista de números pares del 2 al 20 utilizando una comprensión de lista.

lista=[i for i in range(2, 21) if i%2==0]
print(lista)


#Escribe un programa que genere los primeros 
#términos de la serie de Fibonacci a discresión del usuario.

def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Ingrese el numero de terminos de la serie de Fibonacci: "))
for i in range(n):
    print(fibonacci(i))

#Escribe una función calcular_interes_simple que calcule el interés simple dado el principal, la tasa de interés y el tiempo en años.
def calcular_interes_simple(principal, tasa, tiempo):
    interessimple=principal*tasa*tiempo
    return interessimple

principal=float(input("Ingrese el principal: "))
tasa=float(input("Ingrese la tasa de interes: "))
tiempo=float(input("Ingrese el tiempo en años: "))
print("El interes simple es: "+str(calcular_interes_simple(principal, tasa, tiempo)))


#Crea una lista de precios de acciones. Utiliza una función para calcular el promedio de esos precios.

lista=[2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
def calcular_promedio(lista):
    sum=0
    for i in lista:
        sum+=i

    promedio=sum/len(lista)
    return promedio

print("la lista es:" + str(lista) + " y el promedio es: " + str(calcular_promedio(lista)))


#Escribe una función convertir_dolares_a_euros que tome una cantidad en dólares y la convierta a euros (usando una tasa de cambio fija).

def convertir_dolares_a_euros(dolares):
    euros=dolares*0.82
    return euros

dolares=float(input("Ingrese la cantidad de dolares: "))
print("La cantidad de dolares es: "+str(dolares)+" y en euros es: "+str(convertir_dolares_a_euros(dolares)))


#Crea una función calcular_factorial que calcule el factorial de un número dado.

def calcular_factorial(numero):
    factorial=1
    for i in range(1, numero+1):
        factorial*=i
    return factorial

#Define un diccionario que contenga los nombres y saldos de cuentas bancarias. Escribe una función que encuentre la cuenta con el saldo más alto.

diccionario={"Valentina": 1000000, "Santiago": 2000000, "Maria": 3000000, "Juan": 4000000}
def cuenta_mayor(diccionario):
    mayor=0
    for i in diccionario:
        if diccionario[i]>mayor:
            mayor=diccionario[i]
    return mayor

print("La cuenta con el saldo mayor es: "+str(cuenta_mayor(diccionario)))

#Escribe un programa que calcule e imprima los primeros 
 #números triangulares a discresión del usuario.

def calcular_numero_triangulares(n):
    for i in range(1, n+1):
        print(i*(i+1)//2)


#Crea una función calcular_descuento que calcule el precio final después de aplicar un descuento a un artículo.

def calcular_descuento(precio, descuento):
    preciofinal=precio-precio*descuento
    return preciofinal

precio=float(input("Ingrese el precio del articulo: "))
descuento=float(input("Ingrese el descuento: "))
print("El precio final es: "+str(calcular_descuento(precio, descuento)))


# Escribe una función que tome una lista de números y devuelva una nueva lista con solo los números pares.

def lista_pares(lista):
    listapares=[]
    for i in lista:
        if i%2==0:
            listapares.append(i)
    return listapares

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_pares(lista))



# Crea una lista de números y utiliza una función para encontrar el número más grande y el más pequeño.

def numero_mayor(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor

def numero_menor(lista):
    menor=lista[0]
    for i in lista:
        if i<menor:
            menor=i
    return menor

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("El numero mayor de la lista es: "+str(numero_mayor(lista)))
print("El numero menor de la lista es: "+str(numero_menor(lista)))



# Escribe un programa que genere e imprima los primeros 
#  términos de la secuencia de números de Pell a discresión del usuario.

def pell(n):
    if n==0 or n==1:
        return n
    else:
        return 2*pell(n-1)+pell(n-2)

n=int(input("Ingrese el numero de terminos de la secuencia de Pell: "))
for i in range(n):
    print(pell(i))


# Crea una función calcular_amortizacion que calcule la amortización de un préstamo a lo largo del tiempo.

def calcular_amortizacion(prestamo, tasa, tiempo):
    amortizacion=prestamo*tasa*tiempo
    return amortizacion

prestamo=float(input("Ingrese el prestamo: "))
tasa=float(input("Ingrese la tasa de interes: "))
tiempo=float(input("Ingrese el tiempo en años: "))
print("La amortizacion es: "+str(calcular_amortizacion(prestamo, tasa, tiempo)))


# Escribe un programa que determine si un número dado es un número perfecto o no.

def es_perfecto(numero):
    suma=0
    for i in range(1, numero):
        if numero%i==0:
            suma+=i
    if suma==numero:
        return True
    else:
        return False
    
numero=int(input("Ingrese un numero: "))
if es_perfecto(numero):
    print("El numero es perfecto")
else:
    print("El numero no es perfecto")

# Define un diccionario que almacene las tasas de interés para diferentes tipos de préstamos. Pide al usuario que ingrese un tipo de préstamo y muestra la tasa de interés correspondiente.

diccionario={"prestamo1": 0.1, "prestamo2": 0.2, "prestamo3": 0.3}
prestamo=input("Ingrese el tipo de prestamo: ")
print("La tasa de interes es: "+str(diccionario[prestamo])) 

# Escribe una función calcular_media_geometrica que calcule la media geométrica de una lista de números.

def calcular_media_geometrica(lista):
    producto=1
    for i in lista:
        producto*=i
    mediageometrica=producto**(1/len(lista))
    return mediageometrica

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("La media geometrica de la lista es: "+str(calcular_media_geometrica(lista)))

# Crea una lista de números y utiliza una función para encontrar el segundo número más grande.

def segundo_mayor(lista):
    mayor=0
    segundo=0
    for i in lista:
        if i>mayor:
            segundo=mayor
            mayor=i
    return segundo

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("El segundo numero mayor de la lista es: "+str(segundo_mayor(lista)))


# Escribe un programa que calcule e imprima los primeros 
#  números de la serie de los números de Lucas a discresión del usuario.

def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

n=int(input("Ingrese el numero de terminos de la serie de Lucas: "))
for i in range(n):
    print(lucas(i))


# Crea una función calcular_cuota_mensual que calcule la cuota mensual de un préstamo hipotecario.

def calcular_cuota_mensual(prestamo, tasa, tiempo):
    cuotamensual=prestamo*tasa*tiempo
    return cuotamensual

prestamo=float(input("Ingrese el prestamo: "))
tasa=float(input("Ingrese la tasa de interes: "))
tiempo=float(input("Ingrese el tiempo en años: "))
print("La cuota mensual es: "+str(calcular_cuota_mensual(prestamo, tasa, tiempo)))


# Escribe una función que determine si un número es un número de Armstrong (un número de n dígitos que es igual a la suma de sus dígitos elevados a la n).

def es_armstrong(numero):
    suma=0
    for i in str(numero):
        suma+=int(i)**len(str(numero))
    if suma==numero:
        return True
    else:
        return False

numero=int(input("Ingrese un numero: "))
if es_armstrong(numero):
    print("El numero es de Armstrong")
else:
    print("El numero no es de Armstrong")

# Define un diccionario que almacene los símbolos de moneda y sus respectivos códigos. Escribe un programa que convierta una cantidad de dinero de una moneda a otra.

diccionario={"peso": 1, "dolar": 0.00027, "euro": 0.00022}
moneda1=input("Ingrese la moneda de origen: ")
moneda2=input("Ingrese la moneda de destino: ")
cantidad=float(input("Ingrese la cantidad: "))
print("La cantidad en "+moneda2+" es: "+str(diccionario[moneda1]*cantidad/diccionario[moneda2]))
