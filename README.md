Desarrollar una aplicación visual interactiva que permita observar el funcionamiento de algoritmos de ordenamiento (Bubble Sort y Selection Sort), con animaciones en tiempo real que ilustren los pasos de comparación e intercambio de datos.

Python 3

Tkinter: Biblioteca estándar para interfaces gráficas en Python.
ttkbootstrap: Extensión estilizada de ttk (Themed Tkinter) que proporciona temas modernos.
Módulos auxiliares:
random: Para generar listas aleatorias.
time: Para pausar la animación entre pasos.
Clase SortingVisualizer
Encapsula toda la lógica de la interfaz y visualización.
Maneja eventos, dibujo en canvas y ejecución de algoritmos.

Componentes de Interfaz Gráfica
Frame superior: Contiene controles como:
Menú desplegable para seleccionar el algoritmo.
Botones para generar lista, iniciar y reiniciar.
Canvas: Área gráfica para visualizar los datos como barras verticales.
Variables clave
self.data: Lista de números enteros a ordenar.
self.algorithm: Variable StringVar para seleccionar el algoritmo desde el menú.

Flujo de Funcionalidad
Generar Lista

Genera una lista de 50 números aleatorios entre 10 y 400.
Llama a draw_data() para visualizarla en forma de barras.
Iniciar
Detecta el algoritmo seleccionado y ejecuta el método correspondiente:
bubble_sort() o selection_sort()
Reset
Limpia la lista y borra el contenido del canvas.


Algoritmo de ordenamiento burbuja.
Se realizan comparaciones e intercambios repetitivos de elementos adyacentes.
Optimización: se detiene si no hubo intercambios en una pasada.
Colores en animación:
Verde: Barras intercambiadas.
Skyblue: Barras sin cambio.


Algoritmo de ordenamiento por selección.
Encuentra el menor elemento en la porción no ordenada y lo intercambia con el primer elemento no ordenado.
Colores en animación:
Naranja: Comparación actual.
Verde: Intercambio realizado.
