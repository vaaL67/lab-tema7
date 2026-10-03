import math


def es_primo(numero):
    """Devuelve True si 'numero' es primo."""
    if numero < 2:
        return False
    limite = math.isqrt(numero)
    return all(numero % divisor != 0 for divisor in range(2, limite + 1))
