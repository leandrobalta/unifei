from showMessage import ShowMessage
import tkinter as tk

class Produto:
    def __init__(self, code, description, value):
        self.__code = code
        self.__description = description
        self.__value = value

    @property
    def code(self):
        return self.__code

    @property
    def description(self):
        return self.__description

    @property
    def value(self):
        return self.__value

class SubProductView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.geometry('250x100')
        self.title("Cadastrar novo Produto")
        self.controll = controller

        self.frameCode = tk.Frame(self)
        self.frameDescr = tk.Frame(self)
        self.frameValue = tk.Frame(self)
        self.frameButt = tk.Frame(self)
        self.frameCode.pack()
        self.frameButt.pack()
        self.frameDescr.pack()
        self.frameValue.pack()
      
        # code label and input
        self.labelCode = tk.Label(self.frameCode,text="Codigo: ")
        self.labelCode.pack(side="left")

        self.inputCode = tk.Entry(self.frameCode, width=20)
        self.inputCode.pack(side="left")

        # Description label and input
        self.labelDescr = tk.Label(self.frameDescr,text="Descrição: ")
        self.labelDescr.pack(side="left")

        self.inputDescr = tk.Entry(self.frameDescr, width=20)
        self.inputDescr.pack(side="left")

        # Value label and input
        self.labelValue = tk.Label(self.frameValue,text="Valor Unico: ")
        self.labelValue.pack(side="left")

        self.inputValue = tk.Entry(self.frameValue, width=20)
        self.inputValue.pack(side="left")

        #buttons
        self.enterButton = tk.Button(self.frameButt ,text="Enter")      
        self.enterButton.pack(side="left")
        self.enterButton.bind("<Button>", self.controll.OnSubscribe) 

        self.closeButton = tk.Button(self.frameButt ,text="Concluído")      
        self.closeButton.pack(side="left")
        self.closeButton.bind("<Button>", self.controll.OnClose)

class ConsultProductView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.title("Consultar produto")
        self.geometry("200x150")

        self.idFrame = tk.Frame(self)
        self.idLabel = tk.Label(self.idFrame, text="Código")
        self.idEntry = tk.Entry(self.idFrame, width=20)

        self.idFrame.pack()
        self.idLabel.pack(side="left")
        self.idEntry.pack(side="left")

        self.btnFrame = tk.Frame(self)
        self.btnFrame.pack()
        self.submitBtn = tk.Button(self.btnFrame, text="Consultar")
        self.submitBtn.pack(side="left")

        self.submitBtn.bind("<Button>", controller.consultHandler)

class ProdutoController:
    def __init__(self, mainControll):
        self.mainControll = mainControll

    def Subscribe(self):
        self.__subTopLevel = SubProductView(self)

    def Consult(self):
        self.__consultTopLevel = ConsultProductView(self)

    def OnSubscribe(self, event):
        code = self.__subTopLevel.inputCode.get()
        value = self.__subTopLevel.inputValue.get()
        description = self.__subTopLevel.inputDescr.get()

        if self.mainControll.getProductById(id) != None:
            return ShowMessage(title="Erro", message="Produto já cadastrado!")

        self.mainControll.registeredProducts.append(Produto(code, value, description))
        ShowMessage(title="Sucesso", message="Produto cadastrado com sucesso!")

    def onConsult(self, event):
        id = self.__consultTopLevel.inputCode.get()
        consultedProduct = self.mainControll.getProductById(id)

        if consultedProduct != None: 
            return ShowMessage(title="Produto encontrado", message="Código: {}\nValor: {}\nDescrição: {}" \
                .format(consultedProduct.getId(), consultedProduct.getValue(), consultedProduct.getDescription())) 
            
        return ShowMessage(title="Produto não encontrado", message="Produto não cadastrado!")        
    
    def OnClose(self, event):
        pass

