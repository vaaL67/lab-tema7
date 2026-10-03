# Versión inicial (sin refactorizar)
def calc(t, a, b=0):
    if t == "c":
        r = 3.14159 * a * a
        print("area circulo:", r)
        return r
    if t == "r":
        r = a * b
        print("area rectangulo:", r)
        return r
    if t == "t":
        r = a * b / 2
        print("area triangulo:", r)
        return r

calc("c", 5)
calc("r", 4, 6)
calc("t", 3, 8)
