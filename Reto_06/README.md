# Validador de Códigos con Expresiones Regulares 

## Descripción del Proyecto
Este proyecto es un sistema de validación automática diseñado para una empresa de logística. Utiliza expresiones regulares (RegEx) para procesar un lote de códigos a través de la entrada estándar (`stdin`) y determinar su tipo y validez. 

El sistema es capaz de detectar y validar 4 tipos de formatos:
* **Productos:** `ABC-1234-MX`
* **Envíos:** `ENV-2024-03-15-001234`
* **Empleados:** `EMP-VEN-1234`
* **Facturas:** `FAC-A-123456`

---

##  Cómo Ejecutar (Instrucciones de Uso)
El programa está diseñado para leer desde un archivo de texto utilizando redirección de consola, garantizando compatibilidad con sistemas de evaluación automática.

**Desde Windows (PowerShell):**
```bash
Get-Content codigos.txt | python main.py > resultados.csv
```

**Desde Windows (CMD) / Linux / Mac:**

```bash
cmd /c "python main.py < codigos.txt > resultados.csv"
```

---
## Formato de Salida
El script exporta a stdout (o al archivo redirigido) un formato CSV estricto, sin mensajes adicionales:

### Fragmento de código
```bash
codigo,tipo,valido
TEC-0001-MX,producto,VALIDO
tec-0001-MX,producto,INVALIDO
XXX-1234,desconocido,INVALIDO
```
---
## Arquitectura de Validación
El validador utiliza una arquitectura de dos capas:

**Detección Flexible:** Evalúa la estructura general con [A-Za-z] para clasificar el código y atrapar errores de formato.

**Validación Estricta:** Aplica reglas de negocio rigurosas mediante expresiones regulares estrictas y restricciones de calendario con el módulo nativo datetime.

## Desglose de los Patrones RegEx Utilizados

### Desglose del Patrón RegEx: Código de Producto
**Patrón utilizado:** `^([A-Z]{3})-(\d{4})-([A-Z]{2})$`

| Componente | Descripción | Función |
| :--- | :--- | :--- |
| `^` y `$` | Anclas de inicio y fin | Garantizan que la cadena no tenga caracteres extra al principio o al final. |
| `([A-Z]{3})` | Grupo de captura 1 | Extrae exactamente 3 letras mayúsculas (Categoría). |
| `-` | Carácter literal | Exige un guion separador exacto. |
| `(\d{4})` | Grupo de captura 2 | Extrae exactamente 4 dígitos del 0 al 9 (Número secuencial). |
| `([A-Z]{2})` | Grupo de captura 3 | Extrae exactamente 2 letras mayúsculas (País). |

---
### Desglose del Patrón RegEx: Código de Envío
**Patrón utilizado:** `^ENV-(202\d|2030)-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{6})$`

*Nota Arquitectónica: Este patrón forma la "Capa Sintáctica" que valida la estructura básica. La validación matemática de los días del mes (Capa Semántica) se delega a la librería nativa `datetime` para manejar años bisiestos y meses de 30 días de forma robusta.*

| Componente | Descripción | Función |
| :--- | :--- | :--- |
| `^ENV-` | Prefijo literal | La cadena debe comenzar estrictamente con "ENV-". |
| `(202\d\|2030)` | Grupo de captura 1 | Extrae el año. Permite de 2020 a 2029, o explícitamente el 2030. |
| `(0[1-9]\|1[0-2])` | Grupo de captura 2 | Extrae el mes. Permite `0` seguido de `1-9`, o `1` seguido de `0-2` (Meses 01 al 12). |
| `(0[1-9]\|[12][0-9]\|3[01])` | Grupo de captura 3 | Extrae el día. Permite del `01` al `09`, del `10` al `29`, o `30`/`31`. |
| `(\d{6})$` | Grupo de captura 4 | Extrae exactamente 6 dígitos numéricos al final de la cadena. |

---
### Desglose del Patrón RegEx: Código de Empleado
**Patrón utilizado:** `^EMP-([A-Z]{3})-([1-9]\d{3})$`

| Componente | Descripción | Función |
| :--- | :--- | :--- |
| `^EMP-` | Prefijo literal | La cadena debe comenzar estrictamente con "EMP-". |
| `([A-Z]{3})` | Grupo de captura 1 | Extrae exactamente 3 letras mayúsculas (Departamento). |
| `([1-9]\d{3})` | Grupo de captura 2 | Extrae 4 dígitos. El primero debe ser del `1` al `9` (para evitar que inicie con `0`), seguido de 3 dígitos cualesquiera (`\d{3}`). |
| `$` | Ancla de fin | Evita que haya caracteres basura después de los números. |

---
### Desglose del Patrón RegEx: Código de Factura
**Patrón utilizado:** `^FAC-([A-Z])-(\d{6})$`

| Componente | Descripción | Función |
| :--- | :--- | :--- |
| `^FAC-` | Prefijo literal | La cadena debe comenzar estrictamente con "FAC-". |
| `([A-Z])` | Grupo de captura 1 | Extrae exactamente 1 letra mayúscula (Serie). |
| `(\d{6})` | Grupo de captura 2 | Extrae exactamente 6 dígitos del 0 al 9 (Número de factura). |
| `$` | Ancla de fin | Garantiza que no haya texto adicional al final. |

---
## Conclusión Analítica
A partir de la corrida del lote de pruebas, el sistema procesó 26 códigos, detectando correctamente una tasa de error del 53.8% (14 códigos inválidos).

El uso de expresiones regulares (Capa Sintáctica) en combinación con validaciones semánticas nativas (como datetime y listas restrictivas) demostró ser altamente eficaz. La herramienta cumple estrictamente con el formato de evaluación automatizada (I/O estándar en formato CSV), asegurando su fácil integración en pipelines de datos logísticos.

---
## Autor
**Elena Carmina Mata Gonzalez Estudiante de Ciencia de Datos - Instituto Politécnico Nacional (IPN)**