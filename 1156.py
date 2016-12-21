__author__ = 'joaquim'
"""
 URI Online Judge | 1156
Sequência S II

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?
Entrada

Não há nenhuma entrada neste problema.
Saída

A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.

"""
contImpar = 1
contPar = 1
s = 0

while(1):
    if contImpar > 39:
        break
    s += (contImpar/contPar)
    contImpar += 2
    contPar *= 2

print("%.2f" %s)
