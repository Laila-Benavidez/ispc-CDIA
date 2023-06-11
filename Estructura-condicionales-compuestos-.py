
"""
print("ESTRUCTURAS CONDICIONALES COMPUESTOS")
print("----------------------------------------")
print("Ejercicio 1: Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.")

a=int(input("Ingrese la medida del lado A: "))
b=int(input("Ingrese la medida del lado B: "))
c=int(input("Ingrese la medida del lado C: "))

if a==b and a==c:
    print("El triangulo es equilatero")
elif a==b or a==c or b==c:
    print("El triangulo es isoceles")
else:
    print("El triangulo es escaleno")



print("----------------------------------------")
print("Ejercicio 2: Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago: • Contado (1): se aplica un descuento del 10 al importe • Tarjeta (2): se aplica un interés de 10% • Débito (3): se aplica un descuento del 5% Mostrar el importe, el descuento o interés y el importe total.")
print("----------------------------------------")

monto= float(input("Ingrese por favor el monto total a pagar: "))

while True:
    print("Seleccione que medio de pago desea utilizar")
    print("1. Contado")
    print("2. Tarjeta de credito")
    print("3. Tarjeta de debito")
    print("4. Salir ")
    opcion = input("Seleccione alguna de las opciones marcando 1,2,3 o 4 para salir ")
    
    if opcion=="1":
        print("El pago al contado tiene descuento del 10%")
        descuento= 0.1*monto
        print(F"El monto a pagar es {monto-descuento} y el descuento es de {descuento}")
        print("Muchas gracias por su compra")
        break

    elif opcion=="2":
        print("El pago con tarjeta de credito tiene un recardo del 10%")
        recargo=monto*0.1
        print(F"El monto a pagar es {monto+recargo} y el recargo es del {recargo}")
        print("Muchas gracias por su compra")
        break
    
    elif opcion=="3":
         print("El pago con tarjeta de debito tiene descuento del 5%")
         descuento= 0.05*monto
         print(F"El monto a pagar es {monto-descuento} y el descuento es de {descuento}")
         print("Muchas gracias por su compra")
         break

    elif opcion=="4":
        print("Muchas gracias, que tenga un buen dia")
        break

    else:
        print("La opcion ingresada no es correcta. Intente nuevamente")
        continue
    

print("----------------------------------------")
print("Ejercicio 3: Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.")

print("----------------------------------------")

num1=int(input("Ingrese por favor el primer numero: "))
num2=int(input("Ingrese por favor el segundo numero: "))
num3=int(input("Ingrese por favor el tercer numero: "))

if num1>num2 and num1>num3:
    print(F"El primer numero, {num1}, es el mayor de los numeros")
    if num1 % 2 == 0:
        print("El número es par.")
    else:
        print("Este numero es impar.")

elif num2>num1 and num2>num3:
    print(F"El segundo numero, { num2 }, es el mayor de los numeros")
    if num2 % 2 == 0:
        print("Este numero es par.")
    else:
        print("Este numero es impar.")

elif num3>num1 and num3>num2:
    print(F"El tercer numero, { num3 }, es el mayor de los numeros")
    if num3 % 2 == 0:
        print("El número mayor es par.")
    else:
        print("El número mayor es impar.")

elif (num1==num2 and num1==num3):
    print("Los tres numeros son iguales")

else:
    print("La opcion ingresada es incorrecta o dos de los numeros son iguales")



print("----------------------------------------")

print("Ejercicio 4: Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.")

print("----------------------------------------")

numero=int(input("Ingresa un numero del 1-7, para saber que dia de la semana corresponde: "))

while True:
    if numero == 1:
        print("El número corresponde al día Lunes.")
    elif numero == 2:
        print("El número corresponde al día Martes.")
    elif numero == 3:
        print("El número corresponde al día Miércoles.")
    elif numero == 4:
        print("El número corresponde al día Jueves.")
    elif numero == 5:
        print("El número corresponde al día Viernes.")
    elif numero == 6:
        print("El número corresponde al día Sábado.")
    elif numero == 7:
        print("El número corresponde al día Domingo.")
    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 7.")
    
    opcion = input("¿Desea ingresar otro número?: ")
    if opcion!= 'si':
        print("Que tengas un buen dia")
        break

"""
print("----------------------------------------")

print("Ejercicio 4: Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.")

print("----------------------------------------")

numero=int(input("Ingresa un numero del 1-12, para saber el mes corresponde: "))

while True:
    if numero == 1:
        print("El número corresponde al mes de enero.")
    elif numero == 2:
        print("El número corresponde al mes de febrero.")
    elif numero == 3:
        print("El número corresponde al mes de marzo.")
    elif numero == 4:
        print("El número corresponde al mes de abril.")
    elif numero == 5:
        print("El número corresponde al mes de mayo.")
    elif numero == 6:
        print("El número corresponde al mes de junio.")
    elif numero == 7:
        print("El número corresponde al mes de julio.")
    elif numero == 8:
        print("El número corresponde al mes de agosto.")
    elif numero == 9:
        print("El número corresponde al mes de septiembre.")
    elif numero == 10:
        print("El número corresponde al mes de octubre.")
    elif numero == 11:
        print("El número corresponde al mes de noviembre.")
    elif numero == 12:
        print("El número corresponde al mes de diciembre.")
    else:
        print("Número inválido. Por favor, ingrese un número del 1 al 12.")
    
    opcion = input("¿Desea ingresar otro número?: ")
    if opcion!= 'si':
        print("Que tengas un buen dia")
        break