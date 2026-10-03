"""Figuras geométricas con SRP y OCP."""
import math
from abc import ABC, abstractmethod


class Figura(ABC):
    """Abstracción: toda figura sabe calcular su área."""

    nombre = "figura"

    @abstractmethod
    def area(self):
        ...


class Circulo(Figura):
    nombre = "círculo"

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    nombre = "rectángulo"

    def __init__(self, base, altura):
        self.base, self.altura = base, altura

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    nombre = "triángulo"

    def __init__(self, base, altura):
        self.base, self.altura = base, altura

    def area(self):
        return self.base * self.altura / 2


class CalculadoraAreas:
    """SRP: solo suma/calcula áreas; no sabe nada de cada figura."""

    def area_total(self, figuras):
        return sum(f.area() for f in figuras)


class ReporteAreas:
    """SRP: solo presenta resultados."""

    def mostrar(self, figuras):
        for f in figuras:
            print(f"Área del {f.nombre}: {f.area():.2f}")
