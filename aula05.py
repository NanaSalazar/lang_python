# Calcule o faturamento de um representante que ganha R$500,00 fixo + 6% sobre vendas
# Vendas R$12.398,00

valorFixo = 500.00
venda = 12398.00
comissao = venda * 0.06
faturamento = valorFixo + comissao

print(f'O valor fixo do representante e: {valorFixo}')
print(f'O valor total de vendas e: {venda}')
print(f'O total de comissao e: {comissao}')
print(f'O faturamento total e: {faturamento}')