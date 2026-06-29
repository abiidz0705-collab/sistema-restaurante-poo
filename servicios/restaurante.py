# servicios/restaurante.py
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio para gestionar el flujo operativo del restaurante."""
    
    def __init__(self, nombre_establecimiento: str) -> None:
        # Inicialización de atributos principales con tipos correctos
        self.nombre_establecimiento = nombre_establecimiento
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def registrar_producto(self, nuevo_producto: Producto) -> None:
        """Añade un objeto de la clase Producto a la colección."""
        self.lista_productos.append(nuevo_producto)

    def registrar_cliente(self, nuevo_cliente: Cliente) -> None:
        """Añade un objeto de la clase Cliente a la colección."""
        self.lista_clientes.append(nuevo_cliente)

    def mostrar_menu_disponible(self) -> None:
        """Recorre y despliega la información detallada del menú."""
        if not self.lista_productos:
            print("El menú se encuentra vacío en este momento.")
            return
        for producto in self.lista_productos:
            print(producto.generar_detalle())

    def mostrar_clientes_frecuentes(self) -> None:
        """Recorre y despliega el perfil de los clientes en consola."""
        if not self.lista_clientes:
            print("No existen clientes registrados en la base de datos.")
            return
        for cliente in self.lista_clientes:
            print(cliente.obtener_perfil())
            