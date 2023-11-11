import tkinter as tk
import exceptions as e

class Game:
    def __init__(self, code, title, console, gen, price):
        self.code = code
        self.title = title
        self.console = console
        self.gen = gen
        self.price = price
        self.rating = []

    @property
    def code(self):
        return self.code

    @property
    def title(self):
        return self.title

    @property
    def console(self):
        return self.console

    @property
    def gen(self):
        return self.gen

    @property
    def price(self):
        return self.price

    @property
    def rating(self):
        return self.rating

    def addAvaliacao(self, avaliacao):
        self.rating.append(avaliacao)


class GameConsultView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.controller = controller

        self.geometry("250x150")
        self.title("Consulta de Jogos")

        listaAvaliacao = '1 Estrela', '2 Estrelas', '3 Estrelas', '4 Estrelas', '5 Estrelas'

        self.frameAvaliacao = tk.Frame(self)
        self.frameJogos = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameAvaliacao.pack()
        self.frameJogos.pack()
        self.frameButton.pack()

        self.labelAvaliacao = tk.Label(self.frameAvaliacao,
                                        text="Selecione por Avaliacao: ")
        self.labelAvaliacao.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.comboBox = tk.Combobox(self.frameAvaliacao,
                                        width=15,
                                        textvariable=self.escolhaCombo)
        self.comboBox.pack(side="left")
        self.comboBox['values'] = listaAvaliacao
        self.comboBox.bind('<<ComboboxSelected>>', controller.comboBoxSelect)

        self.labelJogos = tk.Label(self.frameJogos, text="Selecione o Jogo: ")
        self.labelJogos.pack(side="left")
        self.listbox = tk.Listbox(self.frameJogos)
        self.listbox.pack(side="left")

        self.buttonConsult = tk.Button(self.frameButton, text="Consultar")
        self.buttonConsult.pack(side="left")
        self.buttonConsult.bind("<Button>", controller.consultHandler)

        self.buttonClose = tk.Button(self.frameButton, text="Concluído")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controller.closeConsultHandler)



