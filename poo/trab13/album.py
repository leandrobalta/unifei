import tkinter as tk
from tkinter import messagebox

def showMessage(title, message):
    messagebox.showinfo(title, message)

class Album():
    def __init__(self, titulo, ano):
        self.__titulo = titulo
        self.__ano = ano

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

class ContentSubAlbum(tk.Toplevel):
    def __init__(self, controller, avaibleTrackList):
        tk.Toplevel.__init__(self)

        self.geometry('250x100')
        self.title("Album")

        self.frameTitle = tk.Frame(self)
        self.frameYear = tk.Frame(self)
        self.frameArtistName = tk.Frame(self)
        self.frameMusicList = tk.Frame(self)
        self.frameButt = tk.Frame(self)

        self.frameTitle.pack()
        self.frameYear.pack()
        self.frameArtistName.pack()
        self.frameMusicList.pack()
        self.frameButt.pack()

        self.labelTitle = tk.Label(self.frameTitle, text="Título: ")
        self.labelTitle.pack(side="left")
        self.labelYear = tk.Label(self.frameYear, text="Ano: ")
        self.labelYear.pack(side="left")
        self.labelArtistName = tk.Label(self.frameArtistName, text="Artista: ")
        self.labelArtistName.pack(side="left")
        self.labelTrackListName = tk.Label(self.frameMusicList, text="Faixas: ")
        self.labelTrackListName.pack(side="left")

        self.inputTitle = tk.Entry(self.frameTitle, width=20)
        self.inputTitle.pack(side="left")
        self.inputYear = tk.Entry(self.frameYear, width=20)
        self.inputYear.pack(side="left")
        self.inputArtistName = tk.Entry(self.frameArtistName, width=20)
        self.inputArtistName.pack(side="left")

        self.trackListOptions = tk.StringVar()
        self.trackListCombobox = tk.Listbox(self.frameMusicList)
        self.trackListCombobox.pack(side="left")
        
        for track in avaibleTrackList:
            self.trackListCombobox.insert(tk.END, track.getTitle())

        self.insertTrackBtn = tk.Button(self.frameButt ,text="Insere faixa")           
        self.insertTrackBtn.pack(side="left")
        self.insertTrackBtn.bind("<Button>", controller.insertTrackHandler)

        self.submitBtn = tk.Button(self.frameButt ,text="Enviar")      
        self.submitBtn.pack(side="left")
        self.submitBtn.bind("<Button>", controller.submitHandler)

        self.buttonClose = tk.Button(self.frameButt ,text="Concluído")      
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controller.closeHandler)


class ContentConsultAlbum(tk.Toplevel):
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

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class AlbumController():
    def __init__(self, mainController):
        self.mainController = mainController

    def insertAlbum(self):
        self.trackList = []
        self.toplevel = ContentSubAlbum(self, self.mainController.avaibleTrackList)

    def consultAlbumByTitle(self):
        self.toplevel = ContentSubAlbum(self)

    def submitHandler(self, event):
        title = self.toplevel.inputTitle.get()
        year = self.toplevel.inputYear.get()
        artist = self.mainController.getArtistByName(self.toplevel.inputArtistName.get())
        self.mainController.savedAlbuns.append(Album(title, year, artist, self.trackList))

        ('Sucesso!', 'Album cadastrado com sucesso')

    def insertTrackHandler(self, event):
        title = self.toplevel.trackListCombobox.get(tk.ACTIVE)
        self.trackList.append(self.mainController.getTrackByTitle(title))
        self.toplevel.trackListCombobox.delete(tk.ACTIVE)

        showMessage('Sucesso!', 'Faixa inserida no album')

    def consultSubmitHandler(self, event):
        title = self.toplevel.inputTitle.get()
        for album in self.mainController.savedAlbuns:
            if title == album.getTitle():
                message = 'Album: {}\nArtista: {}\nAno: {}\nFaixas: \n'.format(album.getTitle(), album.getArtist().getName(), album.getYear())

                for track in album.getTrackList():
                    message += track.getTitle() + '(' + str(track.getTrackNumber()) + ')\n'

                return showMessage('Album encontrado', message)
            
        return showMessage('Album não encontrado', 'Album não cadastrado! Tente Novamente')

    def closeHandler(self, event):
        self.toplevel.destroy()