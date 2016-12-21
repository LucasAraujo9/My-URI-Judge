__author__ = 'joaquim'
"""
 URI Online Judge | 1173
Preenchimento de Vetor I

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição
subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor
devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.
Entrada

A entrada contém um valor inteiro (V<=50).
Saída

Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i.
O primeiro número do vetor N (N[0]) irá receber o valor de V.
Exemplo de Entrada 	Exemplo de Saída

1

N[0] = 1
N[1] = 2
N[2] = 4
"""

n = [0,0,0,0,0,0,0,0,0,0]

num = int(input())

for i in range(len(n)):
    if i == 0:
        n[i] = num
    else:
        n[i] = 2 * n[i-1]

for j in range(len(n)):
    print("N[%d] = %d" %(j,n[j]))