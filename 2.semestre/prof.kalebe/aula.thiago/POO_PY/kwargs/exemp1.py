
##kwargs faz um dicionario cujo conteudo podemos acessar atraves do nome do argumento 
#aqui mandamos os valores do dicionario nomeados, por exmeplo "marca=estrela"
#no args eu deixo a lista em branco e posso colocar varios argumento nessa lista, e nao preciso atribuir valor aos
#  argumentos, diferente ao que fiz no kwargs que atrbui valor a marca=estrela.

##criando dicionario

brinquedo= {
    "marca":"estrela",
    "modelo":"boneca",
    "preco":150
}

#criando um kwargs

def cria_dicionario(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,value)

#chamada de função com parametros NOMEADOS!!!

cria_dicionario(nome="thiago",idade=32,city="campo grande")

