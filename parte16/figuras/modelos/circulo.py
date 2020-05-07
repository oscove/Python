from .figura import Figura
from math import pi

class Circulo(Figura):
    def __init__(self, color_fondo, color_borde, radio):
        super().__init__(color_fondo, color_borde)

        self.radio = radio
    
    def dibujar(self):
        print(f'Se está dibujando el círculo que tiene radio {self.radio}.')
    
    def area(self):
        resultado = pi * self.radio ** 2
