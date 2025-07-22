# #intervalo de numeros

x= (int(input("digite um numero: \n")))
y= (int(input("digite outro numero: \n")))
print("\n")
soma=0

#printa o intervalo da variavel
# for i in range (x+1,y):
#         print(i)
#         print("______")


#printa o intervalo e soma o intervalo
for i in range (x+1,y):
        print(i)
        print("______")
        soma+= i
        print(f'{soma}')
        