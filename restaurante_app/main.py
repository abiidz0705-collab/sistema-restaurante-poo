from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main() -> None:
    # 1. Instanciación usando el atributo correcto de tu imagen
    mi_restaurante = Restaurante("Gourmet Universitario")

    # 2. CREACIÓN DE OBJETOS: PRODUCTO
    producto_uno = Producto("P001", "Almuerzo Ejecutivo", 4.50, 15, True)
    producto_dos = Producto("P002", "Jugo Natural de Lulo", 1.75, 5, True)
    producto_tres = Producto("P003", "Tarta de Chocolate", 3.20, 8, False)

    # 3. CREACIÓN DE OBJETOS: CLIENTE
    cliente_uno = Cliente("0102030405", "Carlos Lascano", 12, True)
    cliente_dos = Cliente("0908070605", "Anahi Martínez", 3, False)

    # 4. REGISTRO DE OBJETOS
    mi_restaurante.registrar_producto(producto_uno)
    mi_restaurante.registrar_producto(producto_dos)
    mi_restaurante.registrar_producto(producto_tres)

    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    # 5. DESPLIEGUE EN CONSOLA (Ajustado a los atributos de tu restaurante.py)
    print(f"==================================================")
    print(f" BIENVENIDO A {mi_restaurante.nombre_establecimiento.upper()} ")
    print(f"==================================================")
    
    print("\n--- CARTA DE PRODUCTOS ---")
    mi_restaurante.mostrar_menu_disponible()

    print("\n--- BASE DE DATOS DE CLIENTES ---")
    mi_restaurante.mostrar_clientes_frecuentes()
    print(f"==================================================")

if __name__ == "__main__":
    main()
    
