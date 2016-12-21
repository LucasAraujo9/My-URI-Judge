__author__ = 'Joaquim Alves'
"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem
“eh o maior”. Utilize a fórmula:
MAIOR AB = (a + b + abs(a - b)) / 2
Entrada
O arquivo de entrada contém três valores inteiros.
Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
Exemplos de
Entrada                    Exemplos de Saída
7 14 106                    106 eh o maior
217 14 6                    217 eh o maior
"""

a,b,c = [int(i) for i in input().split(" ")]

if(a > b):
    MAIOR_AB = (a + b + (+(a - b)))/ 2
else:
    MAIOR_AB = (a + b + (-(a - b)))/2

if(MAIOR_AB >= c):
    print("%d eh o maior"%(MAIOR_AB))
else:
    print("%d eh o maior"%(c))