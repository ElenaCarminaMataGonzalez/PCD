class Producto:
    """
    Clase que representa un producto en el sistema de inventario.
    Attributes:
        sku (str): Identificador unico
        nombre (str): Nombre del producto
        categoria (str): Categoria del producto
        precio (float): Precio unitario (>= 0)
        stock (int): Cantidad actual en inventario (>= 0)
        stock_minimo (int): Nivel minimo de stock (>= 0)
    """
    

    def __init__(self, sku, nombre, categoria, precio, stock, stock_minimo): 
               
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

    def Controlar_Stock(self):
        """
        Verifica si el stock actual es menor o igual al stock mínimo.
        Returns:
            bool: True si el stock es menor o igual al mínimo, False en caso contrario.
        """
        return self.stock <= self.stock_minimo
    
    def unidades_faltantes(self):
        """
        Calcula la cantidad de unidades faltantes para alcanzar el stock mínimo.
        Return:
            int: Cantidad para de alcanzar el stock mínimo.
            str: Mensaje indicando que el stock es suficiente.
        """
        if self.stock < self.stock_minimo:
            return self.stock_minimo - self.stock
        else:
            return f"El stock es suficiente ."
        
    def valor_inventario(self):
        """
        Calcula el valor monetario del stock actual.
        Returns:
            float: Valor total del stock.
        """
        return self.stock * self.precio
    
    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"Producto(SKU: {self.sku}, Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}, Stock Minimo: {self.stock_minimo})"

    def __repr__(self):
        """
        Representacion tecnica para desarrolladores.
        """
        return (f"Producto('{self.sku}', '{self.nombre}', '{self.categoria}', "
                f"{self.precio}, {self.stock}, {self.stock_minimo})")