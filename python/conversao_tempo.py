"""
Conversão de Tempo, o objetivo foi expressar um valor inteiro 
(tempo em segundos) no formato de horas, minutos e segundos - Bee 1019

Name: conversao_tempo.py
Descripition: script para calcular a conversão de segundos em horas, minutos e segundos

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 28/05/2024
Last Modified: 28/05/2024

"""
tempo_segundos = int(input("Digite o valor dos segundos: "))

#hora = 3600s; minuto = 60s; segundo = 1s.

horas = tempo_segundos//3600
resto_tempo = tempo_segundos - horas*3600

minutos = resto_tempo//60
segundos = resto_tempo - minutos*60

print(f"{horas}:{minutos}:{segundos}")




