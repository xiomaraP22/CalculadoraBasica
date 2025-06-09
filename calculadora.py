def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

print("Calculadora básica")
print("Operaciones: suma, resta, multiplicacion, division")

op = input("Elige operación: ")
x = float(input("Ingresa el primer número: "))
y = float(input("Ingresa el segundo número: "))

if op == "suma":
    print("Resultado:", suma(x, y))
elif op == "resta":
    print("Resultado:", resta(x, y))
elif op == "multiplicacion":
    print("Resultado:", multiplicacion(x, y))
elif op == "division":
    print("Resultado:", division(x, y))
else:
    print("Operación inválida")
