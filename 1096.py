__author__ = 'Joaquim Alves'
"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada: Não há nenhuma entrada neste problema.
Saída: Imprima a sequencia conforme exemplo abaixo

Exemplo de Entrada	Exemplo de Saída
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
"""

I = 1
J = 7
contJ = 1

while(I <= 9):
    if(contJ <= 3):

        print("I=%d J=%d"%(I,J))
        contJ += 1
        J -= 1
    else:
        contJ = 1
        I += 2
        J = 7

