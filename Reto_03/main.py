import sys
import math

def procesar_productos():

    productos = {}

    primera_linea = True

    for linea in sys.stdin:
       
        linea = linea.strip()
        
        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue
        
        # Saltar lineas vacias
        if not linea:
            continue
        
        partes = linea.split(',')
        if len(partes) != 4:
            continue  # Ignorar lineas invalidas
        
        # Extraer datos
        fecha = partes[0]
        producto = partes[1]
        
       # Convertir cantidad y precio a numeros, ignorar si no son validos
        try:
            cantidad = int(partes[2])
            precio = float(partes[3])
            
            # Si el precio es Infinito o "Not a Number" (NaN), ignoramos la linea
            if math.isinf(precio) or math.isnan(precio):
                continue
            
        except ValueError:
            continue  # Ignorar si falló al convertir letras o símbolos normales
        
        # Crear entrada si no existe
        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }
        
        # Acumular
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    return productos

def calcular_promedios(productos):
    for i in productos:
        unidades = productos[i]["unidades"]
        ingreso = productos[i]["ingreso"]
        if unidades > 0:
            productos[i]["precio_promedio"] = ingreso / unidades
        else:
            productos[i]["precio_promedio"] = 0.0

    # ordenar descendentemente por ingreso
    productos_ordenados = sorted(productos.items(), key=lambda x: x[1]["ingreso"], reverse=True)

    return productos_ordenados

def imprimir_resultados(productos_ordenados):
    #Imprimir el encabezado 
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    
    # Imprimir los datos separados por comas
    for producto, datos in productos_ordenados:
        print(f"{producto},{datos['unidades']},{datos['ingreso']:.2f},{datos['precio_promedio']:.2f}")

def main():
    productos = procesar_productos()
    productos_ordenados = calcular_promedios(productos)
    imprimir_resultados(productos_ordenados)    

if __name__ == "__main__":
    main()
