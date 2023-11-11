import tkinter as tk
import jogo as game

class MainView:
    def __init__(self, tkinter, controller):
        self.tkinter = tkinter
        self.controller = controller

        self.tkinter.geometry("300x200")
        self.menuBar = tk.Menu(tkinter)

        self.handShakeFrame = tk.Frame(self.tkinter)
        self.handShakeFrame.pack()
        self.handShake = tk.Label(self.handShakeFrame, text="\n\n\n\n Bem-vindo\nNa barra de menu possuem\nalguns Comandos")
        self.handShake.pack()

        self.gameMenu = tk.Menu(self.menuBar)

        self.gameMenu.add_command(label="Cadastrar", command=self.controller.CallSubscribeGame)
        self.gameMenu.add_command(label="Avaliar", command=self.controller.CallRatingGame)
        self.gameMenu.add_command(label="Consulta", command=self.controller.CallConsultGame)
        self.menuBar.add_cascade(label="Jogo", menu=self.gameMenu)

        self.tkinter.config(menu=self.menuBar)


class MainController:
    def __init__(self):
        self.tk = tk.Tk()

        self.gameController = game.GameController(self)
    
        self.view = MainView(self.tk, self)
        self.tk.title("Review de Games")

        self.tk.mainloop()

    def CallSubscribeGame(self):
        self.gameController.Subscribe()

    def CallRatingGame(self):
        self.gameController.Rating()

    def CallConsultGame(self):
        self.gameController.Consult()

if __name__ == "__main__":
    r = MainController()