# Calcule o salario de um funcionario que trabalha por hora
# Ele ganha R$14,25/h
# Trabalhou 163 horas normais
# Trabalhou 20 horas extras (paga em dobro)

valor = 14.25
horaN = 163 * valor
horaE = (20 * valor) * 2
salario = horaN + horaE

print(f'O valor total de horas normais trabalhadas: {horaN}')
print(f'O valor total de horas extras trabalhadas: {horaE}')
print(f'Total do pagamento: {salario}')