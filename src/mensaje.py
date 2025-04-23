import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje_final(mensajes):
    ## Esta función muestra un mensaje final con la información de los mensajes
    contador_mensajes = {}
    for mensaje in mensajes:
        if mensaje in contador_mensajes:
            contador_mensajes[mensaje] += 1
        else:
            contador_mensajes[mensaje] = 1
    texto = ""
    for mensaje, cantidad in contador_mensajes.items():
        texto += f"{mensaje} (x{cantidad})\n"

    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showinfo("Actualización completa", f"La información mostró estos mensajes: \n \n \n {texto}")
    root.destroy()