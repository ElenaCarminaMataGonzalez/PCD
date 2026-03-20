# Reto Semana 2: Clasificador de Temperaturas 

## Descripción 
Este proyecto es un pipeline de datos (ETL) construido en Python para procesar y estandarizar reportes climáticos internacionales. El programa `main.py` lee un archivo CSV desde la entrada estándar (stdin), unifica las mediciones de temperatura y genera un reporte limpio en la salida estándar (stdout).

El programa es robusto ante datos sucios y aplica las siguientes reglas de negocio:
- **Estandarización:** Convierte automáticamente las temperaturas de Fahrenheit a Celsius usando la fórmula estándar.
- **Clasificación:** Asigna una categoría climática (Congelante, Frío, Templado, Cálido o Extremo) dependiendo de los rangos definidos en Celsius.
- **Limpieza:** Ignora líneas con datos incompletos, temperaturas no numéricas o unidades de medida no reconocidas (distintas a 'C' o 'F').
- **Formateo:** La temperatura de salida siempre se reporta exactamente con 1 decimal (ej. `22.0`).

## Instrucciones de Uso
El programa está diseñado para ejecutarse desde la terminal (línea de comandos). Asegúrate de tener Python 3 instalado.

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

## Ejemplos de Entrada y Salida

**Archivo de entrada (`entrada.txt`):**

| ciudad | temperatura | unidad |
| :--- | :--- | :--- |
| CDMX | 22 | C |
| Nueva York | 50 | F |
| Moscu | -10 | C |
| Miami | 95 | F |
| Error | abc | C |
| Chicago | 14 | F |

**Salida generada (stdout):**

| ciudad | temperatura_celsius | clasificacion |
| :--- | :--- | :--- |
| CDMX | 22.0 | Templado |
| Nueva York | 10.0 | Frio |
| Moscu | -10.0 | Congelante |
| Miami | 35.0 | Calido |
| Chicago | -10.0 | Congelante |

*(Nota: La línea con el error "abc" es correctamente filtrada y omitida en el reporte final).*

## Autor
**Elena Carmina Mata Gonzalez Estudiante de Ciencia de Datos - Instituto Politécnico Nacional (IPN)**