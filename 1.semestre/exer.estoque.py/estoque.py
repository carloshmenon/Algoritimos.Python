# Dicionário com os produtos e seus códigos
produtos = {
    10: {"nome": "Caderno", "estoque": 0},
    20: {"nome": "Caneta", "estoque": 0},
    30: {"nome": "Lápis", "estoque": 0},
    40: {"nome": "Borracha", "estoque": 0},
    50: {"nome": "Régua", "estoque": 0}
}

def inicializar_estoque():
    """Função para ler o estoque inicial de cada produto"""
    print("\n--- INICIALIZAÇÃO DE ESTOQUE ---")
    for codigo in produtos:
        while True:
            try:
                quantidade = int(input(f"Digite o estoque inicial para {produtos[codigo]['nome']} (cód. {codigo}): "))
                if quantidade >= 0:
                    produtos[codigo]["estoque"] = quantidade
                    break
                else:
                    print("O estoque não pode ser negativo. Tente novamente.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

def exibir_menu():
    """Exibe o menu de opções"""
    print("\nEscolha a operação:")
    print("E – Entrada no estoque")
    print("S – Saída no estoque")
    print("R – Relatório")
    print("X – Sair")

def entrada_estoque():
    """Processa uma entrada no estoque"""
    try:
        codigo = int(input("Digite o código do produto: "))
        if codigo not in produtos:
            print("Código de produto inválido!")
            return
        
        quantidade = int(input("Digite a quantidade a adicionar: "))
        if quantidade <= 0:
            print("A quantidade deve ser positiva!")
            return
            
        produtos[codigo]["estoque"] += quantidade
        print(f"Entrada de {quantidade} unidades de {produtos[codigo]['nome']} registrada.")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

def saida_estoque():
    """Processa uma saída no estoque"""
    try:
        codigo = int(input("Digite o código do produto: "))
        if codigo not in produtos:
            print("Código de produto inválido!")
            return
        
        quantidade = int(input("Digite a quantidade a retirar: "))
        if quantidade <= 0:
            print("A quantidade deve ser positiva!")
            return
            
        if produtos[codigo]["estoque"] >= quantidade:
            produtos[codigo]["estoque"] -= quantidade
            print(f"Saída de {quantidade} unidades de {produtos[codigo]['nome']} registrada.")
        else:
            print(f"Estoque insuficiente! Há apenas {produtos[codigo]['estoque']} unidades disponíveis.")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

def gerar_relatorio():
    """Gera um relatório com o estoque atual"""
    print("\n--- RELATÓRIO DE ESTOQUE ---")
    print("{:<10} {:<20} {:<10}".format("CÓDIGO", "PRODUTO", "ESTOQUE"))
    for codigo in produtos:
        print("{:<10} {:<20} {:<10}".format(
            codigo, 
            produtos[codigo]["nome"], 
            produtos[codigo]["estoque"]
        ))

def main():
    """Função principal do programa"""
    print("Bem-vindo ao Sistema de Controle de Estoque")
    inicializar_estoque()
    
    while True:
        exibir_menu()
        opcao = input("Digite a operação desejada: ").upper()
        
        if opcao == "E":
            entrada_estoque()
        elif opcao == "S":
            saida_estoque()
        elif opcao == "R":
            gerar_relatorio()
        elif opcao == "X":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()