from tkinter import *

def set(root):
    popup=Toplevel(root)
    popup.title("Ventana emergente")
    popup.geometry("200x100")
    
    # agregar un label y un botón
    label =Label(popup, text="Esta es una ventana emergente")
    label.pack(pady=10)
    button =Button(popup, text="Cerrar", command=popup.destroy)
    button.pack()