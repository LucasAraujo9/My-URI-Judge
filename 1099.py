__author__ = 'Joaquim Alves'
"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois
inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada: A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir.
Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída: Imprima a soma de todos valores ímpares entre X e Y.

Exemplo de Entrada	Exemplo de Saída
7
4 5
13 10
6 4
3 3
3 5
3 4
3 8
0
11
5
0
0
0
12
"""
N = int(input())
lista = []
soma = 0

for i in range(N):
    X,Y = [int(i) for i in input().split(" ")]
    if(X - Y == 1):
        soma = 0
    if(X - Y == -1):
        soma = 0
    if(X > Y):
        for j in range(Y+1,X):
            if(j % 2 > 0):
                soma += j
    else:
        for j in range(X+1,Y):
            if(j % 2 > 0):
                soma += j

    lista.append(soma)
    soma = 0

for i in range(len(lista)):
    print(lista[i])

"""
for i in range(N):
    X,Y = [int(i) for i in input().split(" ")]
    if(X > 0):
        for j in range(X):
            if(j % 2 > 0):
                somaX += j
    else:
        X *= -1
        for j in range(X):
            if(j % 2 > 0):
                somaX += -j
    if(Y > 0):
        for j in range(Y):
            if(j % 2 > 0):
                somaY += j
    else:
        Y *= -1
        for j in range(Y):
            if(j % 2 > 0):
                somaY += -j
    soma = somaX + somaY
    lista.append(soma)
    soma = somaX = somaY = 0

for i in range(len(lista)):
    print(lista[i])
"""

