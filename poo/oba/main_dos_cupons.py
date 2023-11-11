import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
import Produto as prod
import cupom as nf

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry("500x400")
        self.menubar = tk.Menu(self.root)
        self.produto = tk.Menu(self.menubar)
        self.cupom = tk.Menu(self.menubar)
        self.salva = tk.Menu(self.menubar)
        self.sair = tk.Menu(self.menubar)

        self.produto.add_command(label="Insere", command=self.controle.insereProdutos)
        self.produto.add_command(label="Consulta", command=self.controle.consultaProdutos)
        self.menubar.add_cascade(label="Produto", menu=self.produto)

        self.cupom.add_command(label="Insere", command=self.controle.insereCupom)
        self.cupom.add_command(label="Consulta", command=self.controle.consultaCupom)
        self.menubar.add_cascade(label="Cupom", menu=self.cupom)

        self.salva.add_command(label="Salvar os Dados", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Salvar", menu=self.salva)

        self.sair.add_command(label="Sair do Programa", command=self.controle.sair)
        self.menubar.add_cascade(label="Sair", menu=self.sair)

        self.root.config(menu=self.menubar)
    
    def mostraMessagebox(self, titulo, mensagem):   
        messagebox.showinfo(titulo, mensagem)
        
class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = prod.CtrlProduto()
        self.ctrlCupom = nf.CtrlNotaFiscal(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title('Sistema de Nota Fiscal')
        self.root.mainloop()
    
    def insereProdutos(self):
        self.ctrlProduto.insereProdutos(self.root)
    
    def consultaProdutos(self):
        self.ctrlProduto.consultaProdutos(self.root)

    def insereCupom(self):
        self.ctrlCupom.insereCupom(self.root)

    def consultaCupom(self):
        self.ctrlCupom.consultaCupom(self.root)

        
    def salvaDados(self):
        self.ctrlProduto.salvaProdutos()
        self.ctrlCupom.salvaNotaFiscals()
        self.limite.mostraMessagebox('Backup', 'Dados salvos com sucesso')
        
    def sair(self):
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()