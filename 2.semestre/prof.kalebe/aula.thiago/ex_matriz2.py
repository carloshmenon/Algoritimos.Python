i=0 ##contador de linhas
j=0 ##contador de colunas
matriz=[]
lin = int(input("digite a quantidade de linhas: "))
col= int(input("digite a quantidade de colunas: "))

while i<lin:
    linha=[]
    while j< col:
        num=1
        linha.append(num)
        j= j+1
    matriz.append(linha)
    i=i+1
    j=0

print(matriz)