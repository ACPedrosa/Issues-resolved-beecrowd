"""
Sort Simples, o objetivo foi ordenar 3 números de entrada em
ordem crescente- Bee 1042

Name: sort_simples.py
Descripition: script para ordenar números de maneira crescente.

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 28/05/2024
Last Modified: 28/05/2024

"""
# --- Variáveis ---
i1, i2, i3 = input().split(" ")
i1, i2, i3 = int(i1), int(i2), int(i3)

# -- processamento ---
lista = [i1, i2, i3]
nova_lista = sorted(lista)

for i in range(len(nova_lista)):
    print(nova_lista[i])
    
print(f"\n{i1}\n{i2}\n{i3}")