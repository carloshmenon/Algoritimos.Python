pessoa={
    "nome":"gerson",
    "idade":48,
    "cidade":"campo grande"
}

def verifica_cidade(dicionario:dict):
    if dicionario["cidade"]=="CG":
        return "É DE CAMPO GRANDE"
    else:
        return f"é de {dicionario["cidade"]}"

cidade_gerso = verifica_cidade(pessoa)
print(cidade_gerso)

def imprime_listas(listas):
    for item in listas:
        print (item)

frutas = ["banana","maça","pera","uva","salada"]
carros=["gol","corsa","celta","chevette","fusca"]
tupla=(33,44,55,66,77,88,99,00)

imprime_listas(tupla)