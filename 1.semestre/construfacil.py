import json
import os
from datetime import datetime, timedelta

# --- Configurações de Arquivos de Dados ---
DATA_DIR = 'data'
USUARIOS_FILE = os.path.join(DATA_DIR, 'usuarios.json')
PRODUTOS_FILE = os.path.join(DATA_DIR, 'produtos.json')
VENDAS_FILE = os.path.join(DATA_DIR, 'vendas.json')
CLIENTES_FILE = os.path.join(DATA_DIR, 'clientes.json')
CREDIARIO_FILE = os.path.join(DATA_DIR, 'crediario.json')

# --- Funções Auxiliares de Dados ---

def _ensure_data_files_exist():
    """Garante que a pasta de dados e os arquivos JSON existam, e popula com dados iniciais se vazios."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Dados iniciais para usuários
    initial_usuarios = [
        {"nome": "João Ribeiro", "usuario": "joao.vendas", "senha": "123", "setor": "vendas"},
        {"nome": "Carla Menezes", "usuario": "carla.vendas", "senha": "123", "setor": "vendas"},
        {"nome": "Lucas Ferreira", "usuario": "lucas.caixa", "senha": "123", "setor": "caixa"},
        {"nome": "Renata Silva", "usuario": "renata.estoque", "senha": "123", "setor": "estoque"}
    ]
    _initialize_file(USUARIOS_FILE, initial_usuarios)

    # Dados iniciais para produtos
    initial_produtos = [
        {"codigo": "001", "nome": "Cimento Votoran 50kg", "estoque": 120, "preco": 35.0, "estoque_minimo": 20},
        {"codigo": "002", "nome": "Areia Média Lavada 1m³", "estoque": 25, "preco": 110.0, "estoque_minimo": 5},
        {"codigo": "003", "nome": "Brita 1 1m³", "estoque": 20, "preco": 90.0, "estoque_minimo": 5},
        {"codigo": "004", "nome": "Bloco de Concreto 39x19x14cm", "estoque": 800, "preco": 3.0, "estoque_minimo": 100},
        {"codigo": "005", "nome": "Tinta Suvinil 18L branca", "estoque": 35, "preco": 220.0, "estoque_minimo": 10},
        {"codigo": "006", "nome": "Rejunte Quartzolit 1kg", "estoque": 140, "preco": 9.50, "estoque_minimo": 30},
        {"codigo": "007", "nome": "Tubo PVC 100mm - 6m", "estoque": 50, "preco": 78.0, "estoque_minimo": 10},
        {"codigo": "008", "nome": "Caixa d’água 500L Fortlev", "estoque": 18, "preco": 280.0, "estoque_minimo": 5},
        {"codigo": "009", "nome": "Telha fibrocimento 2,44m", "estoque": 60, "preco": 72.0, "estoque_minimo": 15},
        {"codigo": "010", "nome": "Piso cerâmico 45x45 (cx)", "estoque": 70, "preco": 55.0, "estoque_minimo": 20}
    ]
    _initialize_file(PRODUTOS_FILE, initial_produtos)

    # Inicializa outros arquivos como listas vazias se não existirem
    _initialize_file(VENDAS_FILE, [])
    _initialize_file(CLIENTES_FILE, [])
    _initialize_file(CREDIARIO_FILE, [])

def _initialize_file(filepath, initial_data):
    """Cria um arquivo JSON com dados iniciais se ele não existir ou estiver vazio."""
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            json.dump(initial_data, f, indent=4)

def _load_data(filepath):
    """Carrega dados de um arquivo JSON."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo {filepath} não encontrado. Certifique-se de que os arquivos de dados existam.")
        return []
    except json.JSONDecodeError:
        print(f"Erro: Arquivo {filepath} está corrompido ou vazio. Recriando...")
        return [] # Retorna vazio para que a inicialização possa recriar

