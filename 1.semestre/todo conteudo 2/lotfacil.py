import itertools

# Suas 17 dezenas escolhidas
dezenas_escolhidas = [1, 2, 3, 4, 5, 6, 10, 11, 13, 14, 16, 17, 20, 22, 23, 24, 25]

# Gerar todas as combinações de 15 dezenas
combinacoes = list(itertools.combinations(dezenas_escolhidas, 15))

print(f"Total de jogos gerados: {len(combinacoes)}\n")
print("Alguns exemplos dos jogos gerados:")
for i, jogo in enumerate(combinacoes[:10]):  # Exibir os primeiros 10 jogos
    print(f"Jogo {i+1}: {', '.join(f'{n:02d}' for n in sorted(jogo))}")

# Para obter a lista completa de jogos, você pode executá-lo em seu ambiente Python.
# Ou se desejar, posso gerar e fornecer a lista completa em um formato específico (e.g., CSV).