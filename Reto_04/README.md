# Reto Semana 4: Sistema de Inventario Modular

## Descripción
Este proyecto es un sistema modular de análisis de datos desarrollado en Python para gestionar el inventario de una tienda de tecnología. Su función principal es procesar un lote de transacciones, identificar automáticamente los productos que han caído por debajo de su umbral mínimo de stock y generar un reporte de reorden priorizado para el departamento de compras.

**Reglas de negocio:**
- Cada producto aparece una sola vez en el archivo de entrada (no requiere consolidación).
- Se consideran válidos solo los registros con SKU no vacío, precio numérico ≥ 0, stock y stock mínimo enteros ≥ 0, y exactamente 6 columnas.
- Se filtran e ignoran líneas con errores (precios no numéricos, campos faltantes, columnas extra).
- El reporte se ordena por unidades faltantes de forma descendente (los que más urgen primero).

## Estructura del Proyecto
```
    reto_semana_04/
    ├── main.py                # Orquestador y punto de entrada
    ├── README.md              # Documentación del sistema
    ├── .gitignore             # Archivos excluidos de Git
    ├── models/                # Lógica de negocio (Dominio)
    │   ├── __init__.py
    │   └── producto.py        # Clase Producto y sus métodos
    ├── utils/                 # Herramientas auxiliares
    │   ├── __init__.py
    │   ├── io.py              # Gestión de archivos CSV (I/O)
    │   └── validators.py      # Validadores de integridad de datos
    ├── data/                  # Almacenamiento de entradas
    │   └── inventario.csv     # Fuente de datos original
    └── outputs/               # Resultados del proceso
        └── reporte_inventario.csv
```

## Cómo Ejecutar
Requiere Python 3. No necesita librerías externas.

Para iniciar el análisis, abre tu terminal apuntando a la raíz del proyecto y ejecuta el orquestador:
```bash
python main.py
```

*El programa leerá data/inventario.csv, mostrará un resumen en consola y generará el archivo outputs/reporte_inventario.csv.* 

*La carpeta outputs/ se crea automáticamente si no existe.*

**Formato de Entrada**

*Archivo: data/inventario.csv*

El sistema procesa un archivo CSV asumiendo el siguiente formato de 6 columnas. El sistema cuenta con mecanismos de defensa para ignorar silenciosamente registros con errores tipográficos, datos corruptos o columnas faltantes.

*Columnas esperadas (en este orden):*

| Columna | Tipo | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| `sku` | Texto | Identificador único del producto | `SKU001` |
| `nombre` | Texto | Nombre descriptivo | `Laptop HP` |
| `categoria` | Texto | Categoría del producto | `Electronica` |
| `precio` | Decimal | Precio unitario de venta | `15000.00` |
| `stock` | Entero | Cantidad actual en almacén | `5` |
| `stock_minimo` | Entero | Umbral para alertar reorden | `10` |

**Ejemplo de entrada:**

| sku | nombre | categoria | precio | stock | stock_minimo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SKU001 | Laptop HP | Electronica | 15000.00 | 5 | 10 |
| SKU002 | Mouse Logitech | Accesorios | 350.00 | 3 | 15 |

**El sistema ignora automáticamente líneas con:**

-Precio no numérico
-Stock o stock mínimo no numérico
-Número incorrecto de columnas (faltantes o extras)
-SKU o nombre vacíos

**Formato de Salida**

*Archivo: outputs/reporte_inventario.csv*

El reporte exportado contiene exclusivamente los productos que requieren reabastecimiento, ordenados de forma descendente según la urgencia (unidades faltantes).

**Columnas del reporte:**

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `sku` | Texto | Identificador único del producto |
| `nombre` | Texto | Nombre descriptivo |
| `categoria` | Texto | Categoría del producto |
| `stock_actual` | Entero | Cantidad actual en almacén |
| `stock_minimo` | Entero | Umbral requerido por la tienda |
| `unidades_faltantes` | Entero | Diferencia (`stock_minimo` - `stock_actual`) |
| `valor_inventario` | Decimal | Capital invertido (`precio` * `stock_actual`) |

**Ejemplo de salida:**

| sku | nombre | categoria | stock_actual | stock_minimo | unidades_faltantes | valor_inventario |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SKU002 | Mouse Logitech | Accesorios | 3 | 15 | 12 | 1050.00 |
| SKU001 | Laptop HP | Electronica | 5 | 10 | 5 | 75000.00 |

## Autor
**Elena Carmina Mata Gonzalez Estudiante de Ciencia de Datos - Instituto Politécnico Nacional (IPN)**

