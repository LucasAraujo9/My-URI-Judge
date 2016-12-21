__author__ = 'joaquim'
"""
 URI Online Judge | 1177
Preenchimento de Vetor II

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas vezes,
conforme exemplo abaixo. Imprima o vetor N.
Entrada

A entrada contém um valor inteiro T (2 ≤ T ≤ 50).
Saída

Para cada posição do vetor, escreva "N[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.
Exemplo de Entrada 	Exemplo de Saída

3

N[0] = 0
N[1] = 1
N[2] = 2
N[3] = 0
N[4] = 1
N[5] = 2
N[6] = 0
N[7] = 1
N[8] = 2
...
"""

num = int(input())
cont = num
aux = 0

n = [int(i) for i in range(1000)]

for i in range(1000):
    if cont > 0:
        n[i] = aux
        cont -= 1
        aux += 1
    if cont == 0:
        aux = 0
        cont = num

    print("N[%d] = %d" %(i,n[i]))




