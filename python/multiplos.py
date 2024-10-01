'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si - Bee 1044

Name: multiplos.py
Descripition: script para verificar se dois números são múltiplos entre si

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 01/10/2024
Last Modified: 01/10/2024

'''
a, b = input().split(" ")
a, b = int(a), int(b)

if a%b == 0 or b%a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
