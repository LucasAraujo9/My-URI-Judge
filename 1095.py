__author__ = 'Joaquim Alves'
"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada: Não há nenhuma entrada neste problema.
Saída: Imprima a sequencia conforme exemplo abaixo

Exemplo de Entrada	Exemplo de Saída
I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
"""

I = 1
J = 60

while(J >= 0):
    print("I=%d J=%d"%(I,J))
    I += 3
    J -= 5

"""
if(I == 37):
    print("I=? J=%d"%J)
        break
"""