

#criando uma definiçao
#exer9 
#9 – O gestor de uma rede de shoppings, precisa contratar um
# sistema para administrar o estacionamento, a principal função do
# sistema é calcularTempo(). Considere o valor mínimo de R$9,00
# por hora e R$ 1,50 por hora adicional. O principal argumento da
# função é o tempo utilizado em minutos, a função deve retornar o
# valor total. Caso o usuário fique no estacionamento por menos de
# 15 minutos, o tempo utilizado não será cobrado.
# EXERCÍCIOS FUNÇÕES
# 9 – Adicione na função calcularTempo() do sistema para
# estacionamento o valor dos impostos pago pelo cliente. Considere
# o PIS: 0,33% , COFINS: 0,20% e ICMS: 17% no valor e imprima o
# recibo do cliente de acordo com a saída abaixo:

def calcularTtempo(minutos):
    preco_hora=9
    hora_adicional=1.50
    hora=minutos/60

    if minutos<15:
        return "sem custo"

print(calcularTtempo(4))

