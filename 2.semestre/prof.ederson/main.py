from conta import Conta  # importa a classe Conta

contas = []  # lista global para armazenar as contas criadas


def encontrar_conta(agencia, numero):
    for conta in contas:
        if conta.agencia == agencia and conta.numero == numero:
            return conta
    return None


def menu():
    while True:
        print("\n=== BANCO PYTHON ===")
        print("1. Cadastrar conta")
        print("2. Consultar saldo")
        print("3. Consultar extrato")
        print("4. Sacar dinheiro")
        print("5. Depositar dinheiro")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do titular: ")
            agencia = input("Agência: ")
            numero = input("Número da conta: ")
            senha = input("Crie uma senha: ")

            nova_conta = Conta(nome, numero, agencia, senha)
            contas.append(nova_conta)
            print("✅ Conta criada com sucesso!")

        elif opcao == "2":
            agencia = input("Agência: ")
            numero = input("Número da conta: ")
            senha = input("Senha: ")

            conta = encontrar_conta(agencia, numero)
            if conta:
                conta.consultar_saldo(agencia, numero, senha)
            else:
                print("❌ Conta não encontrada.")

        elif opcao == "3":
            agencia = input("Agência: ")
            numero = input("Número da conta: ")
            senha = input("Senha: ")

            conta = encontrar_conta(agencia, numero)
            if conta:
                conta.consultar_extrato(agencia, numero, senha)
            else:
                print("❌ Conta não encontrada.")

        elif opcao == "4":
            agencia = input("Agência: ")
            numero = input("Número da conta: ")
            senha = input("Senha: ")
            valor = float(input("Valor do saque: "))

            conta = encontrar_conta(agencia, numero)
            if conta:
                conta.sacar(agencia, numero, senha, valor)
            else:
                print("❌ Conta não encontrada.")

        elif opcao == "5":
            agencia = input("Agência: ")
            numero = input("Número da conta: ")
            valor = float(input("Valor do depósito: "))

            conta = encontrar_conta(agencia, numero)
            if conta:
                conta.depositar(agencia, numero, valor)
            else:
                print("❌ Conta não encontrada.")

        elif opcao == "6":
            print("👋 Encerrando o sistema bancário. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
