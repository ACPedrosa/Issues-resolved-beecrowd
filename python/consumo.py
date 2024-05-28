"""
Calculando o consumo médio de um automóvel de acordo com a
distência em Km percorrido e o total de combustível gasto - Bee 1014

Name: consumo.py
Descripition: script para calcular o consumo médio de um automóvel

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 28/05/2024
Last Modified: 28/05/2024

"""
x = int(input("Digite a distância total percorrida: "))
y = float(input("Digite o total de combustível gasto: "))

consumo =  x/y

print(f"{consumo:.3f} km/l")
