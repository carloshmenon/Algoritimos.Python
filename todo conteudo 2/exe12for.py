#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). 
#Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cidade = 0
veiculos = 0
acidentes = 0

for i in range(5):
    print(f'cidade{i+1}:')
    codigo = int(input('Diga o codigo da cidade: '))
    veiculos = int(input('Diga o numero de veiculos(1999): '))
    acidentes = int(input('Diga o numero de acidentes(1999)'))

    


