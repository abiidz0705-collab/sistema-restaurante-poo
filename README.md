# Sistema de Gestión de Restaurante - POO

**Estudiante:** Abigail Deleg  
**Asignatura:** Programación Orientada a Objetos  

---

## Descripción del Proyecto
Este sistema ha sido diseñado como una solución de software modular en Python utilizando el paradigma de Programación Orientada a Objetos (POO). El núcleo de la aplicación modela de forma abstracta los elementos comerciales esenciales de un restaurante: el control de los productos ofrecidos en el menú y el registro de la clientela asociada, organizando las responsabilidades y separando el modelo de datos de la lógica del servicio.

---

## Estructura del Repositorio
El proyecto se organiza bajo una arquitectura modular rígida dividida por ámbitos de responsabilidad:

- `restaurante_app/`: Raíz del código fuente.
  - `modelos/`: Módulos que estructuran las entidades de datos básicas mediante clases independientes.
    - `producto.py`: Define atributos físicos e internos de los artículos del menú.
    - `cliente.py`: Contiene los metadatos y estados lógicos de los consumidores.
  - `servicios/`: Aloja la lógica operacional para coordinar las interacciones de los objetos.
    - `restaurante.py`: Administrador funcional que agrupa las colecciones del sistema.
  - `main.py`: Orquestador primario y punto de inicio del programa.
- `README.md`: Documentación técnica del repositorio académico.

---

## Especificación de Tipos de Datos Implementados

| Tipo de Dato | Atributos Representativos | Propósito dentro del Sistema |
| :--- | :--- | :--- |
| `str` | `identificador`, `nombre`, `cedula`, `nombre_completo` | Almacenamiento de textos descriptivos e identificaciones únicas de texto. |
| `int` | `tiempo_preparacion`, `visitas_mes` | Mediciones cuantitativas de minutos cronometrados y frecuencias enteras. |
| `float` | `precio` | Representación exacta y fraccionaria de valores monetarios o financieros. |
| `bool` | `disponible`, `aplica_promocion` | Banderas de control de estado binario para la toma de decisiones lógicas. |
| `list` | `inventario_productos`, `registro_clientes` | Colecciones compuestas en memoria para retener y agrupar múltiples objetos. |

---

## Reflexión Académica 

### Identificadores Descriptivos y Estándares de Codificación
La adopción de nombres explícitos y semánticos (como `tiempo_preparacion` en lugar de una variable efímera `t`) combinada con las directrices de estilo de Python (*PascalCase* para clases y *snake_case* para métodos y variables) es imperativa en el desarrollo de software moderno. Este hábito propicia que el código sea auto-documentado, reduciendo la dependencia de comentarios excesivos y permitiendo una comprensión inmediata del flujo de datos por parte de terceros desarrolladores.

### Tipos de Datos Coherentes y Arquitectura de Paquetes Modulares
Utilizar tipos de datos precisos para cada atributo asegura la integridad estructural del software desde el diseño inicial, mitigando errores lógicos durante la ejecución. Al vincular estos tipos primarios con estructuras estructuradas como las listas (`list`), el software adquiere la capacidad de gestionar dinámicamente un número indefinido de entidades complejas en memoria. Finalmente, segmentar el proyecto en paquetes (`modelos` y `servicios`) evita el código monolítico, aislando las fallas y permitiendo una escalabilidad sostenible donde las modificaciones en un componente no rompan las operaciones de los demás.