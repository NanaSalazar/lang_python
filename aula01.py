# ---- Estruturas

cores = ['azul', 'verde', 'amarelo', 'rosa']

for cor in cores:
    print(f'Posicao: {cores.index(cor)}, valor: {cor}')


frutas = []

frutas.append('banana')
frutas.append('laranja')
frutas.append('uva')
frutas.append('kiwi')

for posicao, fruta in enumerate(frutas):
    print(f'Posicao: {posicao}, fruta: {fruta}')
