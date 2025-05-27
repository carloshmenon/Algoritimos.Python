
candi1 = 0
candi2 = 0
candi3 = 0
candi4 = 0
nulo = 0
votobranco = 0

while True:
    entrada = input("Digite o número do candidato (1-4), 5 para nulo, 6 para branco ou apenas Enter para encerrar: ").strip()

    if entrada == "":
        print("\nVotação encerrada!")
        break

    if not entrada.isdigit():
        print("Entrada inválida! Digite apenas números.")
        continue

    voto = int(entrada)

    if voto == 1:
        candi1 += 1
    elif voto == 2:
        candi2 += 1
    elif voto == 3:
        candi3 += 1
    elif voto == 4:
        candi4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        votobranco += 1
    else:
        print("Código inválido! Digite de 1 a 6.")

# Mostrar resultados
print("\nResultado da votação:")
print("Candidato 1:", candi1)
print("Candidato 2:", candi2)
print("Candidato 3:", candi3)
print("Candidato 4:", candi4)
print("Nulos:", nulo)
print("Brancos:", votobranco)

# Determinar o mais votado
votos = [candi1, candi2, candi3, candi4]
maior = max(votos)

if votos.count(maior) > 1:
    print("\nHouve empate entre os candidatos mais votados.")
else:
    vencedor = votos.index(maior) + 1
    print(f"\nO candidato mais votado foi o Candidato {vencedor}, com {maior} voto(s).")
