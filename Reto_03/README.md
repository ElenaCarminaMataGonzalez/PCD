# Reto Semana 3: Analizador de Ventas 

## Descripción del Proyecto
Este script es una herramienta de análisis de datos (ETL) que procesa transacciones de ventas individuales y genera un reporte consolidado por producto. 

El programa utiliza diccionarios de Python para agrupar datos y aplica las siguientes reglas de negocio:
- **Consolidación:** Suma las unidades vendidas y el ingreso total por cada producto.
- **Métricas:** Calcula el precio promedio de venta histórico de cada artículo.
- **Ordenamiento:** El reporte final se presenta ordenado descendentemente por ingreso total, mostrando los productos más rentables primero.
- **Limpieza:** Filtra y descarta líneas con datos corruptos, no numéricos o con columnas faltantes.

## Instrucciones de Uso
El programa está diseñado para ejecutarse desde la terminal (línea de comandos).

**1. Leer desde un archivo de prueba:**
Puedes pasar un archivo CSV de entrada usando la redirección `<`:
```bash
python3 main.py < tests/entrada.txt
```
**2.Guardar el reporte estandarizado:**
Para guardar el resultado directamente en un nuevo archivo CSV, utiliza `>`:

```bash
python3 main.py < tests/entrada.txt > tests/salida_esperada.txt
```

**3. Prueba manual en consola:**
Puedes ejecutar el script directamente y escribir los datos línea por línea (presiona `Ctrl+D` en Linux/Mac o `Ctrl+Z` en Windows al terminar):

```bash
python3 main.py
```
## Ejemplo de Entrada y Salida

**Archivo de entrada (`entrada.txt`):**
| fecha | producto | cantidad | precio_unitario |
| :--- | :--- | :--- | :--- |
| 2026-01-01 | Laptop | 2 | 15000.00 |
| 2026-01-02 | Mouse | 10 | 250.00 |
| 2026-01-03 | Laptop | 1 | 14500.00 |

**Salida generada (`stdout`):**
| producto | unidades_vendidas | ingreso_total | precio_promedio |
| :--- | :--- | :--- | :--- |
| Laptop | 3 | 44500.00 | 14833.33 |
| Mouse | 10 | 2500.00 | 250.00 |

*(Nota: Se saca un promedio de los productos con el mismo nombre y se acumula la cantidad de estos).*

## Autor
**Elena Carmina Mata Gonzalez Estudiante de Ciencia de Datos - Instituto Politécnico Nacional (IPN)**