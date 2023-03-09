from tkinter import *
from tkinter import filedialog
from Classes import *

class GUI :

    def __init__(self):
        self.root=Tk()
        self.nGeneraciones=StringVar(self.root)
        self.nPadres=StringVar(self.root)
        self.menu()
        self.path=""
        self.root.mainloop()
    
    #-----------------MENU-------------#
        
    def menu(self):
        menu=Menu(self.root)
        self.root.config(menu=menu,width=300,height=300)
        setMenu=Menu(menu,tearoff=False)
        menu.add_cascade(label="Set",menu=setMenu)
        setMenu.add_command(label="SET",command=self.set)
        
    def abrirFichero(self):
        self.path=filedialog.askopenfilename(title="abrir",filetypes=[("Excel separado por comas",".txt")])
    
    def validate_entry(self,input):
        if input.isdigit() or input == "":
            return True
        else:
            return False

    def set(self):
        popup=Toplevel(self.root)
        popup.title("Set")
        popup.geometry("300x300")

        vcmd = (self.root.register(self.validate_entry), '%P')
        
        label1 =Label(popup, text="Path",pady=20).grid(row=0,column=0,padx=20)
        pathBtn =Button(popup, text="Escoger archivo", command=self.abrirFichero).grid(row=0,column=1)

        label2 =Label(popup, text="# Padres").grid(row=1,column=0,padx=20)
        entryPadres =Entry(popup,textvariable=self.nPadres,validate="key", validatecommand=vcmd).grid(row=1,column=1)

        label3 =Label(popup, text="# Generaciones",pady=20).grid(row=2,column=0,padx=20)
        entryGEN =Entry(popup,textvariable=self.nGeneraciones,validate="key", validatecommand=vcmd).grid(row=2,column=1)

        sendBtn=Button(popup,text="Listo",command=lambda:self.save(popup)).grid(row=3,column=0,columnspan=2)
    
    def save(self,popup):
        print(self.path)
        print(self.nPadres.get())
        print(self.nGeneraciones.get())
        self.readFile()
        popup.destroy()
    
    #-------------------COMPONENTES----------------------#

    #-------------------LEER ARCHIVO---------------------#

    def readFile(self):

        self.map=Map()
        i=1

        with open(self.path, 'r') as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            if i==3:
                city.addY(int(linea))
                self.map.add(city)
                print("y: "+linea)
                i=1
            elif i==2:
                city.addX(int(linea))
                print("x: "+linea)
                i=3
            else:
                city=City(linea)
                print("ciudad: "+linea)
                i=2
