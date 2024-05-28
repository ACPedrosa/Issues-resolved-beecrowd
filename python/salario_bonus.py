"""
Calculando o salário de um vendedor de acordo com seu salário fixo, o total de vendas efetuadas
e o valor da comissão - Bee 1009

Name: salario_bonus.py
Descripition: script para realizar o cálculo do salário de um vendedor

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 27/05/2024
Last Modified: 27/05/2024

"""
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o valor do salario fixo: "))
montante_total = float(input("Digite o valor total das vendas efetuadas no mês: "))

salario = salario_fixo + (15*montante_total)/100

print(f"TOTAL = R$ {salario:.2f}")
