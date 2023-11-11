import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
from tkinter import ttk


class ConsoleInvalido(Exception):
  pass


class GeneroInvalido(Exception):
  pass


class PrecoInvalido(Exception):
  pass


class Jogo():

  def __init__(self, codigo, titulo, console, genero, preco):
    self.__codigo = codigo
    self.__titulo = titulo
    self.__console = console
    self.__genero = genero
    self.__preco = preco

    self.__listaAvaliacao = []

  @property
  def codigo(self):
    return self.__codigo

  @property
  def titulo(self):
    return self.__titulo

  @property
  def console(self):
    return self.__console

  @property
  def genero(self):
    return self.__genero

  @property
  def preco(self):
    return self.__preco

  @property
  def listaAvaliacao(self):
    return self.__listaAvaliacao

  def addAvaliacao(self, avaliacao):
    self.listaAvaliacao.append(avaliacao)


class CadastraJogo(tk.Toplevel):

  def __init__(self, controle):

    tk.Toplevel.__init__(self)
    self.geometry('300x250')
    self.title("Cadastro")
    self.controle = controle

    self.frameCodigo = tk.Frame(self)
    self.frameTitulo = tk.Frame(self)
    self.frameConsole = tk.Frame(self)
    self.frameGenero = tk.Frame(self)
    self.framePreco = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameCodigo.pack()
    self.frameTitulo.pack()
    self.frameConsole.pack()
    self.frameGenero.pack()
    self.framePreco.pack()
    self.frameButton.pack()

    self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
    self.labelCodigo.pack(side="left")
    self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
    self.inputCodigo.pack(side="left")

    self.lableTitulo = tk.Label(self.frameTitulo, text="Titulo: ")
    self.lableTitulo.pack(side="left")
    self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
    self.inputTitulo.pack(side="left")

    self.lableConsole = tk.Label(self.frameConsole, text="Console: ")
    self.lableConsole.pack(side="left")
    self.inputConsole = tk.Entry(self.frameConsole, width=20)
    self.inputConsole.pack(side="left")

    self.lableGenero = tk.Label(self.frameGenero, text="Genero: ")
    self.lableGenero.pack(side="left")
    self.inputGenero = tk.Entry(self.frameGenero, width=20)
    self.inputGenero.pack(side="left")

    self.lablePreco = tk.Label(self.framePreco, text="Preco: ")
    self.lablePreco.pack(side="left")
    self.inputPreco = tk.Entry(self.framePreco, width=20)
    self.inputPreco.pack(side="left")

    self.buttonCadastro = tk.Button(self.frameButton, text="Cadastrar")
    self.buttonCadastro.pack(side="left")
    self.buttonCadastro.bind("<Button>", controle.cadastraHandler)

    self.buttonClear = tk.Button(self.frameButton, text="Clear")
    self.buttonClear.pack(side="left")
    self.buttonClear.bind("<Button>", controle.clearHandler)

    self.buttonConcluido = tk.Button(self.frameButton, text="Concluido")
    self.buttonConcluido.pack(side="left")
    self.buttonConcluido.bind("<Button>", controle.concluidoHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class AvaliaJogo(tk.Toplevel):

  def __init__(self, controle):

    tk.Toplevel.__init__(self)
    self.geometry('250x200')
    self.title("Avaliacao")
    self.controle = controle
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
    self.comboBox = ttk.Combobox(self.frameAvaliacao,
                                 width=15,
                                 textvariable=self.escolhaCombo)
    self.comboBox.pack(side="left")
    self.comboBox['values'] = listaAvaliacao

    self.buttonAvaliar = tk.Button(self.frameButton, text="Avaliar")
    self.buttonAvaliar.pack(side="left")
    self.buttonAvaliar.bind("<Button>", controle.avaliaHandler)

    self.buttonClear = tk.Button(self.frameButton, text="Clear")
    self.buttonClear.pack(side="left")
    self.buttonClear.bind("<Button>", controle.clearAvaliaHandler)

    self.buttonClose = tk.Button(self.frameButton, text="Concluído")
    self.buttonClose.pack(side="left")
    self.buttonClose.bind("<Button>", controle.concluiAvaliaHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class ConsultaJogo(tk.Toplevel):

  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('300x250')
    self.title("Consultar Jogos")
    self.controle = controle
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
    self.comboBox = ttk.Combobox(self.frameAvaliacao,
                                 width=15,
                                 textvariable=self.escolhaCombo)
    self.comboBox.pack(side="left")
    self.comboBox['values'] = listaAvaliacao
    self.comboBox.bind('<<ComboboxSelected>>', controle.comboBoxSelect)

    self.labelJogos = tk.Label(self.frameJogos, text="Selecione o Jogo: ")
    self.labelJogos.pack(side="left")
    self.listbox = tk.Listbox(self.frameJogos)
    self.listbox.pack(side="left")

    self.buttonConsult = tk.Button(self.frameButton, text="Consultar")
    self.buttonConsult.pack(side="left")
    self.buttonConsult.bind("<Button>", controle.consultHandler)

    self.buttonClose = tk.Button(self.frameButton, text="Concluído")
    self.buttonClose.pack(side="left")
    self.buttonClose.bind("<Button>", controle.closeConsultHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class CtrlJogo():

  def __init__(self):

    if not os.path.isfile("listaJogo.pickle"):
      self.listaJogo = []
    else:
      with open("listaJogo.pickle", "rb") as f:
        self.listaJogo = pickle.load(f)

  def salvaJogo(self):
    if len(self.listaJogo) != 0:
      with open("listaJogo.pickle", "wb") as f:
        pickle.dump(self.listaJogo, f)

  def cadastraJogo(self):
    self.cadJogo = CadastraJogo(self)

  def avaliaJogo(self):
    self.limiteAvaliaJogo = AvaliaJogo(self)

  def consultaJogo(self):
    self.consultJogo = ConsultaJogo(self)

  def cadastraHandler(self, event):
    codigo = self.cadJogo.inputCodigo.get()
    titulo = self.cadJogo.inputTitulo.get()
    console = self.cadJogo.inputConsole.get().lower()
    genero = self.cadJogo.inputGenero.get().lower()
    preco = int(self.cadJogo.inputPreco.get())

    try:
      if console != 'xbox' and console != 'playstation' and console != 'switch' and console != 'pc':
        raise ConsoleInvalido()
      if genero != 'acao' and genero != 'aventura' and genero != 'estrategia' and genero != 'rpg' and genero != 'esportes' and genero != 'simulacao':
        raise GeneroInvalido()
      if preco < 0 or preco > 500:
        raise PrecoInvalido()
    except ConsoleInvalido:
      msg = 'Console Invalido'
      self.cadJogo.mostraJanela('ERRO', msg)

    except GeneroInvalido:
      msg = 'Genero Invalido'
      self.cadJogo.mostraJanela('ERRO', msg)

    except PrecoInvalido:
      msg = 'Preco Invalido'
      self.cadJogo.mostraJanela('ERRO', msg)

    else:
      console = self.cadJogo.inputConsole.get()
      genero = self.cadJogo.inputGenero.get()
      jogo = Jogo(codigo, titulo, console, genero, preco)
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
