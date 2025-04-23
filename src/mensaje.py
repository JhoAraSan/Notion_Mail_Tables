import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje_final():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showinfo("Actualización completa", "La información fue actualizada exitosamente.")
    root.destroy()