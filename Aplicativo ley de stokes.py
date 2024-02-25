import math

def calcular_diametro_gota(gravidad_api, viscosidad_petroleo_si, Vw, Vo):
    # Constantes
    densidad_agua = 1000  # kg/m^3 (densidad del agua)
    aceleracion_gravedad = 9.81  # m/s^2 (aceleración debida a la gravedad)

    # Convertir gravedad API a densidad del petróleo
    densidad_petroleo = 141.5 / (gravidad_api + 131.5)

    # Calcular la densidad aparente del agua
    densidad_aparente_agua = densidad_agua / (1 - indice_emulsion)

    # Calcular la densidad aparente del petróleo
    densidad_aparente_petroleo = densidad_petroleo * (1 - indice_emulsion)

    # Calcular la viscosidad aparente del fluido
    viscosidad_aparente = viscosidad_petroleo_si * (1 + 2.5 * indice_emulsion)

    # Calcular el radio de la gota de agua usando la ley de Stokes
    radio = ((9 * viscosidad_aparente) / (2 * aceleracion_gravedad * (densidad_aparente_petroleo - densidad_aparente_agua))) ** (1/2)

    # Calcular el diámetro de la gota de agua
    diametro = 2 * radio
    return diametro

def calcular_indice_emulsion(Vw, Vo):
    indice_emulsion = (Vw / (Vw + Vo)) * 100
    return indice_emulsion

# Pedir al usuario la gravedad API del petróleo, la viscosidad del petróleo y los volúmenes de agua y petróleo
gravidad_api = float(input("Introduce la gravedad API del petróleo: "))
viscosidad_petroleo = float(input("Introduce la viscosidad del petróleo en centipoise: "))
Vw = float(input("Introduce el volumen de agua (en litros): "))
Vo = float(input("Introduce el volumen de petróleo (en litros): "))

# Convertir la viscosidad del petróleo a unidades del SI (m^2/s)
viscosidad_petroleo_si = viscosidad_petroleo * 0.001

# Calcular el índice de emulsión
indice_emulsion = calcular_indice_emulsion(Vw, Vo)

# Calcular el diámetro de la gota de agua
diametro_gota = calcular_diametro_gota(gravidad_api, viscosidad_petroleo_si, Vw, Vo)

# Mostrar el resultado
print("El diámetro de la gota de agua es:", diametro_gota*100, "cm")
