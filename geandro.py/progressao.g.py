



import time

def pg(a1, q, n):
    result = a1  # Começa com o primeiro termo
    for i in range(n):  # Laço para gerar os n termos
        print(result)  # Exibe o termo atual
        result *= q  # Atualiza o termo para o próximo
    return result

# Medir o tempo de execução
inicio = time.time()

# Exemplo de uso
pg(1, 2, 5)  # a1=1, q=2, n=5 (Progressão Geométrica com 5 termos)

fim = time.time()
tempo = fim - inicio

print("Tempo de execução: ", tempo)
