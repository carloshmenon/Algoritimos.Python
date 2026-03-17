import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk, messagebox

# --- CONFIGURAÇÃO DE CONEXÃO ---
def conectar():
    try:
        return mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='db_usuario'
        )
    except Error as e:
        messagebox.showerror("Erro de Conexão", f"Falha ao conectar: {e}")
        return None

# --- PASSO 2: IMPLEMENTAR AS FUNÇÕES CRUD ---

def criar_usuario():
    nome = input_nome.get()
    email = input_email.get()
    cpf = input_cpf.get()

    if nome == "" or email == "":
        messagebox.showwarning("Aviso", "Preencha Nome e Email!")
        return

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        # Comando: INSERT INTO
        sql = "INSERT INTO usuario (nome, email, CPF) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, cpf))
        conexao.commit()
        cursor.close()
        conexao.close()
        limpar_campos()
        ler_usuarios() # Atualiza a tabela na tela

def ler_usuarios():
    # Comando: SELECT
    # Limpa a tabela visual antes de recarregar
    for item in tabela.get_children():
        tabela.delete(item)
    
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, CPF FROM usuario")
        for linha in cursor.fetchall():
            tabela.insert("", "end", values=linha)
        cursor.close()
        conexao.close()

def atualizar_usuario():
    selecionado = tabela.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione alguém para editar!")
        return
    
    id_usuario = tabela.item(selecionado)['values'][0]
    nome = input_nome.get()
    email = input_email.get()
    cpf = input_cpf.get()

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE usuario SET nome=%s, email=%s, CPF=%s WHERE id=%s"
        cursor.execute(sql, (nome, email, cpf, id_usuario))
        conexao.commit()
        cursor.close()
        conexao.close()
        ler_usuarios()
        limpar_campos()

def deletar_usuario():
    selecionado = tabela.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione alguém para excluir!")
        return
    
    id_usuario = tabela.item(selecionado)['values'][0]
    
    if messagebox.askyesno("Confirmar", "Deseja excluir este usuário?"):
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            # Comando: DELETE
            sql = "DELETE FROM usuario WHERE id=%s"
            cursor.execute(sql, (id_usuario,))
            conexao.commit()
            cursor.close()
            conexao.close()
            ler_usuarios()
            limpar_campos()


def limpar_campos():
    input_nome.delete(0, tk.END)
    input_email.delete(0, tk.END)
    input_cpf.delete(0, tk.END)

def ao_selecionar(event):
    selecionado = tabela.selection()
    if selecionado:
        valores = tabela.item(selecionado)['values']
        limpar_campos()
        input_nome.insert(0, valores[1])
        input_email.insert(0, valores[2])
        input_cpf.insert(0, valores[3])


janela = tk.Tk()
janela.title("Gerenciador db_usuario")
janela.geometry("600x500")

# Entradas
tk.Label(janela, text="Nome:").pack()
input_nome = tk.Entry(janela, width=40)
input_nome.pack()

tk.Label(janela, text="Email:").pack()
input_email = tk.Entry(janela, width=40)
input_email.pack()

tk.Label(janela, text="CPF:").pack()
input_cpf = tk.Entry(janela, width=40)
input_cpf.pack()

# Botões CRUD
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Criar", command=criar_usuario, bg="green", fg="white").pack(side="left", padx=5)
tk.Button(frame_botoes, text="Atualizar", command=atualizar_usuario, bg="orange").pack(side="left", padx=5)
tk.Button(frame_botoes, text="Excluir", command=deletar_usuario, bg="red", fg="white").pack(side="left", padx=5)

# Tabela
colunas = ("ID", "Nome", "Email", "CPF")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=100)
tabela.pack(fill="both", expand=True, padx=10, pady=10)
tabela.bind("<<TreeviewSelect>>", ao_selecionar)

# Carregar dados ao abrir
ler_usuarios()

janela.mainloop()