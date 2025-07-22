#Escreva uma função que calcule o quadrado de um número.


def soma(x,y):
    result=x**y
    return result

a=int(input("primeiro numero:"))
b=int(input("segundo numero:"))
res=soma(a,b)
print("o numero ",a,"elevado ao numero ",b, "é:", res)