import sys

def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius."""
    return (fahrenheit  - 32) * 5 / 9

def clasificador_temperatura(celsius):
    """Clasifica la temperatura en los rangos definidos."""
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:  # 0 a 15
        return "Frio"
    elif celsius <= 25:  # 16 a 25
        return "Templado"
    elif celsius <= 35:  # 26 a 35
        return "Calido"
    else:  # > 35
        return "Extremo"

def procesar_linea(linea):
    """Procesa cada linea del CSV
    Retorno: Ciudad, Temperatura en Celsius, Clasificacion
    None en caso de que una sea invalida
    """
    # validacion
    partes = linea.strip().split(',')
    if len(partes) != 3:
        return None  # Linea no valida

    ciudad = partes[0].strip()
    temp_str = partes[1].strip()
    unidad = partes[2].upper().strip()

    if unidad not in ['C', 'F']:
        return None  # Unidad no valida
    
    try:
        temperatura = float(temp_str)
    except ValueError:
        return None  # Temperatura no valida

    # Conversion a Celsius si es necesario
    if unidad == 'F':
        temperatura = fahrenheit_a_celsius(temperatura)
    else:
        temperatura = temperatura  # Ya esta en Celsius

    # clasificacion de la temperatura
    clasificacion = clasificador_temperatura(temperatura)

    return ciudad, temperatura, clasificacion

def main():
    """Lee de stdin linea por linea, procesa cada linea e imprime el resultado."""

    primer_linea = True
    print("ciudad,temperatura_celsius,clasificacion")


    for linea in sys.stdin:
        linea = linea.strip()

        if not linea:  # Saltar lineas vacias
            continue

        if not primer_linea:
            primer_linea = False  # Saltar encabezado
            continue

        resultado = procesar_linea(linea) # Procesar cada linea

        if resultado is not None:
            ciudad, temperatura, clasificacion = resultado
            print(f"{ciudad}, {temperatura:.1f}, {clasificacion}")


if __name__ == "__main__":
    main()