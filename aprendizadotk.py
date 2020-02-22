# O Meu objetivo é conseguir criar TXT's usando tkinter, pois vou aprender mais sobre funções e parametros

enc = 'UTF-8'
from tkinter import *
from ferramentas import *
#Propiedades Janela principal
janelaPrincipal = Tk()
janelaPrincipal.geometry("450x400")
janelaPrincipal.title("Janela Principal")
janelaPrincipal["bg"] = ("gray")

variavelTeste = 0 # Crio uma variavel para poder atribuir o valor do entry "valorPastas" referido logo a função abaixo
def peganumero(valorPastas): # Função para receber um numero, ja que no Button o Command=função(Não da pra colocar parametro, pois com parenteses ele executa a função assim que lê)
    variavelTeste = valorPastas
    criausers(variavelTeste)

def janelaAdiciona(): # Janela para o recebimento do valor da criação dos TXT
    #propiedades da janela secundaria
    janelaAdciona = Tk()
    janelaAdciona.geometry("450x600")
    janelaAdciona.title("Janela Principal")
    janelaAdciona["bg"] = ("gray")
    #labels janela secundaria
    infoQtusers = Label(janelaAdciona,font="arial",text="Quantos usuarios quer adicionar?",background="lightgray")
    infoQtusers.place(x=90,y=85)
    infoAddsucess = Label(janelaAdciona,font="arial",text="teste",background="lightgray")
    infoAddsucess.place(x=100,y=275)
    #entrys
    valorPastas = Entry(janelaAdciona,font="arial")
    valorPastas.place(x=100,y=150)
    #Buttons
    criaPastas = Button(janelaAdciona,font="arial",text="Adicionar Usuarios",height='2',command=peganumero)
    criaPastas.place(x=120,y=210)

    janelaAdciona.mainloop()

# Unico botão da janela principal
btAbreJanelaUser = Button(janelaPrincipal,font="arial",height="2",text="Adicionar Usuarios",command=janelaAdiciona)
btAbreJanelaUser.place(x=145,y=150)

janelaPrincipal.mainloop()