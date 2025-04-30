#amento de salario

salario= float (input("qual seu salário?"))

if salario==280.55:
    salario= salario*22.51 /100+salario

    aumento= salario+22.51 /100
    print(f"Seu novo salário é de R$ {salario:.2f}")
    print(aumento)

if salario ==280.56<709.72:
    salario= salario*15.39 /100+salario

    aumento= salario*15.39 /100
    print(f"seu novo salario é de,  {salario:.2f}")

if salario ==709.73<1501.33:
    salario= salario*10.97 /100+salario

    aumento= salario*10.97 /100
    print(f"seu novo salario é de,  {salario:.2f}")

elif salario>=1501.34:
         salario= salario*0.519 /100+salario

         aumento= salario*0.519 /100
         print(f"seu novo salario é de, {salario:.2f}")