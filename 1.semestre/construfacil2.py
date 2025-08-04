# Sistema Construfácil - Versão Simplificada

# --- Estruturas de Dados (em memória) ---
# Dicionário de usuários com senhas e cargos
usuarios = {
    'vendedor1': {'senha': '123', 'cargo': 'vendedor'},
    'caixa1': {'senha': 'abc', 'cargo': 'caixa'},
    'estoquista1': {'senha': '456', 'cargo': 'estoquista'}
}

# Dicionário de estoque
estoque = {
    'Produto A': {'quantidade': 50, 'preco': 10.50},
    'Produto B': {'quantidade': 25, 'preco': 25.00},
    'Produto C': {'quantidade': 100, 'preco': 5.00}
}

# Lista de vendas (simulando um banco de dados de vendas)
vendas = []

# Dicionário para crediário de clientes
crediario = {
    'Cliente Antigo 1': {'debitos': 50.00, 'historico_compras': []},
    'Cliente Antigo 2': {'debitos': 0.00, 'historico_compras': []}
}

# --- Funções do Sistema ---

def login():
    """Realiza o login do usuário no sistema[cite: 2]."""
    while True:
        usuario = input("Digite seu login: ").lower()
        senha = input("Digite sua senha: ")

        if usuario in usuarios and usuarios[usuario]['senha'] == senha:
            print(f"Bem-vindo, {usuario}! Cargo: {usuarios[usuario]['cargo']}\n")
            return usuario, usuarios[usuario]['cargo']
        else:
            print("Login ou senha incorretos. Tente novamente.")

def registrar_venda(vendedor_logado):
    """Permite ao vendedor registrar uma venda e dar baixa no estoque[cite: 4, 11]."""
    print("--- Registrar Nova Venda ---")
    nome_cliente = input("Nome do cliente: ")
    itens_vendidos = []
    total_venda = 0.0

    while True:
        produto = input("Nome do produto (ou 'fim' para terminar): ")
        if produto.lower() == 'fim':
            break

        if produto in estoque:
            try:
                quantidade = int(input(f"Quantidade de '{produto}': "))
                if estoque[produto]['quantidade'] >= quantidade:
                    # Desconto (simulação)
                    desconto_str = input("Há desconto? (s/n): ")
                    desconto_percentual = 0
                    if desconto_str.lower() == 's':
                        desconto_percentual = float(input("Porcentagem de desconto (ex: 10 para 10%): "))
                    
                    preco_unitario = estoque[produto]['preco']
                    preco_com_desconto = preco_unitario * (1 - desconto_percentual / 100)
                    
                    subtotal = preco_com_desconto * quantidade
                    total_venda += subtotal

                    # Atualiza o estoque
                    estoque[produto]['quantidade'] -= quantidade
                    
                    # Adiciona o item à lista de itens vendidos
                    itens_vendidos.append({
                        'produto': produto,
                        'quantidade': quantidade,
                        'preco_unitario': preco_unitario,
                        'desconto': desconto_percentual,
                        'subtotal': subtotal
                    })

                    print(f"Produto '{produto}' adicionado. Subtotal: R${subtotal:.2f}")
                else:
                    print(f"Estoque insuficiente. Disponível: {estoque[produto]['quantidade']}")
            except ValueError:
                print("Quantidade inválida.")
        else:
            print("Produto não encontrado no estoque.")
    
    if itens_vendidos:
        forma_pagamento = input("Forma de pagamento (Cartão, Dinheiro, Crediário): ")
        
        # Simula o fluxo para o crediário
        if forma_pagamento.lower() == 'crediário':
            if nome_cliente in crediario:
                valor_debito = total_venda
                crediario[nome_cliente]['debitos'] += valor_debito
                crediario[nome_cliente]['historico_compras'].append(f"Compra de R${valor_debito:.2f}")
                print(f"Débito de R${valor_debito:.2f} adicionado ao crediário de '{nome_cliente}'.")
            else:
                print("Cliente não cadastrado no crediário. Venda não pode ser concluída nesta modalidade.")
                return

        # Simula o envio para o caixa [cite: 5]
        venda = {
            'vendedor': vendedor_logado,
            'cliente': nome_cliente,
            'itens': itens_vendidos,
            'total': total_venda,
            'data': '03/08/2025', # Data fixa para simulação
            'forma_pagamento': forma_pagamento
        }
        vendas.append(venda)
        print("\n--- Resumo da Venda ---")
        for item in itens_vendidos:
            print(f"- {item['quantidade']}x {item['produto']} (R${item['subtotal']:.2f})")
        print(f"Total da Venda: R${total_venda:.2f}")
        print(f"Forma de Pagamento: {forma_pagamento}")
        print("Venda registrada com sucesso!")

