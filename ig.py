from tkinter import *

raiz=Tk()

raiz.title("TPS")#cambiar titulo
raiz.resizable(False,False)#redimensionar en ninguna direccion
raiz.iconbitmap("map.ico")#colocar icono
raiz.geometry("650x350")#cambiar tamaño
raiz.config(bg="white")#Cambiar la configuracion de la ventana

frame=Frame()

frame.pack(side="left",anchor="n",fill="y",expand="True")#empaquetamos el frame
frame.config(width=100,height=100,bg="black")
frame.config(bd=10,relief="solid")
frame.config(cursor="hand2")

label1=Label(frame,text="hola",bg="black",fg="white")
label1.pack()

raiz.mainloop()