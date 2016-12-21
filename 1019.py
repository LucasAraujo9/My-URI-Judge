__author__ = 'Joaquim Alves'
"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica e informe-o
expresso no formato horas:minutos:segundos.

Entrada: O arquivo de entrada contém um valor inteiro N.

Saída: Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
556                 0:9:16
1                   0:0:1

140153            38:55:53
"""
tempoSegundo = int(input())

horas = int(tempoSegundo / 3600)
minutos = int((tempoSegundo - (3600 * horas))/60)
segundos = int(tempoSegundo - (3600 * horas) - (minutos * 60))

print("%d:%d:%d"%(horas,minutos,segundos))