def gerenciar_estoque():
    """Função para o estoquista visualizar o estoque e fazer pedidos/liquidações[cite: 21]."""
    print("--- Gerenciamento de Estoque ---")
    print("Produtos no estoque:")
    for produto, info in estoque.items():
        print(f"- {produto}: Quantidade={info['quantidade']}, Preço=R${info['preco']:.2f}")
    
    # Simulação de notificação de produto acabando [cite: 23]
    print("\n--- Alertas de Estoque ---")
    for produto, info in estoque.items():
        if info['quantidade'] < 10:
            print(f"ALERTA: O produto '{produto}' está acabando! Quantidade: {info['quantidade']}.")

def gerenciar_relatorios():
    """Função para gerar relatórios básicos[cite: 18, 19, 22]."""
    print("--- Relatórios ---")
    
    print("\n-- Produtos Mais Vendidos --")
    contagem_produtos = {}
    for venda in vendas:
        for item in venda['itens']:
            produto = item['produto']
            quantidade = item['quantidade']
            if produto not in contagem_produtos:
                contagem_produtos[produto] = 0
            contagem_produtos[produto] += quantidade
    
    produtos_ordenados = sorted(contagem_produtos.items(), key=lambda item: item[1], reverse=True)
    for produto, quantidade in produtos_ordenados:
        print(f"- {produto}: {quantidade} unidades vendidas")
    
    print("\n-- Desempenho dos Vendedores --")
    desempenho_vendedores = {}
    for venda in vendas:
        vendedor = venda['vendedor']
        if vendedor not in desempenho_vendedores:
            desempenho_vendedores[vendedor] = 0
        desempenho_vendedores[vendedor] += venda['total']
    
    for vendedor, total_vendas in desempenho_vendedores.items():
        print(f"- {vendedor}: Vendeu R${total_vendas:.2f}")
        
    print("\n-- Crediário Próprio --")
    for cliente, info in crediario.items():
        if info['debitos'] > 0:
            print(f"- {cliente}: Valor devido = R${info['debitos']:.2f}")

def main():
    """Função principal que inicia o programa[cite: 1]."""
    usuario_logado, cargo = login()

    if cargo == 'vendedor':
        while True:
            print("\n--- Menu do Vendedor ---")
            print("1. Registrar Venda")
            print("2. Gerar Orçamento (não implementado nesta versão simplificada)")
            print("3. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                registrar_venda(usuario_logado)
            elif escolha == '2':
                print("Funcionalidade de orçamento não implementada. (Simulando... Orçamento enviado para impressora!)")
            elif escolha == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
    
    elif cargo == 'caixa':
        print("--- Menu do Caixa ---")
        print("1. Visualizar Vendas (Dashboard do Caixa)")
        print("2. Gerar Relatórios")
        print("3. Registrar Devolução (não implementado nesta versão simplificada)")
        print("4. Sair")
        
        while True:
            escolha = input("Escolha uma opção: ")
            if escolha == '1':
                print("\n--- Dashboard do Caixa ---")
                if not vendas:
                    print("Nenhuma venda registrada ainda.")
                for venda in vendas:
                    print(f"Venda de R${venda['total']:.2f} para {venda['cliente']} por {venda['vendedor']}.")
            elif escolha == '2':
                gerenciar_relatorios()
            elif escolha == '3':
                print("Funcionalidade de devolução não implementada. (Simulando... Devolução registrada)")
            elif escolha == '4':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    elif cargo == 'estoquista':
        while True:
            print("\n--- Menu do Estoquista ---")
            print("1. Gerenciar Estoque")
            print("2. Sair")
            escolha = input("Escolha uma opção: ")
            
            if escolha == '1':
                gerenciar_estoque()
            elif escolha == '2':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

# --- Executa o programa ---
if __name__ == "__main__":
    main()