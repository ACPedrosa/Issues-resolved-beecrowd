"""
Calculando o valor total a ser pago por uma peça, de acordo com sua:
quantidade e valor unitário - Bee 10010

Name: calculo_simples.py
Descripition: script para realizar o cálculo do valor a ser pago em uma compra

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 27/05/2024
Last Modified: 27/05/2024

"""
entrada01 = input().split(" ") 

entrada02 = input().split(" ")

codigo01, numero_pecas01, valor_peca01 = entrada01

codigo02, numero_pecas02, valor_peca02 = entrada02


valor_pagar = (int(numero_pecas01)*float(valor_peca01)) + (int(numero_pecas02)*float(valor_peca02))

print(f"VALOR A PAGAR: R$ {valor_pagar:.2f}")
