

def concatena(**kwargs):
    print(f'valores recebidos : {kwargs}')
    resultado=""
    for valor in kwargs.values():
        resultado+=f"{valor}"
    return resultado
    
print(concatena(a="python ", b="academy ", c="rules!"))