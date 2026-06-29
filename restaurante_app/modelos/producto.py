class Producto:

    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        tiempo_preparacion: int,
        disponible: bool
    ) -> None:
        # Identificadores descriptivos para las características del producto
        self.codigo = codigo
        self.nombre = nombre
        
        # Tipos de datos numéricos (decimal y entero)
        self.precio = precio
        self.tiempo_preparacion = tiempo_preparacion  # Medido en minutos
        
        # Tipo de dato lógico para validar stock/disponibilidad
        self.disponible = disponible

    def generar_detalle(self) -> str:
        # Retorna una cadena con la información detallada para el menú
        estado = "Disponible" if self.disponible else "Agotado"
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f} ({self.tiempo_preparacion} min) | Estado: {estado}"

    def __str__(self) -> str:
        # Representación simplificada del objeto Producto en formato de texto
        return f"{self.nombre} (${self.precio:.2f})"
    