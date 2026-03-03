
import tkinter as tk
from tkinter import messagebox

janela=tk.Tk()
janela.title("jogo da velha")

jogador = "x"
botoes=[]

def clicar(botao):
    global jogador
    if botao ["text"] =="":
        botao["text"]=jogador
        verificar_vitoria()
        jogador="0" if jogador=="x" else "x"

    def verificar_vitoria():
        combinacoes=[
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
    
        for c in combinacoes:
            if(botoes[c[0]]["text"] !="" and
           botoes[c[0]]["text"]==botoes[c[1]]["text"]== botoes[c[2]]["text"]):
                messagebox.showinfo("fim de jogo",f"jogador{botoes[c[0]]["text"]}venceu!")
                reiniciar_jogo()

def reiniciar_jogo():
    global jogador 
    jogador="x"

    for botao in botoes:
        botao["text"]=""
        for i in range(9):
            botao=tk.Button(janela,text="", width=10, height=4, command=lambda b=i: clicar(botoes[b])) 
        botao.grid(row=i//3, column=i%3)

        botoes.append(botao)

janela.mainloop()