#funcoes de saida, calculando 
#programando a funcao

def calcular_pagamento(qtd_horas, valor_hora):
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas<=40:
        salario=horas*taxa

    else:
        h_excd=horas-40
        salario=40*taxa+(h_excd*(1.5*taxa))
    
    print(salario)

#posso colocar tambem um imput nas variaveis, deixando a o parenteses em branco da def