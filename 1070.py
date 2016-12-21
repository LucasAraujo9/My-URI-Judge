__author__ = 'Joaquim Alves'
"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada

A entrada será um valor inteiro positivo.

Saída

A saída será uma sequência de seis números ímpares.

Exemplo de Entrada	Exemplo de Saída
8
9
11
13
15
17
19
"""

X = int(input())
if(X % 2 > 0):
    print(X)
    for i in range(0,10):
        X += 1
        if(X % 2 > 0):
            print(X)
else:
    for i in range(0,12):
        X += 1
        if(X % 2 > 0):
            print(X)