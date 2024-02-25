# Importación de librerías necesarias
from numpy import * 
import pandas as pd
from prettytable import PrettyTable

# Creación de la tabla
miTabla = PrettyTable()

# Adición de columnas a la tabla
miTabla.field_names = ["ID","Compuesto", "Tipo de Fluido", "Concentración en ppm"]

# Adición de datos a la tabla
miTabla.add_row([1, "Floculante", "Agua", "50"])
miTabla.add_row([2, "Biocida", "Agua", "500-1000"])
miTabla.add_row([3, "Antiescala", "Agua", "30"])
miTabla.add_row([4, "Clarificador", "Agua", "50"])
miTabla.add_row([5, "Secuestrante de oxígeno", "Fluido", "10"])
miTabla.add_row([6, "Demulsificante", "Aceite", "35"])

# Definición del formato de las líneas
miTabla.horizontal_char = '-'
miTabla.vertical_char = '|'
miTabla.junction_char = '+'

# Impresión de la tabla
print(miTabla)

# Entrada de datos

CaudalFluido = float(input("Ingrese el caudal del fluido en BFPD: "))
Agua = float(input("Ingrese el porcentaje de agua(BSW)(fracción): "))
Diametro = float(input("Ingrese el diámetro del flow line en pies: "))
Longitud = float(input("Ingrese la longitud del flow line en pies: "))
Seleccion = input("Seleccione un compuesto en orden de la tabla(1-6): ")
ppm = float(input("Ingrese las partes por millón(ppm): "))
TiempoBache = float(input("Ingrese el tiempo del bache (horas): "))

# Cálculos

BWPD = CaudalFluido*Agua
BOPD = CaudalFluido-BWPD

# Solución
def opcion_1():
  qw=(BWPD*TiempoBache)/24
  gal=qw*42
  res=(gal*ppm)/(1*10**6-ppm)
  print("Se deben utilizar ",res," galones de Floculante al enviar al PIG")

def opcion_2():
  qw=(BWPD*TiempoBache)/24
  gal=qw*42
  res=(gal*ppm)/(1*10**6-ppm)
  print("Se deben utilizar ",res," galones de Biocida al enviar al PIG")

def opcion_3():
  qw=(BWPD*TiempoBache)/24
  gal=qw*42
  res=(gal*ppm)/(1*10**6-ppm)
  print("Se deben utilizar ",res," galones de Antiescala al enviar al PIG")

def opcion_4():
  qw=(BWPD*TiempoBache)/24
  gal=qw*42
  res=(gal*ppm)/(1*10**6-ppm)
  print("Se deben utilizar ",res," galones de Clarificador al enviar al PIG")

def opcion_5():
  qw=(CaudalFluido*TiempoBache)/24
  gal=qw*42
  res=(gal*ppm)/(1*10**6-ppm)
  print("Se deben utilizar ",res," galones de Secuestrante de oxígeno al enviar al PIG")

def opcion_6():
  qw=(BOPD*TiempoBache)/24
  gal=qw*42
  res=(gal*ppm)/(1*10**6-ppm)
  print("Se deben utilizar ",res," galones de Demulsificante al enviar al PIG")

def seleccionar_opcion(opcion):
    opciones = {
        "1": opcion_1,
        "2": opcion_2,
        "3": opcion_3,
				"4": opcion_4,
        "5": opcion_5,
        "6": opcion_6
    }
    funcion = opciones.get(opcion, lambda: print("Opción no válida"))
    funcion()

opcion = Seleccion
seleccionar_opcion(opcion)


Q=CaudalFluido*2*5.615/1440
A=pi*Diametro**2/4
v=Q/A
print("El PIG llega con una velocidad de ",v," pies/min")
t=A*Longitud/(Q*60)
print("El PIG llega en ",t,"horas")
