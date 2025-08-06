import os
import tkinter as tk
from tkinter import messagebox
#install playsound
from playsound import playsound

def hogwarts():
    ventana = tk.Tk()
    ventana.title("Selector de hechizos")
    ventana.geometry("300x150")

    ancho = 300
    alto = 150

    # Obtener dimensiones de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    # Calcular posición
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2) -60

    # Posicionar ventana
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    # Etiqueta
    etiqueta = tk.Label(ventana, text="Elije tu hechizo")
    etiqueta.pack(pady=5)

    # Caja de texto (input)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

        # Función que se ejecuta al hacer clic en el botón
    def enviar():
        nombre = entrada.get().strip().lower()

        if nombre == '':
            messagebox.showerror("¡Error!", "Ingrese un hechizo!")
        elif nombre.lower() in hechizos_basicos:
            sound = hechizos_basicos[nombre]
            playsound(sound)
        else:
            playsound('sounds/dobby.mp3')

    # Botón
    boton = tk.Button(ventana, text="Hechizar", command=enviar)
    boton.pack(pady=10)

    # Mostrar la ventana
    ventana.mainloop()

hechizos_basicos = {'expecto patronum':'sounds/expecto.mp3','alohomora':'sounds/alohomora.mp3','wingardium leviosa':'sounds/leviosa.mp3'}
hogwarts()
