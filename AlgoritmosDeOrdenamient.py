import tkinter as tk
from tkinter import ttk
import random
import time
import ttkbootstrap as tb

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Algoritmos de Ordenamiento")  # Título de la ventana
        self.root.geometry("900x600")  # Tamaño de la ventana
        self.style = tb.Style("superhero")  # Estilo visual de ttkbootstrap

        self.data = []  # Lista de datos a ordenar
        self.algorithm = tk.StringVar(value="Bubble Sort")  # Algoritmo seleccionado

        self.create_widgets()  # Crear los componentes de la interfaz

    def create_widgets(self):
        # Frame de controles en la parte superior
        control_frame = ttk.Frame(self.root, padding=10)
        control_frame.pack(fill=tk.X)

        # Menú desplegable para seleccionar el algoritmo
        ttk.Label(control_frame, text="Algoritmo:").pack(side=tk.LEFT, padx=5)
        algo_menu = ttk.Combobox(control_frame, textvariable=self.algorithm, values=["Bubble Sort", "Selection Sort"], state="readonly", width=15)
        algo_menu.pack(side=tk.LEFT)

        # Botones para generar lista, iniciar ordenamiento y reiniciar
        ttk.Button(control_frame, text="Generar Lista", command=self.generate_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Iniciar", command=self.start_sorting).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Reiniciar", command=self.reset).pack(side=tk.LEFT, padx=5)

        # Área de dibujo (canvas) para visualizar los datos
        self.canvas = tk.Canvas(self.root, bg="white", height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def generate_data(self):
        # Generar una lista aleatoria de 50 números entre 10 y 400
        self.data = [random.randint(10, 400) for _ in range(50)]
        self.draw_data()  # Dibujar la lista generada

    def draw_data(self, color_array=None):
        self.canvas.delete("all")  # Limpiar el canvas
        if not self.data:
            return

        c_width = 870
        c_height = 500
        x_width = c_width / len(self.data)  # Ancho de cada barra
        spacing = 2
        normalized_data = [i / max(self.data) for i in self.data]  # Normalización de alturas

        for i, height in enumerate(normalized_data):
            # Coordenadas de cada barra
            x0 = i * x_width
            y0 = c_height - height * 450  # Escalar altura a 450 px
            x1 = x0 + x_width - spacing
            y1 = c_height
            color = color_array[i] if color_array else "skyblue"  # Color por defecto o personalizado
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)  # Dibuja la barra
            self.canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(self.data[i]), font=("Arial", 8))  # Texto sobre barra

        self.root.update_idletasks()  # Actualiza la interfaz

    def start_sorting(self):
        # Ejecuta el algoritmo seleccionado
        if self.algorithm.get() == "Bubble Sort":
            self.bubble_sort()
        elif self.algorithm.get() == "Selection Sort":
            self.selection_sort()

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            swapped = False  # Bandera para saber si hubo intercambio
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    # Intercambio si el actual es mayor que el siguiente
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    swapped = True
                    # Visualización del intercambio
                    self.draw_data(["green" if x == j or x == j+1 else "skyblue" for x in range(len(self.data))])
                    time.sleep(0.02)
            if not swapped:
                break  # Termina si no hubo intercambios (lista ordenada)
        self.draw_data(["green"] * len(self.data))  # Mostrar toda la lista en verde al final

    def selection_sort(self):
        n = len(self.data)
        for i in range(n):
            min_idx = i  # Suponemos que el actual es el menor
            for j in range(i+1, n):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j  # Nuevo mínimo encontrado
                # Visualización de comparación
                self.draw_data(["orange" if x == j else "skyblue" for x in range(len(self.data))])
                time.sleep(0.02)
            # Intercambio del menor con el inicio de la porción desordenada
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            # Visualización del intercambio
            self.draw_data(["green" if x == i or x == min_idx else "skyblue" for x in range(len(self.data))])
            time.sleep(0.02)
        self.draw_data(["green"] * len(self.data))  # Mostrar toda la lista en verde al final

    def reset(self):
        # Limpia los datos y borra el canvas
        self.data = []
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tb.Window(themename="superhero")  # Crear ventana con tema de ttkbootstrap
    app = SortingVisualizer(root)  # Instanciar la aplicación
    root.mainloop()  # Ejecutar la app
