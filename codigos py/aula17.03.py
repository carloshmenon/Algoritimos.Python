#manipulação de string (texto entre "") USANDO O COMANDO "LEN" SE CONTA O NUMERO DE CARACTERES

print("exemplo 1 '")
a="ederson"
print("a palavra", a, "tem",len(a), "letras")
print(" ")

#funcao .capitalize coloca a PRIMEIRA LETRA maiuscula.
print("exemplo 2 \n")

a="Carlos"
print(a.capitalize())
print ("  ")


#transformar todo o texto em maiusculo se usa .UPPER
print("exmplo 3\n")

a="hagamenon"
print(a.upper())

#.casefold usado para DEIXAR MINUSCULO
print ("exemplo 4\n")

a="OLIVEIRA"
print(a.casefold())

#identificar se o texto esta minusculo
print ("exemplo 5\n")

a="OLIVEIRA"
print(a.islower())

#.isupper usado para verificar se esta MAISCULO

#.isdigit resultado verdadeiro somente  para numeros
print("exemplo 6 \n")

a="12345"
print(a.isdigit())

#.replace usado para substituir palavras
print ("exemplo 7 \n")

a="Ederson Roberto"
print(a.replace("Roberto","costa"))

#.split usado para separa por virgula OU na variavel que eu quiser. se nao colocar nada vai ser por virgula
print("exemplo 8\n ")

a="carlos hagamenon oliveira gomes"
print(a.split())

#.find encontra onde comeca a string procurada ou .rfind que procura de traz para frente da direita para esquerda
print ("exemplo 9\n")

a="carlos hagamenon oliveira"
print(a.find("oliveira"))

#.in procura se a palavra buscada esta dentro de uma frase ou outra palavra

print("exemplo 9 \n")
a='ederson costa'
print("costa" in a)

#.count retorna quantas vezes aparece a variavel desejada
print("exemplo 10 \n")

a="carlos oliveira"
print(a.count("a"))

#imprimindo por contagem

print("exemplo 11 \n")
s="ola, mundo"
print(s[0])
print(s[2])
print(s[6])

print 
#da direita para a esquerda a string(texto começa no negativo) -1, -2 e assim por diante

#imprimindo duas caracteres,USAR SEMPRE UM NUMERO A MAIS NAQUELE QUE EU QUERO, EX QUERO O 3 CARACTERE, COLOCO O 4
print ("exemplo 12 \n")

s= "ola, mundo"
print(s[1:3])

#colando dois pontos mais o numero pega a quantidade selecionada
print("exemplo 13 \n")

s="ola, mundo"
print(s[:3])

print("APRENDENDO SOBRE LISTA \n")

#lista, usado para juntar numeros e texto. USAR COLCHETES [] ao inves de ()
print("exemplo 14\n")

lista1= [10,20,30]
lista2= ["carlos", "gomes", "oliveira" ]
print (lista1, lista2)

#podemos criar listas dentro de listas [10,20,20["carlos oliveira"]] que o programa pega junto do mesmo jeito

#podemos usar o len para contar quantos objetos temos na lista usar (len(lista1))



