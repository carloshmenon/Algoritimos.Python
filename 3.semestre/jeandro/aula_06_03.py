import tkinter as tk
 
def abrir_janela_novo_usuario():
    janela_usuario= tk.Toplevel()
    janela_usuario.title("novo usuario")
    janela_usuario .geometry("300x200")

    tk.Label(janela_usuario, text="nome: ").grid(row=0, column=0, padx=10, pady=5)
    input_nome = tk.Entry(janela_usuario, width=35)
    input_nome.grid(row=0, column=1, padx=10, pady=5)
    tk.Label(janela_usuario, text="email: ").grid(row=1, column=0, padx=10, pady=5)
    input_email = tk.Entry(janela_usuario, width=35)
    input_email.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(janela_usuario, text="endereço:").grid(row=2, column=0, padx=10, pady=5)
    input_endereco= tk.Entry(janela_usuario, width=35)
    input_endereco.grid(row=2, column=1, padx=10, pady=5)

    def salvar_usuario():
        nome = input_nome.get()
        email = input_email.get()
        endereco= input_endereco.get()

        lista_usuario.insert(tk.END, f"Nome: {nome} - Email: {email} - Endereço: {endereco}")
        janela_usuario. destroy()

    btn_salvar= tk.Button(janela_usuario, text="salvar", command=salvar_usuario)
    btn_salvar.grid(row=3, column=1, padx=10, pady=10, sticky="w")


janela = tk.Tk()
janela.title ("cadastro de usuario")
janela.geometry("405x300")

menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)

menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="sair", command=janela.quit)
menu_arquivo.add_command(label="sair 2", command=janela.quit)

menu_usuario = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="usuario", menu=menu_usuario)
menu_usuario.add_command(label="cadastrar", command=janela.quit)
menu_usuario.add_command(label="alterar", command=janela.quit)

btn_cad= tk.Button(janela, text="novo cadastro", command=abrir_janela_novo_usuario)
btn_cad.grid(row=0, column=0, padx=10, pady=10, sticky="w")

lista_usuario= tk.Listbox(janela, width=63)
lista_usuario.grid(row=1, column=0, padx=10, pady=10)

janela.mainloop()


