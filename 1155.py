__author__ = 'Joaquim Alves'
"""
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 1 /2 + 1 /3 + … + 1 /1 00
Entrada
Não há nenhuma entrada neste problema.
Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
"""
S = 0
n = 1
a = 1
while(a <= 100):
    x = (n/a)
    S = S + x
    a = a + 1

print("%.2f"%S)
