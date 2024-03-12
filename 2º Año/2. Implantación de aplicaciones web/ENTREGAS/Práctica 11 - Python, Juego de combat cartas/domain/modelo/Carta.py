from dataclasses import dataclass, field
from enum import Enum


@dataclass()
class Carta:
    
    """ esto es un comentario de la clase"""
    class PALOS(Enum):
        OROS = 0
        ESPADAS = 1
        COPAS = 2
        BASTOS = 3
        
    class NUMEROS(Enum):
        AS = 1
        DOS = 2
        TRES = 3
        CUATRO = 4
        CINCO = 5
        SEIS = 6
        SIETE = 7
        SOTA = 10
        CABALLO = 11
        REY = 12
    
    valor : NUMEROS
    palo : PALOS

    def __init__(self, valor : NUMEROS, palo : PALOS):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor.name} de {self.palo.name}"