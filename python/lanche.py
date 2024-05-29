"""
Lanche, o objetivo foi ler dois valores, sendo o código de
um item e a qantidade desse item, para calcular o valor a pagar - Bee 1038

Name: lanche.py
Descripition: script para indicar qual o valor a pagar em um lanche

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 29/05/2024
Last Modified: 29/05/2024

"""
# --- Variáveis ---
codigo, quantidade = input().split(" ")
codigo, quantidade = int(codigo), int(quantidade)

# --- processamento ---
match codigo:
    case 1:
        total = quantidade * 4.00
    case 2:
        total = quantidade * 4.50
    case 3: 
        total = quantidade * 5.00
    case 4:
        total = quantidade * 2.00
    case 5: 
        total = quantidade * 1.50

# --- Saída ---
print(f"Total: R$ {total:.2f}")

    