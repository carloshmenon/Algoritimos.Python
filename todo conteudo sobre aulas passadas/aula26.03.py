
#exercicio 1

lista=[1,2,3,4,5]
print("o maior numero da lista é: ", max(lista))
print("o menor numero da lista é: ", min(lista))
print("a quantidade de itens na lista é: ", len(lista))
print("a soma de todos os itens é: ", sum(lista))
print("\n \n")


#exer 2 mostre quantas vezes apareceu o numero 1

a=[1,2,1,5,6,4,3,1]
print("o numero 1 aparece", a.count(1)," vezes. ")
print("\n \n")

#exer 3 subs o segundo elemento do vetor por laranja

a=["maça","banana","pera","uva","beterraba"]
a[1]=("laranja")
print(a)
print("\n \n")

#exer 4 somando todas as listas

t=[[1,2], [3], [4,5,6]]
print(sum(t[0])+sum(t[1])+sum(t[2]))
print("\n\n")

#exer5 somando os elementos. 0 é ele mesmo, 1 é 1 mais 0 e 3 é 3+2+1

t=[[1],[2],[3]]
print (t[0])
print (sum (t[0])+sum (t[1]))
print (sum ((t)[0])+sum((t)[1])+sum((t)[2]))
print ("\n \n")

#exer 6, retirando os itens da lista

t=[1,2,3,4,5]
print (t[1:3])
print("\n \n")

#exerci 7 adicione o brasil na lista

paises= ['alemanha', 'italia', 'japao']
paises.extend(["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela" ])
print("\n")
paises.extend(["paises da america do norte","Canadá", "Estados Unidos", "México"])
print (paises)