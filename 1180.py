__author__ = 'joaquim'
"""
URI Online Judge | 1180
Menor e Posição

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X,
encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.
Entrada

A primeira linha de entrada contem um único inteiro N (1 < N < 1000), indicando o número de elementos que deverão ser
lidos em seguida para o vetor X[N] de inteiros. A segunda linha contém cada um dos N valores, separados por um espaço.
Saída

A primeira linha apresenta a mensagem “Menor valor:” seguida de um espaço e do menor valor lido na entrada. A segunda
linha apresenta a mensagem “Posicao:” seguido de um espaço e da posição do vetor na qual se encontra o menor valor lido,
lembrando que o vetor inicia na posição zero.
Exemplo de Entrada 	Exemplo de Saída

10
1 2 3 4 -5 6 7 8 9 10


Menor valor: -5
Posicao: 4

10
1 2 3 -10 -5 -11 7 8 9 10

Menor valor: -11
Posicao: 5
"""

n = int(input())
menor = 0
posicao = 0
cont = 0
x = [int(i) for i in input().split()]

for i in range(n):
    if cont == 0:
        menor = x[i]
        cont += 1
    else:
        if x[i] < menor:
            menor = x[i]
            posicao = i

print("Menor valor:", menor)
print("Posicao:", posicao)

