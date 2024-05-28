"""
Distância entre Dois Pontos, o objetivo foi calcular a distância
entre 4 valores correspondentes aos eixos x e y de um plano - Bee 1015

Name: distancia_pontos.py
Descripition: script para calcular a distancia de entre dois pontos

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 28/05/2024
Last Modified: 28/05/2024

"""
import math

x1, y1 = input().split(" ")
x1, y1 = float(x1), float(y1)

x2, y2 = input().split(" ")
x2, y2 = float(x2), float(y2)

distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) )

print(f"{distancia:.4f}")
