# ---- Algoritmos --- 

numPar = [2, 8, 16, 24, 6, 14, 18, 30]
valor = int(input('Digite um numero para buscar: '))

def executar_busca(numPar, valor):
    for elemento in numPar:
        if elemento == valor:
            return print('O numero existe na sequencia')
        else:
            return print('O numero nao esta na sequencia')

executar_busca(numPar, valor)