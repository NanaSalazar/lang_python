class ContaBancaria():

    def __init__(self, tipo, cliente):
        self.tipo = tipo
        self.cliente = cliente
    
        pass

class ContaCorrente(ContaBancaria):

    def __init__(self, tipo, cliente, saldo, cartaoCredito):
        super().__init__(tipo, cliente)
        self.tipo = 'Corrente'
        self.cliente = cliente
        self.saldo = 0
        self.cartaoCredito = bool
    
    def setSaldo(valor):
        saldo =+valor
    
    def saque(valor, saldo):
        if (valor < saldo):
            return print('Você não possui saldo suficiente para esta operação')
        else:
            print(f'Voce sacou {valor} da sua conta.')
            print(f'Seu saldo atual e {saldo}')
            return saldo - valor
        

cliente = input('Digite seu nome: ')

print('Digite o tipo de conta: ')
print('1. Conta Corrente: ')
print('2. Conta Poupanca: ')
print('3. Conta Universitaria: ')

tipoConta = int(input())


if tipoConta == 1:
    newCliente = ContaCorrente(tipoConta, cliente, 0, bool)
    saldo = 0
    cartaoCredito = print(input('Deseja cartao de credito?: '))
    if cartaoCredito == 'sim':
        cartaoCredito == True
    elif cartaoCredito == 'nao':
        cartaoCredito == False

print(newCliente.cartaoCredito)
print(newCliente.saldo)        

        
