from tkinter import *
from tkinter import filedialog
from Classes import *


class GUI:

    def __init__(self):
        self.root = Tk()
        self.nGeneraciones = StringVar(self.root)
        self.nPadres = StringVar(self.root)
        self.p = []
        self.pc = []
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

    def validate_entry(self, input):
        if input.isdigit() or input == "":
            return True
        else:
            return False

    def set(self):
        popup = Toplevel(self.root)
        popup.title("Set")
        popup.geometry("300x300")

        vcmd = (self.root.register(self.validate_entry), '%P')

        label1 = Label(popup, text="Path", pady=20).grid(row=0, column=0, padx=20)
        pathBtn = Button(popup, text="Escoger archivo",command=self.abrirFichero).grid(row=0, column=1)

        label2 = Label(popup, text="# Padres").grid(row=1, column=0, padx=20)
        entryPadres = Entry(popup, textvariable=self.nPadres,validate="key", validatecommand=vcmd).grid(row=1, column=1)

        label3 = Label(popup, text="# Generaciones",pady=20).grid(row=2, column=0, padx=20)
        entryGEN = Entry(popup, textvariable=self.nGeneraciones,validate="key", validatecommand=vcmd).grid(row=2, column=1)

        sendBtn = Button(popup, text="Listo",command=lambda: self.save(popup)).grid(row=3,column=0,columnspan=2)

    def save(self, popup):
        self.readFile()
        self.visitadas = {}
        for city in self.map.cities:
            self.visitadas[city.name] = False
        popup.destroy()

    # -------------------COMPONENTES----------------------#
    def components(self):
        startBtn = Button(self.root,text="Start",command=lambda:(startBtn.destroy(), self.selectParents()))
        startBtn.pack()
    #--------------------Seleccionar padres---------------#
    def selectParents(self):
        self.stringParents=[]
        for i in range(int(self.nPadres.get())):
            self.stringParents.append(StringVar(self.root))
            Label(self.root,text=("Ingrese el orden de las ciudades para el padre "+str(i+1)+" :")).grid(row=i+1,column=0)
            Entry(self.root,textvariable=self.stringParents[i]).grid(row=i+1,column=1)
        
        texto="Ciudades disponibles: \n"

        for city in self.map.cities:
            texto=texto+"-"+city.name+"\n"

        Label(self.root,text=texto).grid(row=0,column=2,rowspan=4)

        Button(self.root,text="Enviar",command=self.crearPadres).grid(row=4,column=2)

    def crearPadres(self):
        for mapS in self.stringParents:
            citiesList=mapS.get().split(",")
            mapa=Map()
            for cityS in citiesList:
                for city in self.map.cities:
                    if city.name.strip().__eq__(cityS.strip()):
                        mapa.add(city)
                        print("encontrado")
                    else:
                        print("no encontrado")
            
            self.p.append(mapa)
            
        
        for padre in self.p:
            padre.evaluate()
            print(padre.score)
        

        
    #--------Calculo de Generaciones------------------------------------#

    def AG(self):
        
        i=0

        while i<int(self.nGeneraciones.get()):
            self.pp=self.selectParents()

    def selectParents(self):
        
        print("Hola")

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
