from classe import Garcom, Produto, Pedido

while True:
    print("\n=== SysRestaurante ===")
    print("*" * 30)
    print("Selecione uma opção:")

    opcao = input(
        "\t 1 - Cadastrar Garçom\n"
        "\t 2 - Listar Garçons\n"
        "\t 3 - Excluir Garçom\n"
        "\t 4 - Atualizar Garçom\n"
        "\t 5 - Cadastrar Produto\n"
        "\t 6 - Listar Produtos\n"
        "\t 7 - Excluir Produto\n"
        "\t 8 - Atualizar Produto\n"
        "\t 9 - Cadastrar Pedido\n"
        "\t 10 - Listar Pedidos\n"
        "\t 11 - Excluir Pedido\n"
        "\t 0 - SAIR\n"
    )

    if opcao == "0":
        break

    # ---------------- Garçom ----------------
    if opcao == "1":  # cadastrar garçom
        g = Garcom()
        g.nome = input("Digite o nome do garçom: ")
        result = g.cadastrar()
        if result:
            print("✅ Garçom cadastrado com sucesso!")

    if opcao == "2":  # listar garçons
        g = Garcom()
        result = g.buscar()
        for garcom in result:
            print(f"ID: {garcom[0]} | Nome: {garcom[1]}")

    if opcao == "3":  # excluir garçom
        g = Garcom()
        result = g.buscar()
        for garcom in result:
            print(f"ID: {garcom[0]} | Nome: {garcom[1]}")
        id_del = int(input("Digite o ID do garçom que deseja excluir: "))
        if g.deletar(id_del):
            print("✅ Garçom excluído com sucesso!")

    if opcao == "4":  # atualizar garçom
        g = Garcom()
        result = g.buscar()
        for garcom in result:
            print(f"ID: {garcom[0]} | Nome: {garcom[1]}")
        id_att = int(input("Digite o ID do garçom que deseja atualizar: "))
        dados = list(g.buscar_por_id(id_att))
        dados[1] = input("Digite o novo nome: ")
        if g.atualizar(tuple(dados)):
            print("✅ Garçom atualizado com sucesso!")

    # ---------------- Produto ----------------
    if opcao == "5":  # cadastrar produto
        p = Produto()
        p.nome = input("Digite o nome do produto: ")
        p.preco = float(input("Digite o preço: "))
        if p.cadastrar():
            print("✅ Produto cadastrado com sucesso!")

    if opcao == "6":  # listar produtos
        p = Produto()
        result = p.buscar()
        for prod in result:
            print(f"ID: {prod[0]} | Nome: {prod[1]} | Preço: R$ {prod[2]:.2f}")

    if opcao == "7":  # excluir produto
        p = Produto()
        result = p.buscar()
        for prod in result:
            print(f"ID: {prod[0]} | Nome: {prod[1]} | Preço: R$ {prod[2]:.2f}")
        id_del = int(input("Digite o ID do produto que deseja excluir: "))
        if p.deletar(id_del):
            print("✅ Produto excluído com sucesso!")

    if opcao == "8":  # atualizar produto
        p = Produto()
        result = p.buscar()
        for prod in result:
            print(f"ID: {prod[0]} | Nome: {prod[1]} | Preço: R$ {prod[2]:.2f}")
        id_att = int(input("Digite o ID do produto que deseja atualizar: "))
        dados = list(p.buscar_por_id(id_att))
        dados[1] = input("Digite o novo nome: ")
        dados[2] = float(input("Digite o novo preço: "))
        if p.atualizar(tuple(dados)):
            print("✅ Produto atualizado com sucesso!")

    # ---------------- Pedido ----------------
    if opcao == "9":  # cadastrar pedido
        ped = Pedido()
        ped.garcom_id = int(input("Digite o ID do garçom responsável: "))
        if ped.cadastrar():
            print("✅ Pedido cadastrado com sucesso!")

    if opcao == "10":  # listar pedidos
        ped = Pedido()
        result = ped.buscar()
        for pedido in result:
            print(f"ID: {pedido[0]} | Garçom ID: {pedido[1]}")

    if opcao == "11":  # excluir pedido
        ped = Pedido()
        result = ped.buscar()
        for pedido in result:
            print(f"ID: {pedido[0]} | Garçom ID: {pedido[1]}")
        id_del = int(input("Digite o ID do pedido que deseja excluir: "))
        if ped.deletar(id_del):
            print("✅ Pedido excluído com sucesso!")