class GameRatingView(tk.Toplevel):
    def __init__(self, controller):
        self.controller = controller
        tk.Toplevel.__init__(self)

        self.geometry("250x150")
        self.title("Avaliação de Jogos")

        listaAvaliacao = '1 Estrela', '2 Estrelas', '3 Estrelas', '4 Estrelas', '5 Estrelas'

        self.frameCodigo = tk.Frame(self)
        self.frameAvaliacao = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameAvaliacao.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")

        self.labelAvaliacao = tk.Label(self.frameAvaliacao, text="Avaliar: ")
        self.labelAvaliacao.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.comboBox = tk.Combobox(self.frameAvaliacao,
                                    width=15,
                                    textvariable=self.escolhaCombo)
        self.comboBox.pack(side="left")
        self.comboBox['values'] = listaAvaliacao

        self.buttonAvaliar = tk.Button(self.frameButton, text="Avaliar")
        self.buttonAvaliar.pack(side="left")
        self.buttonAvaliar.bind("<Button>", self.controller.avaliaHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", self.controller.clearAvaliaHandler)

        self.buttonClose = tk.Button(self.frameButton, text="Concluído")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", self.controller.concluiAvaliaHandler)

class GameSubscribeView(tk.Toplevel):
    def __init__(self, controller):
        self.controller = controller
        tk.Toplevel.__init__(self)

        self.geometry("250x150")
        self.title("Cadastro de jogos")

        self.codeFrame = tk.Frame(self)
        self.titleFrame = tk.Frame(self)
        self.consoleFrame = tk.Frame(self)
        self.genFrame = tk.Frame(self)
        self.priceFrame = tk.Frame(self)
        self.buttonFrame = tk.Frame(self)

        self.codeFrame.pack()
        self.titleFrame.pack()
        self.consoleFrame.pack()
        self.genFrame.pack()
        self.priceFrame.pack()
        self.buttonFrame.pack()

        self.codeLabel = tk.Label(self.codeFrame, text="Codigo")
        self.codeLabel.pack(side="left")

        self.codeEntry = tk.Entry(self.codeFrame, width=20)
        self.codeEntry.pack(side="left")

        self.titleLabel = tk.Label(self.titleFrame, text="Titulo")
        self.titleLabel.pack(side="left")

        self.titleEntry = tk.Entry(self.titleFrame, width=20)
        self.titleEntry.pack(side="left")

        self.consoleLabel = tk.Label(self.consoleFrame, text="Console")
        self.consoleLabel.pack(side="left")

        self.consoleEntry = tk.Entry(self.consoleFrame, width=20)
        self.consoleEntry.pack(side="left")

        self.genLabel = tk.Label(self.genFrame, text="Genero")
        self.genLabel.pack(side="left")

        self.genEntry = tk.Entry(self.genFrame, width=20)
        self.genEntry.pack(side="left")

        self.priceLabel = tk.Label(self.priceFrame, text="Preço")
        self.priceLabel.pack(side="left")

        self.priceEntry = tk.Entry(self.priceFrame, width=20)
        self.priceEntry.pack(side="left")

        self.okButt = tk.Button(self.buttonFrame, text="Concluido")
        self.okButt.pack(side="left")
        self.okButt.bind("<Button>", self.controller.SubscribeHandler)


class GameController:
    def __init__(self, mainController):
        self.mainController = mainController

    def Consult(self):
        self.__consult = GameConsultView(self)

    def Rating(self):
        self.__rating = GameRatingView(self)

    def Subscribe(self):
        self.__subscribe = GameSubscribeView(self)

    def SubscribeHandler(self, event):
        codigo = self.__subscribe.codeEntry.get()
        titulo = self.__subscribe.titleEntry.get()
        console = self.__subscribe.consoleEntry.get().lower()
        genero = self.__subscribe.genEntry.get().lower()
        preco = int(self.__subscribe.priceEntry.get())

        try:
            if console != 'xbox' and console != 'playstation' and console != 'switch' and console != 'pc':
                raise e.ConsoleInvalido()
            if genero != 'acao' and genero != 'aventura' and genero != 'estrategia' and genero != 'rpg' and genero != 'esportes' and genero != 'simulacao':
                raise e.GeneroInvalido()
            if preco < 0 or preco > 500:
                raise e.PrecoInvalido()
        except e.ConsoleInvalido:
            msg = 'Console Invalido'
            self.cadJogo.mostraJanela('ERRO', msg)

        except e.GeneroInvalido:
            msg = 'Genero Invalido'
            self.cadJogo.mostraJanela('ERRO', msg)

        except e.PrecoInvalido:
            msg = 'Preco Invalido'
            self.cadJogo.mostraJanela('ERRO', msg)

        else:
            console = self.cadJogo.inputConsole.get()
            genero = self.cadJogo.inputGenero.get()
            jogo = Game(codigo, titulo, console, genero, preco)
            self.listaJogo.append(jogo)
            msg = 'Jogo Cadastrado'
            self.cadJogo.mostraJanela('Sucesso', msg)
            self.clearHandler(event)

    def clearHandler(self, event):
        self.cadJogo.inputCodigo.delete(0, len(self.cadJogo.inputCodigo.get()))
        self.cadJogo.inputConsole.delete(0, len(self.cadJogo.inputConsole.get()))
        self.cadJogo.inputGenero.delete(0, len(self.cadJogo.inputGenero.get()))
        self.cadJogo.inputTitulo.delete(0, len(self.cadJogo.inputTitulo.get()))
        self.cadJogo.inputPreco.delete(0, len(self.cadJogo.inputPreco.get()))

    def concluidoHandler(self, event):
        self.cadJogo.destroy()

    def avaliaHandler(self, event):
        msg = None
        codigo = self.limiteAvaliaJogo.inputCodigo.get()
        avaliacao = self.limiteAvaliaJogo.comboBox.get()

        for i in range(5):
            nmr = i + 1
            msg1 = str(nmr) + ' Estrela'
            msg2 = str(nmr) + ' Estrelas'
            if avaliacao == msg1 or avaliacao == msg2:
                avaliacao = nmr
                break

        for jg in self.listaJogo:
            if codigo == jg.codigo:
                jg.addAvaliacao(avaliacao)
                msg = 'Avaliacao Realizada'
                break
        if msg == None:
            msg = 'Codigo nao encontrado'
            self.limiteAvaliaJogo.mostraJanela('Erro', msg)
        else:
            self.limiteAvaliaJogo.mostraJanela('Sucesso', msg)

    def clearAvaliaHandler(self, event):
        self.limiteAvaliaJogo.inputCodigo.delete(
        0, len(self.limiteAvaliaJogo.inputCodigo.get()))
        self.limiteAvaliaJogo.comboBox.delete(
        0, len(self.limiteAvaliaJogo.comboBox.get()))

    def concluiAvaliaHandler(self, event):
        self.limiteAvaliaJogo.destroy()

    def comboBoxSelect(self, event):
        listaJogos = []
        pnts = 0
        avaliacao = self.consultJogo.comboBox.get()
        for i in range(5):
            nmr = i + 1
            msg1 = str(nmr) + ' Estrela'
            msg2 = str(nmr) + ' Estrelas'
            if avaliacao == msg1 or avaliacao == msg2:
                avaliacao = nmr

        for jg in self.listaJogo:
            for i in range(len(jg.listaAvaliacao)):
                pnts += int(jg.listaAvaliacao[i])

        #calcula a media das avaliações
        pnts = pnts / len(jg.listaAvaliacao)
        if 0 <= pnts and pnts <= 1: pnts = 1
        elif 1 < pnts and pnts <= 2: pnts = 2
        elif 2 < pnts and pnts <= 3: pnts = 3
        elif 3 < pnts and pnts <= 4: pnts = 4
        elif 4 < pnts and pnts <= 5: pnts = 5

        if avaliacao == pnts:
            listaJogos.append(jg.titulo)
        self.consultJogo.listbox.delete(0, tk.END)
        for jg in listaJogos:
            self.consultJogo.listbox.insert(tk.END, jg)

    def consultHandler(self, event):
        msg = ''
        jogo = self.consultJogo.listbox.get(tk.ACTIVE)
        for jg in self.listaJogo:
            if jogo == jg.titulo:
                msg += 'Codigo: ' + jg.codigo + '\n'
                msg += 'Titulo: ' + jg.titulo + '\n'
                msg += 'Console: ' + jg.console + '\n'
                msg += 'Genero: ' + jg.genero + '\n'
                msg += 'Preco: ' + str(jg.preco) + '\n'
                break

        self.consultJogo.mostraJanela('Consulta', msg)

    def closeConsultHandler(self, event):
        self.consultJogo.destroy()
