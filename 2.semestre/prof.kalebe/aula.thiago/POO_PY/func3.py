
def soma(n1,n2):#3definindo atributos
    res=n1+n2#colocando a funcao que n1 e n2 ira fazer
    return res #agora com o resultado de res iremos guardar o dado
print(soma(10,20))#aqui colocamos os valores de n1=10 e n2=20

x= soma(30,30)#aqui criamos uma variavel x e executamos def soma e colocamos os valores de n1=30 e n2=30

print(x)

#criando uma funcao que faça 2 elevado a 3

def soma2(n3,n4):
    res2=n3**n4
    return res2
print(soma2(2,3))

#usando if dentro

def expo(b:int, e : int, z=0):
    if z<0:
        return "ERROR"
    res3= (b**e) + z
    return res3

print(expo(5,10))##o terceiro paramento "z" pode ser alterado sempre, como é zero nao a necessidade de ser colocado