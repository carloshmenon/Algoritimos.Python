#exercio 5.1
#escreva um algoritimo que conta o numero de caracteres escritos pelo usuario

palavra= (input("escreva uma palavra: "))
print("a palavra", palavra, "tem",len(palavra), "letras")
print(" ")


#exercicio5.3
#faça um exercicio que leia um nome e 
# informa as 4 primeiras letras dele

nome=(input("escreva um nome: "))
print(nome[:4])

#exercicio 5.4 é repetido

#exercicio 5.5 
#print o nome e a primeira letra maiuscula

a=(input("digite seu nome: "))
print(a.capitalize())
print ("  ")

#exercicio 5.6
#todo o texto maiusculo

a=(input("escreva uma palavra: "))
print(a.upper())

#exercicio 5.7.1
#imprima o indice 0 ao 8

a=(input("escreva uma palavra"))
print(a[0:8])

#exercicio 5.7.2
#imprima a frequencia da letra "a"

a=(input("escreva uma palavra"))
print(a.count("a"))