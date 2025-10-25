

#criando uma calculadora de texto

def calculate_tax(value, **kwargs):
    total=0
    print(kwargs)
    if "iss" in kwargs:
        total+=value*kwargs["iss"]
    if "pis" in kwargs:
        total+=value*kwargs["pis"]
    return total
    
resultado=calculate_tax(value=1000,iss=0.15, pis=0.033)
print(resultado)