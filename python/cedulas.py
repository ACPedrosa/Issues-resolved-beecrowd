"""
Cédulas, o objetivo foi calcular o menor número de notas
possíveis no qual um valor pode ser decomposto - Bee 1018

Name: cedulas.py
Descripition: script para calcular o número mínimo de notas para decompor um valor

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 28/05/2024
Last Modified: 28/05/2024

"""
valor = int(input("Digite um valor inteiro: "))

valor100 = valor//100 #5
novo_valor = valor%100 #76

valor50 = novo_valor//50 # 1
novo_valor = novo_valor%50 #52

valor20 = novo_valor//20
novo_valor = novo_valor%20 

valor10 = novo_valor//10
novo_valor = novo_valor%10 

valor05 = novo_valor//5
novo_valor = novo_valor%5 

valor02 = novo_valor//2
novo_valor = novo_valor%2 

valor01 = novo_valor//1
novo_valor = novo_valor%1 

 

print(f"{valor}\n{valor100} nota(s) de R$ 100,00\n{valor50} nota(s) de R$ 50,00\n{valor20} nota(s) de R$ 20,00\n{valor10} nota(s) de R$ 10,00\n{valor05} nota(s) de R$ 5,00\n{valor02} nota(s) de R$ 2,00\n{valor01} nota(s) de R$ 1,00")
