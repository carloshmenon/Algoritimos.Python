# decinal para binario

import os

valor =float(input("digite um valor em decimal para converter em binario:\n"))
valor_binario =[]

while valor> 0:
    novovalor= valor%2
    novovalor= int(novovalor)
    print("resto:", novovalor)
    valor=valor/2
    print("divisor:", valor)
    valor =int(valor)
    valor_binario.insert(0, novovalor)
    print('')


print(valor_binario)
print(valor)    

#juntando os numeros

output =("".join(map(str,valor_binario)))
print(output)