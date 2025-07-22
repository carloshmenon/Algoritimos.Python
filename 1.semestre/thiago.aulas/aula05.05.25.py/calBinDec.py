##binario para decimal

valor= input("digite o numero em binario: \n")

valor_decimal=[]

x=len(valor)

for i in valor:
    x=x-1
    if i =="1":
        z=16**x
        valor_decimal.append(z)

print(valor_decimal)
print("decimal", sum(valor_decimal))        