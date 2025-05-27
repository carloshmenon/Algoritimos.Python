#pop remove e mostra qual esta sendo removido e tambem mostra se o item tem ou nao nos dicionarios

tradutor ={}
tradutor={"pineapple":"abacaxi","apple":"maça","orange":"laranja"}
print(type(tradutor))
print(tradutor.pop("apple"))
print(tradutor)
print(tradutor.pop("banana","fruta nao encontrada"))
