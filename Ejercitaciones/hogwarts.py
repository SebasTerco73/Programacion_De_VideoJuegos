import tkinter as tk
from tkinter import messagebox

def generarVentana():
    ventana = tk.Tk()
    ventana.title("Haga su hechizo")
    ventana.geometry("300x150")

    # Etiqueta
    etiqueta = tk.Label(ventana, text="Elije tu hechizo")
    etiqueta.pack(pady=5)

    # Caja de texto (input)
    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    # Función que se ejecuta al hacer clic en el botón
    def enviar():
        nombre = entrada.get()
        messagebox.showinfo("¡Hola!", f"Hola, {nombre}!")

    # Botón
    boton = tk.Button(ventana, text="Enviar", command=enviar)
    boton.pack(pady=10)

    # Mostrar la ventana
    ventana.mainloop()

def hogwarts():
    hechizos_basicos = ['Lumos','Alohomora','Wingardium Leviosa']
    # Crear la ventana principal
    generarVentana()
    

hogwarts()
