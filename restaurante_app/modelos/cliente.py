class Cliente:

    def __init__(
        self,
        cedula: str,
        nombre_completo: str,
        frecuencia_visitas: int,
        tiene_descuento: bool
    ) -> None:
        # Inicialización de atributos con identificadores en snake_case
        self.cedula = cedula
        self.nombre_completo = nombre_completo
        
        # Tipo de dato entero para control estadístico del restaurante
        self.frecuencia_visitas = frecuencia_visitas
        
        # Tipo de dato booleano para lógicas de facturación o fidelidad
        self.tiene_descuento = tiene_descuento

    def obtener_perfil(self) -> str:
        # Retorna una cadena formateada con el perfil del cliente
        beneficio = "Aplica Descuento" if self.tiene_descuento else "Tarifa Estándar"
        return f"Cliente: {self.nombre_completo} | C.I: {self.cedula} | Visitas: {self.frecuencia_visitas} | Tipo: {beneficio}"

    def __str__(self) -> str:
        # Representación textual básica del objeto Cliente
        return f"{self.nombre_completo} (C.I: {self.cedula})"
    