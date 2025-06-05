#Escreva uma função que verifique se um número é par.

def impar_par(x):
    x=int(input("digite um numero: "))
    if (x)%2==0:
       numero_par=x%2==0
    else:
        print("numero é impar")

    print(numero_par)

