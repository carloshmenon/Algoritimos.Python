#paramentros atua como variavel, toda vez que eu for chamar a funcao hello que tem o paramentro chamado(nome) obviamente ele ira printar o hello mais o nome

def hello (nome):
    print("ola!!!,",nome)
#chamado a funcao 
hello("ederson")

#adcionando texto com o usuario, a DEF nao acontece nada se eu nao chamar ela, por isso eu coloco o hello agora com input ()

def hello (nome):
    print("ola!!!,",nome)
#chamado a funcao 
a=input("digite seu nome: ")
hello(a)

#agora pedindo nome e idade que o usuario digita

def hello (nome,idade):
    print("ola!!!,",nome,idade)
#chamado a funcao 
a=input("digite seu nome: ")
b=input("digite sua idade: ")
hello(a,b)