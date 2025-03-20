#lista 

frutas= ["maça", "laranja", "banana", "cereja"]
print([1,2]+[3,4])
print(frutas+[6,7,8,9])

print(["teste"]*4)
print([1,2,["ola, mundo"]*2], "\n")
print("\n \n")

#lista usando "max"  "min" "sun"

a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a))
print(min(a))
print(sum(a))
print('\n \n')

#slice colocar quais itens eu quero mostrar no meu print

lista= ["a","b","c","d","e","f"]

print(lista[1:3])
print(lista[:4])
print(lista[3:])
print(lista[:])
print(lista[0:6])
print("\n \n")

#lista mutavel, posso add strings que nao estao nas listas

frutas=["banana", "maca", "cereja"]
frutas[0]="pera"
frutas[-1]="morango"
print(frutas)
print("\n \n ")

#substituindo mais de um item 

lista=["a","b","c","d"]
lista[1:3]= ["x","y"]
print(lista)
print('\n \n')

#removendo itens de uma lista

lista=['a','b','c','d','e']
print(lista)
print(len(lista))

lista[1:3]=[]
print(lista)
print(len(lista))
print('\n \n')

#adicionado elementos, colocando o local que vamos add os itens

lista=['a','d','f']
lista[1:1]=['b','c']
print(lista)
lista[4:4]=['e']
print(lista)


#