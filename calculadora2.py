import math
import os
os.system('cls')
# menu de las opciones de la calculadora
menu = """
Menu de la Calculadora
1- Suma
2- Resta 
3- Multiplicacion
4- Division
5- verificacion de numeros primos
6- validacion de numero palindromo
7-salir
"""

seleccion = True
while seleccion == True:
    print(menu)
    seleccion = int(input("Seleccione un valor: "))
    if seleccion is 1:
        val1 = (input("Ingrese un número: "))
        val2 = (input("Ingrese un número: "))
        print("El resultado es: ", int(val1) + int(val2))
    elif seleccion is 2:
        val1 = (input("Ingrese un número: "))
        val2 = (input("Ingrese un número: "))
        print(int(val1) - int(val2))
    elif seleccion is 3:
        val1 = (input("Ingrese un número: "))
        val2 = (input("Ingrese un número: "))
        print(int(val1) * int(val2))
    elif seleccion is 4:
        val1 = (input("Ingrese un número: "))
        val2 = (input("Ingrese un número: "))
        print(int(val1) / int(val2))
    elif seleccion is 5:
        numero = (input("Ingrese un número: "))
        validacion1 = 1
        validacion2 = 0
        while validacion1 <= int(numero):
            if int(numero) % validacion1 == 0:
                validacion2 = validacion2 + 1
            validacion1 = validacion1 + 1
            if validacion2 == 2:
                print("EL numero", numero, "Es primo")
            else:

                print("EL numero", numero, "no es primo")

    elif seleccion is 6:
        # leer la entrada como una cadena y luego simplemente buscar palíndromo.
        numero = input("Enter a number")
        if numero == numero[::-1]:
            print("El numero es palindromo")
        else:
            print("No el numero no es palindromo")
    else:
        print("Se ha salido exitosamente")