import csv
import os

def leer_inventario(ruta_archivo):
    """
    Lee el archivo CSV de inventario y retorna una lista de diccionarios.
    Solo se procesan las filas que contengan exactamente 6 columnas.
    """
    productos_raw = []
    encabezados_esperados = ['sku', 'nombre', 'categoria', 'precio', 'stock', 'stock_minimo']

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector)  # Leer primera línea

        # Verificar que el encabezado tenga 6 columnas exactas
        if len(encabezados) != 6:
            raise ValueError("El archivo de inventario no tiene los 6 encabezados requeridos.")

        # Opcional: validar nombres de columnas
        if encabezados != encabezados_esperados:
            print("Advertencia: Los nombres de las columnas no coinciden exactamente con los esperados.")

        for fila in lector:
            # Ignorar líneas vacías o con número de columnas distinto de 6
            if len(fila) != 6:
                continue
            # Crear diccionario con las 6 columnas (sin riesgo de desorden)
            producto = {
                'sku': fila[0].strip(),
                'nombre': fila[1].strip(),
                'categoria': fila[2].strip(),
                'precio': fila[3].strip(),
                'stock': fila[4].strip(),
                'stock_minimo': fila[5].strip()
            }
            productos_raw.append(producto)

    return productos_raw


def escribir_reporte(productos, ruta_archivo):
    """
    Escribe el reporte de productos que necesitan reorden.
    Crea el directorio de salida si no existe.
    """
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

    encabezados = ['sku', 'nombre', 'categoria', 'stock_actual',
                   'stock_minimo', 'unidades_faltantes', 'valor_inventario']

    with open(ruta_archivo, 'w', encoding='utf-8', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        for p in productos:
            escritor.writerow({
                'sku': p.sku,
                'nombre': p.nombre,
                'categoria': p.categoria,
                'stock_actual': p.stock,
                'stock_minimo': p.stock_minimo,
                'unidades_faltantes': p.unidades_faltantes(),
                'valor_inventario': f"{p.valor_inventario():.2f}"
            })