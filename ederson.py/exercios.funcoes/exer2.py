#Crie uma função que receba dois números e retorne sua soma.]

x=1
y=2
def soma(x,y):
    result=x+y
    return result

a=int(input("primeiro numero:"))
b=int(input("segundo numero:"))
res=soma(a,b)
print("soma:",res)