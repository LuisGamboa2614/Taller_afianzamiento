def f1():
    a = int(input("Escriba un número que no sea negativo: "))
    if a >= 0:
        b = a * a
        print(f"El número {a} al cuadrado es {b}")
    else:
        print("Debe ingresar un número no negativo.")


def f2():
    a = int(input("Escriba un número positivo: "))
    if a > 0:
        while a != 1:
            if a % 2 == 0:
                a = a // 2
            else:
                a = (3 * a) + 1
            print(a, end=" ")
        print()
    else:
        print("Debe ingresar un número positivo.")


def f3():
    a = 25
    b = 18.9
    c = 2022
    while a > b:
        a = a + a * 0.02
        b = b + b * 0.03
        c = c + 1
    print(f"En el año {c}, la población de B será mayor a la de A.")


def f4():
    a = 1
    b = 0
    c = 0
    while a != b:
        c = 1 + (2 ** b)
        b = b + 1
        print(c)
        if b > 10:
            break


def f6():
    print("Números impares del 1 al 1000:")
    a = 0
    while a < 1000:
        if a % 2 != 0:
            print(a)
        a = a + 1


def f7():
    a = int(input("Escriba un número mayor o igual a 2: "))
    if a >= 2:
        print("Números pares hasta", a)
        for i in range(2, a + 1, 2):
            print(i)
    else:
        print("Debe ingresar un número mayor o igual a 2.")


def factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado


def imprimir_factoriales(n):
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")


def f9():
    a = int(input("Ingrese un número entero: "))
    b = 2 ** a  # Usar ** en lugar de ^
    print(f"2 elevado a {a} es {b}")


def f10():
    a = int(input("Escriba el exponente: "))
    b = int(input("Escriba la base: "))
    c = b ** a  # ** es potencia en Python
    print(f"El resultado de {b}^{a} es {c}")


def f11():
    for i in range(1, 10):
        print(f"\nTabla del {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")


def main():
    print("=== MENÚ DE FUNCIONES ===")
    print("1. Cuadrado de un número")
    print("2. Secuencia de Collatz")
    print("3. Año en que B supera a A")
    print("4. Serie con potencias")
    print("6. Números impares hasta 1000")
    print("7. Números pares hasta n")
    print("8. Factoriales del 1 al n")
    print("9. Potencia de 2^n")
    print("10. Potencia base^exponente")
    print("11. Tablas de multiplicar del 1 al 9")

    opcion = int(input("\nSeleccione una función a ejecutar: "))

    if opcion == 1:
        f1()
    elif opcion == 2:
        f2()
    elif opcion == 3:
        f3()
    elif opcion == 4:
        f4()
    elif opcion == 6:
        f6()
    elif opcion == 7:
        f7()
    elif opcion == 8:
        n = int(input("Ingrese un número natural: "))
        imprimir_factoriales(n)
    elif opcion == 9:
        f9()
    elif opcion == 10:
        f10()
    elif opcion == 11:
        f11()
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()