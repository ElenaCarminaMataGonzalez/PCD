#!/usr/bin/env python3
"""
Sistema de Inventario Modular
Genera reporte de productos que necesitan reorden.
"""
import os
from models.producto import Producto
from utils.validators import validar_Producto
from utils.io import leer_inventario, escribir_reporte


# Configuración
ARCHIVO_INVENTARIO = os.path.join("data", "inventario.csv")
ARCHIVO_REPORTE = os.path.join("outputs", "reporte_inventario.csv")


def crear_productos(datos_raw):
    """Convierte lista de diccionarios en objetos Producto, ignorando inválidos."""
    productos = []
    for datos in datos_raw:
        es_valido, error = validar_Producto(
            datos.get('sku'),
            datos.get('nombre'),
            datos.get('categoria'),
            datos.get('precio'),
            datos.get('stock'),
            datos.get('stock_minimo')
        )
        if not es_valido:
            print(f"Advertencia: Ignorando registro - {error}")
            continue
        producto = Producto(
            sku=datos['sku'],
            nombre=datos['nombre'],
            categoria=datos['categoria'],
            precio=float(datos['precio']),
            stock=int(datos['stock']),
            stock_minimo=int(datos['stock_minimo'])
        )
        productos.append(producto)
    return productos


def filtrar_necesitan_reorden(productos):
    return [p for p in productos if p.Controlar_Stock()]


def ordenar_por_faltantes(productos):
    return sorted(productos, key=lambda p: p.unidades_faltantes(), reverse=True)


def main():
    print("=" * 50)
    print("SISTEMA DE INVENTARIO - Reporte de Reorden")
    print("=" * 50)

    # Leer datos
    print(f"\nLeyendo inventario de: {ARCHIVO_INVENTARIO}")
    try:
        datos_raw = leer_inventario(ARCHIVO_INVENTARIO)
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{ARCHIVO_INVENTARIO}'.")
        return

    print(f"Registros leídos: {len(datos_raw)}")

    #  Crear objetos Producto
    productos = crear_productos(datos_raw)
    print(f"Productos válidos: {len(productos)}")

    #  Filtrar y ordenar
    necesitan = ordenar_por_faltantes(filtrar_necesitan_reorden(productos))
    print(f"Productos con necesidad de reorden: {len(necesitan)}")

    #  Mostrar resumen
    print("\n" + "-" * 50)
    print("PRODUCTOS QUE NECESITAN REORDEN:")
    print("-" * 50)
    for p in necesitan:
        print(p)

    #  Escribir reporte
    escribir_reporte(necesitan, ARCHIVO_REPORTE)
    print(f"\nReporte guardado en: {ARCHIVO_REPORTE}")
    print("\n" + "=" * 50)
    print("Proceso completado exitosamente")
    print("=" * 50)


if __name__ == "__main__":
    main()