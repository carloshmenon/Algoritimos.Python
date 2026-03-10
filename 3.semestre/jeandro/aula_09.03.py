import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
contador_id=1
def novo_usuario():
    global contador_id
    nome= input_nome.get()
    email= input_email.get()
    endereco= input_endereco.get()

    if nome =="" or email =="" or endereco =="":
        messagebox.showerror("Erro", "Aviso", "nome, email e endereço são obrigatórios")
        return
    tabela.insert("", "end", values=(contador_id, nome, email, endereco))
    contador_id += 1

    limpar_campos()

def selecionar_usuario(event):
    selecionado= tabela.selection()

    if selecionado:
        limpar_campos()
        valores= tabela.item(selecionado, "values")
        input_id.insert(0, valores[0])
        input_nome.insert(0, valores[1])
        input_email.insert(0, valores[2])
        input_endereco.insert(0, valores[3])
        
def limpar_campos():
    input_id.delete(0, tk.END)
    input_nome.delete(0, tk.END)
    input_email.delete(0, tk.END)
    input_endereco.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Usuario")
janela.geometry("750x450")
 
frame_form = tk.Frame(janela)
frame_form.pack(pady=10)
 
tk.Label(frame_form, text="ID").grid(row=0, column=0, padx=5, sticky="e")
input_id = tk.Entry(frame_form, width=10)
input_id.grid(row=0, column=1, padx=5)
 
tk.Label(frame_form, text="Nome").grid(row=1, column=0, padx=5, sticky="e")
input_nome = tk.Entry(frame_form, width=10)
input_nome.grid(row=1, column=1, padx=5)
 
tk.Label(frame_form, text="Email").grid(row=2, column=0, padx=5, sticky="e")
input_email = tk.Entry(frame_form, width=10)
input_email.grid(row=2, column=1, padx=5)
 
tk.Label(frame_form, text="Endereço").grid(row=3, column=0, padx=5, sticky="e")
input_endereco = tk.Entry(frame_form, width=10)
input_endereco.grid(row=3, column=1, padx=5)
 
#botões
frame_button = tk.Frame(janela)
frame_button.pack(pady=10)
 
btn_novo = tk.Button(frame_button, text="Novo", width=10, command="").grid(row=0, column=0, padx=5)
btn_editar = tk.Button(frame_button, text="Editar", width=10, command="").grid(row=0, column=1, padx=5)
btn_excluir = tk.Button(frame_button, text="Excluir", width=10, command="").grid(row=0, column=2, padx=5)
btn_limpar = tk.Button(frame_button, text="Limpar", width=10, command="").grid(row=0, column=3, padx=5)
 
#TABELA

colunas = ("ID", "NOME", "EMAIL", "ENDEREÇO")

tabela= ttk.Treeview(janela, columns= colunas, show="headings")

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=170)

tabela.pack(fill="both", expand=True, padx=20, pady=20)
tabela.bind("<<TreeviewSelect>>", selecionar_usuario)
 
 
 
 
 
janela.mainloop()