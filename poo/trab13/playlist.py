import tkinter as tk
from tkinter import ttk

def showMessage(title, message):
    messagebox.showinfo(title, message)

class Playlist:
    def __init__(self, name, trackList):
        self.__name = name
        self.__trackList = trackList

    def getName(self):
        return self.__name

    def getTrackList(self):
        return self.__trackList

class PlaylistInsertTopLevel(tk.Toplevel):
    def __init__(self, controller, savedArtists, avaibleTrackList):
        tk.Toplevel.__init__(self)

        self.geometry('250x100')
        self.title("Playlist")

        self.frameName = tk.Frame(self)
        self.frameArtist = tk.Frame(self)
        self.frameTrackList = tk.Frame(self)
        self.frameBtn = tk.Frame(self)

        self.frameName.pack()
        self.frameArtist.pack()
        self.frameTrackList.pack()
        self.frameBtn.pack()

        self.labelName = tk.Label(self.frameName, text='Nome')
        self.labelArtist = tk.Label(self.frameArtist, text='Artista')
        self.labelTrackList = tk.Label(self.frameTrackList, text='Faixa')

        self.labelName.pack(side='left')
        self.labelArtist.pack(side='left')
        self.labelTrackList.pack(side='left')

        self.inputName = tk.Entry(self.frameName, width=20)
        self.inputName.pack(side='left')

        self.artistOptions = tk.StringVar()
        self.artistCombobox = ttk.Combobox(self.frameArtist, width = 15 , textvariable = self.artistOptions)
        self.artistCombobox.pack(side="left")
        self.artistCombobox['values'] = [artist.getName() for artist in savedArtists]

        self.updateBtn = tk.Button(self.frameBtn ,text="Buscar")      
        self.updateBtn.pack(side="right")
        self.updateBtn.bind("<Button>", controller.updateTrackList)

        self.trackListOptions = tk.StringVar()
        self.trackListCombobox = tk.Listbox(self.frameTrackList)
        self.trackListCombobox.pack(side="left")

        self.submitBtn = tk.Button(self.frameBtn ,text="Enviar")      
        self.submitBtn.pack(side="left")
        self.submitBtn.bind("<Button>", controller.insertSubmitHandler)

        self.submitBtn = tk.Button(self.frameBtn ,text="Inserir faixa")      
        self.submitBtn.pack(side="left")
        self.submitBtn.bind("<Button>", controller.insertTrackHandler)

class PlaylistConsultToplevel(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.geometry('250x100')
        self.title("Playlist")

        self.frameName = tk.Frame(self)
        self.frameBtn = tk.Frame(self)

        self.frameName.pack()
        self.frameBtn.pack()

        self.labelName = tk.Label(self.frameName, text="Título: ")
        self.labelName.pack(side="left")

        self.inputName = tk.Entry(self.frameName, width=20)
        self.inputName.pack(side="left")

        self.submitBtn = tk.Button(self.frameBtn ,text="Enviar")      
        self.submitBtn.pack(side="left")
        self.submitBtn.bind("<Button>", controller.consultSubmitHandler)
    
class PlaylistController:
    def __init__(self, mainController):
        self.trackList = []
        self.mainController = mainController
        
    def insertPlaylist(self):
        self.toplevel = PlaylistInsertTopLevel(self, self.mainController.savedArtists, self.mainController.avaibleTrackList)
    
    def consultPlaylist(self):
        self.toplevel = PlaylistConsultToplevel(self)

    def updateTrackList(self, event):
        artistName = self.toplevel.artistOptions.get()
        self.toplevel.trackListCombobox.option_clear()

        for album in self.mainController.getAlbunsByArtistName(artistName):
            for track in album.getTrackList():
                self.toplevel.trackListCombobox.insert(tk.END, track.getTitle())

            return

        return showMessage('Artista não encontrado', 'Tente Novamente')

    def insertTrackHandler(self, event):
        title = self.toplevel.trackListCombobox.get(tk.ACTIVE)
        self.trackList.append(self.mainController.getTrackByTitle(title))
        self.toplevel.trackListCombobox.delete(tk.ACTIVE)

        return showMessage('Sucesso!', 'Faixa inserida no album')

    def insertSubmitHandler(self, event):
        name = self.toplevel.inputName.get()
        
        self.mainController.savedPlaylists.append(Playlist(name, self.trackList))

        showMessage('Sucesso!', 'Playlist  cadastrada')

    def consultSubmitHandler(self, event):
        name = self.toplevel.inputName.get()

        for playlist in self.mainController.savedPlaylists:
            if playlist.getName() == name:
                message = playlist.getName() + '\nTracks\n'

                for track in playlist.getTrackList():
                    message += track.getTitle() + '(' + str(track.getTrackNumber()) + ')\n'

                return showMessage('Playlist encontrado', message)

        return showMessage('Playlist não encontrado', 'Playlist não cadastrado! Tente Novamente')
        