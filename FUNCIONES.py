
#FUNCIONES

#Ejercicio 1: Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección. 
"""
def saludo (aula1, aula2, aula3):
    print(F"Hola aula {aula1}, ¿Que tal?, muchos éxitos en el examen")
    print(F"Hola aula {aula2}, ¿Que tal?, van muy bien a seguir estudiando")
    print(F"Hola aula {aula3}, ¿Que tal?, sus notas van excelente sigan así")

saludo(4,7,3)

"""

#Ejercicio 2: A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos ejercicios trabajamos argumentos.
"""
def saludo (nombre1, nombre2, nombre3):
    print(F"Hola {nombre1}, ¿Que tal?, espero que tengas una excelente jornada")
    print(F"Hola {nombre2}, ¿Que tal?, exitos en la semana ")
    print(F"Hola {nombre3}, ¿Que tal?, tu desempeño va excelente sigan así")

saludo("Ana","Laura","Joaquin")
"""

#Ejercicio 3: Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar el resultado dos veces.
"""
def sumar(num1, num2, num3):
    print(F"La suma de {num1} y {num2} es {num1 + num2}")
    print(F"La suma de {num3} y {num2} es {num3 + num2}")

sumar(35,15,1)

""" 


#Ejercicio 4 Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE. 

"""
num1= int(input("Ingrese por favor un numero: "))
num2= int(input("Ingrese por favor otro numero: "))

def comparar (num1, num2):
    if num1 == num2:
        print("Los numeros ingresados son iguales")
    else:
        print("Los numeros ingresados son diferentes ")

comparar(num1, num2)

"""

#Ejercicio 5: Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.

def sumayresta (num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    print(F"La suma de los numeros{num1} y {num1} es: {suma}")
    print(F"La resta de los numeros{num1} y {num1} es: {resta}")

sumayresta(15, 7)