from figuras_solid import Figura


class Trapecio(Figura):
    nombre = "trapecio"

    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor, self.base_menor, self.altura = base_mayor, base_menor, altura

    def area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2
