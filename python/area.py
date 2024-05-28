"""
Calculando o valor da área de polígonos, sendo eles: 
triângulo, círculo, trapézio, quadrado e retângulo - Bee 1012

Name: area.py
Descripition: script para realizar o cálculo da área de polígonos

Author: Ana Caroline P. e Silva
Version: 2.0 
Creation Date: 27/05/2024
Last Modified: 27/05/2024

"""
valores = input().split(" ")

A, B, C = valores

triangulo = (float(A) * float(C))/2
circulo = 3.14159 * float(C)**2
trapezio = (float(A)+float(B)) * float(C)/2
quadrado = float(B)**(2)
retangulo = float(A)*float(B)


print(f"TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}")
