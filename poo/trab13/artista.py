
import tkinter as tk
from tkinter import messagebox

def showMessage(title, message):
    messagebox.showinfo(title, message)

class Artist:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class ArtistInsertToplevel(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.geometry('250x100')
        self.title("Artist")

        self.frameName = tk.Frame(self)
        self.frameBtn = tk.Frame(self)

        self.frameName.pack()
        self.frameBtn.pack()

        self.labelName = tk.Label(self.frameName, text="Nome: ")
        self.labelName.pack(side="left")

        self.inputName = tk.Entry(self.frameName, width=20)
        self.inputName.pack(side="left")

        self.submitBtn = tk.Button(self.frameBtn ,text="Enviar")      
        self.submitBtn.pack(side="left")
        self.submitBtn.bind("<Button>", controller.insertSubmitHandler)

        self.buttonClose = tk.Button(self.frameBtn ,text="Concluído")      
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controller.closeHandler)

class ArtistConsultToplevel(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.geometry('250x100')
        self.title("Artist")

        self.frameName = tk.Frame(self)
        self.frameBtn = tk.Frame(self)

        self.frameName.pack()
        self.frameBtn.pack()

        self.labelName = tk.Label(self.frameName, text="Nome: ")
        self.labelName.pack(side="left")

        self.inputName = tk.Entry(self.frameName, width=20)
        self.inputName.pack(side="left")

        self.submitBtn = tk.Button(self.frameBtn ,text="Enviar")      
        self.submitBtn.pack(side="left")
        self.submitBtn.bind("<Button>", controller.consultSubmitHandler)

        self.buttonClose = tk.Button(self.frameBtn ,text="Concluído")      
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controller.closeHandler)

class ArtistController:
    def __init__(self, mainController):
        self.mainController = mainController

    def insertArtist(self):
        self.toplevel = ArtistInsertToplevel(self)

    def consultArtistAlbuns(self):
        self.toplevel = ArtistConsultToplevel(self)

    def insertSubmitHandler(self, event):
        name = self.toplevel.inputName.get()
        self.mainController.savedArtists.append(Artist(name))

        showMessage('Sucesso!', 'Artista cadastrado com sucesso')

    def consultSubmitHandler(self, event):
        name = self.toplevel.inputName.get()

        for artist in self.mainController.savedArtists:
            if name == artist.getName():
                albuns = self.mainController.getAlbunsByArtistName(name)

                message = 'Album --- Ano\n'
                for album in albuns:
                    message += album.getTitle() + '(' + album.getYear() + ')\n\nFaixas:\n'

                    for track in album.getTrackList():
                        message  += track.getTitle() + '(' + str(track.getTrackNumber()) + ')\n'

                message += '\n'
                return showMessage('Artista encontrado', message)
            
        return showMessage('Artista não encontrado', 'Artista não registrado! Tente Novamente')

    def closeHandler(self, event):
        self.toplevel.destroy()