from figuras_solid import Circulo, Rectangulo, Triangulo, CalculadoraAreas, ReporteAreas
from trapecio import Trapecio

figuras = [Circulo(5), Rectangulo(4, 6), Triangulo(3, 8), Trapecio(10, 6, 4)]
ReporteAreas().mostrar(figuras)
print(f"Área total: {CalculadoraAreas().area_total(figuras):.2f}")
