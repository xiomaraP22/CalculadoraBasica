def calcular(operacion, a, b):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: división por cero"
    else:
        return "Operación inválida"

def main():
    print("Calculadora refactorizada")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")

    op = input("Operación: ").lower()
    try:
        x = float(input("Primer número: "))
        y = float(input("Segundo número: "))
        resultado = calcular(op, x, y)
        print("Resultado:", resultado)
    except ValueError:
        print("Error: entrada inválida")

if __name__ == "__main__":
    main()
