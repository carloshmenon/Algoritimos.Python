
import tkinter as tk
from tkinter import messagebox
from random import randrange

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha - PC vs Você")
        
        # Estrutura do Tabuleiro (Lista de Listas)
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        
        # Dicionário para mapear os botões da interface
        self.buttons = {}
        self.create_widgets()
        
        # Computador começa no centro (Posição '5' -> board[1][1])
        self.computer_start()

    def create_widgets(self):
        # Cria os 9 botões (3x3)
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                                command=lambda r=row, c=col: self.player_move(r, c))
                btn.grid(row=row, column=col)
                self.buttons[(row, col)] = btn

    def computer_start(self):
        # Regra: Computador joga no centro primeiro
        row, col = 1, 1
        self.board[row][col] = 'X'
        self.update_interface()

    def player_move(self, row, col):
        # Verifica se a posição está livre (se contém um número)
        if self.board[row][col] not in ['X', 'O']:
            self.board[row][col] = 'O'
            self.update_interface()
            
            if not self.check_end_game():
                self.root.after(500, self.computer_move) # Pequeno delay para parecer real

    def computer_move(self):
        # Coleta posições livres
        free_positions = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] not in ['X', 'O']:
                    free_positions.append((r, c))
        
        if free_positions:
            # Jogada aleatória usando randrange
            idx = randrange(len(free_positions))
            row, col = free_positions[idx]
            self.board[row][col] = 'X'
            self.update_interface()
            self.check_end_game()

    def update_interface(self):
        # Sincroniza a lista de listas com os botões do Tkinter
        for r in range(3):
            for c in range(3):
                value = self.board[r][c]
                if value in ['X', 'O']:
                    self.buttons[(r, c)].config(text=value, state="disabled", disabledforeground="black")
                else:
                    self.buttons[(r, c)].config(text="")

    def check_winner(self):
        # Verifica linhas, colunas e diagonais
        for i in range(3):
            # Linhas
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            # Colunas
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        
        # Diagonais
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        
        return None

    def check_end_game(self):
        winner = self.check_winner()
        
        if winner:
            msg = "Você venceu!" if winner == 'O' else "O computador venceu!"
            messagebox.showinfo("Fim de jogo", msg)
            self.root.destroy()
            return True
            
        # Verifica empate (se não há mais números no board)
        flat_board = [item for sublist in self.board for item in sublist]
        if not any(x.isdigit() for x in flat_board):
            messagebox.showinfo("Fim de jogo", "Deu empate!")
            self.root.destroy()
            return True
            
        return False

# Inicialização
if __name__ == "__main__":
    root = tk.Tk()
    game = JogoDaVelha(root)
    root.mainloop()