__author__ = 'Joaquim Alves'
"""
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

Entrada: O arquivo de entrada contém 1 valor inteiro qualquer.
Saída: Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

Exemplo de Entrada	Exemplo de Saída
8
1
3
5
7
"""
X = int(input())
for i in range(0,X):
    if( i % 2 > 0):
        print(i)

if(X % 2 > 0):
    print(X)

"""
while(X != 0):
    if(X % 2 > 0):
        Y = X
        print(Y)
    X -= 1
"""