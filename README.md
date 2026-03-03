# Reto Semana 01: Calculadora de Sumas 

## Descripción 
Este proyecto es un pipeline de datos (ETL) básico desarrollado en Python para la materia de Programación para Ciencia de Datos. El programa `main.py` lee un flujo de texto línea por línea desde la entrada estándar (stdin), limpia los datos "sucios" y calcula la suma total por línea, imprimiendo el resultado en la salida estándar (stdout).

El programa es robusto y maneja diferentes casos de error, aplicando las siguientes reglas de negocio:
- Ignora espacios en blanco.
- Filtra caracteres alfanuméricos no válidos o "basura", conservando solo números, puntos y signos negativos.
- Trunca los números decimales a enteros antes de realizar la suma.
- Las líneas vacías o con datos irrecuperables retornan `0`.

## Instrucciones de Uso
El programa está diseñado para ejecutarse desde la terminal (línea de comandos). Asegúrate de tener Python 3 instalado.

**1. Leer desde un archivo de texto:**
Puedes pasar un archivo de texto como entrada usando la redirección `<`:
```bash
python3 main.py < tests/entrada1.txt
```

**2. Guardar el resultado en un nuevo archivo:**
Para procesar un archivo y guardar la salida directamente en otro documento de texto, utiliza >:
```bash
python3 main.py < tests/entrada1.txt > tests/salida1.txt
```

**3. Uso con pipelines (pipes):**
Puedes conectar la salida de otros programas (como un generador de datos) directamente a este script:

```bash
cat tests/entrada1.txt | python3 main.py
```

**Ejemplos de Entrada y Salida**
Archivo de entrada (entrada.txt):

1,2,3
10

1.9,2.1,3.7
1a2,3b,4
  5 , 10 , 15  

Salida en consola (stdout):


6
10
0
6
19
30

## Autor
**Elena Carmina Mata Gonzalez Estudiante de Ciencia de Datos - Instituto Politécnico Nacional (IPN)**