"""
Coordenadas de um ponto, o objetivo foi determinar a qual quadrante
um ponto pertence de acordo com suas coordenadas - Bee 1041

Name: coordenadas_ponto.py
Descripition: script para verificar o quadrante a qual pertence um ponto.

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 29/05/2024
Last Modified: 29/05/2024

"""
# --- Variáveis ---
x, y = input().split(" ")
x, y = float(x), float(y)

# --- processamento ---
if x == 0 and y == 0:
    print("Origem")
elif x != 0 and y == 0:
    print("Eixo X")
elif x == 0 and y != 0:
    print("Eixo Y")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
    