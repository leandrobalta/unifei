import tkinter as tk
from tkinter import messagebox
import album 
import artista
import musica
import playlist

class Content():
    def __init__(self, tkinter, controller):
        self.controller = controller
        self.tkinter = tkinter

        self.tkinter.geometry('300x200')

        # Welcome Message
        self.welcomeMsg = tk.Text(self.tkinter, text = "Bem-Vindo ao Soundzz")
        self.welcomeMsg.pack()

        # Menu Bar configs
        self.menu = tk.Menu(self.tkinter)        
        self.artistaMenu = tk.Menu(self.menu)
        self.albumMenu = tk.Menu(self.menu)
        self.playlistMenu = tk.Menu(self.menu)     


        #Artista configs 
        self.artistaMenu.add_command(label="Cadastrar", command=self.controller.SubscribeArtist)
        self.artistaMenu.add_command(label='Consultar', command=self.controller.ConsultArtist)
        self.menu.add_cascade(label="Artista", menu=self.artistaMenu)

        #Album configs
        self.albumMenu.add_command(label="Cadastrar", command=self.controller.SubscribeAlbum)
        self.albumMenu.add_command(label='Consultar', command=self.controller.ConsultAlbum)    
        self.menu.add_cascade(label="Album", menu=self.albumMenu)

        #Playlist configs
        self.playlistMenu.add_command(label="Cadastrar", command=self.controller.SubscribePlaylist)
        self.playlistMenu.add_command(label='Consultar', command=self.controller.ConsultPlaylist)               
        self.menu.add_cascade(label="Playlist", menu=self.playlistMenu)        

        self.tkinter.config(menu=self.menu)

      
class ContentController():       
    def __init__(self):
        self.avaibleTrackList = [Track('Exemplo1', 0), Track('Exemplo2', 1), Track('Exemplo3', 2)]
        
        self.savedArtists = []
        self.savedAlbuns = []
        self.savedPlaylists = []
        
        self.artistController = ArtistController(self)
        self.albumController = AlbumController(self)
        self.playlistController = PlaylistController(self)
       
    def insertArtist(self):
        self.artistController.insertArtist()

    def consultArtist(self):
        self.artistController.consultArtistAlbuns()

    def insertAlbum(self):
        self.albumController.insertAlbum()

    def consultAlbum(self):
        self.albumController.consultAlbumByTitle()

    def getArtistByName(self, searchedArtistName):
        for artist in self.savedArtists:
            if artist.getName() == searchedArtistName:
                return artist

        return ''

    def getAlbunsByArtistName(self, artistName):
        foundedAlbuns = []

        for album in self.savedAlbuns:
            if album.getArtist().getName() == artistName:
                foundedAlbuns.append(album)

        return foundedAlbuns

    def getTrackByTitle(self, title):
        for track in self.avaibleTrackList:
            if track.getTitle() == title:
                return track

    def insertPlaylist(self):
        self.playlistController.insertPlaylist()

    def consultPlaylist(self):
        self.playlistController.consultPlaylist()

if __name__ == '__main__':
    run = ContentController()