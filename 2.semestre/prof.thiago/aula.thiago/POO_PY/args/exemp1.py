

##aprendendo sobre args 

##criando dicionario

brinquedo= {
    "marca":"estrela",
    "modelo":"boneca",
    "preco":150
}

#quando eu criar uma funcao que nao sei a quantidade de 
# parametros que ira receber, vou usar o *args

def my_func(param1, *args):##args deixa os argumentos em branco, o usuario que ira decidir quantos argumentos se tem ali
    print(param1)##rpecisamos de um parametro OBRIGATORIO, aqui usamos o "param1"
    print(len(args))

def my_func2(*args):#aqui criamos a def my_func2 e deixamos o args aqui para deixar o tanto de parametros que quisermos
    for item in args:#aqui definimos a variavel item atrelada ao args
        print(item)#aqui imprimimos a variavel item 

my_func2(1,2,3,4,5)##aqui definimos os itens dentro da myfunc2, nos decidimos quantos itens colocamos aqui. 

my_func(12,14,16,18)#aqui o "param1" é 12, ja que o usuario decidiu que o 12 é o item na posição 0.
#depois o "len" conta quantos itens se tem dentro do "args" e retorna 3, pq o "len" conta os itens.

