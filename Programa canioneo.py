# Librerías
from numpy import * 
import pandas as pd

# Entrada de datos

LongCasing = float(input("Ingrese la longitud del casing en pies: "))
DiamCasing = float(input("Ingrese el diámetro del casing en pulgadas: "))
ProfAltaLiner = float(input("Ingrese la profundidad de la parte superior del liner en pies: "))
ProfBajaLiner = float(input("Ingrese la profundidad de la parte inferior del liner en pies: "))
DiamLiner = float(input("Ingrese el diámetro del liner en pulgadas: "))
PresReservorio = float(input("Ingrese la presión del reservorio en Psi: "))
UnderBalance = float(input("Ingrese el UnderBalance en Psi: "))
CaudalBomba = float(input("Ingrese el caudal de la bomba en Bls/D: "))
AlturaCanon = float(input("Ingrese la altura a la que se cañonea en pies: "))

# Cálculos que se realizan para Tiempo y Volumen

PresHidrostatica = PresReservorio - UnderBalance
AlturaHidrostatica = PresHidrostatica / (0.052 * 8.33)

NivelEfectivo = AlturaCanon - AlturaHidrostatica
if NivelEfectivo < ProfAltaLiner:
    volumen = pi * NivelEfectivo * ((DiamCasing / 24) ** 2 - 0.021267)
    volumen = volumen / 5.615
    tiempo = volumen * 1440 / CaudalBomba
    print("Se necesitan ", tiempo, " minutos para extraer ", volumen, " barriles de volumen del tubo")
else:
    volCasing = (pi * ProfAltaLiner * (DiamCasing / 24) ** 2)
    volLiner = pi * (NivelEfectivo - ProfAltaLiner) * ((DiamLiner / 24) ** 2)
    volPozo = pi * NivelEfectivo * (0.021267)
    volumen = volCasing + volLiner - volPozo
    volumen = volumen / 5.615
    tiempo = volumen * 1440 / CaudalBomba
    print("Se necesitan ", round(tiempo, 2), " minutos para extraer ", round(volumen, 2), " barriles de volumen de la tubería")
