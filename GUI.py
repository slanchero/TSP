from tkinter import *
from tkinter import filedialog
from Classes import *
import random
from tkinter import messagebox

class GUI:

    def __init__(self):
        self.root = Tk()
        self.nGeneraciones = StringVar(self.root,value="2")
        self.nPadres = StringVar(self.root,value="3")
        self.p = []
        self.pc = []
        self.path=None
        self.menu()
        self.components()
        self.root.mainloop()

    # -----------------MENU-------------#

    def menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu, width=300, height=300)
        setMenu = Menu(menu, tearoff=False)
        menu.add_cascade(label="Set", menu=setMenu)
        setMenu.add_command(label="SET", command=self.set)

    def abrirFichero(self):
        self.path = filedialog.askopenfilename(title="abrir", filetypes=[("Archivo de texto plano", ".txt")])

    def validate_entry(self, new_value):
        if new_value.isdigit():
            return True
        else:
            return False

    def set(self):
        popup = Toplevel(self.root)
        popup.title("Set")
        popup.geometry("300x300")
        vcmd=(self.root.register(self.validate_entry), '%P')

        label1 = Label(popup, text="Path", pady=20).grid(row=0, column=0, padx=20)
        pathBtn = Button(popup, text="Escoger archivo",command=self.abrirFichero).grid(row=0, column=1)

        label2 = Label(popup, text="# Padres").grid(row=1, column=0, padx=20)
        entryPadres = Spinbox(popup, from_=3, to=10**100, validate="key",textvariable=self.nPadres, validatecommand=vcmd).grid(row=1, column=1)

        label3 = Label(popup, text="# Generaciones",pady=20).grid(row=2, column=0, padx=20)
        entryGEN = Spinbox(popup, from_=2, to=10**100, validate="key",textvariable=self.nGeneraciones, validatecommand=vcmd).grid(row=2, column=1)

        sendBtn = Button(popup, text="Listo",command=lambda: self.save(popup)).grid(row=3,column=0,columnspan=2)

    def save(self, popup): 
        if self.path is not None:
            self.readFile()
            self.visitadas = {}
            for city in self.map.cities:
                self.visitadas[city.name] = False
            popup.destroy()
        else:
            messagebox.showwarning("Advertencia", "Debe escoger la direccion del dataset de ciudades.")
        

    # -------------------COMPONENTES----------------------#
    def components(self):
        startBtn = Button(self.root,text="Start",command=lambda:(startBtn.destroy(), self.typeParents()))
        startBtn.pack()
    
    #--------------------Seleccionar padres---------------#
    def typeParents(self):
        if self.path is not None:
            self.stringParents=[]
#            for i in range(int(self.nPadres.get())):
#               self.stringParents.append(StringVar(self.root))
#                Label(self.root,text=("Ingrese el orden de las ciudades para el padre "+str(i+1)+" :")).grid(row=i+1,column=0)
#                Entry(self.root,textvariable=self.stringParents[i]).grid(row=i+1,column=1)
            
            texto="Ciudades disponibles: \n"

            for city in self.map.cities:
                texto=texto+"-"+city.name+"\n"

            Label(self.root,text=texto).grid(row=0,column=2,rowspan=4)

            Button(self.root,text="Enviar",command=self.padresAleatoreos).grid(row=4,column=2)
        else:
            messagebox.showwarning("Advertencia", "Debe escoger la direccion del dataset de ciudades.")
            self.components()

    def crearPadres(self):
        for mapS in self.stringParents:
            citiesList=mapS.get().split(",")
            mapa=Map()
            for cityS in citiesList:
                for city in self.map.cities:
                    if city.name.strip().__eq__(cityS.strip()):
                        mapa.add(city)
            
            self.p.append(mapa)
        
        for padre in self.p:
            padre.evaluate()
            print(padre.score)
        
        self.AG()
    ##-----------------Padres aleatorios-------------------------------#
    def padresAleatoreos(self):
        i=0
        while i<int(self.nPadres.get()):
            temp=Map()
            b = self.map.cities.copy()
            while(b.__len__()>0):
                temp.add(b.pop(random.randint(0,len(b)-1)))
            
            match = False    
            for map in self.p:
                if map.equals(temp):
                    match = True
            self.p.append(temp)
            if match:
                self.p.pop()
            else:
                i = i+1
        
        for padre in self.p:
            padre.evaluate()  

        self.AG() 
    
    #--------Algoritmo Genetico------------------------------------#

    def AG(self):
        
        i=0

        while i<int(self.nGeneraciones.get()):
            self.pp=self.selectParents()
            self.pc=self.reproduction()
            self.mutate()
            self.nextGen()
            i=i+1
        
        self.showLastGen()

    #-----------------------Seleccion de mejores genes------------------#
    
    def selectParents(self):
        self.p.sort()
        
        return self.p[:int(self.nPadres.get())-1]
    
    #------------------------Reproduccion de padres--------------------#

    def reproduction(self):
        children=[]
        for i in range(len(self.pp)-1):
            children.append(self.pp[i].reproduce(self.pp[(i+1)%len(self.pp)]))
        
        return children
        
    #----------------------------Mutar----------------------------#
    def mutate(self):
        a=random.randint(0,len(self.pc)-1)
        b=random.randint(1,100)
        if b<10:
            self.pc[a].mutate()
    
    #--------------------------Siguiente Gneracion----------------#
    def nextGen(self):
        self.p.extend(self.pc)
        self.p.sort()
        self.p=self.p[:int(self.nPadres.get())]

    # -------------------LEER ARCHIVO---------------------#

    def readFile(self):

        self.map = Map()
        i = 1

        with open(self.path, 'r') as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            if i == 3:
                city.addY(int(linea))
                self.map.add(city)
                i = 1
            elif i == 2:
                city.addX(int(linea))
                i = 3
            else:
                city = City(linea)
                i = 2

    #---------------------Mostrar Ultima Generacion------------------------------#
    def showLastGen(self):
        texto=""
        for map in self.p:
            texto=texto+""+map.imprimir()+"\n"
            texto=texto+"Recorrido: "+str(map.score)+" unds\n"
            texto=texto+"-----------------------------\n"
        Label(self.root,text="Ultima Generacion",font=("Arial", 12, "bold")).grid(row=4,column=2)
        Label(self.root,text=texto).grid(row=5,column=2,columnspan=6)
        