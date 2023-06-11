

print("Estructura condicionales simples")

print("----------------------------------------")
print("Ejercicio 1: Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.")

letra1= input("Ingrese por favor una letra ")
letra2= input("Ingrese por favor otra letra ")

if letra1 == letra2:
    print("Las dos letras son iguales")
else:
    print(F"Las dos letras ingresadas {letra1, letra2} son diferentes")

print("----------------------------------------")
print("Ejercicio 2: Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.")

palabra1= input("Ingrese por favor una palabra ")
palabra2= input("Ingrese por favor otra palabra para ser comparada ")

if palabra1 == palabra2:
    print("Las dos palabras son iguales")
else:
    print(F"Las dos palabras ingresadas {palabra1, palabra2} son diferentes")


print("----------------------------------------")
print("Ejercicio 3: Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.")

genero=input("Ingrese por favor su genero, F para femenino, M para masculino, asi indicarle la mesa donde debe votar: ")

if genero== "f":
    print("Por favor diríjase a la mesas pares, donde votan las mujeres ")
elif genero== "m":
    print("Por favor dirijase a las mesas impares, donde votan los hombres")
else:
    print("El valor ingresado no corresponde a masculino o femenino. Intente nuevamente")


print("----------------------------------------")
print("Ejercicio 4: Realice un programa que lea dos números y diga cuál es el mayor.")

num1=int(input("Ingrese por favor un numero "))
num2=int(input("Ingrese por favor otro numero "))

if num1<num2:
    print(F"El primer numero ingresado: {num1} es menor que el segundo numero:  {num2} ")
elif num1>num2:
    print(F"El primer numero ingresado: {num1} es mayor que el segundo numero:  {num2} ")
else:
    print(F"Los dos numeros ingresados {num1, num2} son iguales")


print("----------------------------------------")
print("Ejercicio 5: Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.")

print("Por favor eliga que operacion desea realizar ")
valorDOlar=480

while True:
    print("1. Pesos a Dólares")
    print("2. Dólares a Pesos")
    print("3. Salir")
    opcion = input("Seleccione una de las tres opciones (1, 2 o 3): ")

    if opcion == "1":
        cantidadPesos= float(input("Ingrese la cantidad en pesos: "))
        conversionP_D= cantidadPesos/valorDOlar 
        print(f"{cantidadPesos} pesos equivale a {conversionP_D} dólares.")

    elif opcion == "2":
        cantidadDolar = float(input("Ingrese la cantidad en dólares: "))
        conversionD_P= cantidadPesos*cantidadDolar
        print(f"{cantidadDolar} dólares equivale a {conversionD_P} pesos.")

    elif opcion=="3":
        print("Gracias por utilizar nuestro servicio que tenga un buen día")
        break
        
    else:
        print("Opción inválida. Selecciones una opcion valida.")
        continue

print("----------------------------------------")
print("Ejercicio 6:Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.")

edad=int(input("Ingrese por favor su edad: "))

if edad>=18:
    print("Usted es mayor de edad, por ende puede votar ")
elif edad<18:
    print("Usted es menor de edad, por ende no puede votar")
else:
    print("La opcion ingresada no es correcta")

