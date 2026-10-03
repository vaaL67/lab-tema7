"""Cálculo de áreas de figuras geométricas (versión refactorizada)."""
import math


def area_circulo(radio):
    return math.pi * radio ** 2


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return base * altura / 2


def mostrar_area(nombre_figura, area):
    print(f"Área del {nombre_figura}: {area:.2f}")


if __name__ == "__main__":
    mostrar_area("círculo", area_circulo(5))
    mostrar_area("rectángulo", area_rectangulo(4, 6))
    mostrar_area("triángulo", area_triangulo(3, 8))
