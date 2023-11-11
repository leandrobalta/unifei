import tkinter as tk

class MainView:
    def __init__(self, tkinter, controller):
        
        #controlador e tela -> controller - tkinter
        self.tkinter = tkinter
        self.controller = controller

        # tamanho da dela
        self.tkinter.geometry("300x200")
        self.menuBar = tk.Menu(tkinter) #

        # mensagem no meio da tela de bem vindo
        self.handShakeFrame = tk.Frame(self.tkinter)
        self.handShakeFrame.pack()
        self.handShake = tk.Label(self.handShakeFrame, text="\n\n\n\n Bem-vindo\nNa barra de menu possuem\nalguns Comandos")
        self.handShake.pack()

        # configura item no menu
        self.comidaMenu = tk.Menu(self.menuBar) # --- nome ---
        self.menuBar.add_cascade(label="Comida", menu=self.comidaMenu)
        self.comidaMenu.add_command(label="Cadastrar", command=self.controller.CallSubscribeGame)
        self.comidaMenu.add_command(label="Avaliar", command=self.controller.CallRatingGame)
        self.comidaMenu.add_command(label="Consulta", command=self.controller.CallConsultGame)


        self.restauranteMenu = tk.Menu(self.menuBar) # --- nome ---
        self.menuBar.add_cascade(label="restaurante", menu=self.restauranteMenu)
        self.restauranteMenu.add_command(label="Cadastrar", command=self.controller.CallSubscribeGame)
        self.restauranteMenu.add_command(label="Avaliar", command=self.controller.CallRatingGame)
        self.restauranteMenu.add_command(label="Consulta", command=self.controller.CallConsultGame)

        
        

        #final 
        self.tkinter.config(menu=self.menuBar) #


class MainController:
    def __init__(self):
        self.tk = tk.Tk()

        self.view = MainView(self.tk, self)
        self.tk.title("Review de Games")

        self.tk.mainloop()


    # comandos do menu
    def CallSubscribeGame(self):
        self.gameController.Subscribe()

    def CallRatingGame(self):
        self.gameController.Rating()

    def CallConsultGame(self):
        self.gameController.Consult()

if __name__ == "__main__":
    r = MainController()