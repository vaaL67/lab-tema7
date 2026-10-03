from figuras_solid import Circulo, Rectangulo, Triangulo, CalculadoraAreas, ReporteAreas

figuras = [Circulo(5), Rectangulo(4, 6), Triangulo(3, 8)]
ReporteAreas().mostrar(figuras)
print(f"Área total: {CalculadoraAreas().area_total(figuras):.2f}")
