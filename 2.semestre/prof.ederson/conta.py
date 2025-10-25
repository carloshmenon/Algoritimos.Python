
class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Conta(Pessoa):
    def __init__(self, nome, numero, agencia, senha):
        super().__init__(nome)
        self.numero = numero
        self.agencia = agencia
        self.__senha = senha  # atributo privado
        self.saldo = 0.0
        self.extrato = []

    def autenticar(self, agencia, numero, senha):
        """Verifica se agência, conta e senha estão corretos."""
        return self.agencia == agencia and self.numero == numero and self.__senha == senha

    def depositar(self, agencia, numero, valor):
        """Deposita se agência e conta estiverem corretas."""
        if self.agencia == agencia and self.numero == numero:
            self.saldo += valor
            self.extrato.append(f"Depósito de R${valor:.2f}")
            print(f"✅ Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("❌ Agência ou conta inválida.")

    def sacar(self, agencia, numero, senha, valor):
        """Realiza saque se autenticação e saldo forem válidos."""
        if not self.autenticar(agencia, numero, senha):
            print("❌ Autenticação falhou. Verifique agência, conta ou senha.")
            return
        if valor > self.saldo:
            print("❌ Saldo insuficiente.")
            return
        self.saldo -= valor
        self.extrato.append(f"Saque de R${valor:.2f}")
        print(f"💸 Saque de R${valor:.2f} realizado com sucesso!")

    def consultar_saldo(self, agencia, numero, senha):
        if self.autenticar(agencia, numero, senha):
            print(f"💰 Saldo atual: R${self.saldo:.2f}")
        else:
            print("❌ Autenticação falhou. Verifique agência, conta ou senha.")

    def consultar_extrato(self, agencia, numero, senha):
        if self.autenticar(agencia, numero, senha):
            print(f"\n📜 Extrato da conta {self.numero} - {self.nome}:")
            if not self.extrato:
                print("   Nenhuma movimentação registrada.")
            else:
                for mov in self.extrato:
                    print(f"   - {mov}")
            print(f"➡ Saldo atual: R${self.saldo:.2f}\n")
        else:
            print("❌ Autenticação falhou. Verifique agência, conta ou senha.")
