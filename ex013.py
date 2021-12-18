## Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

raw_salary = float(input('Digite o salário do funcionário: R$'))
increased_percentage = 15 / 100

new_salary = raw_salary + (raw_salary * increased_percentage)

print(f'O novo salário do funcionário é de {new_salary}.')