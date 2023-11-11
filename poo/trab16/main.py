import tkinter as tk
from components import curso 
from components import estudante

class MainView:
    def __init__(self, tkinter, controller):
        self.tk = tkinter
        self.controller = controller

        self.tk.geometry("300x200")
        self.tk.title("Campeonato de Futebol UNIFEI")
        
        self.menuBar = tk.Menu(self.tk)

        self.menuBar.add_command(label="Criação de equipes", command=self.controller.CallCreateTeam)
        self.menuBar.add_command(label="Consulta de equipes", command=self.controller.CallConsultTeam)
        self.menuBar.add_command(label="Dados do Campeonato", command=self.controller.CallCampData)

        self.tk.config(menu=self.menuBar)


class MainController:
    def __init__(self) -> None:
        self.tkinter = tk.Tk()
        
        #tkinter configs
        self.view = MainView(self.tkinter, self)
    
        c1 = curso.Curso("CCO", "Ciencia da COmputação")
        c2 = curso.Curso("SIN", "Sistemas de informação")
        c3 = curso.Curso("EEL", "Engenharia Eletrica")

        listaCurso = []
        listaCurso.append(c1)
        listaCurso.append(c2)
        listaCurso.append(c3)

        listaEstudante = []
        listaEstudante.append(estudante.Estudante(1001, "Ana", c1))
        listaEstudante.append(estudante.Estudante(1002, "Leandro", c2))
        listaEstudante.append(estudante.Estudante(1003, "Beto", c3))
        listaEstudante.append(estudante.Estudante(1004, "Renno", c1))
        listaEstudante.append(estudante.Estudante(1005, "Canas", c2))
        listaEstudante.append(estudante.Estudante(1006, "Leão", c3))
        listaEstudante.append(estudante.Estudante(1007, "Shand", c1))
        listaEstudante.append(estudante.Estudante(1008, "Murilo", c2))
        listaEstudante.append(estudante.Estudante(1009, "JV", c3))
        listaEstudante.append(estudante.Estudante(1010, "Adryan", c1))

        self.tkinter.mainloop()

    def CallCreateTeam(self):
        pass

    def CallConsultTeam(self):
        pass

    def CallCampData(self):
        pass

if __name__== "__main__":
    run = MainController()