"""
Calculando o salário de um funcionário de acordo com o número de horas 
trabalhadas e o valor que recebe por hora - Bee 1008

Name: salario.py
Descripition: script para realizar o cálculo do salário de um funcionário

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 27/05/2024
Last Modified: 27/05/2024

"""
numero_funcio = int(input("Digite o número correspondente ao funcionário: "))
numero_horas = int(input("Digite o número de horas trabalhadas desse funcionário:  "))
valor_hora = float(input("Digite o valor que receber por hora: "))

salario = numero_horas * valor_hora

print(f"NUMBER = {numero_funcio}\nSALARY = U$ {salario:.2f}")
