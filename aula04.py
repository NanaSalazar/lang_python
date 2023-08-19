# ---- Calculadora

class Calculadora():

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        pass


    def soma (self, n1, n2):
        return n1 + n2
        
    def subtracao (self, n1, n2):
        return n1 - n2
        
    def multiplicacao (self, n1, n2):
        return n1 * n2
        
    def divisao (self, n1, n2):
        return n1 / n2


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

calc = Calculadora(n1, n2)


print(f'A soma dos dois numeros e: ', calc.soma(n1, n2))
print(f'A subtracao dos dois numeros e: ', calc.subtracao(n1, n2))
print(f'A divisao dos dois numeros e: ', calc.divisao(n1, n2))
print(f'A multiplicacao dos dois numeros e: ', calc.multiplicacao(n1, n2))
