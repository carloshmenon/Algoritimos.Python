#media salario

salario= float (input("qual seu salário?"))

if salario==500:
    salario= salario*15 /100+salario

    aumento= salario*15 /100
    print(("seu novo salario é de, ",  salario))

elif salario >=500:
    salario= salario*10 /100+salario

    aumento= salario*10 /100
    print(("seu novo salario é de, ",  salario))

    #elif salario >1000:
         #salario= salario*0.5 /100+salario

    aumento= salario*0.5 /100
    print(("seu novo salario é de, ",  salario))