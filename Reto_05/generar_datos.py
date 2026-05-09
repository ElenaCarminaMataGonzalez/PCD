"""
Genera archivos CSV de prueba para el Perfilador de Datasets.
Crea:
- data/ventas.csv (≥150 filas)
- data/empleados.csv (≥150 filas)
- data/sensores.csv (≥150 filas)
"""
import csv
import random
import os

# Fijar semilla para reproducibilidad
random.seed(42)

# Directorio de salida
os.makedirs("data", exist_ok=True)

# --------------------------------------------------
# 1. ventas.csv
# --------------------------------------------------
productos = [
    "Laptop", "Mouse", "Teclado", "Monitor", "Impresora",
    "Webcam", "Disco Duro", "Memoria USB", "Audífonos",
    "Cable HDMI", "Hub USB-C", "Soporte Monitor", "Tablet",
    "Cargador", "Bocina Bluetooth"
]
vendedores = ["Ana", "Bob", "Carlos", "Diana", "Eva", "", "  ", None]

def generar_ventas(n=150):
    filas = []
    for i in range(n):
        fecha = f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
        prod = random.choice(productos)
        if random.random() < 0.1:  # 10% cantidad vacía o no numérica
            cant = random.choice(["", "N/A", "  ", "err"])
        else:
            cant = random.randint(1, 30)
        if random.random() < 0.15:  # 15% precio vacío o no numérico
            precio = random.choice(["", "??", "sin_dato", "  "])
        else:
            precio = round(random.uniform(100, 20000), 2)
        vend = random.choice(vendedores)
        if vend is None:
            vend = ""
        # Armar línea con posibles irregularidades en columnas
        # Normalmente 5 columnas. A veces omitimos el último campo.
        if random.random() < 0.05:  # 5% omitir vendedor
            fila = [fecha, prod, str(cant), str(precio)]  # 4 columnas
        elif random.random() < 0.05:  # 5% agregar columna extra
            fila = [fecha, prod, str(cant), str(precio), vend, "extra"]
        else:
            fila = [fecha, prod, str(cant), str(precio), vend]
        filas.append(fila)
    return filas

with open("data/ventas.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["fecha", "producto", "cantidad", "precio", "vendedor"])
    writer.writerows(generar_ventas(155))  # un poco más de 150

# --------------------------------------------------
# 2. empleados.csv
# --------------------------------------------------
nombres = ["Ana", "Bob", "Carlos", "Diana", "Eva", "Fernando", "Gabriela", "", "  "]
apellidos = ["García", "López", "Ruiz", "Torres", "Martínez", "Hernández", None, ""]
dominios = ["@empresa.com", "@corp.net", "", " "]
departamentos = ["TI", "Ventas", "RRHH", "Marketing", "", "  ", None]
booleans = ["true", "false", "yes", "no", "1", "0", "t", "f", " ", ""]

def generar_empleados(n=150):
    filas = []
    for i in range(1, n+1):
        id_ = str(i)
        nom = random.choice(nombres)
        ape = random.choice(apellidos)
        if ape is None:
            ape = ""
        nombre_completo = f"{nom} {ape}".strip()
        if not nombre_completo:
            nombre_completo = ""  # podría ser vacío

        if random.random() < 0.1:
            email = ""  # nulo
        else:
            email = f"{nom.lower()}.{ape.lower()}{random.choice(dominios)}".replace(" ", "")
        depto = random.choice(departamentos)
        if depto is None:
            depto = ""
        if random.random() < 0.1:
            salario = ""  # nulo
        elif random.random() < 0.05:
            salario = random.choice(["N/A", "pendiente", "??"])
        else:
            salario = round(random.uniform(25000, 80000), 2)
        activo = random.choice(booleans)
        # fila normal
        fila = [id_, nombre_completo, email, depto, str(salario), activo]
        # 5% omitir última columna
        if random.random() < 0.05:
            fila = fila[:-1]
        # 5% añadir columna extra
        elif random.random() < 0.05:
            fila.append("extra")
        filas.append(fila)
    return filas

with open("data/empleados.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nombre", "email", "departamento", "salario", "activo"])
    writer.writerows(generar_empleados(155))

# --------------------------------------------------
# 3. sensores.csv
# --------------------------------------------------
sensores_id = [f"S{i:03d}" for i in range(1, 11)]  # 10 sensores
def generar_sensores(n=150):
    filas = []
    for i in range(n):
        ts = f"2026-{random.randint(1,6):02d}-{random.randint(1,28):02d} " \
             f"{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
        sensor = random.choice(sensores_id)
        if random.random() < 0.1:
            temp = ""  # nulo
        elif random.random() < 0.05:
            temp = random.choice(["ERR", "NaN", "inf", " "])
        else:
            temp = round(random.uniform(10.0, 40.0), 2)
        if random.random() < 0.1:
            hum = ""
        elif random.random() < 0.05:
            hum = random.choice(["N/A", "fail", "  "])
        else:
            hum = round(random.uniform(30.0, 90.0), 2)
        if random.random() < 0.1:
            bat = ""
        elif random.random() < 0.05:
            bat = "low"  # no numérico
        else:
            bat = random.randint(0, 100)
        fila = [ts, sensor, str(temp), str(hum), str(bat)]
        # irregularidades de columnas
        if random.random() < 0.05:
            fila.pop()  # quitar bateria
        elif random.random() < 0.05:
            fila.append("ruido")  # añadir columna extra
        filas.append(fila)
    return filas

with open("data/sensores.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "sensor_id", "temperatura", "humedad", "bateria"])
    writer.writerows(generar_sensores(160))