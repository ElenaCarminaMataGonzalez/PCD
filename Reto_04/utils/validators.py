import math

def Validar_sku(sku):
    """
    Valida que el SKU sea una cadena no vacía.
    Se espera un str (todos los campos del CSV se leen como texto)
    Args:
        sku (str): El SKU a validar.
    Returns:
        bool: True si el SKU es válido, False en caso contrario.
    """
    return isinstance(sku, str) and len(sku.strip()) > 0


def Validar_Precio(precio):
    """
    Valida que el precio sea un número > 0.

    Args:
        precio : El precio a validar.
    Returns:
        bool: True si el precio es válido, False en caso contrario.
    """
    try:
        valor_precio = float(precio)
        # Bloqueo de inf y nan
        if math.isinf(valor_precio) or math.isnan(valor_precio):
            return False
        return valor_precio > 0
    except (ValueError, TypeError):
        return False
        
    
def Validar_Stock(stock):
    """
    Valida que el stock sea un número entero >= 0.  

    Args:
        stock : El stock a validar.
    Returns:
        bool: True si el stock es válido, False en caso contrario.
    """
    try:
        valor_stock = int(stock)
        return valor_stock >= 0
    except (ValueError, TypeError):
        return False


def validar_Producto(sku, nombre, categoria, precio, stock, stock_minimo):
    """
    Valida todos los campos de un producto.
    
    Returns:
        tuple: (es_valido: bool, mensaje_error: str o None)
    """
    if not Validar_sku(sku):
        return False, "SKU inválido: debe ser una cadena no vacía o incorrecta."
    if not isinstance(nombre, str) or len(nombre.strip()) == 0:
        return False, "Nombre inválido: debe ser una cadena no vacía."
    if not isinstance(categoria, str) or len(categoria.strip()) == 0:
        return False, "Categoría inválida: debe ser una cadena no vacía."
    if not Validar_Precio(precio):
        return False, "Precio inválido: debe ser un número mayor a 0."
    if not Validar_Stock(stock):
        return False, "Stock inválido: debe ser un número entero mayor o igual a 0."
    if not Validar_Stock(stock_minimo):
        return False, "Stock mínimo inválido: debe ser un número entero mayor o igual a 0."
    
    return True, None
