import tkinter as tk
import cupom 
import produto
from showMessage import ShowMessage

class MainView:
    def __init__(self, tkinter, controller):
        self.controll = controller
        self.tkinter = tkinter
        
        #NEED TO EDIT
        self.tkinter.geometry('300x250')
        self.menubar = tk.Menu(self.tkinter)
        self.info = tk.Frame(self.tkinter)
        self.info.pack()
        self.infoLabel = tk.Label(self.info, text="\n\n\n\n\n Emissor de Cupom Fiscal Online")
        self.infoLabel.pack()
        
        self.cupomMenu = tk.Menu(self.menubar)
        self.produtoMenu = tk.Menu(self.menubar)

        self.cupomMenu.add_command(label="Cadastrar", \
                    command=self.controll.SubscribeProduct)
        self.cupomMenu.add_command(label='Consultar', \
                    command=self.controll.ConsultProduct)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.produtoMenu)

        self.produtoMenu.add_command(label="Criar", \
                    command=self.controll.CreateCard)    
        self.produtoMenu.add_command(label='Consultar', \
                    command=self.controll.ConsultCard)    
        self.menubar.add_cascade(label="Cupom Fiscal", \
                    menu=self.cupomMenu)

        self.tkinter.config(menu=self.menubar)
 
        
        
class MainController:
    def __init__(self):
        self.tkinter = tk.Tk()

        #instanciate controller
        self.cupom = cupom.CupomController(self)
        self.produto = produto.ProdutoController(self)

        self.view = MainView(self.tkinter, self)
        self.tkinter.title("Cupom Fiscal")
        self.tkinter.mainloop()
        self.tkinter

        self.registeredProducts = []
        self.generatedReceipts = []

    #product call functions
    def SubscribeProduct(self):
        self.produto.Subscribe()

    def ConsultProduct(self):
        self.produto.Consult()

    #card call functions
    def CreateCard(self):
        self.cupom.Create()

    def ConsultCard(self):
        self.cupom.Consult()

    def getProductById(self, id):
        for product in self.registeredProducts:
            if product.getId() == id:
                return product

        return None

    def getProductByDescription(self,  description):
        for product in self.registeredProducts:
            if product.description == description:
                return product

        return None

    def getReceiptById(self, id):
        for receipt in self.generatedReceipts:
            if receipt.code == id:
                return receipt

        return None

if __name__ == "__main__":
    run = MainController()
