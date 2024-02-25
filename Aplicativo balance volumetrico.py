from prettytable import PrettyTable

def calculate_iteration(q, bsw, ae, ar, al_prev, ae_difference_prev):
    # Calcular Qw (caudal de agua en BWPD) y Qo (caudal de aceite en BOPD)
    qw = q * (bsw / 100)
    qo = q - qw
    
    # Calcular AE (agua emulsionada en BOPD), E (producción de emulsión en BOPD) y AL (agua libre en BWPD)
    ae_calc = (qo * ae) / (100 - ae)
    e = qo + ae_calc
    al = qw - ae_calc
    
    # Calcular AR(BL)
    ar_bl = ((al + ae_difference_prev) * ar) / (1000000 - ar)
    
    # Corregir OIL
    oil_corrected = qo - ar_bl
    
    # Corregir AE
    ae_corrected = (oil_corrected * ae) / (100 - ae)
    
    # Corregir E
    e_corrected = oil_corrected + ae_corrected
    
    # Calcular la diferencia entre AE y AE corregido
    ae_difference = ae_calc - ae_corrected
    
    return al, ae_difference, oil_corrected, ae_corrected, e_corrected, ar_bl

def print_table(iteration, oil_corrected, ae_corrected, e_corrected, al, ar_bl, ae_difference):
    # Crear la tabla
    table = PrettyTable()
    table.add_column("", ["OIL", "AE", "E", "AL", "AR"])
    table.add_column("A", [oil_corrected, ae_corrected, e_corrected, "", ""])
    table.add_column("B", ["", ae_difference, "", al, ar_bl])
    
    # Imprimir la tabla
    print(f"\nTabla de resultados (Iteración {iteration}):")
    print(table)

def main():
    # Solicitar al usuario que ingrese los datos
    q = float(input("Ingrese el caudal total del fluido (BFPD): "))
    bsw = float(input("Ingrese el BSW (%): "))
    ae = float(input("Ingrese el %AE: "))
    ar = float(input("Ingrese el AR (PPM): "))
    
    # Valores iniciales para la primera iteración
    al_prev = 0
    ae_difference_prev = 0
    
    # Realizar la primera iteración
    al_prev, ae_difference_prev, oil_corrected, ae_corrected, e_corrected, ar_bl = calculate_iteration(q, bsw, ae, ar, al_prev, ae_difference_prev)
    print_table(1, oil_corrected, ae_corrected, e_corrected, al_prev, ar_bl, ae_difference_prev)
    
    # Preguntar al usuario si desea realizar más iteraciones
    more_iterations = input("¿Desea realizar más iteraciones? (Ingrese '1' para Sí, '2' para No): ")
    iteration = 2
    
    # Realizar más iteraciones si el usuario lo desea
    while more_iterations == "1":
        # Calcular la siguiente iteración
        al_prev, ae_difference_prev, oil_corrected, ae_corrected, e_corrected, ar_bl = calculate_iteration(q, bsw, ae, ar, al_prev, ae_difference_prev)
        print_table(iteration, oil_corrected, ae_corrected, e_corrected, al_prev, ar_bl, ae_difference_prev)
        
        # Preguntar nuevamente si desea realizar más iteraciones
        more_iterations = input("¿Desea realizar más iteraciones? (Ingrese '1' para Sí, '2' para No): ")
        iteration += 1

if __name__ == "__main__":
    main()
