
lista=[0,1,2,3,4,5,6,7,8,9,10]
print(lista[1:10])

print(lista[8:]), print("\n\n")

#numeros pares

lista=[0,1,2,3,4,5,6,7,8,9,10]
numpares = [num for num in lista if num % 2 == 0]
print(numpares)

#numeros impares

lista=[0,1,2,3,4,5,6,7,8,9,10]
numimpares = [num for num in lista if num % 2 == 1]
print(numimpares)
print("\n\n")

#numeros reversos

lista=[0,1,2,3,4,5,6,7,8,9,10]
lista.reverse ()
print (lista)
print("\n\n")

#numeros pares de outro jeito

lista=[0,1,2,3,4,5,6,7,8,9,10]
print(lista[2::2])
print(lista[1::2])
print("\n \n")

#media da lista


#P1= input("escreva quais as 5 notas do aluno: ")
#P2= input("escreva quais as 5 notas do aluno em P2: ")

P1=[7.0,8.3,10,6.5,9.3]
P2=[8.5,6.9,5,7.5,9.8]

print("a media da turma P1 FOI DE :", (sum(P1))/5)
print(f"a media da turma P2 FOI DE : {(sum(P2))/5:.2f}")
