

print("ESTRUCTURAS REPETITIVAS Y CONDICIONALES")

print("----------------------------------------")
print("Ejercicio 1: Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.")

while True:
    pares = 0
    sumatoria_pares = 0

    for i in range(1, 5):
        numero = int(input(f"Ingrese el número {i} de 4: "))

        if numero % 2 == 0:
            pares += 1
            sumatoria_pares += numero

    impares = 4 - pares

    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)
    print("Sumatoria de números pares:", sumatoria_pares)

    break


print("----------------------------------------")
print("Ejercicio 2: Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.")

while True:
    numeros = []

    for i in range(10):
        numero = float(input("Ingrese un número: "))
        numeros.append(numero)

    print("Números ingresados:", numeros)

    mayores_100 = 0
    menores_100 = 0
    maximo = max(numeros)
    minimo = min(numeros)

    for numero in numeros:
        if numero > 100:
            mayores_100 += 1
        else:
            menores_100 += 1

    print("Cantidad de números mayores a 100:", mayores_100)
    print("Cantidad de números menores a 100:", menores_100)
    print("Número máximo:", maximo)
    print("Número mínimo:", minimo)

    break

print("----------------------------------------")
print("Ejercicio 3: Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.")


contador_mujeres = 0
contador_varones = 0
contador_mayores = 0
contador_menores = 0

for i in range(15):
    edad = int(input("Ingrese la edad de la persona {}: ".format(i + 1)))
    sexo = input("Ingrese el sexo de la persona {}): ".format(i + 1))

    if sexo == "femenino" or sexo=="mujer":
        contador_mujeres += 1
    elif sexo == "masculino" or sexo=="varon":
        contador_varones += 1

    if edad >= 18:
        contador_mayores += 1
    else:
        contador_menores += 1

print("Cantidad de mujeres:", contador_mujeres)
print("Cantidad de varones:", contador_varones)
print("Cantidad de mayores de edad:", contador_mayores)
print("Cantidad de menores de edad:", contador_menores)


print("----------------------------------------")
print("Ejercicio 4:Leer 10 números y mostrar solamente los números positivos, y su sumatoria.")

sumatoria_positivos = 0

for i in range(10):
    numero = float(input("Ingrese un número: "))
    if numero > 0:
        sumatoria_positivos += numero
    elif numero<0:
        print("El numero ingresado es negativo")

print("La sumatoria de los números positivos es:", sumatoria_positivos)



print("----------------------------------------")
print("Ejercicio 5: Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.")

for i in range(15):
    numero = float(input("Ingrese un número negativo: "))    
    if numero < 0:
        numero = abs(numero)
        
        print("Número convertido a positivo es: ", numero)
    else:
        print("El número ingresado no es negativo.")