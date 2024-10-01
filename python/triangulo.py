'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Bee - 1043

Name: triangulo.py
Descripition: script para verificar se os valores de entrada formam um trinagulo

Author: Ana Caroline P. e Silva
Version: 1.0
Creation Date: 01/10/2024
Last Modified: 01/10/2024
'''
x = input().split()
a, b, c =x
a = float(a)
b = float(b)
c = float(c)

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {:.1f}'.format(((a + b) / 2) * c))
