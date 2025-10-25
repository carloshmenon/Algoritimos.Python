from banco import Conta
clientes = []
while True:
    print("\n===== cripto carlos=====")
    print("1- cadastro")
    print("2- consultar saldo")
    print("3- consultar extrato")
    print("4- sacar")
    print("5- depositar")
    print("6- sair")

    opção= input("escolha uma opção: ")

    if opção=="1":
        conta=Conta(None,None,0,[])
        conta.preencher_dados()
        clientes.append(conta)
        print("conta cadastrada com sucesso!")
      
