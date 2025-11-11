### tela de interação com o usuario 

from Cliente import Cliente

while True:
    print("SysPerkal")  
    print("*"*30)
    print("selecione uma opção")

    opcao= input("\t 1- Cadastrar um cliente \n\t 2- listar clientes \n\t  3- excluir um cliente \n\t  0 SAIR \n\t | 4 - atualizar \n " )

    if opcao =="0":
        break

    if opcao=="1":#cadastrar
        cli=Cliente()
        cli.nome= input ("Digite o nome do cliente : ")
        cli.cpf= input("Digite o CPF: ")
        cli.fone= input("digite o telefone do cliente : ")
        cli.cidade= input("digite a cidade do cliente: ")
        result= cli.cadastrar()

        if result==True:
            print("Cadastrado com sucesso!! ")

    if opcao =="2":#listar
        cli=Cliente ()
        result = cli.buscar()
        for cliente in result:
            print(f"ID: {cliente[0]} | nome : {cliente[1]} | CPF: {cliente[2]} | fone: {cliente[3]} | cidade: {cliente[4]} ")

    if opcao=="3":##excluir
        cli=Cliente()
        result=cli.buscar()
        for cliente in result:
            print(f"ID: {cliente[0]} | nome : {cliente[1]} | CPF: {cliente[2]} | fone: {cliente[3]} | cidade: {cliente[4]} ")

        id_deletar= int(input(" digite o id que deseja deletar: "))
        result=cli.deletar(id_deletar)
        if result ==True:
            print("deletado com sucesso!")

    if opcao =="4":
        cli=Cliente ()
        result = cli.buscar()
        for cliente in result:
            print(f"ID: {cliente[0]} | nome : {cliente[1]} | CPF: {cliente[2]} | fone: {cliente[3]} | cidade: {cliente[4]} ")

        id_atualiza= int(input(" Digite o ID que deseja atualizar: "))
        result=list(cli.buscar_por_id(id_atualiza))
        result[1]= input("digite o novo nome:")
        result[2]= input("digite o novo CPF:")
        result[3]= input("digite o novo fone:")
        result[4]= input("digite o novo cidade:")

        atualizacao= cli.atualizar(tuple(result))
        if atualizacao ==True:
            print("cliente atualizado com sucesso!!")

