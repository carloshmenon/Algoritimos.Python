#localizando com o .get 

dados={
    "crossfox": {"km":35000,"ano":2005},
    "ds5": {"km":17000,"ano":2015},
    "fusca": {"km":130000,"ano":1979},
    "jetta": {"km":56000,"ano":2011},
    "passat": {"km":62000,"ano":1999}  
}

print(dados.get("gol","veiculo nao encontrado"))
print(dados.get("fusca"))