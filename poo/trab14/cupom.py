import tkinter as tk
from showMessage import ShowMessage

class CupomFiscal:
    def __init__(self, nroCupom):
        self.__nroCupom = nroCupom
        self.__itensCupom = []

    @property
    def nroCupom(self):
        return self.__nroCupom

    @property
    def itemsCupom(self):
        return self.__itensCupom

    def AddItem(self, newItem):
        self.__itensCupom.append(newItem)


class CreateCardView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.geometry('250x100')
        self.title("Consultar")
        self.controll = controller

        self.frameTitulo = tk.Frame(self)
        self.frameButt = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameButt.pack()
      
        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.labelTitulo.pack(side="left")

        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
      
        self.enterButton = tk.Button(self.frameButt ,text="Enter")      
        self.enterButton.pack(side="left")
        self.enterButton.bind("<Button>", self.controll.searchHandler) 

        self.closeButton = tk.Button(self.frameButt ,text="Concluído")      
        self.closeButton.pack(side="left")
        self.closeButton.bind("<Button>", self.controll.closeHandler)

class ConsultCardView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.geometry('250x100')
        self.title("Consultar")
        self.controll = controller

        self.frameTitulo = tk.Frame(self)
        self.frameButt = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameButt.pack()
      
        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.labelTitulo.pack(side="left")

        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
      
        self.enterButton = tk.Button(self.frameButt ,text="Enter")      
        self.enterButton.pack(side="left")
        self.enterButton.bind("<Button>", self.controll.searchHandler) 

        self.closeButton = tk.Button(self.frameButt ,text="Concluído")      
        self.closeButton.pack(side="left")
        self.closeButton.bind("<Button>", self.controll.closeHandler)


class CupomController:
    def __init__(self, mainControll):
        self.mainControll = mainControll

    def Create(self):
        pass

    def Consult(self):
        pass
    
