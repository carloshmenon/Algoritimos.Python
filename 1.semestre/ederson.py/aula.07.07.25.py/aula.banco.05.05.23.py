#sistema de banco
#novo_saldo= (saldo_conta+depositar)
saldo_conta=1
depositar=2
sacar=3
sair=4

cliente=[]



while True:
    print("====cadastro de cliente banco BB===\n")


    cliente.append (input("digite seu nome completo: \n")) #0
    cliente.append (input("digite seu CPF: \n"))#1
    cliente.append (input("digite seu RG: \n"))#2
    cliente.append (input("digite seu telefone:\n"))#3
    cliente.append (input("digite sua agência:\n"))#4
    cliente.append (input("digite o número da sua conta com digito:\n"))#5
    cliente.append (float(input("digite seu saldo em conta: \n")))#6


    while True:

     print("====cadastro de cliente banco BB===\n")

     print("Digite a opção desejada:")
     print("'1' para ver saldo ")
     print("'2' para depositar ")
     print("'3' para realizar um saque ")
     print("'4' para sair ")

     x=(input(""))


     if x=="1":
       print("seu saldo é, ", cliente[6])
       
    
     elif x=="2":
        depositar=(float(input("qual valor deseja depositar? \n")))
        cliente[6]=cliente[6]+depositar
        print("seu novo saldo é de, ",cliente[6])

     elif x=="3":
        saque=(float(input("qual valor deseja sacar? \n")))
        
        if saque <= 0:
         print("Valor inválido para saque.")

        elif saque > cliente[6]:
         print("Saldo insuficiente.")

        else:
         cliente[6] -= saque
         print("Saque realizado. Seu novo saldo é:", cliente[6])

     if x=="4":
       break



        









