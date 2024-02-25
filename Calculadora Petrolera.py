# Definiciones de conversiones
def convertir_volumen(valor, unidad_entrada, unidad_salida):
    # Convertir a metros cúbicos
    if unidad_entrada == 1: # acres-pies
        valor = valor * 1233.48
    elif unidad_entrada == 2: # pies cúbicos
        valor = valor * 0.0283168
    elif unidad_entrada == 3: # galones
        valor = valor * 0.00378541
    elif unidad_entrada == 4: # litros
        valor = valor * 0.001
    elif unidad_entrada == 5: # barriles
        valor = valor * 0.158987

    # Convertir a la unidad de salida
    if unidad_salida == 1: # acres-pies
        valor = valor / 1233.48
    elif unidad_salida == 2: # pies cúbicos
        valor = valor / 0.0283168
    elif unidad_salida == 3: # galones
        valor = valor / 0.00378541
    elif unidad_salida == 4: # litros
        valor = valor / 0.001
    elif unidad_salida == 5: # barriles
        valor = valor / 0.158987

    return valor

def convertir_presion(valor, unidad_entrada, unidad_salida):
    # Convertir a pascales
    if unidad_entrada == 1: # bar
        valor = valor * 100000
    elif unidad_entrada == 2: # psi
        valor = valor * 6894.76
    elif unidad_entrada == 3: # atm
        valor = valor * 101325
    elif unidad_entrada == 4: # mmHg
        valor = valor * 133.322
    elif unidad_entrada == 5: # kgf/cm²
        valor = valor * 98066.5

    # Convertir a la unidad de salida
    if unidad_salida == 1: # bar
        valor = valor / 100000
    elif unidad_salida == 2: # psi
        valor = valor / 6894.76
    elif unidad_salida == 3: # atm
        valor = valor / 101325
    elif unidad_salida == 4: # mmHg
        valor = valor / 133.322
    elif unidad_salida == 5: # kgf/cm²
        valor = valor / 98066.5

    return valor

# Menús de selección
def menu_volumen():
    print("Seleccione la unidad de volumen:")
    print("1. Acres-pies")
    print("2. Pies cúbicos")
    print("3. Galones")
    print("4. Litros")
    print("5. Barriles")

def menu_presion():
    print("Seleccione la unidad de presión:")
    print("1. Bar")
    print("2. Psi")
    print("3. Atm")
    print("4. mmHg")
    print("5. kgf/cm²")

# Solicitar al usuario que elija la variable a convertir
variable = int(input("¿Qué variable quieres convertir? (1. Volumen, 2. Presión): "))

# Solicitar al usuario que ingrese la unidad de entrada y la unidad de salida
if variable == 1:
    menu_volumen()
    unidad_entrada = int(input("Ingrese el número de la unidad de entrada: "))
    menu_volumen()
    unidad_salida = int(input("Ingrese el número de la unidad de salida: "))
elif variable == 2:
    menu_presion()
    unidad_entrada = int(input("Ingrese el número de la unidad de entrada: "))
    menu_presion()
    unidad_salida = int(input("Ingrese el número de la unidad de salida: "))

# Solicitar al usuario que ingrese el valor a convertir
valor = float(input("Ingrese el valor a convertir: "))

# Realizar la conversión
if variable == 1:
    resultado = convertir_volumen(valor, unidad_entrada, unidad_salida)
    unidades = ["acres-pies", "pies cúbicos", "galones", "litros", "barriles"]
    print(f"El valor convertido es: {round(resultado, 2)} {unidades[unidad_salida - 1]}")
elif variable == 2:
    resultado = convertir_presion(valor, unidad_entrada, unidad_salida)
    unidades = ["bar", "psi", "atm", "mmHg", "kgf/cm²"]
    print(f"El valor convertido es: {round(resultado, 2)} {unidades[unidad_salida - 1]}")
