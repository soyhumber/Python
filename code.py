from calculadora import *

def esnumero(candidato):
    valido=True
    for caracter in candidato :
        if caracter in '0123456789':
            continue
        else :
            valido=False
            break
    return valido

print("Bienvenido a la calculadora")
nombre = input("Dígame su nombre: ")
apellido = input(f"Gracias {nombre}, por favor tambien su apellido : ")
print(f"Gracias {nombre} {apellido}.")
operacion=input(f"{nombre} Indique la operación que quiere realizar (+, -, *, /): ")
for operador in operacion:
    if operador == "+" or operador == "-" or operador == "*" or operador == "/":
        # Si aquí agregaba un  "continue" me sacaba por qué?
        oper1=input("Indique el primer número: ")
        oper2=input("Indique el segundo número: ")
        if esnumero(oper1) and esnumero(oper2) :
            oper1 = int(oper1)
            oper2 = int(oper2)
        if operacion == "+" :
            print("El restultado de la suma es: ")
            print(suma(oper1,oper2))
        if operacion == "-" :
            print("El restultado de la resta es: ")
            print(resta(oper1, oper2))
        if operacion == "*" :
            print("El restultado de la multiplicación es: ")
            print(multiplicacion(oper1, oper2))
        if operacion == "/" :
            print("El restultado de la división es: ")
            print(division(oper1, oper2))
    else :
        print("Error! Eso no es una operación válida!")
