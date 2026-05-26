import sys
import re
from typing import Dict
from datetime import datetime

# Departamentos válidos para empleados
DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RHH']

# Series válidas para facturas
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']

# Funcion para detectar tipo de codigo y facilitar validacion posteriores
def detectar_tipo(codigo: str) -> str:
    """
    Detecta el tipo de codigo basado en su formato.
    """

    if re.match(r'^[A-Za-z]{3}-\d{4}-[A-Z]{2}$', codigo):
        return 'producto'
    
    if re.match(r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$', codigo):
        return 'envio'
    
    if re.match(r'^EMP-[A-Za-z]{3}-\d{4}$', codigo):
        return 'empleado'
    
    if re.match(r'^FAC-[A-Za-z]-\d{6}$', codigo):
        return 'factura'
    
    return 'desconocido'

def validar_producto(codigo: str) -> Dict:
    """
    Valida codigo de producto. Formato: ABC-1234-MX
    """
    resultado = {"valido": False, "categoria": None, "numero": None, "pais": None, "error": ""}
    
    # Patron: 3 letras mayusculas - 4 digitos - 2 letras mayusculas
    patron = r'^([A-Z]{3})-(\d{4})-([A-Z]{2})$'
    match = re.match(patron, codigo)
    
    if match:

        resultado["valido"] = True
        resultado["categoria"] = match.group(1)
        resultado["numero"] = match.group(2)
        resultado["pais"] = match.group(3)

    else:

        resultado["error"] = "Formato invalido. Debe 3 letras mayusculas - 4 digitos - 2 letras mayusculas " \
                             "(ej: ABC-1234-MX)"
        
    return resultado

def validar_envio(codigo: str) -> Dict:
    """
    Valida codigo de envio. Formato: ENV-YYYY-MM-DD-NNNNNN
    """
    resultado = {"valido": False, "fecha": None, "secuencial": None, "error": ""}
    
    # Patron: ENV - Año(2020-2030) - Mes(01-12) - Día(01-31) - 6 dígitos
    patron = r'^ENV-(202\d|2030)-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{6})$'
    match = re.match(patron, codigo)
    
    if match:
        year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
       
        try:
            datetime(year, month, day)  # Verifica si la fecha es válida
            resultado["valido"] = True
            resultado["fecha"] = f"{year:04d}-{month:02d}-{day:02d}"
            resultado["secuencial"] = match.group(4)
       
        except ValueError:
            resultado["error"] = f"Fecha invalida: {year:04d}-{month:02d}-{day:02d} no existe."
    
    else: 
        resultado["error"] = "Formato invalido. Debe ser ENV-YYYY-MM-DD-NNNNNN con anio entre 2020 y 2030,"\
                             " mes entre 01 y 12, y dia entre 01 y 31."

    return resultado
 

def validar_empleado(codigo: str) -> Dict:
    """
    Valida codigo de empleado. Formato: EMP-XXX-NNNN
    """
    resultado = {"valido": False, "departamento": None, "numero": None, "error": ""}
    
    # Patron: EMP - 3 letras mayusculas - 4 digitos (sin empezar en 0, es decir [1-9])
    patron = r'^EMP-([A-Z]{3})-([1-9]\d{3})$'
    match = re.match(patron, codigo)
    
    if match:
        depto = match.group(1)

        # Verificamos la regla de negocio extra
        if depto in DEPARTAMENTOS_VALIDOS:

            resultado["valido"] = True
            resultado["departamento"] = depto
            resultado["numero"] = match.group(2)

        else:
            resultado["error"] = f"Departamento invalido: {depto}. Debe ser uno de {DEPARTAMENTOS_VALIDOS}."    
    else:
        resultado["error"] = "Formato invalido. Debe ser EMP-XXX-NNNN con 3 letras mayusculas y 4 digitos (sin empezar en 0)."
    
    return resultado


def validar_factura(codigo: str) -> Dict:
    """
    Valida codigo de factura. Formato: FAC-S-NNNNNN
    """
    resultado = {"valido": False, "serie": None, "numero": None, "error": ""}
    
    # Patron: FAC - 1 letra mayuscula - 6 digitos
    patron = r'^FAC-([A-Z])-(\d{6})$'
    match = re.match(patron, codigo)
    
    if match:
        serie = match.group(1)
        
        # Verificamos la regla de negocio extra
        if serie in SERIES_VALIDAS:
            resultado["valido"] = True
            resultado["serie"] = serie
            resultado["numero"] = match.group(2)
            
        else:
            resultado["error"] = f"Serie '{serie}' no valida. Validas: {SERIES_VALIDAS}"                        
    else:
        resultado["error"] = "Formato invalido. Debe ser FAC-S-NNNNNN con S: A-E y N: 6 digitos"
    
    return resultado

def validar_codigo(codigo: str) -> Dict:
    """
    Detecta el tipo de codigo y lo valida.
    """
    resultado = {
        "codigo": codigo,
        "tipo": "desconocido",
        "valido": False,
        "detalles": {},
        "error": ""
    }
    
    # Detectamos el tipo de codigo para mostrarlo incluso si no es valido
    tipo = detectar_tipo(codigo)
    resultado["tipo"] = tipo

    if tipo == "producto":
        val = validar_producto(codigo)

    elif tipo == "envio":
        val = validar_envio(codigo)

    elif tipo == "empleado":
        val = validar_empleado(codigo)

    elif tipo == "factura":
        val = validar_factura(codigo)

    # Si el tipo es desconocido, no intentamos validar y solo ponemos el error    
    else:
        val = {"valido": False, "error": "Formato no reconocido"}

    resultado["valido"] = val["valido"]

    if val["valido"]:

        # copiar detalles excluyendo 'valido' y 'error' que ya están en resultado
        for k, v in val.items():
            if k not in ("valido", "error") and v is not None:
                resultado["detalles"][k] = v
    
    # Si no es valido, el error ya está en val["error"] o se asignó un error genérico para formato desconocido
    else:
        resultado["error"] = val.get("error", "Error desconocido")
    
    return resultado

def validar_fecha_real(year: int, month: int, day: int) -> bool:
    """
    Valida que una fecha sea matematicamente real (Ej: rechaza 31 de Febrero).
    """
    try:
        datetime(year, month, day)
        return True
    
    except ValueError:
        return False

def main():
    """
    Función principal adaptada para el evaluador automático.
    Lee de stdin y regresa un CSV estricto a stdout.
    """
    # Imprimir el encabezado exacto
    print("codigo,tipo,valido")
    
    # Leer línea por línea desde la entrada estándar (stdin)
    for linea in sys.stdin:
        codigo = linea.strip() # Quitar espacios y saltos de línea
        
        # Ignorar líneas vacías
        if not codigo:
            continue
            
        # Validar y formatear la salida exacta
        resultado = validar_codigo(codigo)
        estado = "VALIDO" if resultado["valido"] else "INVALIDO"
        
        print(f"{codigo},{resultado['tipo']},{estado}")

if __name__ == "__main__":
    main()