def _save_data(data, filepath):
    """Salva dados em um arquivo JSON."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

# --- Funções de Autenticação ---

def login():
    """Realiza o login do usuário."""
    usuarios = _load_data(USUARIOS_FILE)
    usuario_input = input("Usuário: ")
    senha_input = input("Senha: ")

    for u in usuarios:
        if u['usuario'] == usuario_input and u['senha'] == senha_input:
            print(f"\nBem-vindo(a), {u['nome']} ({u['setor'].capitalize()})!\n")
            return u
    print("Login inválido! Usuário ou senha incorretos.")
    return None

# --- Menus por Setor ---

def menu_vendas(logged_in_user):
    """Menu para o setor de Vendas."""
    while True:
        print("\n=== Menu Vendas ===")
        print("1. Registrar Venda")
        print("2. Fazer Orçamento")
        print("3. Cadastrar Cliente Crediário")
        print("4. Registrar Devolução")
        print("5. Relatório de Produtos Mais Vendidos")
        print("6. Relatório de Desempenho de Vendedores")
        print("7. Voltar ao Login")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_venda(logged_in_user)
        elif opcao == "2":
            fazer_orcamento(logged_in_user)
        elif opcao == "3":
            cadastrar_cliente_crediario()
        elif opcao == "4":
            registrar_devolucao()
        elif opcao == "5":
            relatorio_produtos_mais_vendidos()
        elif opcao == "6":
            relatorio_vendedores()
        elif opcao == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_estoque(logged_in_user):
    """Menu para o setor de Estoque."""
    while True:
        print("\n=== Menu Estoque ===")
        print("1. Visualizar Estoque Atual")
        print("2. Notificações de Estoque Baixo")
        print("3. Relatório de Produtos para Comprar/Liquidar")
        print("4. Voltar ao Login")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            visualizar_estoque()
        elif opcao == "2":
            notificacoes_estoque()
        elif opcao == "3":
            relatorio_estoque_comprar_liquidar()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_caixa(logged_in_user):
    """Menu para o setor de Caixa."""
    while True:
        print("\n=== Menu Caixa ===")
        print("1. Dashboard do Caixa (Vendas do Dia)")
        print("2. Consultar Crediário (Débitos em Aberto)")
        print("3. Relatórios de Vendas (Por Período, Produto, Vendedor, Cliente)")
        print("4. Voltar ao Login")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dashboard_caixa()
        elif opcao == "2":
            consultar_crediario()
        elif opcao == "3":
            relatorio_vendas_geral()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# --- Funções do Setor de Vendas ---

def registrar_venda(logged_in_user, itens_orcamento=None, cliente_orcamento=None):
    """Registra uma venda no sistema."""
    produtos = _load_data(PRODUTOS_FILE)
    vendas = _load_data(VENDAS_FILE)
    clientes = _load_data(CLIENTES_FILE)

    carrinho = []
    total_venda = 0.0

    if itens_orcamento: # Se a venda vem de um orçamento
        carrinho = itens_orcamento
        print("\n--- Itens do Orçamento ---")
        for item in carrinho:
            print(f"  - {item['nome_produto']} (x{item['quantidade']}) - R${item['subtotal']:.2f}")
        total_venda = sum(item['subtotal'] for item in carrinho)
    else: # Venda normal
        print("\n--- Registrar Nova Venda ---")
        while True:
            cod = input("Código do produto (ou 'f' para finalizar): ").strip().lower()
            if cod == 'f':
                break

            produto = next((item for item in produtos if item['codigo'] == cod), None)
            if not produto:
                print("Produto não encontrado.")
                continue

            try:
                qtd = int(input(f"Quantidade de '{produto['nome']}' (Estoque: {produto['estoque']}): "))
                if qtd <= 0:
                    print("Quantidade deve ser positiva.")
                    continue
                if qtd > produto['estoque']:
                    print("Estoque insuficiente para esta quantidade.")
                    continue
            except ValueError:
                print("Quantidade inválida.")
                continue

            subtotal_item = produto['preco'] * qtd
            carrinho.append({
                "codigo_produto": cod,
                "nome_produto": produto['nome'],
                "quantidade": qtd,
                "preco_unitario": produto['preco'],
                "subtotal": subtotal_item
            })
            total_venda += subtotal_item
            print(f"Item '{produto['nome']}' adicionado ao carrinho.")

    if not carrinho:
        print("Nenhum item na venda.")
        return

    print(f"\nTotal bruto da venda: R${total_venda:.2f}")
    desconto_percentual = 0.0
    try:
        desconto_str = input("Desconto em % (ex: 10 para 10%, ou ENTER para 0%): ").strip()
        if desconto_str:
            desconto_percentual = float(desconto_str)
            if not (0 <= desconto_percentual <= 100):
                print("Desconto percentual inválido. Deve ser entre 0 e 100.")
                desconto_percentual = 0.0
    except ValueError:
        print("Valor de desconto inválido. Aplicando 0% de desconto.")
        desconto_percentual = 0.0

    valor_desconto = total_venda * (desconto_percentual / 100)
    total_com_desconto = total_venda - valor_desconto

    print(f"Valor do desconto: R${valor_desconto:.2f}")
    print(f"Total a pagar: R${total_com_desconto:.2f}")

    forma_pgto = ""
    while forma_pgto not in ["dinheiro", "credito", "debito", "pix", "crediario"]:
        forma_pgto = input("Forma de pagamento (dinheiro, credito, debito, pix, crediario): ").strip().lower()
        if forma_pgto == "crediario":
            if not cliente_orcamento: # Se não veio de orçamento, pede o cliente
                cpf_cliente = input("CPF do cliente para crediário: ").strip()
                cliente_encontrado = next((c for c in clientes if c['cpf'] == cpf_cliente), None)
                if not cliente_encontrado:
                    print("Cliente não encontrado no crediário. Por favor, cadastre-o primeiro.")
                    return # Aborta a venda para crediário
                cliente_orcamento = cliente_encontrado # Usa o cliente encontrado
            
            # Registra no crediário
            crediario = _load_data(CREDIARIO_FILE)
            crediario.append({
                "id_cliente": cliente_orcamento['cpf'], # Usando CPF como ID único
                "nome_cliente": cliente_orcamento['nome'],
                "valor_devido": total_com_desconto,
                "data_venda": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "data_vencimento": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"), # Exemplo: 30 dias para pagar
                "itens_vendidos": [
                    {"codigo": item['codigo_produto'], "nome": item['nome_produto'], "quantidade": item['quantidade']}
                    for item in carrinho
                ],
                "vendedor": logged_in_user['nome']
            })
            _save_data(crediario, CREDIARIO_FILE)
            print(f"Venda registrada no crediário para {cliente_orcamento['nome']}. Valor devido: R${total_com_desconto:.2f}")
        elif forma_pgto not in ["dinheiro", "credito", "debito", "pix"]:
            print("Forma de pagamento inválida.")

    # Pede dados do cliente, se não veio de orçamento
    if not cliente_orcamento:
        nome_cliente = input("Nome do cliente (opcional): ").strip()
        cpf_cliente = input("CPF do cliente (opcional): ").strip()
        endereco_cliente = input("Endereço do cliente (opcional): ").strip()
        telefone_cliente = input("Telefone do cliente (opcional): ").strip()
    else:
        nome_cliente = cliente_orcamento.get('nome', 'N/A')
        cpf_cliente = cliente_orcamento.get('cpf', 'N/A')
        endereco_cliente = cliente_orcamento.get('endereco', 'N/A')
        telefone_cliente = cliente_orcamento.get('telefone', 'N/A')


    # Atualiza estoque
    for item_carrinho in carrinho:
        for p in produtos:
            if p['codigo'] == item_carrinho['codigo_produto']:
                p['estoque'] -= item_carrinho['quantidade']
                break
    _save_data(produtos, PRODUTOS_FILE)

    # Registro de venda
    venda = {
        "id_venda": len(vendas) + 1,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vendedor": logged_in_user['nome'],
        "itens": carrinho,
        "total_bruto": total_venda,
        "desconto_percentual": desconto_percentual,
        "valor_desconto": valor_desconto,
        "total_final": total_com_desconto,
        "forma_pagamento": forma_pgto,
        "cliente": {
            "nome": nome_cliente,
            "cpf": cpf_cliente,
            "endereco": endereco_cliente,
            "telefone": telefone_cliente
        }
    }
    vendas.append(venda)
    _save_data(vendas, VENDAS_FILE)

    print("\nVenda registrada com sucesso!")
    print(f"Total: R${total_com_desconto:.2f}")
    print("-----------------------------------")


def fazer_orcamento(logged_in_user):
    """Cria um orçamento e permite convertê-lo em venda."""
    produtos = _load_data(PRODUTOS_FILE)
    orcamento_itens = []
    total_orcamento = 0.0

    print("\n--- Fazer Orçamento ---")
    while True:
        cod = input("Código do produto (ou 'f' para finalizar): ").strip().lower()
        if cod == 'f':
            break

        produto = next((item for item in produtos if item['codigo'] == cod), None)
        if not produto:
            print("Produto não encontrado.")
            continue

        try:
            qtd = int(input(f"Quantidade de '{produto['nome']}': "))
            if qtd <= 0:
                print("Quantidade deve ser positiva.")
                continue
        except ValueError:
            print("Quantidade inválida.")
            continue

        subtotal_item = produto['preco'] * qtd
        orcamento_itens.append({
            "codigo_produto": cod,
            "nome_produto": produto['nome'],
            "quantidade": qtd,
            "preco_unitario": produto['preco'],
            "subtotal": subtotal_item
        })
        total_orcamento += subtotal_item
        print(f"Item '{produto['nome']}' adicionado ao orçamento.")

    if not orcamento_itens:
        print("Nenhum item no orçamento.")
        return

    print("\n--- Resumo do Orçamento ---")
    for item in orcamento_itens:
        print(f"  - {item['nome_produto']} (x{item['quantidade']}) - R${item['subtotal']:.2f}")
    print(f"Total do Orçamento: R${total_orcamento:.2f}")

    # Simula impressão
    print("\nSimulando envio para impressora de rede...")
    print("Orçamento impresso com sucesso!")

    converter = input("Deseja converter este orçamento em venda? (s/n): ").strip().lower()
    if converter == 's':
        print("\nConvertendo orçamento em venda...")
        registrar_venda(logged_in_user, itens_orcamento=orcamento_itens)
    else:
        print("Orçamento finalizado sem conversão para venda.")

def cadastrar_cliente_crediario():
    """Cadastra um novo cliente para o crediário próprio."""
    clientes = _load_data(CLIENTES_FILE)
    print("\n--- Cadastrar Cliente para Crediário ---")
    nome = input("Nome completo do cliente: ").strip()
    cpf = input("CPF do cliente (apenas números): ").strip()
    telefone = input("Telefone do cliente: ").strip()
    endereco = input("Endereço completo do cliente: ").strip()

    if any(c['cpf'] == cpf for c in clientes):
        print("Erro: Cliente com este CPF já cadastrado.")
        return

    clientes.append({
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco,
        "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    _save_data(clientes, CLIENTES_FILE)
    print("Cliente cadastrado no crediário com sucesso!")

def registrar_devolucao():
    """Registra a devolução de um item e estorna o estoque."""
    vendas = _load_data(VENDAS_FILE)
    produtos = _load_data(PRODUTOS_FILE)

    print("\n--- Registrar Devolução ---")
    try:
        id_venda_devolucao = int(input("ID da venda para devolução: "))
    except ValueError:
        print("ID da venda inválido.")
        return

    venda_encontrada = next((v for v in vendas if v['id_venda'] == id_venda_devolucao), None)

    if not venda_encontrada:
        print("Venda não encontrada.")
        return

    data_venda_str = venda_encontrada['data_hora']
    data_venda = datetime.strptime(data_venda_str, "%Y-%m-%d %H:%M:%S")
    if datetime.now() - data_venda > timedelta(days=30):
        print("Prazo de 30 dias para devolução excedido.")
        return

    print("\nItens da Venda:")
    for i, item in enumerate(venda_encontrada['itens']):
        print(f"{i+1}. {item['nome_produto']} (x{item['quantidade']})")

    try:
        idx_item_devolver = int(input("Número do item a devolver (ex: 1 para o primeiro item): ")) - 1
        if not (0 <= idx_item_devolver < len(venda_encontrada['itens'])):
            print("Número de item inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    item_devolver = venda_encontrada['itens'][idx_item_devolver]
    
    try:
        qtd_devolver = int(input(f"Quantidade de '{item_devolver['nome_produto']}' a devolver (máx {item_devolver['quantidade']}): "))
        if not (0 < qtd_devolver <= item_devolver['quantidade']):
            print("Quantidade inválida para devolução.")
            return
    except ValueError:
        print("Quantidade inválida.")
        return

    # Estorna o estoque
    for p in produtos:
        if p['codigo'] == item_devolver['codigo_produto']:
            p['estoque'] += qtd_devolver
            break
    _save_data(produtos, PRODUTOS_FILE)

    # Marca o item como devolvido ou ajusta a quantidade vendida na venda original (simplificado aqui)
    # Para um sistema real, você criaria um registro de devolução separado ou ajustaria o item na venda.
    # Aqui, apenas diminuímos a quantidade vendida na venda original para fins de relatório futuro.
    item_devolver['quantidade'] -= qtd_devolver
    if item_devolver['quantidade'] == 0:
        venda_encontrada['itens'].pop(idx_item_devolver) # Remove o item se tudo foi devolvido

    print(f"Devolução de {qtd_devolver} unidades de '{item_devolver['nome_produto']}' registrada com sucesso!")
    print("Estoque estornado.")
    
    # Atualiza a venda no arquivo
    _save_data(vendas, VENDAS_FILE)

# --- Funções do Setor de Estoque ---

def visualizar_estoque():
    """Exibe o estoque atual de todos os produtos."""
    produtos = _load_data(PRODUTOS_FILE)
    print("\n--- Estoque Atual ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'Código':<10} {'Nome do Produto':<40} {'Estoque':<10} {'Preço (R$)':<15}")
    print("-" * 75)
    for p in produtos:
        print(f"{p['codigo']:<10} {p['nome']:<40} {p['estoque']:<10} {p['preco']:<15.2f}")
    print("-" * 75)

def notificacoes_estoque():
    """Notifica quando produtos estão com estoque baixo."""
    produtos = _load_data(PRODUTOS_FILE)
    print("\n--- Notificações de Estoque ---")
    itens_baixo_estoque = [p for p in produtos if p['estoque'] <= p['estoque_minimo']]

    if not itens_baixo_estoque:
        print("Nenhum produto com estoque abaixo do mínimo.")
        return

    print("Os seguintes produtos estão com estoque baixo e precisam ser reabastecidos:")
    for item in itens_baixo_estoque:
        print(f"- {item['nome']} (Código: {item['codigo']}) - Estoque atual: {item['estoque']} (Mínimo: {item['estoque_minimo']})")

def relatorio_estoque_comprar_liquidar():
    """Sugere produtos para comprar e liquidar com base no estoque e vendas."""
    produtos = _load_data(PRODUTOS_FILE)
    vendas = _load_data(VENDAS_FILE)

    print("\n--- Relatório de Estoque: Comprar e Liquidar ---")

    # Produtos para comprar (baixo estoque)
    print("\n--- Sugestão de Compra ---")
    comprar = [p for p in produtos if p['estoque'] <= p['estoque_minimo']]
    if comprar:
        for p in comprar:
            print(f"- Comprar: {p['nome']} (Estoque atual: {p['estoque']}, Mínimo: {p['estoque_minimo']})")
    else:
        print("Nenhum produto abaixo do estoque mínimo.")

    # Produtos para liquidar (alto estoque e/ou baixa saída)
    print("\n--- Sugestão de Liquidação ---")
    # Calcular vendas recentes para identificar produtos com baixa saída
    vendas_recentes = {} # {codigo_produto: total_vendido_ultimos_30_dias}
    trinta_dias_atras = datetime.now() - timedelta(days=30)

    for venda in vendas:
        data_venda = datetime.strptime(venda['data_hora'], "%Y-%m-%d %H:%M:%S")
        if data_venda > trinta_dias_atras:
            for item in venda['itens']:
                vendas_recentes[item['codigo_produto']] = vendas_recentes.get(item['codigo_produto'], 0) + item['quantidade']

    liquidar = []
    for p in produtos:
        # Critério simplificado: alto estoque e pouca ou nenhuma venda nos últimos 30 dias
        if p['estoque'] > (p['estoque_minimo'] * 2) and vendas_recentes.get(p['codigo'], 0) < 5: # Exemplo: mais que o dobro do mínimo e menos de 5 vendas
            liquidar.append(p)
    
    if liquidar:
        for p in liquidar:
            print(f"- Liquidar: {p['nome']} (Estoque atual: {p['estoque']}, Vendas nos últimos 30 dias: {vendas_recentes.get(p['codigo'], 0)})")
    else:
        print("Nenhum produto sugerido para liquidação no momento.")

# --- Funções do Setor de Caixa ---

def dashboard_caixa():
    """Exibe um dashboard com as vendas do dia."""
    vendas = _load_data(VENDAS_FILE)
    hoje = datetime.now().strftime("%Y-%m-%d")
    vendas_do_dia = [v for v in vendas if v['data_hora'].startswith(hoje)]

    total_vendas_dia = sum(v['total_final'] for v in vendas_do_dia)
    num_vendas_dia = len(vendas_do_dia)

    print(f"\n--- Dashboard do Caixa - {hoje} ---")
    print(f"Total de Vendas do Dia: R${total_vendas_dia:.2f}")
    print(f"Número de Vendas: {num_vendas_dia}")

    if vendas_do_dia:
        print("\nÚltimas Vendas:")
        # Exibe as últimas 5 vendas do dia
        for i, venda in enumerate(reversed(vendas_do_dia[-5:])):
            print(f"  Venda #{venda['id_venda']} - Vendedor: {venda['vendedor']} - Total: R${venda['total_final']:.2f} ({venda['forma_pagamento'].capitalize()})")
            if i >= 4: # Limita a 5 para não sobrecarregar
                break
    else:
        print("Nenhuma venda registrada hoje ainda.")

def consultar_crediario():
    """Consulta e exibe os débitos em aberto do crediário."""
    crediario = _load_data(CREDIARIO_FILE)
    print("\n--- Crediário: Débitos em Aberto ---")
    if not crediario:
        print("Nenhum débito em aberto no crediário.")
        return

    print(f"{'Cliente':<30} {'Valor Devido (R$)':<20} {'Vencimento':<15} {'Vendedor':<20}")
    print("-" * 85)
    for debito in crediario:
        print(f"{debito['nome_cliente']:<30} {debito['valor_devido']:<20.2f} {debito['data_vencimento']:<15} {debito['vendedor']:<20}")
    print("-" * 85)

    # Opção para "pagar" um débito (remover do crediário)
    try:
        pagar_opcao = input("\nDeseja registrar um pagamento de crediário? (s/n): ").strip().lower()
        if pagar_opcao == 's':
            cpf_pagar = input("CPF do cliente que está pagando: ").strip()
            debito_encontrado = next((d for d in crediario if d['id_cliente'] == cpf_pagar), None)
            if debito_encontrado:
                crediario.remove(debito_encontrado)
                _save_data(crediario, CREDIARIO_FILE)
                print(f"Débito de {debito_encontrado['nome_cliente']} removido (simulando pagamento).")
            else:
                print("Cliente não encontrado ou sem débitos em aberto.")
    except Exception as e:
        print(f"Erro ao processar pagamento: {e}")


def relatorio_vendas_geral():
    """Gera relatórios de vendas por período, produto, vendedor e cliente."""
    vendas = _load_data(VENDAS_FILE)
    print("\n--- Relatórios de Vendas ---")
    print("1. Por Período")
    print("2. Por Produto")
    print("3. Por Vendedor")
    print("4. Por Cliente")
    opcao = input("Escolha o tipo de relatório: ").strip()

    if opcao == '1':
        data_inicio_str = input("Data de início (AAAA-MM-DD): ").strip()
        data_fim_str = input("Data de fim (AAAA-MM-DD): ").strip()
        try:
            data_inicio = datetime.strptime(data_inicio_str, "%Y-%m-%d")
            data_fim = datetime.strptime(data_fim_str, "%Y-%m-%d")
            vendas_filtradas = [
                v for v in vendas
                if data_inicio <= datetime.strptime(v['data_hora'].split(' ')[0], "%Y-%m-%d") <= data_fim
            ]
            print(f"\n--- Relatório de Vendas de {data_inicio_str} a {data_fim_str} ---")
            for venda in vendas_filtradas:
                print(f"ID: {venda['id_venda']}, Data: {venda['data_hora']}, Vendedor: {venda['vendedor']}, Total: R${venda['total_final']:.2f}")
            print(f"Total de vendas no período: R${sum(v['total_final'] for v in vendas_filtradas):.2f}")
        except ValueError:
            print("Formato de data inválido. Use AAAA-MM-DD.")
    elif opcao == '2':
        codigo_produto = input("Código do produto: ").strip()
        vendas_filtradas = []
        for venda in vendas:
            for item in venda['itens']:
                if item['codigo_produto'] == codigo_produto:
                    vendas_filtradas.append(venda)
                    break # Evita duplicar a venda se o produto aparecer mais de uma vez
        print(f"\n--- Relatório de Vendas para o Produto '{codigo_produto}' ---")
        for venda in vendas_filtradas:
            for item in venda['itens']:
                if item['codigo_produto'] == codigo_produto:
                    print(f"ID: {venda['id_venda']}, Data: {venda['data_hora']}, Vendedor: {venda['vendedor']}, Quantidade: {item['quantidade']}, Total Item: R${item['subtotal']:.2f}")
        print(f"Total de vendas do produto: R${sum(item['subtotal'] for v in vendas_filtradas for item in v['itens'] if item['codigo_produto'] == codigo_produto):.2f}")
    elif opcao == '3':
        nome_vendedor = input("Nome do vendedor: ").strip()
        vendas_filtradas = [v for v in vendas if v['vendedor'].lower() == nome_vendedor.lower()]
        print(f"\n--- Relatório de Vendas do Vendedor '{nome_vendedor}' ---")
        for venda in vendas_filtradas:
            print(f"ID: {venda['id_venda']}, Data: {venda['data_hora']}, Total: R${venda['total_final']:.2f}")
        print(f"Total de vendas do vendedor: R${sum(v['total_final'] for v in vendas_filtradas):.2f}")
    elif opcao == '4':
        nome_cliente = input("Nome do cliente: ").strip()
        vendas_filtradas = [v for v in vendas if v['cliente']['nome'].lower() == nome_cliente.lower()]
        print(f"\n--- Relatório de Vendas do Cliente '{nome_cliente}' ---")
        for venda in vendas_filtradas:
            print(f"ID: {venda['id_venda']}, Data: {venda['data_hora']}, Vendedor: {venda['vendedor']}, Total: R${venda['total_final']:.2f}")
        print(f"Total de compras do cliente: R${sum(v['total_final'] for v in vendas_filtradas):.2f}")
    else:
        print("Opção inválida.")

# --- Relatórios Gerais (acessíveis de múltiplos menus) ---

def relatorio_produtos_mais_vendidos():
    """Gera um relatório dos produtos mais vendidos e anota a época de maior venda."""
    vendas = _load_data(VENDAS_FILE)
    
    vendas_por_produto = {} # {codigo_produto: {'nome': nome, 'total_vendido': quantidade, 'meses_venda': {mes: quantidade}}}

    for venda in vendas:
        data_venda = datetime.strptime(venda['data_hora'], "%Y-%m-%d %H:%M:%S")
        mes_venda = data_venda.strftime("%Y-%m") # Ano-Mês para agrupar

        for item in venda['itens']:
            codigo = item['codigo_produto']
            quantidade = item['quantidade']

            if codigo not in vendas_por_produto:
                vendas_por_produto[codigo] = {'nome': item['nome_produto'], 'total_vendido': 0, 'meses_venda': {}}
            
            vendas_por_produto[codigo]['total_vendido'] += quantidade
            vendas_por_produto[codigo]['meses_venda'][mes_venda] = vendas_por_produto[codigo]['meses_venda'].get(mes_venda, 0) + quantidade
    
    # Ordenar por total vendido
    produtos_ordenados = sorted(vendas_por_produto.values(), key=lambda x: x['total_vendido'], reverse=True)

    print("\n--- Relatório de Produtos Mais Vendidos ---")
    if not produtos_ordenados:
        print("Nenhuma venda registrada para gerar o relatório.")
        return

    for produto in produtos_ordenados:
        print(f"\nProduto: {produto['nome']} (Total Vendido: {produto['total_vendido']} unidades)")
        
        if produto['meses_venda']:
            # Encontrar o mês de maior venda
            mes_pico = max(produto['meses_venda'], key=produto['meses_venda'].get)
            print(f"  Época de maior venda: {mes_pico} (com {produto['meses_venda'][mes_pico]} unidades)")
        else:
            print("  Dados de época de venda não disponíveis.")

def relatorio_vendedores():
    """Exibe o desempenho de cada vendedor."""
    vendas = _load_data(VENDAS_FILE)
    desempenho_vendedores = {} # {nome_vendedor: {'total_vendas': valor, 'num_vendas': quantidade}}

    for venda in vendas:
        vendedor = venda['vendedor']
        total_final = venda['total_final']

        if vendedor not in desempenho_vendedores:
            desempenho_vendedores[vendedor] = {'total_vendas': 0.0, 'num_vendas': 0}
        
        desempenho_vendedores[vendedor]['total_vendas'] += total_final
        desempenho_vendedores[vendedor]['num_vendas'] += 1
    
    # Ordenar por total de vendas
    vendedores_ordenados = sorted(desempenho_vendedores.items(), key=lambda item: item[1]['total_vendas'], reverse=True)

    print("\n--- Relatório de Desempenho de Vendedores ---")
    if not vendedores_ordenados:
        print("Nenhuma venda registrada para os vendedores.")
        return

    print(f"{'Vendedor':<30} {'Total de Vendas (R$)':<25} {'Número de Vendas':<20}")
    print("-" * 75)
    for vendedor, dados in vendedores_ordenados:
        print(f"{vendedor:<30} {dados['total_vendas']:<25.2f} {dados['num_vendas']:<20}")
    print("-" * 75)

# --- Programa Principal ---

def main():
    """Função principal do sistema Construfácil."""
    _ensure_data_files_exist() # Garante que os arquivos de dados existam e estejam populados

    while True:
        logged_in_user = None
        while not logged_in_user:
            logged_in_user = login()
            if not logged_in_user:
                input("Pressione Enter para tentar novamente...") # Pausa para o usuário ver a mensagem de erro

        setor = logged_in_user['setor']
        if setor == "vendas":
            menu_vendas(logged_in_user)
        elif setor == "estoque":
            menu_estoque(logged_in_user)
        elif setor == "caixa":
            menu_caixa(logged_in_user)
        else:
            print("Setor não reconhecido. Contate o administrador.")
        
        print("\nSaindo do menu do setor. Retornando para a tela de login...")

if __name__ == "__main__":
    main()
