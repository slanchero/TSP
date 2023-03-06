from tkinter import *
from tkinter import messagebox
import Views

def set():
    Views.set(root)

#-------------------------------------------------------------------------#
root=Tk()
path=""
nGeneraciones=0
nPadres=0

#--------------------------------MENU-------------------------------------#

menu=Menu(root)
root.config(menu=menu,width=300,height=300)

setMenu=Menu(menu,tearoff=False)
menu.add_cascade(label="Set",menu=setMenu,command=set)
setMenu.add_command(label="SET",command=set)
#-------------------------------------------------------------------------#
root.mainloop()